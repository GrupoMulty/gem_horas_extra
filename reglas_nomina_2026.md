# Reglas Nómina Colombia 2026 — Multy

Fuente de verdad para el Gem: **recargos** (extras, nocturno, dominical/festivo).

## Alcance

**Sí liquida:** horas extra, recargo nocturno, horas dominicales/festivas, prestacional 42% sobre recargos.

**No liquida:** salario base, auxilio de transporte, deducciones (salvo petición explícita).

Puede liquidar **cualquier empleado** aunque no esté en un registro: basta con saber **qué horario de empresa** aplica (`horarios_empresa.md`).

---

## Parámetros base

| Concepto | Valor |
|----------|-------|
| Salario mínimo 2026 | $1.750.905 COP |
| Jornada semanal máxima | 42 horas |
| Jornada mensual (divisor) | 210 horas |
| Factor prestacional | 42% |

Semana calendario: **lunes a domingo**. Festivos: `festivos_colombia_2026.md`.

---

## Tarifas horarias Multy 2026

Salario variable: `Hora ordinaria = Salario mensual ÷ 210`, luego aplicar factores.

| Concepto | Factor | SMLV |
|----------|--------|------|
| Ordinaria | — | $8.338 |
| Ordinaria nocturna | × 1,35 | $11.256 |
| Extra diurna | × 1,25 | $10.422 |
| Extra nocturna | × 1,75 | $14.591 |
| Dominical/festiva | × 1,75 | $14.591 |
| Extra dominical/festiva diurna | × 2,00 | $16.675 |
| Extra dominical/festiva nocturna | × 2,50 | $20.844 |

Franjas: diurna **06:00–19:00** | nocturna **19:00–06:00**.

---

## Horarios de empresa

Usar catálogo en `horarios_empresa.md`. Preguntar: **¿En qué horario trabaja [nombre]?**

Cada horario define:
- Días laborados
- Entrada / salida / descansos
- **Horas programadas** por tipo de día (para exigible y festivos)
- **Horas efectivas** (tiempo real trabajado)

---

## Jornada ordinaria exigible

Base legal: **42 horas semanales**. Ajuste por festivos **no laborados** en días que el empleado habría trabajado según su horario.

### Semana COMPLETA

Trabajó (o debía trabajar) **todos los días habituales** del horario en esa semana calendario.

```
Jornada exigible = 42 − Σ (horas programadas del festivo NO laborado)
```

Ejemplos (horario H2):
- Festivo lunes no laborado → resta **8 h** → exigible = **34 h**
- Festivo sábado no laborado → resta **5,67 h** → exigible = **36,33 h**

Si **trabajó** el festivo → no resta; liquida recargo dominical/festivo.

### Semana INCOMPLETA — REGLA CRÍTICA

Solo trabajó **algunos días** de la semana (ej. únicamente un sábado, semana corta, empleado que no vino varios días).

```
Jornada exigible = Σ (horas programadas SOLO de los días que debía trabajar EN ESA semana)
```

**Prohibido** en semanas incompletas:
- Usar 42 h fijas.
- Proyectar el horario habitual completo (lun–sáb) si esos días **no aplican** esa semana.
- Tratar todo el sábado como extra por comparar contra 42 h o contra 34 h “compensadas”.

Ejemplo — solo sábado 2 mayo (festivo vie 1 mayo no laborado):
- Días en scope: **solo sábado**
- Exigible = **5,67 h** (programado del sábado)
- Trabajó 5,67 h → **0 h extra**

### Horas extra

```
Horas extra = max(0, horas efectivas trabajadas − jornada exigible)
```

Solo hay extra si trabajó **más** de lo acordado/programado para **esa** semana.

Clasificar extras según franja y si el día es festivo/dominical (árbol abajo).

---

## Descansos

Descontar desayuno + almuerzo del tiempo trabajado. Solo importa la **duración total**, no la hora.

Cruce de medianoche: si salida ≤ entrada, la salida es del día siguiente.

---

## Árbol de decisión (recargo)

```
¿Es domingo o festivo TRABAJADO?
├─ SÍ → ¿Supera jornada exigible de la semana?
│       ├─ NO → Recargo dominical/festivo (× 1,75)
│       └─ SÍ → Extra dominical diurna (× 2,00) o nocturna (× 2,50)
└─ NO (día hábil) → ¿Supera jornada exigible?
        ├─ NO → ¿Franja nocturna? → Recargo nocturno (× 1,35)
        └─ SÍ → Extra diurna (× 1,25) o nocturna (× 1,75)
```

Una hora → una sola tarifa (no acumular recargos).

---

## Orden de cálculo

1. Identificar horario de empresa (H1–H4 u otro).
2. Determinar días en scope de la semana (¿completa o incompleta?).
3. Identificar festivos; preguntar si los trabajó.
4. Calcular **jornada exigible** (completa vs incompleta).
5. Calcular horas efectivas por día trabajado.
6. Clasificar diurna / nocturna.
7. Separar ordinarias vs extras según exigible.
8. Liquidar recargos y prestacional 42%.

---

## Prestacional

Siempre mostrar: recargos sin prestaciones | prestaciones 42% | total con prestaciones.

Redondeo: pesos enteros; horas con 2 decimales.
