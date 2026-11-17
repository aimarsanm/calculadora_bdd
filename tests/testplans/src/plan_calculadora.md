# Plan de Pruebas — `src/plan_calculadora`

Fuente analizada: `src/calculadora.py`. Framework: `pytest`. Test futuro: `tests/src/test_calculadora.py`.

Los enlaces de los IDs son preliminares (solo ruta de archivo). Tras implementar los tests, deben añadir `#L<línea>` con la línea de cada `def test_...`.

## Inventario de Funciones (1 función detectada)
1. `calcular`

Exclusiones: el bloque `if __name__ == '__main__'` no es función y queda fuera. Solo lee tres valores con `input()` y convierte los operandos con `int()`, por lo que no aporta lógica de cálculo propia. Si se desea cubrirlo, debe ser un test de integración aparte con `input` simulado.

Convención de IDs: `test_M_Calculadora_calcular`. `Calculadora` es un nombre asumido, porque el módulo no define clase.

---

## Función `1`: `calcular`

Firma: `calcular(numero1, numero2, operacion)`. Devuelve `respuesta` según `operacion` mediante `match`. Por defecto lanza `ValueError("Operación inválida.")`.

Nota sobre ramas: cada `case` del `match` es una rama. Como cada entrada activa exactamente un `case`, la rama FALSE de cada `case` queda cubierta por las demás filas. Por eso la tabla lista solo la rama TRUE de cada `case` y las rutas de excepción.

### CAJA BLANCA — Cobertura de Líneas y Ramas

| ID | Descripción | Tipo | Condición / Línea | Input | Expected Output |
|----|-------------|------|-------------------|-------|-----------------|
| [test_1_Calculadora_calcular](../../src/test_calculadora.py#L12) | Ejecuta la función completa de inicio a fin con suma | Line Coverage | Camino completo; incluye `case '+'` | numero1=2, numero2=3, operacion='+' | 5 |
| [test_2_Calculadora_calcular](../../src/test_calculadora.py#L22) | Activa la rama de resta | Branch TRUE | `case '-'` | numero1=5, numero2=3, operacion='-' | 2 |
| [test_3_Calculadora_calcular](../../src/test_calculadora.py#L32) | Activa la rama de multiplicación | Branch TRUE | `case '*'` | numero1=4, numero2=3, operacion='*' | 12 |
| [test_4_Calculadora_calcular](../../src/test_calculadora.py#L42) | Activa la rama de división | Branch TRUE | `case '/'` | numero1=6, numero2=3, operacion='/' | 2.0 |
| [test_5_Calculadora_calcular](../../src/test_calculadora.py#L52) | Activa la rama de potencia | Branch TRUE | `case '**'` | numero1=2, numero2=3, operacion='**' | 8 |
| [test_6_Calculadora_calcular](../../src/test_calculadora.py#L62) | Activa la rama de división entera | Branch TRUE | `case '//'` | numero1=7, numero2=2, operacion='//' | 3 |
| [test_7_Calculadora_calcular](../../src/test_calculadora.py#L72) | Activa la rama de módulo | Branch TRUE | `case '%'` | numero1=7, numero2=2, operacion='%' | 1 |
| [test_8_Calculadora_calcular](../../src/test_calculadora.py#L82) | Activa la rama de raíz cuadrada | Branch TRUE | `case '√'` | numero1=16, numero2=0, operacion='√' | 4.0 |
| [test_9_Calculadora_calcular](../../src/test_calculadora.py#L92) | Activa la rama de cubo | Branch TRUE | `case 'c'` | numero1=3, numero2=0, operacion='c' | 27 |
| [test_10_Calculadora_calcular](../../src/test_calculadora.py#L102) | Activa la rama de raíz cúbica con clave `√3` | Branch TRUE | `case '√3'` | numero1=27, numero2=0, operacion='√3' | 3.0 (comparación aproximada) |
| [test_11_Calculadora_calcular](../../src/test_calculadora.py#L112) | Activa la rama de raíz cúbica alternativa | Branch TRUE | `case 'cbrt'` | numero1=8, numero2=0, operacion='cbrt' | 2.0 (comparación aproximada) |
| [test_12_Calculadora_calcular](../../src/test_calculadora.py#L122) | Activa la rama de valor absoluto | Branch TRUE | `case 'abs'` | numero1=-5, numero2=0, operacion='abs' | 5 |
| [test_13_Calculadora_calcular](../../src/test_calculadora.py#L132) | Activa la rama de negación | Branch TRUE | `case 'neg'` | numero1=5, numero2=0, operacion='neg' | -5 |
| [test_14_Calculadora_calcular](../../src/test_calculadora.py#L142) | Activa la rama de logaritmo natural (importa `math` dentro de la rama) | Branch TRUE | `case 'ln'` | numero1=10, numero2=0, operacion='ln' | ln(10) (comparación aproximada) |
| [test_15_Calculadora_calcular](../../src/test_calculadora.py#L152) | Activa el caso por defecto con operación desconocida | Branch TRUE (default) | `case _` → `raise ValueError` | numero1=1, numero2=2, operacion='x' | `ValueError` con mensaje "Operación inválida." |
| [test_16_Calculadora_calcular](../../src/test_calculadora.py#L161) | Ejecuta la ruta de excepción de `math.log` con cero | Branch EXC | `case 'ln'` → llamada `math.log(0)` | numero1=0, numero2=0, operacion='ln' | `ValueError` de dominio de `math` (mensaje distinto de "Operación inválida.") |

> Candidatos a parametrización: IDs test_2 a test_14 (mismo test con `operacion` y resultado esperado). Los IDs test_10 y test_11 comparten resultado aproximado y son candidatos del mismo grupo. test_15 y test_16 se verifican con `pytest.raises` y deben distinguirse por mensaje.

### CAJA NEGRA — EP y Valores Límite

| ID | Descripción | Técnica | Clase / Límite | Input | Expected Output |
|----|-------------|---------|----------------|-------|-----------------|
| [test_17_Calculadora_calcular](../../src/test_calculadora.py#L172) | Resta de enteros positivos devuelve la diferencia | EP Válida | Binaria, enteros positivos | numero1=7, numero2=3, operacion='-' | 4 |
| [test_18_Calculadora_calcular](../../src/test_calculadora.py#L182) | Multiplicación de enteros negativos devuelve producto positivo | EP Válida | Binaria, negativos | numero1=-4, numero2=-6, operacion='*' | 24 |
| [test_19_Calculadora_calcular](../../src/test_calculadora.py#L192) | Suma de decimales devuelve el resultado decimal | EP Válida | Binaria, flotantes | numero1=2.5, numero2=0.5, operacion='+' | 3.0 |
| [test_20_Calculadora_calcular](../../src/test_calculadora.py#L202) | División con divisor no nulo devuelve cociente real | EP Válida | Binaria, divisor distinto de cero | numero1=7, numero2=2, operacion='/' | 3.5 |
| [test_21_Calculadora_calcular](../../src/test_calculadora.py#L212) | Raíz cuadrada de positivo; `numero2` no influye | EP Válida | Unaria, entrada positiva | numero1=9, numero2=0, operacion='√' | 3.0 |
| [test_22_Calculadora_calcular](../../src/test_calculadora.py#L222) | Cubo de negativo devuelve negativo | EP Válida | Unaria, entrada negativa | numero1=-2, numero2=0, operacion='c' | -8 |
| [test_23_Calculadora_calcular](../../src/test_calculadora.py#L232) | Operación desconocida rechazada | EP Inválida | Cadena no reconocida | numero1=1, numero2=2, operacion='x' | `ValueError` "Operación inválida." |
| [test_24_Calculadora_calcular](../../src/test_calculadora.py#L241) | Operación en mayúsculas rechazada (sensible a mayúsculas) | EP Inválida | Cadena con otra capitalización | numero1=4, numero2=2, operacion='ABS' | `ValueError` "Operación inválida." |
| [test_25_Calculadora_calcular](../../src/test_calculadora.py#L250) | Operación vacía rechazada | EP Inválida | Cadena vacía | numero1=4, numero2=2, operacion='' | `ValueError` "Operación inválida." |
| [test_26_Calculadora_calcular](../../src/test_calculadora.py#L259) | Operación `None` rechazada | EP Inválida | Tipo no cadena | numero1=4, numero2=2, operacion=None | `ValueError` "Operación inválida." (tipo no validado explícitamente; ver ambigüedades) |
| [test_27_Calculadora_calcular](../../src/test_calculadora.py#L268) | Operación con espacio sobrante rechazada | EP Inválida | Cadena con espacios | numero1=2, numero2=3, operacion=' +' | `ValueError` "Operación inválida." |
| [test_28_Calculadora_calcular](../../src/test_calculadora.py#L277) | Logaritmo de 1 devuelve 0 | EP Válida | `ln`, positivo | numero1=1, numero2=0, operacion='ln' | 0.0 |
| [test_29_Calculadora_calcular](../../src/test_calculadora.py#L287) | Logaritmo de negativo rechazado por dominio | EP Inválida | `ln`, valor no positivo | numero1=-1, numero2=0, operacion='ln' | `ValueError` de dominio de `math` |
| [test_30_Calculadora_calcular](../../src/test_calculadora.py#L298) | División por cero lanza error | EP Inválida | `/`, divisor cero | numero1=5, numero2=0, operacion='/' | `ZeroDivisionError` |
| [test_31_Calculadora_calcular](../../src/test_calculadora.py#L307) | División entera por cero lanza error | EP Inválida | `//`, divisor cero | numero1=5, numero2=0, operacion='//' | `ZeroDivisionError` |
| [test_32_Calculadora_calcular](../../src/test_calculadora.py#L316) | Módulo por cero lanza error | EP Inválida | `%`, divisor cero | numero1=5, numero2=0, operacion='%' | `ZeroDivisionError` |
| [test_33_Calculadora_calcular](../../src/test_calculadora.py#L325) | Cero elevado a exponente negativo lanza error | EP Inválida | `**`, base cero y exponente negativo | numero1=0, numero2=-1, operacion='**' | `ZeroDivisionError` |
| [test_34_Calculadora_calcular](../../src/test_calculadora.py#L334) | Operandos no numéricos rechazados | EP Inválida | Tipo no numérico | numero1='a', numero2=1, operacion='+' | `TypeError` (por definir; ver ambigüedades) |
| [test_35_Calculadora_calcular](../../src/test_calculadora.py#L353) | Raíz de negativo | EP Límite de dominio | `√` y `cbrt` con negativo | numero1=-4, numero2=0, operacion='√' | ValueError (xfail estricto hasta cambiar calculadora.py) |
| [test_36_Calculadora_calcular](../../src/test_calculadora.py#L362) | `√3` y `cbrt` dan el mismo resultado para la misma entrada | EP Equivalencia | Claves alias | numero1=27, numero2=0, operacion='√3' y operacion='cbrt' | Ambos iguales (comparación aproximada) |
| [test_37_Calculadora_calcular](../../src/test_calculadora.py#L373) | Cero elevado a cero | BVA Límite | `**`, base 0 y exponente 0 | numero1=0, numero2=0, operacion='**' | 1 |
| [test_38_Calculadora_calcular](../../src/test_calculadora.py#L383) | Raíz cuadrada en el límite inferior | BVA Límite | `√`, valor 0 | numero1=0, numero2=0, operacion='√' | 0.0 |
| [test_39_Calculadora_calcular](../../src/test_calculadora.py#L393) | Cubo en el límite cero | BVA Límite | `c`, valor 0 | numero1=0, numero2=0, operacion='c' | 0 |
| [test_40_Calculadora_calcular](../../src/test_calculadora.py#L403) | Valor absoluto en el límite cero | BVA Límite | `abs`, valor 0 | numero1=0, numero2=0, operacion='abs' | 0 |
| [test_41_Calculadora_calcular](../../src/test_calculadora.py#L413) | Negación en el límite cero | BVA Límite | `neg`, valor 0 | numero1=0, numero2=0, operacion='neg' | 0 |
| [test_42_Calculadora_calcular](../../src/test_calculadora.py#L423) | Logaritmo justo por encima del límite de dominio | BVA Límite+ | `ln`, valor 0.001 | numero1=0.001, numero2=0, operacion='ln' | ln(0.001) (comparación aproximada) |
| [test_43_Calculadora_calcular](../../src/test_calculadora.py#L433) | Módulo con dividendo negativo sigue el signo del divisor | BVA Límite | `%`, dividendo negativo | numero1=-7, numero2=3, operacion='%' | 2 |
| [test_44_Calculadora_calcular](../../src/test_calculadora.py#L443) | División entera con dividendo negativo redondea hacia menos infinito | BVA Límite | `//`, dividendo negativo | numero1=-7, numero2=2, operacion='//' | -4 |
| [test_45_Calculadora_calcular](../../src/test_calculadora.py#L453) | Raíz cúbica en el valor identidad | BVA Límite | `cbrt`, valor 1 | numero1=1, numero2=0, operacion='cbrt' | 1.0 (comparación aproximada) |

> Candidatos a parametrización: IDs test_17 a test_22 (aritmética y unarias válidas, mismo test con parámetros). IDs test_23 a test_27 (operaciones inválidas, `pytest.raises(ValueError)`). IDs test_30 a test_33 (`pytest.raises(ZeroDivisionError)`). IDs test_37 a test_41 (límites de cero). IDs test_42, test_28 y test_29 (dominio de `ln`).

---

## Ambigüedades y datos faltantes

1. `√3` frente a `cbrt`: ambas ramas calculan `numero1 ** (1/3)`, no una raíz cúbica real. Para valores negativos devuelven un número complejo (por ejemplo, −8 da un complejo, no −2). Falta decidir si se espera −2, un error o el complejo. Afecta a test_35 y a la coherencia de test_10 y test_11.
2. `√` con negativos: mismo problema que el anterior, pero para la raíz cuadrada. Pendiente de decisión (test_35).
3. División entre cero: el código no la controla. Se asume `ZeroDivisionError` (test_30 a test_33). Falta confirmar si el contrato debe ser ese error o un error propio.
4. `numero2` en operaciones unarias (`√`, `c`, `√3`, `cbrt`, `abs`, `neg`, `ln`) se ignora. Se asume que cualquier valor es válido; no se especifica.
5. Tipos no validados: `operacion=None` (test_26) se trata como inválida por caer en el `case _`. Operandos no numéricos (test_34) producen `TypeError` por Python, sin contrato explícito.
6. `ln` con valor no positivo: `math.log` lanza `ValueError` con mensaje de dominio. Se debe distinguir del `ValueError` de operación inválida (test_15 y test_16 comprueban el mensaje).
7. Precisión de punto flotante: `√3`, `cbrt`, `ln`, `√` y `/` requieren comparación aproximada, no igualdad exacta.
8. Desbordamiento (`OverflowError`) con potencias de flotantes muy grandes: no está especificado y no se incluye en el plan.
9. El bloque `__main__` queda fuera del plan (ver Inventario).
10. Raíz de negativos (`√`, `√3`, `cbrt` con valor negativo; test_35): decisión de contrato ValueError. El código devuelve número complejo, así que test_35 es xfail estricto. No se modifica `calculadora.py`.
11. División por cero (test_30 a test_33): se espera `ZeroDivisionError` nativo de Python.
12. Tipos no válidos: `operacion=None` (test_26) produce `ValueError` "Operación inválida." por el `case _`; operandos no numéricos (test_34, p. ej. `'a' + 1`) producen `TypeError` nativo.
13. Logaritmo de no positivo (test_16, test_29): `ValueError` de dominio de `math`; el mensaje se verifica distinto de "Operación inválida.".

## Resumen

| Función | Caja Blanca | Caja Negra | Total IDs |
|---------|-------------|------------|-----------|
| `calcular` | 16 (1 Line Coverage + 14 ramas TRUE + 1 default + 1 excepción de `math.log`) | 29 (EP y BVA) | 45 (test_1 a test_45) |

Ruta del plan: `tests/testplans/src/plan_calculadora.md`.
