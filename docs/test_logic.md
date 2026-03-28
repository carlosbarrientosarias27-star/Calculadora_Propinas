# test_logic.py — Tests del Módulo de Lógica

Módulo de pruebas unitarias para verificar el correcto funcionamiento de las tres funciones de cálculo definidas en `app/logic.py`, usando `pytest` con el patrón **Arrange / Act / Assert**.

---

# Dependencias

| Módulo | Uso |
|---|---|
| `pytest` | Framework de testing |
| `app.logic.calcular_propina_porcentaje` | Función bajo prueba |
| `app.logic.calcular_propina_fija` | Función bajo prueba |
| `app.logic.dividir_cuenta` | Función bajo prueba |

---

# Casos de prueba

### `calcular_propina_porcentaje`

## `test_calcular_propina_porcentaje_normal` — Normal (N)

Verifica que el 10% de una cuenta de $100.00 resulte en una propina de $10.00.

| Parámetro | Valor |
|---|---|
| `monto_cuenta` | `100.0` |
| `porcentaje` | `10.0` |
| **Resultado esperado** | `10.0` |

---

## `test_calcular_propina_porcentaje_limite_cero` — Límite (L)

Verifica que al aplicar un porcentaje del 0%, la propina resultante sea exactamente `0.0`.

| Parámetro | Valor |
|---|---|
| `monto_cuenta` | `50.0` |
| `porcentaje` | `0.0` |
| **Resultado esperado** | `0.0` |

---

## `test_calcular_propina_porcentaje_error_negativo` — Error (E)

Verifica que se lance `ValueError` cuando el monto de la cuenta es negativo.

| Parámetro | Valor |
|---|---|
| `monto_cuenta` | `-10.0` |
| `porcentaje` | `15.0` |
| **Excepción esperada** | `ValueError: "El monto y el porcentaje deben ser positivos."` |

---

## `test_calcular_propina_porcentaje_edge_monto_muy_pequeno` — Edge Case

Verifica el manejo correcto de porcentajes aplicados sobre montos decimales mínimos.

| Parámetro | Valor |
|---|---|
| `monto_cuenta` | `0.01` |
| `porcentaje` | `50.0` |
| **Resultado esperado** | `0.005` |

---

### `calcular_propina_fija`

## `test_calcular_propina_fija_normal` — Normal (N)

Verifica que la función retorne exactamente el monto fijo de propina ingresado.

| Parámetro | Valor |
|---|---|
| `monto_cuenta` | `200.0` |
| `monto_propina` | `30.0` |
| **Resultado esperado** | `30.0` |

---

## `test_calcular_propina_fija_error_propina_negativa` — Error (E)

Verifica que se lance `ValueError` cuando el monto fijo de propina es negativo.

| Parámetro | Valor |
|---|---|
| `monto_cuenta` | `100.0` |
| `monto_propina` | `-5.0` |
| **Excepción esperada** | `ValueError: "Los montos deben ser positivos."` |

---

### `dividir_cuenta`

## `test_dividir_cuenta_normal` — Normal (N)

Verifica la división equitativa de una cuenta entre 4 personas.

| Parámetro | Valor |
|---|---|
| `monto_total` | `100.0` |
| `num_personas` | `4` |
| **Resultado esperado** | `25.0` |

---

## `test_dividir_cuenta_limite_una_persona` — Límite (L)

Verifica que al dividir entre una sola persona, el resultado sea igual al monto total.

| Parámetro | Valor |
|---|---|
| `monto_total` | `85.50` |
| `num_personas` | `1` |
| **Resultado esperado** | `85.50` |

---

## `test_dividir_cuenta_error_cero_personas` — Error (E)

Verifica que se lance `ValueError` al intentar dividir entre cero personas.

| Parámetro | Valor |
|---|---|
| `monto_total` | `100.0` |
| `num_personas` | `0` |
| **Excepción esperada** | `ValueError: "El número de personas debe ser al menos 1."` |

---

## `test_dividir_cuenta_edge_decimales_periodicos` — Edge Case

Verifica que el redondeo a 4 decimales funcione correctamente en divisiones con resultado periódico.

| Parámetro | Valor |
|---|---|
| `monto_total` | `100.0` |
| `num_personas` | `3` |
| **Resultado esperado** | `33.3333` |
> $100.00 / 3 = 33.3333... → redondeado a 4 decimales: `33.3333`

---

# Resumen de casos

| Test | Función | Categoría | Resultado esperado |
|---|---|---|---|
| `test_calcular_propina_porcentaje_normal` | `calcular_propina_porcentaje` | Normal | `10.0` |
| `test_calcular_propina_porcentaje_limite_cero` | `calcular_propina_porcentaje` | Límite | `0.0` |
| `test_calcular_propina_porcentaje_error_negativo` | `calcular_propina_porcentaje` | Error | `ValueError` |
| `test_calcular_propina_porcentaje_edge_monto_muy_pequeno` | `calcular_propina_porcentaje` | Edge | `0.005` |
| `test_calcular_propina_fija_normal` | `calcular_propina_fija` | Normal | `30.0` |
| `test_calcular_propina_fija_error_propina_negativa` | `calcular_propina_fija` | Error | `ValueError` |
| `test_dividir_cuenta_normal` | `dividir_cuenta` | Normal | `25.0` |
| `test_dividir_cuenta_limite_una_persona` | `dividir_cuenta` | Límite | `85.50` |
| `test_dividir_cuenta_error_cero_personas` | `dividir_cuenta` | Error | `ValueError` |
| `test_dividir_cuenta_edge_decimales_periodicos` | `dividir_cuenta` | Edge | `33.3333` |

---

# Ejecución

```bash
# Ejecutar solo este módulo de tests
pytest tests/test_logic.py

# Con reporte detallado
pytest tests/test_logic.py -v
```