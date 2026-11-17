import math
import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "src"))

from calculadora import calcular  # noqa: E402


def test_suma_flujo_completo():
    # Test ID  : test_1_Calculadora_calcular
    # Descripción: Ejecuta la función completa de inicio a fin con suma
    numero1, numero2, operacion = 2, 3, '+'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == 5


def test_resta_activa_rama():
    # Test ID  : test_2_Calculadora_calcular
    # Descripción: Activa la rama de resta
    numero1, numero2, operacion = 5, 3, '-'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == 2


def test_multiplicacion_activa_rama():
    # Test ID  : test_3_Calculadora_calcular
    # Descripción: Activa la rama de multiplicación
    numero1, numero2, operacion = 4, 3, '*'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == 12


def test_division_activa_rama():
    # Test ID  : test_4_Calculadora_calcular
    # Descripción: Activa la rama de división
    numero1, numero2, operacion = 6, 3, '/'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == pytest.approx(2.0)


def test_potencia_activa_rama():
    # Test ID  : test_5_Calculadora_calcular
    # Descripción: Activa la rama de potencia
    numero1, numero2, operacion = 2, 3, '**'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == 8


def test_division_entera_activa_rama():
    # Test ID  : test_6_Calculadora_calcular
    # Descripción: Activa la rama de división entera
    numero1, numero2, operacion = 7, 2, '//'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == 3


def test_modulo_activa_rama():
    # Test ID  : test_7_Calculadora_calcular
    # Descripción: Activa la rama de módulo
    numero1, numero2, operacion = 7, 2, '%'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == 1


def test_raiz_cuadrada_activa_rama():
    # Test ID  : test_8_Calculadora_calcular
    # Descripción: Activa la rama de raíz cuadrada
    numero1, numero2, operacion = 16, 0, '√'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == pytest.approx(4.0)


def test_cubo_activa_rama():
    # Test ID  : test_9_Calculadora_calcular
    # Descripción: Activa la rama de cubo
    numero1, numero2, operacion = 3, 0, 'c'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == 27


def test_raiz_cubica_clave_raiz3_activa_rama():
    # Test ID  : test_10_Calculadora_calcular
    # Descripción: Activa la rama de raíz cúbica con clave `√3`
    numero1, numero2, operacion = 27, 0, '√3'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == pytest.approx(3.0)


def test_raiz_cubica_clave_cbrt_activa_rama():
    # Test ID  : test_11_Calculadora_calcular
    # Descripción: Activa la rama de raíz cúbica alternativa
    numero1, numero2, operacion = 8, 0, 'cbrt'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == pytest.approx(2.0)


def test_valor_absoluto_activa_rama():
    # Test ID  : test_12_Calculadora_calcular
    # Descripción: Activa la rama de valor absoluto
    numero1, numero2, operacion = -5, 0, 'abs'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == 5


def test_negacion_activa_rama():
    # Test ID  : test_13_Calculadora_calcular
    # Descripción: Activa la rama de negación
    numero1, numero2, operacion = 5, 0, 'neg'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == -5


def test_logaritmo_natural_activa_rama():
    # Test ID  : test_14_Calculadora_calcular
    # Descripción: Activa la rama de logaritmo natural (importa `math` dentro de la rama)
    numero1, numero2, operacion = 10, 0, 'ln'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == pytest.approx(math.log(10))


def test_operacion_desconocida_activa_default():
    # Test ID  : test_15_Calculadora_calcular
    # Descripción: Activa el caso por defecto con operación desconocida
    numero1, numero2, operacion = 1, 2, 'x'

    with pytest.raises(ValueError, match="Operación inválida."):
        calcular(numero1, numero2, operacion)


def test_ln_cero_lanza_excepcion_de_math():
    # Test ID  : test_16_Calculadora_calcular
    # Descripción: Ejecuta la ruta de excepción de `math.log` con cero
    numero1, numero2, operacion = 0, 0, 'ln'

    with pytest.raises(ValueError) as exc_info:
        calcular(numero1, numero2, operacion)

    assert str(exc_info.value) != "Operación inválida."


def test_resta_enteros_positivos():
    # Test ID  : test_17_Calculadora_calcular
    # Descripción: Resta de enteros positivos devuelve la diferencia
    numero1, numero2, operacion = 7, 3, '-'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == 4


def test_multiplicacion_negativos_producto_positivo():
    # Test ID  : test_18_Calculadora_calcular
    # Descripción: Multiplicación de enteros negativos devuelve producto positivo
    numero1, numero2, operacion = -4, -6, '*'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == 24


def test_suma_decimales():
    # Test ID  : test_19_Calculadora_calcular
    # Descripción: Suma de decimales devuelve el resultado decimal
    numero1, numero2, operacion = 2.5, 0.5, '+'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == pytest.approx(3.0)


def test_division_divisor_no_nulo():
    # Test ID  : test_20_Calculadora_calcular
    # Descripción: División con divisor no nulo devuelve cociente real
    numero1, numero2, operacion = 7, 2, '/'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == pytest.approx(3.5)


def test_raiz_cuadrada_positivo_ignora_numero2():
    # Test ID  : test_21_Calculadora_calcular
    # Descripción: Raíz cuadrada de positivo; `numero2` no influye
    numero1, numero2, operacion = 9, 0, '√'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == pytest.approx(3.0)


def test_cubo_negativo_devuelve_negativo():
    # Test ID  : test_22_Calculadora_calcular
    # Descripción: Cubo de negativo devuelve negativo
    numero1, numero2, operacion = -2, 0, 'c'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == -8


def test_operacion_desconocida_rechazada():
    # Test ID  : test_23_Calculadora_calcular
    # Descripción: Operación desconocida rechazada
    numero1, numero2, operacion = 1, 2, 'x'

    with pytest.raises(ValueError, match="Operación inválida."):
        calcular(numero1, numero2, operacion)


def test_operacion_mayusculas_rechazada():
    # Test ID  : test_24_Calculadora_calcular
    # Descripción: Operación en mayúsculas rechazada (sensible a mayúsculas)
    numero1, numero2, operacion = 4, 2, 'ABS'

    with pytest.raises(ValueError, match="Operación inválida."):
        calcular(numero1, numero2, operacion)


def test_operacion_vacia_rechazada():
    # Test ID  : test_25_Calculadora_calcular
    # Descripción: Operación vacía rechazada
    numero1, numero2, operacion = 4, 2, ''

    with pytest.raises(ValueError, match="Operación inválida."):
        calcular(numero1, numero2, operacion)


def test_operacion_none_rechazada():
    # Test ID  : test_26_Calculadora_calcular
    # Descripción: Operación `None` rechazada
    numero1, numero2, operacion = 4, 2, None

    with pytest.raises(ValueError, match="Operación inválida."):
        calcular(numero1, numero2, operacion)


def test_operacion_con_espacio_rechazada():
    # Test ID  : test_27_Calculadora_calcular
    # Descripción: Operación con espacio sobrante rechazada
    numero1, numero2, operacion = 2, 3, ' +'

    with pytest.raises(ValueError, match="Operación inválida."):
        calcular(numero1, numero2, operacion)


def test_logaritmo_de_uno_es_cero():
    # Test ID  : test_28_Calculadora_calcular
    # Descripción: Logaritmo de 1 devuelve 0
    numero1, numero2, operacion = 1, 0, 'ln'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == pytest.approx(0.0)


def test_logaritmo_negativo_rechazado_por_dominio():
    # Test ID  : test_29_Calculadora_calcular
    # Descripción: Logaritmo de negativo rechazado por dominio
    numero1, numero2, operacion = -1, 0, 'ln'

    with pytest.raises(ValueError) as exc_info:
        calcular(numero1, numero2, operacion)

    assert str(exc_info.value) != "Operación inválida."


def test_division_por_cero_lanza_error():
    # Test ID  : test_30_Calculadora_calcular
    # Descripción: División por cero lanza error
    numero1, numero2, operacion = 5, 0, '/'

    with pytest.raises(ZeroDivisionError):
        calcular(numero1, numero2, operacion)


def test_division_entera_por_cero_lanza_error():
    # Test ID  : test_31_Calculadora_calcular
    # Descripción: División entera por cero lanza error
    numero1, numero2, operacion = 5, 0, '//'

    with pytest.raises(ZeroDivisionError):
        calcular(numero1, numero2, operacion)


def test_modulo_por_cero_lanza_error():
    # Test ID  : test_32_Calculadora_calcular
    # Descripción: Módulo por cero lanza error
    numero1, numero2, operacion = 5, 0, '%'

    with pytest.raises(ZeroDivisionError):
        calcular(numero1, numero2, operacion)


def test_cero_elevado_exponente_negativo_lanza_error():
    # Test ID  : test_33_Calculadora_calcular
    # Descripción: Cero elevado a exponente negativo lanza error
    numero1, numero2, operacion = 0, -1, '**'

    with pytest.raises(ZeroDivisionError):
        calcular(numero1, numero2, operacion)


def test_operandos_no_numericos_rechazados():
    # Test ID  : test_34_Calculadora_calcular
    # Descripción: Operandos no numéricos rechazados
    numero1, numero2, operacion = 'a', 1, '+'

    with pytest.raises(TypeError):
        calcular(numero1, numero2, operacion)


@pytest.mark.xfail(
    raises=pytest.fail.Exception,
    strict=True,
    reason="Contrato pendiente: el código devuelve complejo para negativos",
)
@pytest.mark.parametrize(
    "numero1, operacion",
    [(-4, '√'), (-8, '√3')],
    ids=["raiz_cuadrada_negativo", "raiz_cubica_negativo"],
)
def test_raiz_de_negativo_lanza_value_error(numero1, operacion):
    # Test ID  : test_35_Calculadora_calcular
    # Descripción: Raíz de negativo
    numero2 = 0

    with pytest.raises(ValueError):
        calcular(numero1, numero2, operacion)


def test_raiz_cubica_alias_equivalentes():
    # Test ID  : test_36_Calculadora_calcular
    # Descripción: `√3` y `cbrt` dan el mismo resultado para la misma entrada
    numero1, numero2 = 27, 0

    resultado_raiz3 = calcular(numero1, numero2, '√3')
    resultado_cbrt = calcular(numero1, numero2, 'cbrt')

    assert resultado_raiz3 == pytest.approx(resultado_cbrt)


def test_cero_elevado_cero():
    # Test ID  : test_37_Calculadora_calcular
    # Descripción: Cero elevado a cero
    numero1, numero2, operacion = 0, 0, '**'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == 1


def test_raiz_cuadrada_limite_inferior():
    # Test ID  : test_38_Calculadora_calcular
    # Descripción: Raíz cuadrada en el límite inferior
    numero1, numero2, operacion = 0, 0, '√'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == pytest.approx(0.0)


def test_cubo_en_limite_cero():
    # Test ID  : test_39_Calculadora_calcular
    # Descripción: Cubo en el límite cero
    numero1, numero2, operacion = 0, 0, 'c'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == 0


def test_valor_absoluto_en_limite_cero():
    # Test ID  : test_40_Calculadora_calcular
    # Descripción: Valor absoluto en el límite cero
    numero1, numero2, operacion = 0, 0, 'abs'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == 0


def test_negacion_en_limite_cero():
    # Test ID  : test_41_Calculadora_calcular
    # Descripción: Negación en el límite cero
    numero1, numero2, operacion = 0, 0, 'neg'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == 0


def test_logaritmo_justo_sobre_limite_dominio():
    # Test ID  : test_42_Calculadora_calcular
    # Descripción: Logaritmo justo por encima del límite de dominio
    numero1, numero2, operacion = 0.001, 0, 'ln'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == pytest.approx(math.log(0.001))


def test_modulo_dividendo_negativo_sigue_signo_divisor():
    # Test ID  : test_43_Calculadora_calcular
    # Descripción: Módulo con dividendo negativo sigue el signo del divisor
    numero1, numero2, operacion = -7, 3, '%'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == 2


def test_division_entera_dividendo_negativo_redondea_a_menos_infinito():
    # Test ID  : test_44_Calculadora_calcular
    # Descripción: División entera con dividendo negativo redondea hacia menos infinito
    numero1, numero2, operacion = -7, 2, '//'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == -4


def test_raiz_cubica_en_identidad():
    # Test ID  : test_45_Calculadora_calcular
    # Descripción: Raíz cúbica en el valor identidad
    numero1, numero2, operacion = 1, 0, 'cbrt'

    resultado = calcular(numero1, numero2, operacion)

    assert resultado == pytest.approx(1.0)
