# Horas Extra Colombia 2026 — Multy

Fuente de conocimiento para un **Gem de Gemini**: calculadora de **recargos** laborales por empleado (Colombia 2026).

Repositorio: [GrupoMulty/gem_horas_extra](https://github.com/GrupoMulty/gem_horas_extra)

## Objetivo

Liquidar por empleado:

- Horas extra (diurnas, nocturnas, dominicales/festivas).
- Recargo nocturno.
- Horas dominicales y festivas.
- Prestacional 42% sobre recargos.

**No incluye:** salario base ordinario diurno, auxilio de transporte ni deducciones.

## Archivos

| Archivo | Propósito |
|---------|-----------|
| `instrucciones_gem.md` | Prompt del Gem — copiar en AI Studio |
| `reglas_nomina_2026.md` | Tarifas Multy, jornada exigible, árbol de recargos |
| `horarios_empresa.md` | Catálogo turnos **H1–H8** (programadas y efectivas por día) |
| `festivos_colombia_2026.md` | 19 festivos Colombia 2026 |
| `casos_prueba.md` | 6 escenarios básicos |
| `ejemplos_complejos.md` | Escenarios avanzados — **Ejemplo 18** = caso gold standard |
| `calculos.py` | Motor Python de referencia (tarifas y liquidación semanal) |

## Parámetros Multy 2026

| Concepto | Valor |
|----------|-------|
| SMLV | $1.750.905 |
| Jornada semanal | 42 h |
| Divisor mensual | 210 h |
| Hora ordinaria (SMLV) | $8.338 |
| Extra diurna (× 1,25) | $10.422 |
| Prestacional | 42% sobre recargos |

## Flujo de liquidación

1. Identificar **turno** (H1–H8) en `horarios_empresa.md`.
2. Definir **periodo** (quincena, mes o fechas) y **festivos** trabajados/no laborados.
3. Partir en **semanas calendario** (lun–dom); por cada una elegir **método 1–4** (ver `instrucciones_gem.md`).
4. **Programadas** del catálogo → jornada exigible. **Efectivas** del usuario si difieren del turno → horas trabajadas.
5. `Extras = max(0, efectivas − exigible)` por semana; sumar periodo.
6. Liquidar recargos y prestacional 42%.

**Caso más complejo validado:** Karen · H8 · mayo 2026 → `ejemplos_complejos.md` Ejemplo 18 ($464.992 total con prestaciones).

## Uso con Gemini

1. Crear Gem en [Google AI Studio](https://aistudio.google.com/).
2. Pegar **`instrucciones_gem.md`** en instrucciones del sistema.
3. Adjuntar los 6 archivos `.md` + `calculos.py` como conocimiento.

## Verificar cálculos (Python)

```bash
python -c "from calculos import *; print(round(calcular_tarifas().hora_ordinaria))"
# ≈ 8338

python -c "from calculos import *; j=[Jornada(21,6,0,60) for _ in range(5)]; print(liquidar_semana(j).valor_recargos)"
# 450233 — recargo nocturno Pedro (casos_prueba.md)
```
