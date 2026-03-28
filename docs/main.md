# main.py — Punto de Entrada de la Aplicación

Archivo principal del proyecto. Actúa como punto de entrada para lanzar la **Calculadora de Propinas Interactiva** desde la línea de comandos.

---

# Descripción

`main.py` importa y ejecuta `menu_interactivo()` de `app.ui`, arrancando el flujo completo de la aplicación. Su único rol es servir de punto de entrada; toda la lógica reside en los módulos internos.

---

# Estructura del proyecto

```
proyecto/
├── main.py          ← Punto de entrada
└── app/
    ├── ui.py        ← Interfaz de usuario en terminal
    ├── logic.py     ← Lógica de cálculo de propinas
    └── utils.py     ← Utilidades de formato
```

---

# Requisitos

- Python 3.14
- Los módulos `app.ui`, `app.logic` y `app.utils` deben estar presentes en el directorio `app/`.

---

# Ejecución

Desde la raíz del proyecto:

```bash
python main.py
```

---

# Dependencias internas

| Módulo | Función importada |
|---|---|
| `app.ui` | `menu_interactivo` |

> Para más detalles sobre el comportamiento de la aplicación, consulta el README de cada módulo interno: [`ui.py`](app/ui.py), [`logic.py`](app/logic.py) y [`utils.py`](app/utils.py).