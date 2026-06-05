# Reglas Nómina Colombia 2026

Fuente de verdad para el Gem calculadora de **recargos** (extras, nocturno, dominical/festivo).

## Alcance del Gem

Este Gem liquida **por empleado** únicamente:

- Horas extra (diurnas, nocturnas, dominicales/festivas).
- Recargo nocturno (horas ordinarias en franja 21:00–06:00).
- Horas dominicales y festivas.

**No calcula:** salario base mensual, auxilio de transporte, deducciones ni horas ordinarias diurnas (ya cubiertas por el salario).

## Parámetros base

| Concepto | Valor |
|----------|-------|
| Salario mínimo 2026 | $1.750.000 COP |
| Jornada semanal máxima | 44 horas |
| Jornada mensual referencia | 220 horas |
| Factor prestacional | 42% |

## Semana laboral

La semana va de **lunes a domingo** (calendario).

## Festivos

Usar la lista de `festivos_colombia_2026.md` (19 festivos). Todo **domingo** también aplica recargo dominical.

## Tarifas horarias (salario variable)

```
Valor hora ordinaria = Salario mensual ÷ 220
```

| Tipo | Recargo | Tarifa | Ejemplo SMLV |
|------|---------|--------|--------------|
| Ordinaria diurna | — | No liquida recargo | — |
| Ordinaria nocturna | +35% | Ordinaria × 1,35 | $10.738,64 |
| Extra diurna | +25% | Ordinaria × 1,25 | $9.943,18 |
| Extra nocturna | +75% | Ordinaria × 1,75 | $13.920,45 |
| Dominical/festiva | +75% | Ordinaria × 1,75 | $13.920,45 |
| Extra dominical/festiva | +100% | Ordinaria × 2,00 | $15.909,09 |

Si el usuario no indica salario, usar salario mínimo 2026.

## Jornada ordinaria

Máximo **44 horas efectivas por semana**. Lo que excede es hora extra.

## Franjas horarias

| Franja | Rango |
|--------|-------|
| Diurna | 06:00 a 21:00 |
| Nocturna | 21:00 a 06:00 (cruza medianoche) |

## Definiciones

### Hora ordinaria diurna (día laboral)

Hora efectiva dentro de las 44 h semanales, en franja diurna, en día laboral normal.

**Recargo: $0** — ya incluida en salario base.

### Hora ordinaria nocturna (día laboral)

Hora efectiva dentro de las 44 h semanales, en franja nocturna (21:00–06:00), en día laboral normal.

**Recargo nocturno: +35%** sobre hora ordinaria.

### Hora extra

Hora efectiva que supera las 44 horas semanales en día laboral normal:

| Franja | Recargo |
|--------|---------|
| Diurna | +25% |
| Nocturna | +75% |

### Hora dominical o festiva

Hora efectiva en **domingo o festivo** que aún no supera las 44 h semanales.

**Recargo: +75%** sobre hora ordinaria.

### Hora extra dominical o festiva

Hora efectiva en **domingo o festivo** que además supera las 44 h semanales.

**Recargo: +100%** sobre hora ordinaria.

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
7. Asignar horas a ordinarias (máx. 44) y extras.
8. Liquidar recargos según tipo.
9. Redondear valores monetarios a pesos enteros.

## Árbol de decisión (recargo)

```
¿Es domingo o festivo?
├─ SÍ → ¿Ya se completaron 44 h ordinarias en la semana?
│       ├─ NO → Recargo dominical/festivo (+75%)
│       └─ SÍ → Recargo extra dominical/festivo (+100%)
└─ NO → ¿Supera 44 h semanales?
        ├─ NO → ¿Franja nocturna (21:00-06:00)?
        │       ├─ SÍ → Recargo nocturno (+35%)
        │       └─ NO → Sin recargo (ordinaria diurna)
        └─ SÍ → ¿Franja nocturna?
                ├─ SÍ → Extra nocturna (+75%)
                └─ NO → Extra diurna (+25%)
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
3. Horas dominicales/festivas dentro de 44 h → recargo dominical (+75%).
4. Una hora tiene **una sola tarifa** según el árbol (no se acumulan recargos).
5. Salario: si no se indica → salario mínimo 2026.
6. Valor hora: siempre salario mensual ÷ 220.
