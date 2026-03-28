import pytest
from app.ui import menu_interactivo

# --- Pruebas para menu_interactivo (Versión con Bucle y Salida) ---

def test_menu_interactivo_salir_inmediato(monkeypatch, capsys):
    """N: Verifica que el programa termine correctamente al escribir 'salir' al inicio."""
    # Arrange
    monkeypatch.setattr("builtins.input", lambda _: "salir")

    # Act
    menu_interactivo()
    captura = capsys.readouterr()

    # Assert
    assert "¡Gracias por usar la calculadora! 👋" in captura.out


def test_menu_interactivo_opcion_salir_menu(monkeypatch, capsys):
    """N: Verifica que la opción '3' del menú de propinas finalice el programa."""
    # Arrange
    entradas = iter(["100", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    # Act
    menu_interactivo()
    captura = capsys.readouterr()

    # Assert
    assert "¡Hasta luego! 👋" in captura.out


def test_menu_interactivo_flujo_normal_y_salir(monkeypatch, capsys):
    """N: Realiza un cálculo completo y luego sale del programa."""
    # Arrange
    # Flujo: Cuenta(100) -> Opción(1) -> Pct(10) -> Personas(2) -> Salir
    entradas = iter(["100", "1", "10", "2", "salir"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    # Act
    menu_interactivo()
    captura = capsys.readouterr()

    # Assert
    assert "Por persona:   $55.00" in captura.out


def test_menu_interactivo_limite_personas_minimo(monkeypatch, capsys):
    """L: Verifica el cálculo cuando se divide entre el límite inferior (1 persona)."""
    # Arrange
    entradas = iter(["50", "2", "10", "1", "salir"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    # Act
    menu_interactivo()
    captura = capsys.readouterr()

    # Assert
    assert "Total General: $60.00" in captura.out


def test_menu_interactivo_error_valor_no_numerico(monkeypatch, capsys):
    """E: Verifica que el programa capture letras donde espera números y no se cierre."""
    # Arrange
    # Intentamos poner letras en la cuenta, el try/except captura y el bucle sigue, luego salimos.
    entradas = iter(["abc", "salir"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    # Act
    menu_interactivo()
    captura = capsys.readouterr()

    # Assert
    assert "Error de entrada" in captura.out


def test_menu_interactivo_edge_opcion_invalida_continua(monkeypatch, capsys):
    """Edge: Verifica que una opción de menú inválida asuma propina 0 y permita continuar."""
    # Arrange
    # Cuenta(100), Opción inválida(9), Personas(1), Salir
    entradas = iter(["100", "9", "1", "salir"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    # Act
    menu_interactivo()
    captura = capsys.readouterr()

    # Assert
    assert "Opción no válida. Se usará 0 de propina." in captura.out