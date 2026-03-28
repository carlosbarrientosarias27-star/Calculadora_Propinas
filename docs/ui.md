# ui.py — Interfaz de Usuario en Terminal

Módulo de Python que proporciona una interfaz interactiva por línea de comandos para la calculadora de propinas. Integra la lógica de cálculo de `logic.py` y el formateo de `utils.py` en un flujo guiado paso a paso.

---

# Dependencias internas

| Módulo | Funciones importadas |
|---|---|
| `app.logic` | `calcular_propina_porcentaje`, `calcular_propina_fija`, `dividir_cuenta` |
| `app.utils` | `formatear_moneda` |

---

# Funciones

## `menu_interactivo()`

Lanza un menú en terminal que guía al usuario para calcular y dividir una propina. Al finalizar, muestra un resumen detallado del pago.

**No recibe parámetros ni retorna ningún valor** — interactúa directamente con `stdin` y `stdout`.

## Flujo de ejecución

```
1. Solicita el total de la cuenta
2. Pregunta el tipo de propina:
   ├── Opción 1 → Porcentaje (ej. 10%, 15%, 20%)
   └── Opción 2 → Monto fijo
3. Solicita el número de personas
4. Calcula el total con propina y el pago por persona
5. Muestra el resumen de pago
```

## Ejemplo de ejecución

```
--- 🧮 CALCULADORA DE PROPINAS INTERACTIVA ---
Ingrese el total de la cuenta: 80

Opciones de propina:
1. Porcentaje (ej. 10%, 15%, 20%)
2. Monto fijo
Seleccione una opción (1 o 2): 1
Ingrese el porcentaje de propina: 15
¿Entre cuántas personas se divide la cuenta? 4

--- RESUMEN DE PAGO ---
Subtotal:      $80.00
Propina:       $12.00
Total General: $92.00
Por persona:   $23.00
-----------------------
```

---

# Manejo de errores

Los errores de entrada quedan capturados mediante `try-except` y se muestran mensajes descriptivos sin interrumpir abruptamente el programa.

| Situación | Comportamiento |
|---|---|
| Entrada no numérica | Muestra `❌ Error de entrada` con el detalle del error |
| Opción de propina inválida | Usa `0` de propina y continúa |
| Valores negativos (propagados desde `logic.py`) | Capturados como `ValueError` |

---

# Requisitos

- Python 3.14
- Módulos internos: `app.logic` y `app.utils` deben estar accesibles en el `PYTHONPATH`.

---

# Ejecución

```python
from app.ui import menu_interactivo

menu_interactivo()
```

O directamente desde la raíz del proyecto:

```bash
python -m app.ui
```