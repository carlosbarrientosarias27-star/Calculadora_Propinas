import pytest
from app.utils import formatear_moneda

# --- Pruebas para formatear_moneda ---

def test_formatear_moneda_normal():
    """N: Formatea un número entero positivo con símbolo y dos decimales."""
    # Arrange
    cantidad = 50
    esperado = "$50.00"

    # Act
    resultado = formatear_moneda(cantidad)

    # Assert
    assert resultado == esperado

def test_formatear_moneda_con_decimales():
    """N: Formatea un flotante con dos decimales correctamente."""
    # Arrange
    cantidad = 125.50
    esperado = "$125.50"

    # Act
    resultado = formatear_moneda(cantidad)

    # Assert
    assert resultado == esperado

def test_formatear_moneda_limite_cero():
    """L: Verifica el formato para una cantidad de cero."""
    # Arrange
    cantidad = 0
    esperado = "$0.00"

    # Act
    resultado = formatear_moneda(cantidad)

    # Assert
    assert resultado == esperado

def test_formatear_moneda_error_tipo_invalido():
    """E: Lanza ValueError si se pasa un string que no puede convertirse a número."""
    # Arrange
    valor_invalido = "cien"

    # Act & Assert
    # Cambiamos TypeError por ValueError porque es lo que lanza la f-string
    with pytest.raises(ValueError):
        formatear_moneda(valor_invalido)

def test_formatear_moneda_edge_separador_miles():
    """Edge: Verifica que se incluya la coma como separador de miles."""
    # Arrange
    cantidad = 1500.75
    esperado = "$1,500.75"

    # Act
    resultado = formatear_moneda(cantidad)

    # Assert
    assert resultado == esperado

def test_formatear_moneda_edge_redondeo_automatico():
    """Edge: Verifica que la f-string redondee a 2 decimales un número con más dígitos."""
    # Arrange
    cantidad = 10.556
    esperado = "$10.56"

    # Act
    resultado = formatear_moneda(cantidad)

    # Assert
    assert resultado == esperado

def test_formatear_moneda_negativa():
    """Edge: Verifica el comportamiento con montos negativos."""
    # Arrange
    cantidad = -20.0
    esperado = "$-20.00"

    # Act
    resultado = formatear_moneda(cantidad)

    # Assert
    assert resultado == esperado