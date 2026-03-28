# test_utils.py — Tests del Módulo de Utilidades

Módulo de pruebas unitarias para verificar el comportamiento de la función `formatear_moneda()` definida en `app/utils.py`, usando `pytest` con el patrón **Arrange / Act / Assert**.

---

# Dependencias

| Módulo | Uso |
|---|---|
| `pytest` | Framework de testing |
| `app.utils.formatear_moneda` | Función bajo prueba |

---

# Casos de prueba

## `test_formatear_moneda_normal` — Normal (N)

Verifica que un número entero positivo se formatee correctamente con símbolo `$` y dos decimales.

| Parámetro | Valor |
|---|---|
| `cantidad` | `50` |
| **Resultado esperado** | `"$50.00"` |

---

## `test_formatear_moneda_con_decimales` — Normal (N)

Verifica que un número flotante con decimales se formatee correctamente.

| Parámetro | Valor |
|---|---|
| `cantidad` | `125.50` |
| **Resultado esperado** | `"$125.50"` |

---

## `test_formatear_moneda_limite_cero` — Límite (L)

Verifica el formato cuando la cantidad es exactamente cero.

| Parámetro | Valor |
|---|---|
| `cantidad` | `0` |
| **Resultado esperado** | `"$0.00"` |

---

## `test_formatear_moneda_error_tipo_invalido` — Error (E)

Verifica que se lance `ValueError` cuando se pasa una cadena de texto que no puede convertirse a número.

| Parámetro | Valor |
|---|---|
| `cantidad` | `"cien"` |
| **Excepción esperada** | `ValueError` |

> La f-string con formato numérico (`{cantidad:,.2f}`) no puede aplicarse sobre un `str` no numérico, lo que genera el error.

---

## `test_formatear_moneda_edge_separador_miles` — Edge Case

Verifica que cantidades superiores a mil incluyan la coma como separador de miles.

| Parámetro | Valor |
|---|---|
| `cantidad` | `1500.75` |
| **Resultado esperado** | `"$1,500.75"` |

---

## `test_formatear_moneda_edge_redondeo_automatico` — Edge Case

Verifica que la f-string redondee automáticamente a 2 decimales cuando el número tiene más dígitos.

| Parámetro | Valor |
|---|---|
| `cantidad` | `10.556` |
| **Resultado esperado** | `"$10.56"` |

> `10.556` redondeado a 2 decimales → `10.56`

---

## `test_formatear_moneda_negativa` — Edge Case

Verifica el comportamiento de la función al recibir un monto negativo.

| Parámetro | Valor |
|---|---|
| `cantidad` | `-20.0` |
| **Resultado esperado** | `"$-20.00"` |

---

# Resumen de casos

| Test | Categoría | Entrada | Resultado esperado |
|---|---|---|---|
| `test_formatear_moneda_normal` | Normal | `50` | `"$50.00"` |
| `test_formatear_moneda_con_decimales` | Normal | `125.50` | `"$125.50"` |
| `test_formatear_moneda_limite_cero` | Límite | `0` | `"$0.00"` |
| `test_formatear_moneda_error_tipo_invalido` | Error | `"cien"` | `ValueError` |
| `test_formatear_moneda_edge_separador_miles` | Edge | `1500.75` | `"$1,500.75"` |
| `test_formatear_moneda_edge_redondeo_automatico` | Edge | `10.556` | `"$10.56"` |
| `test_formatear_moneda_negativa` | Edge | `-20.0` | `"$-20.00"` |

---

# Ejecución

```bash
# Ejecutar solo este módulo de tests
pytest tests/test_utils.py

# Con reporte detallado
pytest tests/test_utils.py -v
```