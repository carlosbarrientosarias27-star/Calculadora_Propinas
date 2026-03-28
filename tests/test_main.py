import pytest
import main
from app.ui import menu_interactivo

# --- Pruebas para main.py ---

def test_ejecucion_main_flujo_completo_normal(monkeypatch, capsys):
    """N: Verifica que la ejecución principal inicie el menú y procese una cuenta válida."""
    # Arrange
    # Simulamos una interacción completa: Cuenta(200), Opción(1), Porcentaje(15), Personas(2)
    entradas = iter(["200", "1", "15", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    # Act
    # Invocamos la función que el bloque __main__ llamaría
    menu_interactivo()
    captura = capsys.readouterr()

    # Assert
    # Verificamos que el cálculo ($230 total / 2) aparezca en el resumen
    assert "Por persona:   $115.00" in captura.out

def test_ejecucion_main_limite_propina_cero(monkeypatch, capsys):
    """L: Verifica el comportamiento del punto de entrada con propina del 0%."""
    # Arrange
    # Entradas: Cuenta(100), Opción(1), Porcentaje(0), Personas(1)
    entradas = iter(["100", "1", "0", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    # Act
    menu_interactivo()
    captura = capsys.readouterr()

    # Assert
    assert "Propina:       $0.00" in captura.out

def test_ejecucion_main_error_entrada_vacia(monkeypatch, capsys):
    """E: Verifica que el programa maneje una entrada vacía al inicio sin colapsar."""
    # Arrange
    # Simulamos que el usuario presiona Enter sin escribir nada en el monto de la cuenta
    monkeypatch.setattr("builtins.input", lambda _: "")

    # Act
    menu_interactivo()
    captura = capsys.readouterr()

    # Assert
    # El código en ui.py captura ValueError y muestra el mensaje de error de entrada
    assert "Error de entrada" in captura.out

def test_ejecucion_main_edge_muchas_personas(monkeypatch, capsys):
    """Edge: Verifica la división de la cuenta entre un grupo muy grande de personas."""
    # Arrange
    # Cuenta(100), Opción(2), Fijo(0), Personas(1000)
    entradas = iter(["100", "2", "0", "1000"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    # Act
    menu_interactivo()
    captura = capsys.readouterr()

    # Assert
    # 100 / 1000 = 0.10
    assert "Por persona:   $0.10" in captura.out