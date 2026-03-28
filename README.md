# 🧮 Calculadora de Propinas

Aplicación de línea de comandos desarrollada en Python para calcular propinas y dividir cuentas entre varias personas de forma interactiva.

---

# 📋 Características

- Cálculo de propina por **porcentaje** (10%, 15%, 20%, etc.)
- Cálculo de propina con **monto fijo**
- **División de cuenta** entre cualquier número de personas
- **Formateo de moneda** en los resultados
- Manejo de errores con mensajes descriptivos
- Tests unitarios con `pytest`
- Pipeline de CI/CD con GitHub Actions

---

# 📁 Estructura del proyecto

```
CALCULADORA_PROPINAS/
├── .github/
│   └── workflows/
│       └── pipeline.yml        # Pipeline de CI/CD
├── app/
│   ├── __init__.py
│   ├── logic.py                # Lógica de cálculo de propinas
│   ├── ui.py                   # Interfaz de usuario en terminal
│   └── utils.py                # Utilidades de formato
├── docs/
│   ├── asistencia_ia.md        # Documentación de asistencia IA
│   ├── logic.md                # Docs del módulo logic
│   ├── main.md                 # Docs del módulo main
│   ├── ui.md                   # Docs del módulo ui
│   └── utils.md                # Docs del módulo utils
├── tests/
│   ├── test_iu.py              # Tests de la interfaz de usuario
│   ├── test_logic.py           # Tests de la lógica de negocio
│   ├── test_main.py            # Tests del punto de entrada
│   └── test_utils.py           # Tests de las utilidades
├── .gitignore
├── conftest.py                 # Configuración global de pytest
├── LICENSE
├── main.py                     # Punto de entrada de la aplicación
├── pytest.ini                  # Configuración de pytest
├── README.md
└── requirements.txt            # Dependencias del proyecto
```

---

# ⚙️ Requisitos

- Python 3.8 o superior
- Dependencias listadas en `requirements.txt`

---

# 🚀 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/calculadora-propinas.git
cd calculadora-propinas
```

2. Crea y activa un entorno virtual:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

---

# ▶️ Ejecución

```bash
python main.py
```

Ejemplo de sesión interactiva:

```
--- 🧮 CALCULADORA DE PROPINAS INTERACTIVA ---
Ingrese el total de la cuenta: 100

Opciones de propina:
1. Porcentaje (ej. 10%, 15%, 20%)
2. Monto fijo
Seleccione una opción (1 o 2): 1
Ingrese el porcentaje de propina: 15
¿Entre cuántas personas se divide la cuenta? 3

--- RESUMEN DE PAGO ---
Subtotal:      $100.00
Propina:       $15.00
Total General: $115.00
Por persona:   $38.33
-----------------------
```

---

# 🧪 Tests

Ejecuta todos los tests con:

```bash
pytest
```

Para ver un reporte detallado:

```bash
pytest -v
```

Los tests cubren los módulos `logic`, `utils`, `ui` y `main`.

---

# 📦 Módulos

| Módulo | Descripción |
|---|---|
| `app/logic.py` | Funciones de cálculo de propina (porcentaje, monto fijo) y división de cuenta |
| `app/utils.py` | Formateo de valores numéricos como moneda |
| `app/ui.py` | Menú interactivo en terminal con manejo de errores |
| `main.py` | Punto de entrada que lanza la interfaz de usuario |

---

# 🔄 CI/CD

El proyecto incluye un pipeline de GitHub Actions (`.github/workflows/pipeline.yml`) que ejecuta automáticamente los tests en cada push o pull request.

---

# 📄 Licencia

Este proyecto está bajo los términos de la licencia incluida en el archivo [LICENSE](LICENSE MIT).