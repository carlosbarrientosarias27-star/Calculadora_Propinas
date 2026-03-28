import pytest
from app.logic import calcular_propina_porcentaje, calcular_propina_fija, dividir_cuenta

# --- Pruebas para calcular_propina_porcentaje ---

def test_calcular_propina_porcentaje_normal():
    """N: Calcula correctamente el 10% de una cuenta de 100."""
    # Arrange
    monto = 100.0
    porcentaje = 10.0
    esperado = 10.0

    # Act
    resultado = calcular_propina_porcentaje(monto, porcentaje)

    # Assert
    assert resultado == esperado

def test_calcular_propina_porcentaje_limite_cero():
    """L: Verifica que la propina sea 0 cuando el porcentaje es 0%."""
    # Arrange
    monto = 50.0
    porcentaje = 0.0
    esperado = 0.0

    # Act
    resultado = calcular_propina_porcentaje(monto, porcentaje)

    # Assert
    assert resultado == esperado

def test_calcular_propina_porcentaje_error_negativo():
    """E: Lanza ValueError si el monto de la cuenta es negativo."""
    # Arrange
    monto = -10.0
    porcentaje = 15.0

    # Act & Assert
    with pytest.raises(ValueError, match="El monto y el porcentaje deben ser positivos."):
        calcular_propina_porcentaje(monto, porcentaje)

def test_calcular_propina_porcentaje_edge_monto_muy_pequeno():
    """Edge: Maneja correctamente porcentajes en montos decimales mínimos."""
    # Arrange
    monto = 0.01
    porcentaje = 50.0
    esperado = 0.005

    # Act
    resultado = calcular_propina_porcentaje(monto, porcentaje)

    # Assert
    assert resultado == esperado

# --- Pruebas para calcular_propina_fija ---

def test_calcular_propina_fija_normal():
    """N: Retorna el monto de propina fija ingresado."""
    # Arrange
    monto_cuenta = 200.0
    propina_fija = 30.0
    esperado = 30.0

    # Act
    resultado = calcular_propina_fija(monto_cuenta, propina_fija)

    # Assert
    assert resultado == esperado

def test_calcular_propina_fija_error_propina_negativa():
    """E: Lanza ValueError si la propina fija es negativa."""
    # Arrange
    monto_cuenta = 100.0
    propina_negativa = -5.0

    # Act & Assert
    with pytest.raises(ValueError, match="Los montos deben ser positivos."):
        calcular_propina_fija(monto_cuenta, propina_negativa)

# --- Pruebas para dividir_cuenta ---

def test_dividir_cuenta_normal():
    """N: Divide una cuenta de 100 entre 4 personas equitativamente."""
    # Arrange
    monto_total = 100.0
    num_personas = 4
    esperado = 25.0

    # Act
    resultado = dividir_cuenta(monto_total, num_personas)

    # Assert
    assert resultado == esperado

def test_dividir_cuenta_limite_una_persona():
    """L: Verifica el resultado cuando solo hay 1 persona (total íntegro)."""
    # Arrange
    monto_total = 85.50
    num_personas = 1
    esperado = 85.50

    # Act
    resultado = dividir_cuenta(monto_total, num_personas)

    # Assert
    assert resultado == esperado

def test_dividir_cuenta_error_cero_personas():
    """E: Lanza ValueError al intentar dividir entre cero personas."""
    # Arrange
    monto_total = 100.0
    num_personas = 0

    # Act & Assert
    with pytest.raises(ValueError, match="El número de personas debe ser al menos 1."):
        dividir_cuenta(monto_total, num_personas)

def test_dividir_cuenta_edge_decimales_periodicos():
    """Edge: Verifica que el redondeo a 4 decimales funcione en divisiones infinitas."""
    # Arrange
    monto_total = 100.0
    num_personas = 3
    esperado = 33.3333

    # Act
    resultado = dividir_cuenta(monto_total, num_personas)

    # Assert
    assert resultado == esperado