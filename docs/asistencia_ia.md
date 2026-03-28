# 🤖 Asistencia IA — Calculadora de Propinas

Documento que registra el uso de inteligencia artificial (Claude - Anthropic) durante el desarrollo de la documentación del proyecto **Calculadora de Propinas**.

---

# 🛠️ Herramienta utilizada

| Campo | Detalle |
|---|---|
| **IA** | Claude (Anthropic) |
| **Modelo** | Claude Sonnet 4.6 |
| **Interfaz** | claude.ai |
| **Propósito** | Generación de documentación técnica (archivos `.md`) |
| **Fecha** | Marzo 2026 |

---

# 💬 Prompts utilizados

## Prompt 1 — Documentación de `logic.py`

```
Genérame un Readme.md del archivo logic.py
```

**Archivo adjunto:** `logic.py`  
**Resultado obtenido:** `docs/logic.md`  
**Descripción:** Se generó la documentación del módulo de lógica de negocio, incluyendo descripción de las tres funciones (`calcular_propina_porcentaje`, `calcular_propina_fija`, `dividir_cuenta`), tabla de parámetros, valores de retorno, excepciones y ejemplos de uso.

---

## Prompt 2 — Documentación de `utils.py`

```
Genérame un Readme.md del archivo utils.py
```

**Archivo adjunto:** `utils.py`  
**Resultado obtenido:** `docs/utils.md`  
**Descripción:** Se generó la documentación del módulo de utilidades, detallando la función `formatear_moneda`, su parámetro, valor de retorno y ejemplos de salida con distintos valores numéricos.

---

## Prompt 3 — Documentación de `ui.py`

```
Genérame un Readme.md del archivo ui.py
```

**Archivo adjunto:** `ui.py`  
**Resultado obtenido:** `docs/ui.md`  
**Descripción:** Se generó la documentación de la interfaz de usuario en terminal, incluyendo dependencias internas, flujo de ejecución paso a paso, ejemplo de sesión interactiva y tabla de manejo de errores.

---

## Prompt 4 — Documentación de `main.py`

```
Genérame un Readme.md del archivo main.py
```

**Archivo adjunto:** `main.py`  
**Resultado obtenido:** `docs/main.md`  
**Descripción:** Se generó la documentación del punto de entrada de la aplicación, incluyendo su rol dentro del proyecto, la estructura de carpetas, instrucciones de ejecución y referencias a los módulos internos.

---

## Prompt 5 — README general del proyecto

```
Genérame un Readme.md de la descripción del proyecto Calculadora_Propinas
```

**Archivo adjunto:** Captura de pantalla de la estructura del proyecto en VS Code  
**Resultado obtenido:** `README.md`  
**Descripción:** Se generó el README principal del proyecto con características generales, árbol completo de archivos, instrucciones de instalación y ejecución, ejemplo de sesión en terminal, tabla de módulos, instrucciones de tests y sección de CI/CD.

---

## Prompt 6 — Primera versión del documento de asistencia IA

```
Creame un asistencia_ia.md del proyecto calculadora_propinas de los prompts que utilice
```

**Archivo adjunto:** Captura de pantalla de la estructura del proyecto en VS Code  
**Resultado obtenido:** `docs/asistencia_ia.md` (versión 1)  
**Descripción:** Se generó la primera versión del documento de asistencia IA, registrando los primeros 5 prompts utilizados hasta ese momento.

---

## Prompt 7 — Documentación de `test_main.py`

```
Genérame un Readme.md del archivo test_main.py
```

**Archivo adjunto:** `test_main.py`  
**Resultado obtenido:** `docs/test_main.md`  
**Descripción:** Se generó la documentación del módulo de tests del punto de entrada, detallando los fixtures de pytest utilizados (`monkeypatch`, `capsys`), los 4 casos de prueba (Normal, Límite, Error, Edge) con sus entradas simuladas y resultados esperados.

---

## Prompt 8 — Documentación de `test_logic.py`

```
Genérame un Readme.md del archivo test_logic.py
```

**Archivo adjunto:** `test_logic.py`  
**Resultado obtenido:** `docs/test_logic.md`  
**Descripción:** Se generó la documentación del módulo de tests de lógica de negocio, cubriendo los 10 casos de prueba distribuidos entre las tres funciones (`calcular_propina_porcentaje`, `calcular_propina_fija`, `dividir_cuenta`), con tablas de parámetros, resultados esperados y excepciones.

---

## Prompt 9 — Documentación de `test_ui.py`

```
Genérame un Readme.md del archivo test_ui.py
```

**Archivo adjunto:** `test_ui.py`  
**Resultado obtenido:** `docs/test_ui.md`  
**Descripción:** Se generó la documentación del módulo de tests de interfaz de usuario, detallando los 5 casos de prueba con entradas simuladas, flujo de cálculo y resultado esperado en pantalla para cada escenario.

---

## Prompt 10 — Documentación de `test_utils.py`

```
Genérame un Readme.md del archivo test_utils.py
```

**Archivo adjunto:** `test_utils.py`  
**Resultado obtenido:** `docs/test_utils.md`  
**Descripción:** Se generó la documentación del módulo de tests de utilidades, cubriendo los 7 casos de prueba de `formatear_moneda` (enteros, decimales, cero, tipo inválido, separador de miles, redondeo automático y montos negativos).

---

## Prompt 11 — Versión final del documento de asistencia IA

```
Creame un asistencia_ia.md del proyecto calculadora_propinas de los prompts que utilice
```

**Archivo adjunto:** Captura de pantalla de la estructura del proyecto en VS Code  
**Resultado obtenido:** `docs/asistencia_ia.md` (versión final)  
**Descripción:** Se generó la versión final y completa de este documento, incorporando todos los prompts utilizados a lo largo de la sesión.

---

# 📊 Resumen de interacciones

| # | Prompt | Adjunto | Resultado |
|---|---|---|---|
| 1 | Documentación de `logic.py` | `logic.py` | `docs/logic.md` |
| 2 | Documentación de `utils.py` | `utils.py` | `docs/utils.md` |
| 3 | Documentación de `ui.py` | `ui.py` | `docs/ui.md` |
| 4 | Documentación de `main.py` | `main.py` | `docs/main.md` |
| 5 | README general del proyecto | Captura VS Code | `README.md` |
| 6 | Documento de asistencia IA (v1) | Captura VS Code | `docs/asistencia_ia.md` |
| 7 | Documentación de `test_main.py` | `test_main.py` | `docs/test_main.md` |
| 8 | Documentación de `test_logic.py` | `test_logic.py` | `docs/test_logic.md` |
| 9 | Documentación de `test_ui.py` | `test_ui.py` | `docs/test_ui.md` |
| 10 | Documentación de `test_utils.py` | `test_utils.py` | `docs/test_utils.md` |
| 11 | Documento de asistencia IA (final) | Captura VS Code | `docs/asistencia_ia.md` |

---

# ✅ Observaciones

- Todos los prompts fueron directos y orientados a un archivo o entregable concreto.
- La IA infirió el contexto del proyecto a partir del código fuente adjunto en cada interacción.
- Los archivos de código fuente (`.py`) y capturas de pantalla de VS Code fueron los únicos adjuntos utilizados.
- No fue necesario iterar ni corregir ningún prompt; cada interacción produjo el resultado esperado en un solo intento.
- La documentación generada respeta la estructura real del proyecto observada en VS Code.
- La cobertura de documentación alcanzada es total: módulos de negocio, interfaz, utilidades, punto de entrada y todos los módulos de tests.