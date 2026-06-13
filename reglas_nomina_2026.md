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

Base legal: **42 horas semanales** en semana **completa**. Liquidación mensual o quincenal: **semana calendario por semana** (lun–dom), luego sumar. Ver `instrucciones_gem.md` para los **4 métodos**.

| Método | Cuándo | Exigible |
|--------|--------|----------|
| **1** | Semana completa | 42 h |
| **2** | Completa + festivo no laborado | 42 − programadas del festivo |
| **3** | Incompleta (quincena cortada, días sueltos) | Σ programadas día por día en scope |
| **4** | Incompleta + festivo en scope | Σ programadas en scope; festivo no laborado no suma |

Programadas y efectivas por turno → `horarios_empresa.md`. Si el usuario reporta otras horas con un turno indicado, son **efectivas reales**, no cambian las programadas del catálogo.

### Semana COMPLETA (métodos 1 y 2)

Trabajó (o debía trabajar) **todos los días habituales** del turno esa semana calendario.

```
Jornada exigible = 42 − Σ (horas programadas del festivo NO laborado)
```

Ejemplos (**H8** — programadas lun–vie 7,75 h · sáb 5,25 h):
- Festivo lunes no laborado → exigible = 42 − 7,75 = **34,25 h**
- Festivo sábado no laborado → exigible = 42 − 5,25 = **36,75 h**
- Sin festivo → **42,00 h**

Si **trabajó** el festivo → no resta; liquida recargo dominical/festivo.

### Semana INCOMPLETA (métodos 3 y 4)

Solo algunos días en scope (quincena, mes parcial, días concretos).

```
Jornada exigible = Σ (programadas del turno, solo días en scope)
```

**Prohibido:** usar 42 h; proyectar lun–sáb si no aplican; restar festivo fuera de scope.

Ejemplo — **mayo 2026**, semana 27 abr–3 may, scope solo días de mayo (vie festivo + sáb):
- Exigible = **5,25 h** (solo sáb programado; festivo no laborado no suma)
- Caso completo validado → `ejemplos_complejos.md` **Ejemplo 18**

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

1. Identificar turno (**H1–H8**) en `horarios_empresa.md`.
2. Definir periodo (quincena / mes / fechas) y días en scope por semana calendario.
3. Clasificar cada semana: método **1, 2, 3 o 4**.
4. Preguntar festivos trabados / no laborados.
5. Por semana: programadas (catálogo) vs efectivas (usuario si difieren).
6. Calcular jornada exigible → extras → recargos.
7. Sumar semanas del periodo; aplicar prestacional 42%.

---

## Prestacional

Siempre mostrar: recargos sin prestaciones | prestaciones 42% | total con prestaciones.

Redondeo: pesos enteros; horas con 2 decimales.
