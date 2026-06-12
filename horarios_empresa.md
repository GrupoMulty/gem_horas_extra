# Horarios de la Empresa — Multy 2026

Catálogo oficial de turnos para el Gem. **Solo entran horarios validados por Multy (RRHH / nómina).**

Si un turno no está aquí, el Gem debe pedir entrada, salida, descansos y días laborados — no inferirlos.

---

## Cómo completar este archivo

Por cada turno de Multy documentar:

| Campo | Qué es | Quién lo define |
|-------|--------|-----------------|
| **Código y alias** | Ej. `H2`, "operativo" | Multy |
| **Días laborados** | Lun–vie, lun–sáb, etc. | Multy |
| **Entrada / salida** | Hora real del turno | Multy |
| **Descansos** | Minutos desayuno + almuerzo (total diario) | Multy |
| **Horas efectivas** | Tiempo trabajado según reloj (ver fórmula abajo) | Se calcula |
| **Horas programadas** | Lo acordado para jornada exigible y resta por festivo | Multy |

### Fórmula — horas efectivas

```text
Efectivas = (salida − entrada) − descansos
```

### Fórmula — horas programadas

No se deducen automáticamente de entrada/salida.

Las define Multy y son las que se utilizarán para:

- Jornada exigible.
- Semanas incompletas.
- Festivos no laborados.
- Determinación de horas extra.

---

# Turnos Multy

## H1 — Administrativo Turno 1

| Campo | Lun–vie | Sábado |
|---------|---------|---------|
| Días laborados | Sí | Sí |
| Entrada / salida | 08:00 – 17:00 | 07:30 – 13:30 |
| Descanso | 20 min desayuno + 60 min almuerzo | 20 min desayuno |
| Horas efectivas *(calculadas)* | 7,67 h | 5,67 h |
| **Horas programadas** | **Pendiente RRHH** | **Pendiente RRHH** |

**Alias:** `administrativo`, `administrativo 1`, `H1`

**Estado:** ✅ Validado

---

## H2 — Administrativo Turno 2

| Campo | Lun–vie | Sábado |
|---------|---------|---------|
| Días laborados | Sí | Sí |
| Entrada / salida | 08:10 – 17:30 | 07:30 – 15:00 |
| Descanso | 30 min desayuno + 80 min almuerzo | 30 min desayuno + 30 min almuerzo |
| Horas efectivas *(calculadas)* | 7,5 h | 6,50 h |
| **Horas programadas** | **Pendiente RRHH** | **Pendiente RRHH** |

**Alias:** `administrativo 2`, `H2`

**Estado:** ✅ Validado

---

## H3 — Punto de Venta Turno 1

| Campo | Lun–vie | Sábado | Domingo |
|---------|---------|---------|---------|
| Días laborados | Sí | Sí | Según programación |
| Entrada / salida | 08:00 – 17:30 | 07:10 – 15:00 | 07:30 – 12:30 |
| Descanso | 30 min desayuno + 90 min almuerzo | 30 min desayuno + 50 min almuerzo | Sin descanso |
| Horas efectivas *(calculadas)* | 7,50 h | 6,50 h | 5,00 h |
| **Horas programadas** | **Pendiente RRHH** | **Pendiente RRHH** | **Pendiente RRHH** |

**Alias:** `punto venta 1`, `H3`

**Estado:** ✅ Validado

---

## H4 — Punto de Venta Turno 2

| Campo | Lun–vie | Sábado | Domingo |
|---------|---------|---------|---------|
| Días laborados | Sí | Sí | Según programación |
| Entrada / salida | 07:00 – 16:30 | 07:10 – 15:00 | 07:30 – 12:30 |
| Descanso | 30 min desayuno + 90 min almuerzo | 30 min desayuno + 50 min almuerzo | Sin descanso |
| Horas efectivas *(calculadas)* | 7,50 h | 6,50 h | 5,00 h |
| **Horas programadas** | **Pendiente RRHH** | **Pendiente RRHH** | **Pendiente RRHH** |

**Alias:** `operativo`, `punto venta 2`, `H4`

**Estado:** ✅ Validado

---

## H5 — Punto de Venta Turno 3

| Campo | Lun–vie | Sábado | Domingo |
|---------|---------|---------|---------|
| Días laborados | Sí | Sí | Según programación |
| Entrada / salida | 07:30 – 17:00 | 07:10 – 15:00 | 07:30 – 12:30 |
| Descanso | 30 min desayuno + 90 min almuerzo | 30 min desayuno + 50 min almuerzo | Sin descanso |
| Horas efectivas *(calculadas)* | 7,50 h | 6,50 h | 5,00 h |
| **Horas programadas** | **Pendiente RRHH** | **Pendiente RRHH** | **Pendiente RRHH** |

**Alias:** `punto venta 3`, `H5`

**Estado:** ✅ Validado

---

## H6 — Punto de Venta Turno 6

| Campo | Lun–vie | Sábado | Domingo |
|---------|---------|---------|---------|
| Días laborados | Sí | Sí | Según programación |
| Entrada / salida | 08:30 – 17:30 | 07:10 – 15:00 | 07:30 – 12:30 |
| Descanso |90 min almuerzo | 30 min desayuno + 50 min almuerzo | Sin descanso |
| Horas efectivas *(calculadas)* | 7,50 h | 6,50 h | 5,00 h |
| **Horas programadas** | **Pendiente RRHH** | **Pendiente RRHH** | **Pendiente RRHH** |

**Alias:** `punto venta 6`, `H6`

**Estado:** ✅ Validado

---

## H7 — Bodega de Distribución Turno 1

| Campo | Lun–vie | Sábado |
|---------|---------|---------|
| Días laborados | Sí | Sí |
| Entrada / salida | 06:15 – 15:30 | 07:15 – 13:00 |
| Descanso | 30 min desayuno + 90 min almuerzo | 30 min desayuno |
| Horas efectivas *(calculadas)* | 7,75 h | 5,25 h |
| **Horas programadas** | **Pendiente RRHH** | **Pendiente RRHH** |

**Alias:** `bodega 1`, `H7`

**Estado:** ✅ Validado

---

## H8 — Bodega de Distribución Turno 2

| Campo | Lun–vie | Sábado |
|---------|---------|---------|
| Días laborados | Sí | Sí |
| Entrada / salida | 07:15 – 16:30 | 07:15 – 13:00 |
| Descanso | 30 min desayuno + 60 min almuerzo | 30 min desayuno |
| Horas efectivas *(calculadas)* | 7,75 h | 5,25 h |
| **Horas programadas** | **Pendiente RRHH** | **Pendiente RRHH** |

**Alias:** `bodega 2`, `H8`

**Estado:** ✅ Validado

---

## Uso en el Gem

1. Usuario indica turno por código o alias.
2. El Gem toma automáticamente entrada, salida y descansos del turno.
3. Solo pregunta por excepciones:
   - Ausencias.
   - Festivos trabajados.
   - Cambios de turno.
4. Las horas programadas son la base para calcular jornada exigible y festivos.
5. Las horas efectivas son la base para liquidar recargos.

## Semanas incompletas

Si solo liquidan uno o varios días concretos:

```text
Jornada Exigible =
Σ Horas Programadas de los días incluidos en el cálculo
```

Nunca usar automáticamente 42 horas semanales en semanas incompletas.