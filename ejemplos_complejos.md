# Ejemplos de Complejidad — Entradas de Usuario

Escenarios realistas para entrenar y validar el Gem. Cada ejemplo incluye el **mensaje del usuario** (informal, incompleto o ambiguo), lo que el Gem debe **interpretar**, y el **resultado validado**.

Todos los valores son **recargos** (sin salario base ordinario diurno).  
Salario por defecto: **SMLV $1.750.905** | Jornada **42 h/semana** | Divisor **210 h/mes**.

---

## Ejemplo 7 — Turno mixto con cruce de medianoche

### Entrada del usuario

```
hola, necesito liquidar a andres
trabaja de 6pm a 2am de lunes a viernes
almuerzo 1 hora y desayuno 15 min
gana el minimo
```

### Información extraída

| Campo | Valor |
|-------|-------|
| Empleado | Andrés |
| Salario | $1.750.905 (SMLV) |
| Horario | Lun–Vie 18:00 – 02:00 |
| Desayuno | 15 min |
| Almuerzo | 60 min |
| Cruce medianoche | Sí (02:00 = día siguiente) |

### Horas por día

| Día | Efectivas | Diurnas | Nocturnas |
|-----|-----------|---------|-----------|
| Lun–Vie (×5) | 6,75 c/u | 0,86 | 5,89 |

> Franja diurna 18:00–19:00 (1 h) + nocturna 19:00–02:00 (7 h bruto). Descansos repartidos proporcionalmente.

### Recargos semanales

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Recargo nocturno (ordinarias) | 29,45 | $331.484 |
| **Recargos sin prestaciones** | | **$331.484** |
| Prestaciones (42%) | | $139.223 |
| **Total con prestaciones** | | **$470.707** |

---

## Ejemplo 8 — Festivo + domingo + sábado extra (semana 15–21 jun 2026)

### Entrada del usuario

```
liquida a diana porfa
semana del 15 al 21 de junio 2026:
- lunes trabajó 7am-5pm (ese día creo es festivo?)
- martes a viernes igual 7 a 5
- el sabado solo medio dia, 7am a 2pm
- domingo tambien trabajó 7am-5pm
desayuno 15 min, almuerzo 1 hora todos los dias
salario minimo
```

### Información extraída

| Día | Fecha | Festivo | Horario |
|-----|-------|---------|---------|
| Lunes | 2026-06-15 | Sí — Sagrado Corazón | 07:00–17:00 |
| Martes | 2026-06-16 | No | 07:00–17:00 |
| Miércoles | 2026-06-17 | No | 07:00–17:00 |
| Jueves | 2026-06-18 | No | 07:00–17:00 |
| Viernes | 2026-06-19 | No | 07:00–17:00 |
| Sábado | 2026-06-20 | No | 07:00–14:00 |
| Domingo | 2026-06-21 | Sí — domingo | 07:00–17:00 |

### Acumulado semanal

| Concepto | Horas |
|----------|-------|
| Horas semanales totales | 58,25 |
| Horas dominicales/festivas (lunes, dentro 42 h) | 8,75 |
| Horas extra diurnas | 7,50 |
| Horas extra dominicales diurnas (domingo) | 8,75 |

> Lun festivo 8,75 h dominical. Mar–Jue acumulan hasta 35 h. Vie completa 42 h (7 h ordinarias diurnas). Sábado: 5,75 h extra diurna + 1,75 h extra del viernes ya contadas → total extra diurna 7,5 h. Domingo: 8,75 h extra dominical diurna.

### Recargos semanales

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Recargo dominical/festivo (lunes) | 8,75 | $127.670 |
| Extra diurna | 7,50 | $78.165 |
| Extra dominical diurna (domingo) | 8,75 | $145.909 |
| **Recargos sin prestaciones** | | **$351.744** |
| Prestaciones (42%) | | $147.733 |
| **Total con prestaciones** | | **$499.477** |

---

## Ejemplo 9 — Guardia nocturna + sábado con extras mixtas

### Entrada del usuario

```
para roberto el vigilante:
lun a vie entra 10pm sale 6am, almuerzo 1h
el sabado lo llamaron de 10pm a 10am (tambien con 1h almuerzo)
cuanto le debo de recargos? gana 1.750.905
```

### Información extraída

| Día | Horario | Efectivas | Diurnas | Nocturnas |
|-----|---------|-----------|---------|-----------|
| Lun–Vie | 22:00–06:00 | 7,00 | 0,00 | 7,00 |
| Sábado | 22:00–10:00 | 11,00 | 3,65 | 7,35 |

### Acumulado semanal

| Concepto | Horas |
|----------|-------|
| Horas semanales | 46,00 |
| Ordinarias nocturnas | 39,68 |
| Extra diurna (sábado) | 1,33 |
| Extra nocturna (sábado) | 2,67 |

### Recargos semanales

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Recargo nocturno | 39,68 | $446.631 |
| Extra diurna | 1,33 | $13.861 |
| Extra nocturna | 2,67 | $38.958 |
| **Recargos sin prestaciones** | | **$499.450** |
| Prestaciones (42%) | | $209.769 |
| **Total con prestaciones** | | **$709.219** |

---

## Ejemplo 10 — Puente de julio (festivo nuevo + sábado largo + domingo)

### Entrada del usuario

```
necesito los recargos de patricia semana 13-19 julio 2026

lunes 13: 7:00 a 17:00
martes a viernes: 7:00 a 17:00
sabado 18: entro 7am y salio 8pm (desayuno 15min, almuerzo 1h)
domingo 19: 7:00 a 17:00

salario 1.750.905
```

### Información extraída

| Día | Fecha | Festivo | Efectivas |
|-----|-------|---------|-----------|
| Lunes | 2026-07-13 | Sí — Virgen de Chiquinquirá | 8,75 |
| Mar–Vie | 2026-07-14 al 17 | No | 8,75 c/u |
| Sábado | 2026-07-18 | No | 11,75 |
| Domingo | 2026-07-19 | Sí — domingo | 8,75 |

### Recargos semanales

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Recargo dominical/festivo (lunes) | 8,75 | $127.670 |
| Extra diurna (sábado) | 12,60 | $131.318 |
| Extra nocturna (sábado) | 0,90 | $13.132 |
| Extra dominical diurna (domingo) | 8,75 | $145.909 |
| **Recargos sin prestaciones** | | **$418.029** |
| Prestaciones (42%) | | $175.572 |
| **Total con prestaciones** | | **$593.601** |

---

## Ejemplo 11 — Viernes con jornada extendida (diurna + nocturna + extras)

### Entrada del usuario

```
calcula recargos de luis
lunes a jueves 7am-5pm
el viernes se quedo hasta las 10pm (6am-10pm con 15 min desayuno y 1h almuerzo)
salario minimo, descansos iguales todos los dias
```

### Información extraída

| Día | Horario | Efectivas | Diurnas | Nocturnas |
|-----|---------|-----------|---------|-----------|
| Lun–Jue | 07:00–17:00 | 8,75 | 8,75 | 0,00 |
| Vie | 06:00–22:00 | 14,75 | 11,98 | 2,77 |

### Recargos semanales

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Recargo nocturno (vie, ordinarias) | 1,31 | $14.745 |
| Extra diurna (vie) | 6,29 | $65.555 |
| Extra nocturna (vie) | 1,46 | $21.303 |
| **Recargos sin prestaciones** | | **$101.603** |
| Prestaciones (42%) | | $42.673 |
| **Total con prestaciones** | | **$144.276** |

---

## Ejemplo 12 — Salario superior + turno mixto + domingo

### Entrada del usuario

```
recargos de camila por favor
gana 2.800.000 mensuales
turno noche 6pm-2am de lunes a viernes
el domingo trabajó 7 a 5 (15 min desayuno, 1 hora almuerzo)
```

### Tarifas derivadas ($2.800.000 ÷ 210)

| Tipo | COP |
|------|-----|
| Ordinaria | $13.333 |
| Ordinaria nocturna (+35%) | $18.000 |
| Dominical (+75%) | $25.000 |
| Extra dominical diurna (+100%) | $26.667 |

### Recargos semanales

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Recargo nocturno (lun–vie) | 29,45 | $530.100 |
| Recargo dominical (domingo, dentro 42 h) | 8,25 | $192.500 |
| Extra dominical diurna (domingo) | 0,50 | $13.333 |
| **Recargos sin prestaciones** | | **$735.933** |
| Prestaciones (42%) | | $309.092 |
| **Total con prestaciones** | | **$1.045.025** |

---

## Ejemplo 13 — Semana Santa con dos festivos y extras

### Entrada del usuario

```
semena santa para fernando:
lunes 30 mar 7-5pm
martes 31 mar 7-5pm
miercoles 1 abr 7-5pm
jueves 2 abr trabajó 7am-7pm (es festivo no?)
viernes 3 abr 7-6pm
sabado 4 abr 7-6pm
desayuno 15 almuerzo 60
minimo
```

### Información extraída

| Día | Fecha | Festivo | Efectivas |
|-----|-------|---------|-----------|
| Lun | 2026-03-30 | No | 8,75 |
| Mar | 2026-03-31 | No | 8,75 |
| Mié | 2026-04-01 | No | 8,75 |
| Jue | 2026-04-02 | Sí — Jueves Santo | 10,75 |
| Vie | 2026-04-03 | Sí — Viernes Santo | 9,75 |
| Sáb | 2026-04-04 | No | 9,75 |

> El Gem debe detectar **Jueves Santo y Viernes Santo** en `festivos_colombia_2026.md`.

### Acumulado semanal

| Concepto | Horas |
|----------|-------|
| Horas semanales | 56,50 |
| Recargo festivo (jueves santo) | 10,75 |
| Recargo festivo (viernes santo, dentro 42 h) | 5,00 |
| Extra dominical/festiva diurna (viernes) | 4,75 |
| Extra diurna (sábado) | 9,75 |

### Recargos semanales

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Recargo festivo (jueves + viernes santo, dentro 42 h) | 15,75 | $229.806 |
| Extra dominical/festiva diurna (viernes) | 4,75 | $79.206 |
| Extra diurna (sábado) | 9,75 | $101.615 |
| **Recargos sin prestaciones** | | **$410.629** |
| Prestaciones (42%) | | $172.464 |
| **Total con prestaciones** | | **$583.093** |

---

## Ejemplo 14 — Entrada incompleta (conversación en dos turnos)

### Turno 1 — Entrada del usuario

```
necesito los recargos de paola, trabaja de noche esta semana
```

### Respuesta esperada del Gem (preguntas)

```
Para liquidar los recargos de Paola necesito:

1. Horario exacto de entrada y salida (¿cruza medianoche?)
2. Qué días trabajó (lun–dom, con fechas si hay festivos)
3. Minutos de desayuno y almuerzo
4. Salario mensual (¿SMLV $1.750.905?)
```

### Turno 2 — Entrada del usuario

```
lun a vie 9pm a 6am, almuerzo 60 min sin desayuno, gana 2.100.000
```

### Información extraída

| Campo | Valor |
|-------|-------|
| Horario | Lun–Vie 21:00–06:00 |
| Efectivas/día | 8,00 h (todas nocturnas) |
| Salario | $2.100.000 |

### Tarifas ($2.100.000 ÷ 210)

| Tipo | COP |
|------|-----|
| Ordinaria nocturna (+35%) | $13.500 |

### Recargos semanales

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Recargo nocturno | 40,00 | $540.000 |
| **Recargos sin prestaciones** | | **$540.000** |
| Prestaciones (42%) | | $226.800 |
| **Total con prestaciones** | | **$766.800** |

---

## Ejemplo 15 — Dos empleados en un solo mensaje

### Entrada del usuario

```
liquida recargos de esta semana:

JUAN - lun a vie 7am a 6pm, desayuno 15 min almuerzo 1h, gana el minimo

PEDRO - lun a vie 10pm a 6am, solo almuerzo 1 hora, tambien minimo
```

### Respuesta esperada del Gem

El Gem debe devolver **dos liquidaciones separadas**, una por empleado.

#### Juan

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Extra diurna | 6,75 | $70.349 |
| **Recargos sin prestaciones** | | **$70.349** |
| **Total con prestaciones** | | **$99.896** |

#### Pedro

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Recargo nocturno | 40,00 | $450.233 |
| **Recargos sin prestaciones** | | **$450.233** |
| **Total con prestaciones** | | **$639.331** |

---

## Ejemplo 16 — Formato informal de horas y descansos

### Entrada del usuario

```
recargos de sandra
de lunes a viernes entra 7 y sale a las 5 y media
media hora de almuerzo y 10 min de desayuno
salario minimo
```

### Información extraída

| Campo | Valor interpretado |
|-------|-------------------|
| Horario | 07:00 – 17:30 |
| Desayuno | 10 min |
| Almuerzo | 30 min |
| Efectivas/día | 9,83 h |

### Recargos semanales

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Extra diurna | 7,15 | $74.518 |
| **Recargos sin prestaciones** | | **$74.518** |
| Prestaciones (42%) | | $31.298 |
| **Total con prestaciones** | | **$105.816** |

---

## Ejemplo 17 — Día del Trabajo con horas extra (1 mayo 2026)

### Entrada del usuario

```
para ricardo semana del 28 abril al 2 mayo 2026:
lun 28 y mar 29: 7-5pm
miercoles 30 abr: 7-5pm
jueves 1 mayo: 7-7pm (trabajó el festivo hasta las 7pm)
viernes 2 mayo: 7-6pm
15 min desayuno, 1h almuerzo, salario minimo
```

### Información extraída

| Día | Fecha | Festivo | Efectivas |
|-----|-------|---------|-----------|
| Lun–Mié | 28–30 abr | No | 8,75 c/u |
| Jue | 2026-05-01 | Sí — Día del Trabajo | 10,75 |
| Vie | 2026-05-02 | No | 9,75 |

### Recargos semanales

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Recargo festivo (1 mayo, dentro 42 h) | 10,75 | $156.852 |
| Extra diurna (viernes) | 4,75 | $49.505 |
| **Recargos sin prestaciones** | | **$206.357** |
| Prestaciones (42%) | | $86.670 |
| **Total con prestaciones** | | **$293.027** |

> Lun–Mié = 26,25 h. Jueves festivo 10,75 h → total 37 h. Viernes 9,75 h → 46,75 h. Del viernes: 5 h ordinarias diurnas (sin recargo) + 4,75 h extra diurna.

---

## Ejemplo 18 — Karen H2: semana incompleta vs festivo (mayo 2026)

Caso real que expone el error de **proyectar 42 h** o el horario habitual cuando la semana no está completa.

### Entrada del usuario

```
liquida recargos de karen mayo 2026, horario operativo, gana el minimo
no trabajó 1 ni 18 de mayo
semana del 27 abril al 2 mayo: solo trabajó el sabado 2
semana del 11 al 17 mayo: lun a sab normal
```

### Horario aplicado: **H2 Operativo**

| Día | Programado | Efectivas |
|-----|------------|-----------|
| Lun–vie | 8,00 | 9,00 |
| Sábado | 5,67 | 5,67 |

Festivos mayo: **1 may** (jue) y **18 may** (lun) — **no laborados**.

---

### Semana 27 abr – 2 may — **INCOMPLETA** (solo sábado)

| Concepto | Valor |
|----------|-------|
| Días en scope | Solo sáb 2 may |
| Jornada exigible | **5,67 h** (programado del sábado; **no** usar 42 h ni lun–vie) |
| Horas efectivas | 5,67 h |
| **Horas extra** | **0** |

> **Error común del Gem:** comparar el sábado contra 42 h o contra 34 h “compensadas” por el festivo del 1 mayo. Ese festivo **no aplica** a una semana donde Karen solo debía trabajar el sábado.

| Recargos sin prestaciones | **$0** |

---

### Semana 11 – 17 may — **COMPLETA** (sin festivo en scope)

| Concepto | Horas |
|----------|-------|
| Lun–vie (×5) | 45,00 efectivas |
| Sábado | 5,67 |
| **Total efectivas** | **50,67** |
| Jornada exigible | **42,00** |
| **Extra diurna** | **8,67** |

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Extra diurna | 8,67 | $90.359 |
| **Recargos sin prestaciones** | | **$90.359** |
| Prestaciones (42%) | | $37.951 |
| **Total con prestaciones** | | **$128.310** |

---

### Semana 12 – 18 may — **COMPLETA** con festivo lun no laborado

Karen debía trabajar lun–sáb (H2). **No trabajó el festivo lunes 18 may.**

| Concepto | Valor |
|----------|-------|
| Jornada exigible | 42 − 8,00 = **34,00 h** |
| Trabajó mar–sáb (4 lv + sáb) | 41,67 h efectivas |
| **Extra diurna** | **7,67 h** |

| Concepto | Horas | Valor COP |
|----------|-------|-----------|
| Extra diurna | 7,67 | $79.937 |
| **Recargos sin prestaciones** | | **$79.937** |
| Prestaciones (42%) | | $33.574 |
| **Total con prestaciones** | | **$113.511** |

> **Error común del Gem:** liquidar 8,67 h extra como si fuera semana sin festivo, o tratar todo el sábado como extra por no “ver” la reducción de exigible.
