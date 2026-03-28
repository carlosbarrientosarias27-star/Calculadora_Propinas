# utils.py — Utilidades de Formato

Módulo de Python con funciones auxiliares para el formateo de datos.

---

# Funciones

## `formatear_moneda(cantidad)`

Formatea un número como cadena de texto en formato moneda, añadiendo el símbolo `$` y separadores de miles.

| Parámetro | Tipo | Descripción |
|---|---|---|
| `cantidad` | `float` / `int` | Valor numérico a formatear |

**Retorna:** `str` — El número formateado como moneda (ej. `$1,234.56`).

```python
formatear_moneda(1234.5)   # → "$1,234.50"
formatear_moneda(50)       # → "$50.00"
formatear_moneda(1000000)  # → "$1,000,000.00"
```

---

# Ejemplo de uso

```python
from utils import formatear_moneda

precio = 3999.9
print(f"Precio: {formatear_moneda(precio)}")  # → "Precio: $3,999.90"
```

---

# Requisitos

- Python 3.14