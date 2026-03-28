# 🤖 Asistencia IA — Calculadora de Propinas

Documento que registra el uso de inteligencia artificial (Claude - Anthropic) durante el desarrollo de la documentación del proyecto **Calculadora de Propinas**.

---

# 🛠️ Herramienta utilizada

| Campo | Detalle |
|---|---|
| **IA** | Claude (Anthropic) |
| **Interfaz** | claude.ai |
| **Propósito** | Generación de documentación técnica (archivos `.md`) |
| **Fecha** | Marzo 2026 |

---

# 💬 Prompts utilizados

## Prompt 1 — README de `logic.py`

```
Genérame un Readme.md del archivo logic.py
```

**Archivo adjunto:** `logic.py`  
**Resultado obtenido:** `docs/logic.md`  
**Descripción:** Se generó la documentación del módulo de lógica de negocio, incluyendo descripción de las tres funciones (`calcular_propina_porcentaje`, `calcular_propina_fija`, `dividir_cuenta`), tabla de parámetros, valores de retorno, excepciones y ejemplos de uso.

---

## Prompt 2 — README de `utils.py`

```
Genérame un Readme.md del archivo utils.py
```

**Archivo adjunto:** `utils.py`  
**Resultado obtenido:** `docs/utils.md`  
**Descripción:** Se generó la documentación del módulo de utilidades, detallando la función `formatear_moneda`, su parámetro, valor de retorno y ejemplos de salida con distintos valores numéricos.

---

## Prompt 3 — README de `ui.py`

```
Genérame un Readme.md del archivo ui.py
```

**Archivo adjunto:** `ui.py`  
**Resultado obtenido:** `docs/ui.md`  
**Descripción:** Se generó la documentación de la interfaz de usuario en terminal, incluyendo dependencias internas, flujo de ejecución paso a paso, ejemplo de sesión interactiva y tabla de manejo de errores.

---

## Prompt 4 — README de `main.py`

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

## Prompt 6 — Documento de asistencia IA

```
Creame un asistencia_ia.md del proyecto calculadora_propinas de los prompts que utilice
```

**Archivo adjunto:** Captura de pantalla de la estructura del proyecto en VS Code  
**Resultado obtenido:** `docs/asistencia_ia.md`  
**Descripción:** Se generó el presente documento, que registra todos los prompts utilizados durante la sesión, los archivos adjuntos proporcionados y los resultados obtenidos en cada interacción.

---

# 📊 Resumen de interacciones

| # | Prompt | Adjunto | Resultado |
|---|---|---|---|
| 1 | README de `logic.py` | `logic.py` | `docs/logic.md` |
| 2 | README de `utils.py` | `utils.py` | `docs/utils.md` |
| 3 | README de `ui.py` | `ui.py` | `docs/ui.md` |
| 4 | README de `main.py` | `main.py` | `docs/main.md` |
| 5 | README general del proyecto | Captura VS Code | `README.md` |
| 6 | Documento de asistencia IA | Captura VS Code | `docs/asistencia_ia.md` |

---

# ✅ Observaciones

- Todos los prompts fueron directos y orientados a un archivo o entregable concreto.
- La IA infirió el contexto del proyecto (calculadora de propinas, estructura modular) a partir del código fuente adjunto.
- No fue necesario iterar ni corregir ningún prompt; cada interacción produjo el resultado esperado en un solo intento.
- La documentación generada respeta la estructura real del proyecto observada en VS Code.