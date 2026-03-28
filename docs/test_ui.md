# test_ui.py — Tests de la Interfaz de Usuario (con Bucle y Salida)

Módulo de pruebas unitarias para verificar el comportamiento de la función `menu_interactivo()` definida en `app/ui.py` en su versión con bucle y opción de salida. Utiliza `monkeypatch` para simular entradas del usuario y `capsys` para capturar la salida en pantalla.

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

## `test_menu_interactivo_salir_inmediato` — Normal (N)

Verifica que el programa termine de forma limpia cuando el usuario escribe `"salir"` en el primer prompt, sin realizar ningún cálculo.

| Entrada simulada | Valor |
|---|---|
| Monto de la cuenta | `"salir"` |

**Resultado esperado en pantalla:**
```
¡Gracias por usar la calculadora! 👋
```

---

## `test_menu_interactivo_opcion_salir_menu` — Normal (N)

Verifica que al seleccionar la opción `3` en el menú de tipo de propina, el programa finalice correctamente.

| Entrada simulada | Valor |
|---|---|
| Monto de la cuenta | `100` |
| Tipo de propina | `3` (salir) |

**Resultado esperado en pantalla:**
```
¡Hasta luego! 👋
```

---

## `test_menu_interactivo_flujo_normal_y_salir` — Normal (N)

Verifica que se realice un cálculo completo con porcentaje y que el programa acepte la instrucción de salida en la siguiente iteración del bucle.

| Entrada simulada | Valor |
|---|---|
| Monto de la cuenta | `100` |
| Tipo de propina | `1` (porcentaje) |
| Porcentaje | `10%` |
| Número de personas | `2` |
| Segunda iteración | `"salir"` |

**Resultado esperado en pantalla:**
```
Por persona:   $55.00
```
> $100.00 + $10.00 propina = $110.00 / 2 personas = $55.00

---

## `test_menu_interactivo_limite_personas_minimo` — Límite (L)

Verifica el cálculo correcto cuando se divide entre el número mínimo de personas (1), usando monto fijo de propina.

| Entrada simulada | Valor |
|---|---|
| Monto de la cuenta | `50` |
| Tipo de propina | `2` (monto fijo) |
| Monto fijo | `10` |
| Número de personas | `1` |
| Segunda iteración | `"salir"` |

**Resultado esperado en pantalla:**
```
Total General: $60.00
```
> $50.00 + $10.00 propina = $60.00 / 1 persona = $60.00

---

## `test_menu_interactivo_error_valor_no_numerico` — Error (E)

Verifica que el programa capture una entrada de texto no numérico, muestre el mensaje de error y continúe ejecutándose sin cerrarse abruptamente.

| Entrada simulada | Valor |
|---|---|
| Monto de la cuenta | `"abc"` |
| Segunda iteración | `"salir"` |

**Resultado esperado en pantalla:**
```
Error de entrada
```
> El bloque `try-except` captura el `ValueError` generado por `float("abc")` y el bucle permite al usuario volver a intentarlo.

---

## `test_menu_interactivo_edge_opcion_invalida_continua` — Edge Case

Verifica que al ingresar una opción de menú inexistente, el programa asuma propina `$0.00`, muestre el aviso correspondiente y permita continuar con normalidad.

| Entrada simulada | Valor |
|---|---|
| Monto de la cuenta | `100` |
| Tipo de propina | `9` (inválido) |
| Número de personas | `1` |
| Segunda iteración | `"salir"` |

**Resultado esperado en pantalla:**
```
Opción no válida. Se usará 0 de propina.
```

---

# Resumen de casos

| Test | Categoría | Escenario | Resultado esperado |
|---|---|---|---|
| `test_menu_interactivo_salir_inmediato` | Normal | `"salir"` como primer input | `¡Gracias por usar la calculadora! 👋` |
| `test_menu_interactivo_opcion_salir_menu` | Normal | Opción `3` en menú de propina | `¡Hasta luego! 👋` |
| `test_menu_interactivo_flujo_normal_y_salir` | Normal | Cálculo completo con porcentaje y salida | `Por persona: $55.00` |
| `test_menu_interactivo_limite_personas_minimo` | Límite | División entre 1 persona con monto fijo | `Total General: $60.00` |
| `test_menu_interactivo_error_valor_no_numerico` | Error | Texto no numérico en el monto | `Error de entrada` |
| `test_menu_interactivo_edge_opcion_invalida_continua` | Edge | Opción de menú inexistente | `Opción no válida. Se usará 0 de propina.` |

---

# Diferencias respecto a la versión anterior

Esta versión de `test_ui.py` cubre la interfaz de usuario **con bucle y opción de salida**, lo que introduce nuevos comportamientos respecto a la versión original:

| Comportamiento | Versión anterior | Esta versión |
|---|---|---|
| Salida del programa | No contemplada | `"salir"` o opción `3` del menú |
| Opción inválida | Asumía propina `0` y terminaba | Asume propina `0`, avisa y continúa en el bucle |
| Error de entrada | Terminaba con mensaje de error | Muestra error y permite reintentar |

---

# Ejecución

```bash
# Ejecutar solo este módulo de tests
pytest tests/test_ui.py

# Con reporte detallado
pytest tests/test_ui.py -v
```