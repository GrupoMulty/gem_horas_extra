# Horas Extra Colombia 2026

Fuente de conocimiento para un **Gem de Gemini**: calculadora de recargos laborales por empleado bajo normativa colombiana 2026.

## Objetivo

Liquidar por empleado:

- Horas extra (diurnas, nocturnas, dominicales/festivas).
- Recargo nocturno.
- Horas dominicales y festivas.

No incluye salario base, auxilio de transporte ni deducciones.

## Archivos

| Archivo | Propósito |
|---------|-----------|
| `reglas_nomina_2026.md` | Definiciones, tarifas Multy, jornada exigible (completa/incompleta) |
| `horarios_empresa.md` | Catálogo de turnos H1–H4 (programadas vs efectivas) |
| `festivos_colombia_2026.md` | Calendario oficial de 19 festivos 2026 |
| `calculos.py` | Lógica de referencia en Python |
| `casos_prueba.md` | Escenarios básicos validados |
| `ejemplos_complejos.md` | Escenarios avanzados con entradas reales de usuario |
| `instrucciones_gem.md` | Texto listo para pegar en el Gem de Gemini |

## Parámetros base 2026

- Salario mínimo: $1.750.905 COP
- Jornada semanal: **42 horas**
- Jornada mensual: **210 horas**
- Valor hora ordinaria (SMLV): **$8.338 COP**

## Flujo de cálculo

1. Identificar **horario de empresa** (H1–H4) o pedir entrada/salida/descansos.
2. Determinar si la semana es **completa** o **incompleta** (ver `reglas_nomina_2026.md`).
3. Preguntar si trabajó cada festivo; calcular **jornada exigible**.
4. Calcular horas efectivas (con cruce de medianoche si aplica).
5. Clasificar diurna (06:00–19:00) / nocturna (19:00–06:00).
6. Separar ordinarias de extras según exigible (no usar 42 h fijas en semanas incompletas).
7. Liquidar recargos según tipo y aplicar prestacional (42%).

## Uso con Gemini

1. Crear un Gem en [Google AI Studio](https://aistudio.google.com/).
2. Copiar el contenido de `instrucciones_gem.md` en las instrucciones.
3. Subir los archivos de conocimiento como adjuntos (`reglas_nomina_2026.md`, `horarios_empresa.md`, `festivos_colombia_2026.md`, `calculos.py`, `casos_prueba.md`, `ejemplos_complejos.md`).

## Verificar cálculos

```bash
python -c "from calculos import *; print(calcular_tarifas().hora_ordinaria)"
```

Debe retornar `8337.64...` (≈ $8.338).

```bash
python -c "from calculos import *; j=[Jornada(21,6,0,60) for _ in range(5)]; print(liquidar_semana(j).valor_recargos)"
```

Debe retornar `450233` (recargo nocturno Pedro).
