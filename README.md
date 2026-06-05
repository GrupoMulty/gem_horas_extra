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
| `reglas_nomina_2026.md` | Definiciones, tarifas, flujo y árbol de decisión |
| `festivos_colombia_2026.md` | Calendario oficial de 19 festivos 2026 |
| `calculos.py` | Lógica de referencia en Python |
| `casos_prueba.md` | Escenarios básicos validados |
| `ejemplos_complejos.md` | Escenarios avanzados con entradas reales de usuario |
| `instrucciones_gem.md` | Texto listo para pegar en el Gem de Gemini |

## Parámetros base 2026

- Salario mínimo: $1.750.000 COP
- Jornada semanal: 44 horas
- Jornada mensual: 220 horas
- Valor hora ordinaria (SMLV): $7.954,55 COP

## Flujo de cálculo

1. Recibir horarios, descansos y salario del empleado.
2. Calcular horas efectivas (con cruce de medianoche si aplica).
3. Clasificar en diurna / nocturna.
4. Identificar domingos y festivos.
5. Acumular semana y separar ordinarias (44 h) de extras.
6. Liquidar recargos según tipo.
7. Aplicar prestacional (42%) y presentar desglose.

## Uso con Gemini

1. Crear un Gem en [Google AI Studio](https://aistudio.google.com/).
2. Copiar el contenido de `instrucciones_gem.md` en las instrucciones.
3. Subir los 5 archivos de conocimiento como adjuntos.

## Verificar cálculos

```bash
python -c "from calculos import *; print(calcular_horas_efectivas(7, 17, 15, 60))"
```

Debe retornar `8.75`.

```bash
python -c "from calculos import *; j=[Jornada(21,6,0,60) for _ in range(5)]; print(liquidar_semana(j).valor_recargos)"
```

Debe retornar `429545` (recargo nocturno Pedro).
