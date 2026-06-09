"""Motor de referencia para cálculo de recargos — extras, nocturno y dominical — Colombia 2026."""

from dataclasses import dataclass

JORNADA_SEMANAL = 42
JORNADA_DIURNA_INICIO = 6.0   # 06:00
JORNADA_DIURNA_FIN = 19.0      # 19:00 (reforma laboral Ley 2466/2025)

SALARIO_MINIMO = 1_750_905
JORNADA_MENSUAL = 210          # 42 h semanales × 5 días / semana

FACTOR_PRESTACIONAL = 0.42

RECARGO_NOCTURNO = 0.35
RECARGO_EXTRA_DIURNA = 0.25
RECARGO_EXTRA_NOCTURNA = 0.75
RECARGO_DOMINICAL = 0.90
RECARGO_EXTRA_DOMINICAL_DIURNA = 1.15
RECARGO_EXTRA_DOMINICAL_NOCTURNA = 1.65

FESTIVOS_2026 = {
    "2026-01-01", "2026-01-12", "2026-03-23", "2026-04-02", "2026-04-03",
    "2026-05-01", "2026-05-18", "2026-06-08", "2026-06-15", "2026-06-29",
    "2026-07-13", "2026-07-20", "2026-08-07", "2026-08-17", "2026-10-12",
    "2026-11-02", "2026-11-16", "2026-12-08", "2026-12-25",
}


@dataclass
class Tarifas:
    hora_ordinaria: float
    ordinaria_nocturna: float
    extra_diurna: float
    extra_nocturna: float
    dominical: float
    extra_dominical_diurna: float
    extra_dominical_nocturna: float


@dataclass
class Jornada:
    entrada_horas: float
    salida_horas: float
    desayuno_min: int = 0
    almuerzo_min: int = 0
    es_dominical_o_festivo: bool = False


@dataclass
class ClasificacionDia:
    horas_efectivas: float
    horas_diurnas: float
    horas_nocturnas: float


@dataclass
class LiquidacionSemanal:
    horas_ordinarias: float
    horas_extra: float
    horas_ordinarias_nocturnas: float
    horas_extra_diurnas: float
    horas_extra_nocturnas: float
    horas_dominicales: float
    horas_extra_dominicales_diurnas: float
    horas_extra_dominicales_nocturnas: float
    valor_recargo_nocturno: int
    valor_extra_diurnas: int
    valor_extra_nocturnas: int
    valor_dominicales: int
    valor_extra_dominicales_diurnas: int
    valor_extra_dominicales_nocturnas: int
    valor_recargos: int
    valor_prestaciones: int
    valor_total_con_prestaciones: int
    tarifas: Tarifas


def es_festivo(fecha: str) -> bool:
    """Verifica si una fecha ISO (YYYY-MM-DD) es festivo en Colombia 2026."""
    return fecha in FESTIVOS_2026


def calcular_tarifas(salario_mensual: float = SALARIO_MINIMO) -> Tarifas:
    """Deriva tarifas horarias a partir del salario mensual (÷ 210 h)."""
    hora_ordinaria = salario_mensual / JORNADA_MENSUAL
    return Tarifas(
        hora_ordinaria=hora_ordinaria,
        ordinaria_nocturna=hora_ordinaria * (1 + RECARGO_NOCTURNO),
        extra_diurna=hora_ordinaria * (1 + RECARGO_EXTRA_DIURNA),
        extra_nocturna=hora_ordinaria * (1 + RECARGO_EXTRA_NOCTURNA),
        dominical=hora_ordinaria * (1 + RECARGO_DOMINICAL),
        extra_dominical_diurna=hora_ordinaria * (1 + RECARGO_EXTRA_DOMINICAL_DIURNA),
        extra_dominical_nocturna=hora_ordinaria * (1 + RECARGO_EXTRA_DOMINICAL_NOCTURNA),
    )


def hora_texto_a_decimal(hora: str) -> float:
    """Convierte 'HH:MM' a horas decimales."""
    partes = hora.strip().split(":")
    return int(partes[0]) + int(partes[1]) / 60


def calcular_horas_efectivas(
    entrada_horas: float,
    salida_horas: float,
    desayuno_min: int = 0,
    almuerzo_min: int = 0,
) -> float:
    """Horas trabajadas descontando descansos. Soporta cruce de medianoche."""
    if salida_horas <= entrada_horas:
        salida_horas += 24

    horas = salida_horas - entrada_horas
    descanso = (desayuno_min + almuerzo_min) / 60
    return round(max(horas - descanso, 0), 2)


def _minutos_en_franja(inicio: float, fin: float, franja_inicio: float, franja_fin: float) -> float:
    """Minutos de [inicio, fin) que caen dentro de [franja_inicio, franja_fin)."""
    total = 0.0
    cursor = inicio
    while cursor < fin:
        paso = min(fin - cursor, 1 / 60)
        hora_dia = cursor % 24
        if franja_inicio <= hora_dia < franja_fin:
            total += paso * 60
        cursor += paso
    return total


def clasificar_diurna_nocturna(
    entrada_horas: float,
    salida_horas: float,
    desayuno_min: int = 0,
    almuerzo_min: int = 0,
) -> ClasificacionDia:
    """
    Reparte horas efectivas entre jornada diurna (06:00-19:00) y nocturna (19:00-06:00).
    Solo importa el total de minutos de descanso, no la hora del descanso.
    """
    if salida_horas <= entrada_horas:
        salida_horas += 24

    bruto_min = (salida_horas - entrada_horas) * 60
    descanso_min = desayuno_min + almuerzo_min
    efectivas_min = max(bruto_min - descanso_min, 0)

    if bruto_min == 0:
        return ClasificacionDia(0, 0, 0)

    diurna_bruta = _minutos_en_franja(entrada_horas, salida_horas, JORNADA_DIURNA_INICIO, JORNADA_DIURNA_FIN)
    nocturna_bruta = bruto_min - diurna_bruta

    factor = efectivas_min / bruto_min
    horas_diurnas = round((diurna_bruta * factor) / 60, 2)
    horas_nocturnas = round((nocturna_bruta * factor) / 60, 2)
    horas_efectivas = round(efectivas_min / 60, 2)

    return ClasificacionDia(horas_efectivas, horas_diurnas, horas_nocturnas)


def calcular_horas_semanales(horas_totales: float) -> dict[str, float]:
    ordinarias = min(horas_totales, JORNADA_SEMANAL)
    extras = max(horas_totales - JORNADA_SEMANAL, 0)
    return {
        "ordinarias": round(ordinarias, 2),
        "extras": round(extras, 2),
    }


def liquidar_semana(
    jornadas: list[Jornada],
    salario_mensual: float = SALARIO_MINIMO,
) -> LiquidacionSemanal:
    """
    Liquida recargos semanales por empleado: nocturno, dominical/festivo y extras.
    No incluye salario base de horas ordinarias diurnas.
    """
    tarifas = calcular_tarifas(salario_mensual)
    horas_ordinarias_restantes = float(JORNADA_SEMANAL)
    horas_ordinarias_nocturnas = 0.0
    horas_extra_diurnas = 0.0
    horas_extra_nocturnas = 0.0
    horas_dominicales = 0.0
    horas_extra_dominicales_diurnas = 0.0
    horas_extra_dominicales_nocturnas = 0.0
    horas_ordinarias = 0.0

    for jornada in jornadas:
        clasificacion = clasificar_diurna_nocturna(
            jornada.entrada_horas,
            jornada.salida_horas,
            jornada.desayuno_min,
            jornada.almuerzo_min,
        )
        horas_dia = clasificacion.horas_efectivas
        if horas_dia <= 0:
            continue

        ordinarias_dia = min(horas_dia, horas_ordinarias_restantes)
        extras_dia = horas_dia - ordinarias_dia
        horas_ordinarias += ordinarias_dia
        horas_ordinarias_restantes -= ordinarias_dia

        ratio_diurna = clasificacion.horas_diurnas / horas_dia if horas_dia else 0
        ratio_nocturna = clasificacion.horas_nocturnas / horas_dia if horas_dia else 0

        if jornada.es_dominical_o_festivo:
            horas_dominicales += ordinarias_dia
            if extras_dia > 0:
                horas_extra_dominicales_diurnas += round(extras_dia * ratio_diurna, 2)
                horas_extra_dominicales_nocturnas += round(extras_dia * ratio_nocturna, 2)
            continue

        if ordinarias_dia > 0:
            horas_ordinarias_nocturnas += round(ordinarias_dia * ratio_nocturna, 2)

        if extras_dia <= 0:
            continue

        horas_extra_diurnas += round(extras_dia * ratio_diurna, 2)
        horas_extra_nocturnas += round(extras_dia * ratio_nocturna, 2)

    horas_extra_dominicales = round(
        horas_extra_dominicales_diurnas + horas_extra_dominicales_nocturnas, 2
    )
    horas_extra = round(
        horas_extra_diurnas + horas_extra_nocturnas + horas_extra_dominicales, 2
    )

    valor_recargo_nocturno = round(horas_ordinarias_nocturnas * tarifas.ordinaria_nocturna, 0)
    valor_dominicales = round(horas_dominicales * tarifas.dominical, 0)
    valor_extra_diurnas = round(horas_extra_diurnas * tarifas.extra_diurna, 0)
    valor_extra_nocturnas = round(horas_extra_nocturnas * tarifas.extra_nocturna, 0)
    valor_extra_dominicales_diurnas = round(
        horas_extra_dominicales_diurnas * tarifas.extra_dominical_diurna, 0
    )
    valor_extra_dominicales_nocturnas = round(
        horas_extra_dominicales_nocturnas * tarifas.extra_dominical_nocturna, 0
    )

    valor_recargos = (
        valor_recargo_nocturno
        + valor_dominicales
        + valor_extra_diurnas
        + valor_extra_nocturnas
        + valor_extra_dominicales_diurnas
        + valor_extra_dominicales_nocturnas
    )
    valor_prestaciones = round(valor_recargos * FACTOR_PRESTACIONAL, 0)
    valor_total_con_prestaciones = valor_recargos + valor_prestaciones

    return LiquidacionSemanal(
        horas_ordinarias=round(horas_ordinarias, 2),
        horas_extra=horas_extra,
        horas_ordinarias_nocturnas=round(horas_ordinarias_nocturnas, 2),
        horas_extra_diurnas=round(horas_extra_diurnas, 2),
        horas_extra_nocturnas=round(horas_extra_nocturnas, 2),
        horas_dominicales=round(horas_dominicales, 2),
        horas_extra_dominicales_diurnas=round(horas_extra_dominicales_diurnas, 2),
        horas_extra_dominicales_nocturnas=round(horas_extra_dominicales_nocturnas, 2),
        valor_recargo_nocturno=valor_recargo_nocturno,
        valor_extra_diurnas=valor_extra_diurnas,
        valor_extra_nocturnas=valor_extra_nocturnas,
        valor_dominicales=valor_dominicales,
        valor_extra_dominicales_diurnas=valor_extra_dominicales_diurnas,
        valor_extra_dominicales_nocturnas=valor_extra_dominicales_nocturnas,
        valor_recargos=valor_recargos,
        valor_prestaciones=valor_prestaciones,
        valor_total_con_prestaciones=valor_total_con_prestaciones,
        tarifas=tarifas,
    )
