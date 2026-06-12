# Casos de Prueba

Ejemplos de referencia para validar respuestas del Gem.  
Todos los valores son **recargos** (no incluyen salario base ordinario diurno).

Parámetros: SMLV **$1.750.905**, jornada **42 h/semana**, divisor **210 h/mes**.

> Escenarios avanzados con entradas reales de usuario → ver `ejemplos_complejos.md`

---

## Caso 1 — Karen (casi sin recargos)

**Empleado:** Karen  
**Horario:** Lunes a Viernes, 07:00 - 17:00  
**Descansos:** Desayuno 15 min, Almuerzo 60 min

### Por día

- Horas efectivas: **8,75**
- Clasificación: 8,75 h diurnas, 0 h nocturnas

### Semana

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Horas semanales | 43,75 | |
| Horas extra diurnas (vie) | 1,75 | $18.239 |
| **Recargos sin prestaciones** | | **$18.239** |
| Prestaciones (42%) | | $7.660 |
| **Total con prestaciones** | | **$25.899** |

> Con 42 h semanales, el viernes genera 1,75 h extra diurna.

---

## Caso 2 — Juan (extras diurnas)

**Empleado:** Juan  
**Horario:** Lunes a Viernes, 07:00 - 18:00  
**Descansos:** Desayuno 15 min, Almuerzo 60 min

### Semana

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Horas semanales | 48,75 | |
| Horas extra diurnas | 6,75 | $70.349 |
| **Recargos sin prestaciones** | | **$70.349** |
| Prestaciones (42%) | | $29.547 |
| **Total con prestaciones** | | **$99.896** |

---

## Caso 3 — Pedro (recargo nocturno)

**Empleado:** Pedro  
**Horario:** Lunes a Viernes, 21:00 - 06:00  
**Descansos:** Desayuno 0 min, Almuerzo 60 min

### Por día

- Horas efectivas: **8,00**
- Clasificación: 0 h diurnas, **8,00 h nocturnas**

### Semana

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Horas semanales | 40,00 | |
| Horas ordinarias nocturnas | 40,00 | $450.233 |
| **Recargos sin prestaciones** | | **$450.233** |
| Prestaciones (42%) | | $189.098 |
| **Total con prestaciones** | | **$639.331** |

### Validaciones

- Salida 06:00 = día siguiente.
- Toda la jornada es franja nocturna (19:00–06:00).
- Tarifa: $8.338 × 1,35 = $11.256/h.

---

## Caso 4 — Laura (domingo con recargo dominical)

**Empleado:** Laura  
**Horario:** Lunes a Viernes 07:00-17:00 + Domingo 07:00-17:00  
**Descansos:** Desayuno 15 min, Almuerzo 60 min

### Semana

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Horas semanales | 52,50 | |
| Horas extra diurnas (vie) | 1,75 | $18.239 |
| Horas extra dominicales diurnas (dom) | 8,75 | $145.909 |
| **Recargos sin prestaciones** | | **$164.148** |
| Prestaciones (42%) | | $68.942 |
| **Total con prestaciones** | | **$233.090** |

> Lun-vie acumulan 43,75 h → 42 h ordinarias + 1,75 h extra diurna el viernes. Domingo completo (8,75 h) es extra dominical diurna.

---

## Caso 5 — Carlos (festivo 20 de julio)

**Empleado:** Carlos  
**Horario:** Lunes 07:00-17:00 + Martes 07:00-17:00 + Festivo 07:00-15:00 (20 jul)  
**Descansos:** 15 min desayuno + 60 min almuerzo  
**Salario:** SMLV $1.750.905

### Semana parcial (3 días)

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Horas efectivas totales | 24,25 | |
| Horas dominicales/festivas (20 jul) | 6,75 | $98.488 |
| **Recargos sin prestaciones** | | **$98.488** |
| Prestaciones (42%) | | $41.365 |
| **Total con prestaciones** | | **$139.853** |

---

## Caso 6 — María (salario superior al mínimo)

**Empleado:** María  
**Salario mensual:** $3.500.000 COP  
**Horario:** Lunes a Viernes, 07:00 - 18:00  
**Descansos:** Desayuno 15 min, Almuerzo 60 min

### Tarifas derivadas ($3.500.000 ÷ 210)

| Tipo | COP |
|------|-----|
| Ordinaria | $16.667 |
| Ordinaria nocturna (+35%) | $22.500 |
| Extra diurna (+25%) | $20.833 |
| Extra nocturna (+75%) | $29.167 |
| Dominical (+75%) | $29.167 |
| Extra dominical diurna (+100%) | $33.333 |
| Extra dominical nocturna (+150%) | $41.667 |

### Recargos semanales

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Horas extra diurnas | 6,75 | $140.625 |
| **Recargos sin prestaciones** | | **$140.625** |
| Prestaciones (42%) | | $59.062 |
| **Total con prestaciones** | | **$199.687** |
