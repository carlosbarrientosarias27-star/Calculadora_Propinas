# ui.py — Interfaz de Usuario en Terminal (con Bucle y Salida)

Módulo de Python que proporciona una interfaz interactiva por línea de comandos para la calculadora de propinas. Integra la lógica de cálculo de `logic.py` y el formateo de `utils.py` en un flujo continuo con bucle, que permite realizar múltiples cálculos y salir en cualquier momento.

---

# Dependencias internas

| Módulo | Funciones importadas |
|---|---|
| `app.logic` | `calcular_propina_porcentaje`, `calcular_propina_fija`, `dividir_cuenta` |
| `app.utils` | `formatear_moneda` |

---

# Funciones

## `menu_interactivo()`

Lanza un menú en terminal con **bucle continuo** que guía al usuario para calcular y dividir propinas. Permite realizar múltiples cálculos consecutivos y ofrece dos vías de salida. Al finalizar cada cálculo, muestra un resumen detallado del pago.

**No recibe parámetros ni retorna ningún valor** — interactúa directamente con `stdin` y `stdout`.

---

## Flujo de ejecución

```
┌─────────────────────────────────────────┐
│         Inicio del bucle (while True)   │
└────────────────────┬────────────────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │ Ingresa total cuenta  │
         └──────────┬────────────┘
                    │
         ┌──────────▼────────────┐
         │  ¿Escribió 'salir'?  │──── Sí ──► "¡Gracias por usar la calculadora! 👋" → FIN
         └──────────┬────────────┘
                    │ No
                    ▼
         ┌───────────────────────┐
         │  Menú tipo de propina │
         │  1. Porcentaje        │
         │  2. Monto fijo        │
         │  3. Salir             │
         └──────────┬────────────┘
                    │
         ┌──────────▼────────────┐
         │   ¿Opción 3?         │──── Sí ──► "¡Hasta luego! 👋" → FIN
         └──────────┬────────────┘
                    │ No
                    ▼
         ┌───────────────────────┐
         │  Calcula propina      │
         │  (% o fijo o 0)      │
         └──────────┬────────────┘
                    │
                    ▼
         ┌───────────────────────┐
         │  Ingresa nº personas  │
         └──────────┬────────────┘
                    │
                    ▼
         ┌───────────────────────┐
         │   Muestra resumen     │
         └──────────┬────────────┘
                    │
                    └──────────────► Vuelve al inicio del bucle
```

---

# Opciones de salida

| Vía | Cuándo | Mensaje mostrado |
|---|---|---|
| Escribir `salir` | Al ingresar el monto de la cuenta | `¡Gracias por usar la calculadora! 👋` |
| Seleccionar opción `3` | En el menú de tipo de propina | `¡Hasta luego! 👋` |

---

# Ejemplo de sesión interactiva

```
--- 🧮 CALCULADORA DE PROPINAS INTERACTIVA ---
Escriba 'salir' en cualquier momento para finalizar.
Ingrese el total de la cuenta: 100

Opciones de propina:
1. Porcentaje (ej. 10%, 15%, 20%)
2. Monto fijo
3. Salir
Seleccione una opción (1, 2 o 3): 1
Ingrese el porcentaje de propina: 15
¿Entre cuántas personas se divide la cuenta? 3

--- RESUMEN DE PAGO ---
Subtotal:      $100.00
Propina:       $15.00
Total General: $115.00
Por persona:   $38.33
-----------------------

--- 🧮 CALCULADORA DE PROPINAS INTERACTIVA ---
Escriba 'salir' en cualquier momento para finalizar.
Ingrese el total de la cuenta: salir
¡Gracias por usar la calculadora! 👋
```

---

# Manejo de errores

Los errores de entrada son capturados por `try-except` dentro del bucle, de modo que el programa muestra un aviso y **continúa en la siguiente iteración** sin cerrarse.

| Situación | Comportamiento |
|---|---|
| Entrada no numérica en el monto | Muestra `❌ Error de entrada` y reinicia el bucle |
| Opción de propina inválida (distinta de 1, 2 o 3) | Avisa `Opción no válida. Se usará 0 de propina.` y continúa |
| Valores negativos (propagados desde `logic.py`) | Capturados como `ValueError`, reinicia el bucle |

---

# Diferencias respecto a la versión anterior

| Comportamiento | Versión anterior | Esta versión |
|---|---|---|
| Ejecución | Un solo cálculo y termina | Bucle continuo hasta que el usuario sale |
| Salida del programa | No contemplada | `"salir"` o opción `3` del menú |
| Error de entrada | Terminaba el programa | Muestra error y permite reintentar |
| Opción inválida de menú | Asumía `0` y terminaba | Avisa, asume `0` y continúa el bucle |

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
python main.py
```