# test_main.py — Tests del Punto de Entrada (con Bucle y Salida)

Módulo de pruebas unitarias para verificar el comportamiento del punto de entrada de la aplicación (`main.py`) y la función `menu_interactivo()` de `app/ui.py` en su versión con bucle continuo y opción de salida. Usa `monkeypatch` para simular entradas y `capsys` para capturar la salida en pantalla.

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

> **Nota:** Al tratarse de un bucle `while True`, todas las secuencias de entradas deben incluir `"salir"` o la opción `"3"` al final para romper el bucle y evitar que el test quede bloqueado indefinidamente.

---

# Casos de prueba

## `test_ejecucion_main_flujo_completo_normal` — Normal (N)

Verifica que ante una interacción completa y válida el cálculo sea correcto y el programa finalice al recibir `"salir"`.

| Entrada simulada | Valor |
|---|---|
| Total de la cuenta | `200` |
| Tipo de propina | `1` (porcentaje) |
| Porcentaje | `15%` |
| Número de personas | `2` |
| Segunda iteración | `"salir"` |

**Resultado esperado en pantalla:**
```
Por persona:   $115.00
```
> $200.00 + $30.00 propina = $230.00 / 2 personas = $115.00

---

## `test_ejecucion_main_limite_propina_cero` — Límite (L)

Verifica el comportamiento cuando se aplica una propina del 0%, asegurando que el resultado sea correcto y el programa salga limpiamente.

| Entrada simulada | Valor |
|---|---|
| Total de la cuenta | `100` |
| Tipo de propina | `1` (porcentaje) |
| Porcentaje | `0%` |
| Número de personas | `1` |
| Segunda iteración | `"salir"` |

**Resultado esperado en pantalla:**
```
Propina:       $0.00
```

---

## `test_ejecucion_main_error_entrada_vacia` — Error (E)

Verifica que el programa capture una entrada vacía sin colapsar, muestre el mensaje de error y permita al usuario continuar hasta salir.

| Entrada simulada | Valor |
|---|---|
| Monto de la cuenta | `""` (vacío) |
| Segunda iteración | `"salir"` |

**Resultado esperado en pantalla:**
```
Error de entrada
```
> `float("")` genera un `ValueError` capturado por el bloque `try-except`. El bucle continúa y permite al usuario volver a intentarlo o salir.

---

## `test_ejecucion_main_edge_opcion_salir_directa` — Edge Case

Verifica que seleccionar la opción `3` en el menú de tipo de propina finalice el programa correctamente, sin necesidad de escribir `"salir"`.

| Entrada simulada | Valor |
|---|---|
| Total de la cuenta | `100` |
| Tipo de propina | `3` (salir) |

**Resultado esperado en pantalla:**
```
¡Hasta luego! 👋
```

---

# Resumen de casos

| Test | Categoría | Escenario | Resultado esperado |
|---|---|---|---|
| `test_ejecucion_main_flujo_completo_normal` | Normal | Flujo completo con porcentaje + salir | `Por persona: $115.00` |
| `test_ejecucion_main_limite_propina_cero` | Límite | Propina del 0% + salir | `Propina: $0.00` |
| `test_ejecucion_main_error_entrada_vacia` | Error | Entrada vacía + salir | `Error de entrada` |
| `test_ejecucion_main_edge_opcion_salir_directa` | Edge | Opción `3` en menú de propina | `¡Hasta luego! 👋` |

---

# Diferencias respecto a la versión anterior

| Comportamiento | Versión anterior | Esta versión |
|---|---|---|
| Fin del bucle | No había bucle, el programa terminaba solo | Requiere `"salir"` u opción `3` para romper el `while True` |
| Test de salida directa | No contemplado | Nuevo caso Edge con opción `3` del menú |
| Error de entrada vacía | El programa terminaba tras el error | El bucle continúa; se añade `"salir"` para finalizar el test |

---

# Ejecución

```bash
# Ejecutar solo este módulo de tests
pytest tests/test_main.py

# Con reporte detallado
pytest tests/test_main.py -v
```