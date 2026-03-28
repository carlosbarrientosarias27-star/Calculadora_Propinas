# test_ui.py — Tests de la Interfaz de Usuario

Módulo de pruebas unitarias para verificar el comportamiento de la función `menu_interactivo()` definida en `app/ui.py`, simulando interacciones completas de usuario mediante `monkeypatch` y capturando la salida con `capsys`.

---

# Dependencias

| Módulo | Uso |
|---|---|
| `pytest` | Framework de testing |
| `app.ui.menu_interactivo` | Función bajo prueba |

---

# Fixtures utilizados

| Fixture | Descripción |
|---|---|
| `monkeypatch` | Reemplaza `builtins.input` para simular entradas del usuario sin interacción real |
| `capsys` | Captura la salida estándar (`stdout`) para verificar los mensajes impresos en pantalla |

---

# Casos de prueba

## `test_menu_interactivo_flujo_porcentaje_normal` — Normal (N)

Simula un flujo completo con propina calculada por porcentaje y verifica el monto por persona.

| Entrada simulada | Valor |
|---|---|
| Total de la cuenta | `100` |
| Tipo de propina | `1` (porcentaje) |
| Porcentaje | `10%` |
| Número de personas | `2` |

**Resultado esperado en pantalla:**
```
Por persona:   $55.00
```
> $100.00 + $10.00 propina = $110.00 / 2 personas = $55.00

---

## `test_menu_interactivo_flujo_monto_fijo_normal` — Normal (N)

Simula un flujo completo con propina de monto fijo y verifica la división correcta entre varios comensales.

| Entrada simulada | Valor |
|---|---|
| Total de la cuenta | `80` |
| Tipo de propina | `2` (monto fijo) |
| Monto fijo | `20` |
| Número de personas | `4` |

**Resultado esperado en pantalla:**
```
Por persona:   $25.00
```
> $80.00 + $20.00 propina = $100.00 / 4 personas = $25.00

---

## `test_menu_interactivo_limite_una_persona` — Límite (L)

Verifica que cuando solo hay una persona, el monto por persona sea igual al total con propina.

| Entrada simulada | Valor |
|---|---|
| Total de la cuenta | `50` |
| Tipo de propina | `1` (porcentaje) |
| Porcentaje | `0%` |
| Número de personas | `1` |

**Resultado esperado en pantalla:**
```
Por persona:   $50.00
```

---

## `test_menu_interactivo_error_entrada_no_numerica` — Error (E)

Verifica que el programa maneje sin colapsar una entrada de texto en lugar de un número al solicitar el monto de la cuenta.

| Entrada simulada | Valor |
|---|---|
| Total de la cuenta | `"hola"` |

**Resultado esperado en pantalla:**
```
Error de entrada
```
> El bloque `try-except` de `ui.py` captura el `ValueError` generado por `float("hola")`.

---

## `test_menu_interactivo_edge_opcion_invalida` — Edge Case

Verifica que al seleccionar una opción de propina inexistente (distinta de `1` o `2`), la propina quede en `$0.00` y la ejecución continúe normalmente.

| Entrada simulada | Valor |
|---|---|
| Total de la cuenta | `100` |
| Tipo de propina | `3` (inválido) |
| Número de personas | `1` |

**Resultado esperado en pantalla:**
```
Propina:       $0.00
```
> Al no coincidir con `1` ni `2`, el código asigna `propina = 0.0` por defecto.

---

# Resumen de casos

| Test | Categoría | Escenario | Resultado esperado |
|---|---|---|---|
| `test_menu_interactivo_flujo_porcentaje_normal` | Normal | Porcentaje del 10%, 2 personas | `Por persona: $55.00` |
| `test_menu_interactivo_flujo_monto_fijo_normal` | Normal | Monto fijo de $20, 4 personas | `Por persona: $25.00` |
| `test_menu_interactivo_limite_una_persona` | Límite | Propina 0%, 1 persona | `Por persona: $50.00` |
| `test_menu_interactivo_error_entrada_no_numerica` | Error | Texto en lugar de número | `Error de entrada` |
| `test_menu_interactivo_edge_opcion_invalida` | Edge | Opción de menú inexistente | `Propina: $0.00` |

---

# Ejecución

```bash
# Ejecutar solo este módulo de tests
pytest tests/test_ui.py

# Con reporte detallado
pytest tests/test_ui.py -v
```