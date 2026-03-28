# test_main.py — Tests del Punto de Entrada

Módulo de pruebas unitarias para verificar el comportamiento del punto de entrada de la aplicación (`main.py`) y la función `menu_interactivo()` de `app/ui.py`, usando `pytest` con `monkeypatch` y `capsys`.

---

# Dependencias

| Módulo | Uso |
|---|---|
| `pytest` | Framework de testing |
| `main` | Módulo principal del proyecto |
| `app.ui.menu_interactivo` | Función bajo prueba |

---

# Fixtures utilizados

| Fixture | Descripción |
|---|---|
| `monkeypatch` | Simula entradas del usuario reemplazando `builtins.input` |
| `capsys` | Captura la salida estándar (`stdout`) para verificar el resultado impreso |

---

# Casos de prueba

## `test_ejecucion_main_flujo_completo_normal` — Flujo Normal (N)

Verifica que ante una interacción completa y válida, el cálculo y el resumen de pago sean correctos.

| Entrada simulada | Valor |
|---|---|
| Total de la cuenta | `200` |
| Tipo de propina | `1` (porcentaje) |
| Porcentaje | `15%` |
| Número de personas | `2` |

**Resultado esperado en pantalla:**
```
Por persona:   $115.00
```
> Total con propina: $230.00 / 2 personas = $115.00

---

## `test_ejecucion_main_limite_propina_cero` — Límite (L)

Verifica el comportamiento cuando se aplica una propina del 0%, asegurando que el sistema no falle y muestre el resultado correcto.

| Entrada simulada | Valor |
|---|---|
| Total de la cuenta | `100` |
| Tipo de propina | `1` (porcentaje) |
| Porcentaje | `0%` |
| Número de personas | `1` |

**Resultado esperado en pantalla:**
```
Propina:       $0.00
```

---

## `test_ejecucion_main_error_entrada_vacia` — Error (E)

Verifica que el programa maneje sin colapsar una entrada vacía al solicitar el monto de la cuenta (el usuario presiona Enter sin escribir nada).

| Entrada simulada | Valor |
|---|---|
| Monto de la cuenta | `""` (vacío) |

**Resultado esperado en pantalla:**
```
Error de entrada
```
> La excepción `ValueError` es capturada por el bloque `try-except` de `ui.py`.

---

## `test_ejecucion_main_edge_muchas_personas` — Edge Case

Verifica que la división de la cuenta funcione correctamente ante un número muy elevado de personas.

| Entrada simulada | Valor |
|---|---|
| Total de la cuenta | `100` |
| Tipo de propina | `2` (monto fijo) |
| Monto fijo | `0` |
| Número de personas | `1000` |

**Resultado esperado en pantalla:**
```
Por persona:   $0.10
```
> $100.00 / 1000 personas = $0.10

---

# Resumen de casos

| Test | Categoría | Escenario | Resultado esperado |
|---|---|---|---|
| `test_ejecucion_main_flujo_completo_normal` | Normal | Flujo válido completo con porcentaje | `Por persona: $115.00` |
| `test_ejecucion_main_limite_propina_cero` | Límite | Propina del 0% | `Propina: $0.00` |
| `test_ejecucion_main_error_entrada_vacia` | Error | Entrada vacía en el monto | `Error de entrada` |
| `test_ejecucion_main_edge_muchas_personas` | Edge | División entre 1000 personas | `Por persona: $0.10` |

---

# Ejecución

```bash
# Ejecutar solo este módulo de tests
pytest tests/test_main.py

# Con reporte detallado
pytest tests/test_main.py -v
```