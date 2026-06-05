# Casos de Prueba

Ejemplos de referencia para validar respuestas del Gem.  
Todos los valores son **recargos** (no incluyen salario base ordinario diurno).

> Escenarios avanzados con entradas reales de usuario → ver `ejemplos_complejos.md`
---

## Caso 1 — Karen (sin recargos)

**Empleado:** Karen  
**Horario:** Lunes a Viernes, 07:00 - 17:00  
**Descansos:** Desayuno 15 min, Almuerzo 60 min

### Por día

- Horas efectivas: **8,75**
- Clasificación: 8,75 h diurnas, 0 h nocturnas

### Recargos semanales

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Recargo nocturno | 0 | $0 |
| Extras | 0 | $0 |
| Dominical/festivo | 0 | $0 |
| **Recargos sin prestaciones** | | **$0** |
| Prestaciones (42%) | | $0 |
| **Total con prestaciones** | | **$0** |

---

## Caso 2 — Juan (extras diurnas)

**Empleado:** Juan  
**Horario:** Lunes a Viernes, 07:00 - 18:00  
**Descansos:** Desayuno 15 min, Almuerzo 60 min

### Semana

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Horas semanales | 48,75 | |
| Horas extra diurnas | 4,75 | $47.230 |
| **Recargos sin prestaciones** | | **$47.230** |
| Prestaciones (42%) | | $19.837 |
| **Total con prestaciones** | | **$67.067** |

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
| Horas ordinarias nocturnas | 40,00 | $429.545 |
| **Recargos sin prestaciones** | | **$429.545** |
| Prestaciones (42%) | | $180.409 |
| **Total con prestaciones** | | **$609.954** |

### Validaciones

- Salida 06:00 = día siguiente.
- Toda la jornada es franja nocturna.
- Tarifa: $7.954,55 × 1,35 = $10.738,64/h.

---

## Caso 4 — Laura (domingo con recargo dominical)

**Empleado:** Laura  
**Horario:** Lunes a Viernes 07:00-17:00 + Domingo 07:00-17:00  
**Descansos:** Desayuno 15 min, Almuerzo 60 min

### Semana

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Horas semanales | 52,50 | |
| Horas dominicales (dentro de 44 h) | 0,25 | $3.480 |
| Horas extra dominicales | 8,50 | $135.227 |
| **Recargos sin prestaciones** | | **$138.707** |
| Prestaciones (42%) | | $58.257 |
| **Total con prestaciones** | | **$196.964** |

> Lun-vie acumulan 43,75 h. Del domingo: 0,25 h completan las 44 h (dominical); 8,50 h restantes son extra dominical.

---

## Caso 5 — Carlos (festivo 20 de julio)

**Empleado:** Carlos  
**Horario:** Lunes 07:00-17:00 (14 jul) + Martes 07:00-17:00 (15 jul) + Festivo 07:00-15:00 (20 jul, Independencia)  
**Descansos:** 15 min desayuno + 60 min almuerzo  
**Salario:** SMLV $1.750.000

### Semana parcial (3 días)

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Horas efectivas totales | 24,25 | |
| Horas dominicales/festivas (20 jul, dentro de 44 h) | 6,75 | $93.963 |
| **Recargos sin prestaciones** | | **$93.963** |
| Prestaciones (42%) | | $39.464 |
| **Total con prestaciones** | | **$133.427** |

> El 20 de julio está en `festivos_colombia_2026.md`. No hay extras porque no supera 44 h.

---

## Caso 6 — María (salario superior al mínimo)

**Empleado:** María  
**Salario mensual:** $3.500.000 COP  
**Horario:** Lunes a Viernes, 07:00 - 18:00  
**Descansos:** Desayuno 15 min, Almuerzo 60 min

### Tarifas derivadas

| Tipo | COP |
|------|-----|
| Ordinaria | $15.909,09 |
| Ordinaria nocturna (+35%) | $21.477,27 |
| Extra diurna (+25%) | $19.886,36 |
| Extra nocturna (+75%) | $27.840,91 |
| Dominical (+75%) | $27.840,91 |
| Extra dominical (+100%) | $31.818,18 |

### Recargos semanales

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Horas extra diurnas | 4,75 | $94.460 |
| **Recargos sin prestaciones** | | **$94.460** |
| Prestaciones (42%) | | $39.673 |
| **Total con prestaciones** | | **$134.133** |
