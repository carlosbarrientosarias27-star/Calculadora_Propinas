# logic.py — Calculadora de Propinas

Módulo de Python con utilidades para calcular propinas y dividir cuentas entre varias personas.

---

# Funciones

## `calcular_propina_porcentaje(monto_cuenta, porcentaje)`

Calcula el monto de la propina aplicando un porcentaje sobre el total de la cuenta.

| Parámetro | Tipo | Descripción |
|---|---|---|
| `monto_cuenta` | `float` | Importe total de la cuenta |
| `porcentaje` | `float` | Porcentaje de propina a aplicar |

**Retorna:** `float` — Monto de la propina.

**Lanza:** `ValueError` si alguno de los valores es negativo.

```python
calcular_propina_porcentaje(50.0, 15)  # → 7.5
```

---

## `calcular_propina_fija(monto_cuenta, monto_propina)`

Devuelve un monto de propina fijo, independientemente del importe de la cuenta.

| Parámetro | Tipo | Descripción |
|---|---|---|
| `monto_cuenta` | `float` | Importe total de la cuenta |
| `monto_propina` | `float` | Monto fijo de propina |

**Retorna:** `float` — El propio `monto_propina` recibido.

**Lanza:** `ValueError` si alguno de los valores es negativo.

```python
calcular_propina_fija(80.0, 5.0)  # → 5.0
```

---

## `dividir_cuenta(monto_total, num_personas)`

Divide el total (cuenta + propina) entre el número de comensales.

| Parámetro | Tipo | Descripción |
|---|---|---|
| `monto_total` | `float` | Suma de la cuenta más la propina |
| `num_personas` | `int` | Número de personas entre las que se divide |

**Retorna:** `float` — Monto por persona redondeado a 4 decimales.

**Lanza:** `ValueError` si `num_personas` es menor o igual a cero.

```python
dividir_cuenta(57.5, 4)  # → 14.375
```

---

# Ejemplo de uso

```python
from logic import calcular_propina_porcentaje, dividir_cuenta

monto_cuenta = 100.0
propina = calcular_propina_porcentaje(monto_cuenta, 10)   # 10.0
total = monto_cuenta + propina                            # 110.0
por_persona = dividir_cuenta(total, 3)                    # 36.6667

print(f"Propina: {propina} €")
print(f"Total: {total} €")
print(f"Por persona: {por_persona} €")
```

---

# Requisitos

- Python 3.14

---

# Manejo de errores

Todas las funciones lanzan `ValueError` ante entradas inválidas (valores negativos o número de personas igual a cero), por lo que se recomienda capturar esta excepción al integrar el módulo:

```python
try:
    propina = calcular_propina_porcentaje(-20, 15)
except ValueError as e:
    print(f"Error: {e}")
```