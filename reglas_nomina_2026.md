# Reglas Nómina Colombia 2026

Fuente de verdad para el Gem calculadora de **recargos** (extras, nocturno, dominical/festivo).

Vigencia: jornada **42 horas semanales**, recargos **Ley 2466/2025** (desde julio 2026).

## Alcance del Gem

Este Gem liquida **por empleado** únicamente:

- Horas extra (diurnas, nocturnas, dominicales/festivas).
- Recargo nocturno (horas ordinarias en franja 19:00–06:00).
- Horas dominicales y festivas.

**No calcula:** salario base mensual, auxilio de transporte, deducciones ni horas ordinarias diurnas (ya cubiertas por el salario).

## Parámetros base

| Concepto | Valor |
|----------|-------|
| Salario mínimo 2026 | $1.750.905 COP |
| Jornada semanal máxima | 42 horas |
| Jornada mensual referencia | 210 horas |
| Factor prestacional | 42% |

## Semana laboral

La semana va de **lunes a domingo** (calendario).

## Festivos

Usar la lista de `festivos_colombia_2026.md` (19 festivos). Todo **domingo** también aplica recargo dominical.

## Tarifas horarias (salario variable)

```
Valor hora ordinaria = Salario mensual ÷ 210
```

| Tipo | Recargo | Factor | Ejemplo SMLV |
|------|---------|--------|--------------|
| Ordinaria diurna | — | No liquida recargo | — |
| Ordinaria nocturna | +35% | × 1,35 | $11.256 |
| Extra diurna | +25% | × 1,25 | $10.422 |
| Extra nocturna | +75% | × 1,75 | $14.591 |
| Dominical/festiva | +90% | × 1,90 | $15.842 |
| Extra dominical/festiva diurna | +115% | × 2,15 | $17.926 |
| Extra dominical/festiva nocturna | +165% | × 2,65 | $22.095 |

Valores SMLV de referencia: hora ordinaria **$8.338**.

Si el usuario no indica salario, usar salario mínimo 2026.

## Jornada ordinaria

Máximo **42 horas efectivas por semana**. Lo que excede es hora extra.

## Franjas horarias

| Franja | Rango |
|--------|-------|
| Diurna | 06:00 a 19:00 |
| Nocturna | 19:00 a 06:00 (cruza medianoche) |

## Definiciones

### Hora ordinaria diurna (día laboral)

Hora efectiva dentro de las 42 h semanales, en franja diurna, en día laboral normal.

**Recargo: $0** — ya incluida en salario base.

### Hora ordinaria nocturna (día laboral)

Hora efectiva dentro de las 42 h semanales, en franja nocturna (19:00–06:00), en día laboral normal.

**Recargo nocturno: +35%** → tarifa × 1,35.

### Hora extra (día laboral)

Hora efectiva que supera las 42 horas semanales en día laboral normal:

| Franja | Factor |
|--------|--------|
| Diurna | × 1,25 |
| Nocturna | × 1,75 |

### Hora dominical o festiva

Hora efectiva en **domingo o festivo** que aún no supera las 42 h semanales.

**Recargo: +90%** → tarifa × 1,90.

### Hora extra dominical o festiva

Hora efectiva en **domingo o festivo** que además supera las 42 h semanales:

| Franja | Factor |
|--------|--------|
| Diurna | × 2,15 |
| Nocturna | × 2,65 |

## Descansos

Descontar del tiempo trabajado:

- Desayuno (minutos totales)
- Almuerzo (minutos totales)

**No importa la hora del descanso**, solo la duración total.

## Cruce de medianoche

Si la salida es menor o igual que la entrada (ej. 21:00 → 06:00), la salida corresponde al **día siguiente**.

## Orden de cálculo

1. Convertir horarios a horas decimales.
2. Detectar cruce de medianoche.
3. Descontar descansos → horas efectivas del día.
4. Clasificar horas efectivas en diurna / nocturna.
5. Identificar domingo o festivo (`festivos_colombia_2026.md`).
6. Acumular semana en orden cronológico.
7. Asignar horas a ordinarias (máx. 42) y extras.
8. Liquidar recargos según tipo.
9. Redondear valores monetarios a pesos enteros.

## Árbol de decisión (recargo)

```
¿Es domingo o festivo?
├─ SÍ → ¿Ya se completaron 42 h ordinarias en la semana?
│       ├─ NO → Recargo dominical/festivo (× 1,90)
│       └─ SÍ → ¿Franja nocturna?
│               ├─ SÍ → Extra dominical/festiva nocturna (× 2,65)
│               └─ NO → Extra dominical/festiva diurna (× 2,15)
└─ NO → ¿Supera 42 h semanales?
        ├─ NO → ¿Franja nocturna (19:00-06:00)?
        │       ├─ SÍ → Recargo nocturno (× 1,35)
        │       └─ NO → Sin recargo (ordinaria diurna)
        └─ SÍ → ¿Franja nocturna?
                ├─ SÍ → Extra nocturna (× 1,75)
                └─ NO → Extra diurna (× 1,25)
```

## Carga prestacional

Siempre mostrar:

1. **Valor recargos** (sin prestaciones).
2. **Prestaciones (42%)** sobre recargos.
3. **Total con prestaciones**.

## Redondeo

Valores monetarios a **pesos enteros**. Horas con **2 decimales**.

## Reglas fijas

1. Semana laboral: lunes a domingo.
2. Festivos: lista en `festivos_colombia_2026.md`.
3. Horas dominicales/festivas dentro de 42 h → recargo dominical (+90%).
4. Una hora tiene **una sola tarifa** según el árbol (no se acumulan recargos).
5. Salario: si no se indica → salario mínimo 2026 ($1.750.905).
6. Valor hora: salario mensual ÷ **210**.

## Referencia normativa

- Ley 2101/2021 — jornada 42 h semanales.
- Ley 2466/2025 — recargos dominical (+90%), extras dominicales (+115% / +165%), franja nocturna desde las 19:00.
