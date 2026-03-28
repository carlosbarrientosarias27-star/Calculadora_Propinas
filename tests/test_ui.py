import pytest
from app.ui import menu_interactivo

# --- Pruebas para menu_interactivo ---

def test_menu_interactivo_flujo_porcentaje_normal(monkeypatch, capsys):
    """N: Simula un flujo completo usando porcentaje (10% de 100 entre 2)."""
    # Arrange
    # Simulamos entradas: Cuenta(100), Opción(1), Porcentaje(10), Personas(2)
    entradas = iter(["100", "1", "10", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    # Act
    menu_interactivo()
    captura = capsys.readouterr()

    # Assert
    # Verificamos que el cálculo final por persona sea correcto ($55.00)
    assert "Por persona:   $55.00" in captura.out


def test_menu_interactivo_flujo_monto_fijo_normal(monkeypatch, capsys):
    """N: Simula un flujo completo usando monto fijo ($20 de propina)."""
    # Arrange
    # Entradas: Cuenta(80), Opción(2), Monto Fijo(20), Personas(4)
    entradas = iter(["80", "2", "20", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    # Act
    menu_interactivo()
    captura = capsys.readouterr()

    # Assert
    # Total 100 / 4 personas = $25.00
    assert "Por persona:   $25.00" in captura.out


def test_menu_interactivo_limite_una_persona(monkeypatch, capsys):
    """L: Verifica el resumen cuando la cuenta se divide entre una sola persona."""
    # Arrange
    entradas = iter(["50", "1", "0", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    # Act
    menu_interactivo()
    captura = capsys.readouterr()

    # Assert
    assert "Por persona:   $50.00" in captura.out


def test_menu_interactivo_error_entrada_no_numerica(monkeypatch, capsys):
    """E: Verifica el manejo de error cuando el usuario ingresa texto en lugar de números."""
    # Arrange
    # Simulamos que el usuario escribe "hola" en la cuenta
    monkeypatch.setattr("builtins.input", lambda _: "hola")

    # Act
    menu_interactivo()
    captura = capsys.readouterr()

    # Assert
    assert "Error de entrada" in captura.out


def test_menu_interactivo_edge_opcion_invalida(monkeypatch, capsys):
    """Edge: Verifica que si se elige una opción inexistente (ej. '3'), la propina sea 0."""
    # Arrange
    # Cuenta(100), Opción inválida(3), Personas(1)
    # Nota: El código actual no pide monto si la opción no es 1 o 2
    entradas = iter(["100", "3", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    # Act
    menu_interactivo()
    captura = capsys.readouterr()

    # Assert
    assert "Propina:       $0.00" in captura.out