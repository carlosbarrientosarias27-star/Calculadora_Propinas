import pytest
from app.ui import menu_interactivo

# --- Pruebas para main.py (Punto de entrada) ---

def test_ejecucion_main_flujo_completo_normal(monkeypatch, capsys):
    """N: Verifica que la ejecución principal procese una cuenta y salga correctamente."""
    # Arrange
    # Importante: Agregamos "salir" al final para romper el bucle while True
    entradas = iter(["200", "1", "15", "2", "salir"]) 
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    # Act
    menu_interactivo()
    captura = capsys.readouterr()

    # Assert
    # Verificamos el resultado del cálculo ($200 + 15% = $230 / 2 = $115)
    assert "Por persona:   $115.00" in captura.out


def test_ejecucion_main_limite_propina_cero(monkeypatch, capsys):
    """L: Verifica el comportamiento con 0% de propina y salida posterior."""
    # Arrange
    # Entradas: Cuenta(100), Opción(1), Porcentaje(0), Personas(1), Salir
    entradas = iter(["100", "1", "0", "1", "salir"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    # Act
    menu_interactivo()
    captura = capsys.readouterr()

    # Assert
    assert "Propina:       $0.00" in captura.out


def test_ejecucion_main_error_entrada_vacia(monkeypatch, capsys):
    """E: Verifica que el programa maneje entradas vacías y permita salir después."""
    # Arrange
    # Simulamos un Enter vacío (genera ValueError) y luego cerramos el programa
    entradas = iter(["", "salir"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    # Act
    menu_interactivo()
    captura = capsys.readouterr()

    # Assert
    # El mensaje proviene del bloque except ValueError en ui.py
    assert "Error de entrada" in captura.out


def test_ejecucion_main_edge_opcion_salir_directa(monkeypatch, capsys):
    """Edge: Verifica que la opción '3' del menú de propinas también finalice el programa."""
    # Arrange
    # Entradas: Cuenta(100), Opción(3)
    entradas = iter(["100", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    # Act
    menu_interactivo()
    captura = capsys.readouterr()

    # Assert
    assert "¡Hasta luego! 👋" in captura.out