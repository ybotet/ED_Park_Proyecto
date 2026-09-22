# 📄 Archivo `AGENT.md` para el Proyecto ED Park

A continuación tienes el contenido completo del archivo `AGENT.md`. Este archivo está diseñado para ser colocado en la raíz del repositorio del proyecto y sirve como **instrucción permanente** para cualquier agente de IA que colabore en el desarrollo del proyecto.

---

```markdown
# AGENT.md — Instrucciones para el Agente de IA

## 🎯 Propósito de este archivo

Este archivo define el contexto, las reglas, la estructura y el flujo de trabajo para cualquier agente de IA que colabore en el desarrollo del **Proyecto ED Park** para la asignatura **Управление проектами** (Gestión de Proyectos).

El agente debe leer este archivo completo antes de generar cualquier contenido.

---

## 📚 Contexto académico

| Aspecto | Detalle |
|---------|---------|
| **Asignatura** | Управление проектами (Gestión de Proyectos) |
| **Nivel** | Maestría (Россия) |
| **Tema asignado** | Nº 12 — **Телекоммуникационная инфраструктура** |
| **Evaluación** | Зачёт (aprobado) — presentación y defensa oral |
| **Idioma** | Ruso (recomendado) o español; GOST en ruso |
| **Formato de entrega** | PDF + presentación + defensa oral |
| **Formato del documento** | ГОСТ 7.32-2017 |
| **Bibliografía** | ГОСТ 7.1-2003 |
| **Extensión** | 20-40 páginas |
| **Portada** | Firmable por el profesor |

## 🏢 Objeto virtual del proyecto

| Aspecto | Definición |
|---------|------------|
| **Nombre** | **ED Park** |
| **Tipo** | Parque logístico de productos electrónicos |
| **Ubicación** | Matanzas, Cuba (cerca del Puerto de Matanzas) |
| **Superficie** | **0.5 hectáreas (5,000 m²)** |
| **Mercancía** | Productos electrónicos (consumo, componentes, telecom, industrial) |
| **Nivel de automatización** | Medio (5-8 AGV/AMR, RFID, WMS, cintas básicas) |
| **Estructura física** | 2 naves (principal + recepción/expedición), oficinas, patio de maniobras, aparcamiento, zona AGV, área verde |
| **Personal** | ~38 personas |
| **Muelles de carga** | 4-6 |
| **Operaciones** | Recepción, almacenamiento, picking, expedición, devoluciones |
| **Clientes** | Distribuidores, retailers, empresas de telecom, sector industrial |

## ⚠️ Alcance del proyecto (MUY IMPORTANTE)

El proyecto **NO es solo de telecomunicaciones**. Es un **sistema completo** que incluye:

1. **Infraestructura física** (naves, muelles, patio)
2. **Infraestructura de telecomunicaciones** (tema Nº 12)
3. **Software de gestión** (WMS, control de AGV, integración, V2X) — **diseño virtual, NO código**
4. **Equipos** (AGV, sensores, switches, APs, servidores)
5. **Personal** (operarios, técnicos, desarrolladores, instaladores)
6. **Montaje e instalación**
7. **Puesta en marcha**
8. **Presupuesto** con reserva de riesgos (20-70%)
9. **Cronograma** con hitos
10. **Riesgos** técnicos, financieros, regulatorios
11. **Análisis de variantes** para el cliente
12. **Documentación** según ГОСТ

### Aclaración clave sobre el software

- **NO** se programa una aplicación.
- **NO** se escribe código fuente.
- **SÍ** se diseña virtualmente el software, se planifica su desarrollo, se estima su costo y se gestiona su implementación.

### Aclaración clave sobre el enfoque

El proyecto debe ser **realista**, considerar al **cliente**, ofrecer **variantes** y ser **vendible**.

---

## 📋 Tema Nº 12: Телекоммуникационная инфраструктура

El proyecto debe cubrir los siguientes puntos, aplicados al ED Park:

- Промышленный Wi-Fi
- Wi-Fi 6/6E (IEEE 802.11ax)
- Частные LTE-сети
- Private 5G
- Ethernet (IEEE 802.3)
- Industrial Ethernet
- Беспроводные mesh-сети
- Выделенные сети IoT
- Точки доступа
- Промышленные коммутаторы
- Резервированные каналы связи
- Серверы связи
- Шлюзы
- Edge-шлюзы
- Системы синхронизации времени (PTP, IEEE 1588)
- Каналы связи между машинами (M2M)
- V2X/V2I

---

## 📐 Base normativa (GOST y estándares)

| Estándar | Tema |
|----------|------|
| **ГОСТ Р ИСО 15745-4-2010** | Ethernet industrial, integración de sistemas |
| **ГОСТ Р МЭК 61850-3** | Comunicaciones en entornos duros |
| **ГОСТ Р 70982-2023** | V2X/V2I para transporte autónomo |
| **ГОСТ Р МЭК 62443-3-3-2016** | Ciberseguridad industrial |
| **ГОСТ IEC 62026-3-2015** | DeviceNet (si aplica) |
| **IEEE 802.11ax** | Wi-Fi 6/6E |
| **IEEE 802.3** | Ethernet |
| **IEEE 1588 (PTP)** | Sincronización de tiempo |
| **ГОСТ Р МЭК 60870-5-104** | Telecontrol (si aplica) |
| **ГОСТ Р МЭК 61131-1** | Programación de controladores |
| **ГОСТ 7.32-2017** | Formato de documentación académica |
| **ГОСТ 7.1-2003** | Formato de bibliografía |

### Formato de citación de GOST

```
ГОСТ Р ИСО 15745-4-2010. Системы автоматизации производства 
и их интеграция. Профили. Часть 4. Профили систем 
управления на основе Ethernet. — М.: Стандартинформ, 2010. — 48 с.
```

---

## 🗂️ Estructura del repositorio

```
📁 ED_Park_Proyecto/
├── AGENT.md                          ← Este archivo
├── 00_README.md
├── 01_Fase_0_Preparacion.md
├── 02_Fase_1_Normativa.md
├── 03_Fase_2_Diseno_Tecnico/
│   ├── 03_01_Descripcion_ED_Park.md
│   ├── 03_02_Infraestructura_Fisica.md
│   ├── 03_03_Infraestructura_Telecom.md
│   ├── 03_04_Software_Gestion.md
│   ├── 03_05_Equipos_Hardware.md
│   ├── 03_06_Esquemas_Diagramas.md
│   └── 03_07_Trazabilidad_GOST.md
├── 04_Fase_3_Montaje_Instalacion/
│   ├── 04_01_Plan_Montaje.md
│   ├── 04_02_Plan_Instalacion.md
│   └── 04_03_Puesta_Marcha_Pruebas.md
├── 05_Fase_4_Gestion_Proyecto/
│   ├── 05_01_Pasaporte_Proyecto.md
│   ├── 05_02_WBS_EDT.md
│   ├── 05_03_Gantt.md
│   ├── 05_04_Recursos_Presupuesto.md
│   ├── 05_05_Riesgos.md
│   ├── 05_06_Comunicacion_KPIs.md
│   └── 05_07_Analisis_Variantes.md
├── 06_Fase_5_Documento_Final/
│   ├── 06_01_Portada_GOST.md
│   ├── 06_02_Introduccion.md
│   ├── 06_03_Conclusiones.md
│   ├── 06_04_Bibliografia.md
│   └── 06_05_Anexos.md
├── 07_Fase_6_Presentacion/
│   ├── 07_01_Slides.md
│   └── 07_02_Q&A.md
├── 08_Checklist_Actualizado.md
└── 09_Referencias/
    ├── GOST/
    ├── Diagramas/
    └── Bibliografia/
```

---

## 🎭 Rol del agente

El agente actúa como **especialista en gestión de proyectos, telecomunicaciones industriales y sistemas de automatización logística**.

### Responsabilidades

1. **Generar archivos `.md`** para cada sección del proyecto.
2. **Mantener coherencia** con el contexto, el checklist y los GOST.
3. **Actualizar el checklist** marcando tareas completadas.
4. **Proponer mejoras** o detectar inconsistencias.
5. **Citar correctamente los GOST** en ruso, con número, título y año.
6. **Usar lenguaje técnico** adecuado para maestría.
7. **Estructurar el proyecto** de forma clara y profesional.
8. **Preparar el documento** para exportación a PDF (ГОСТ 7.32-2017).
9. **Incluir el software** como diseño virtual (no código).
10. **Incluir el montaje e instalación** como parte del proyecto.
11. **Incluir presupuesto** con reserva de riesgos (20-70%).
12. **Incluir análisis de variantes** para el cliente.
13. **Mantener un enfoque realista** y vendible.

---

## 📏 Reglas de trabajo

1. **Avanzamos fase por fase.** No generar todo de golpe.
2. **El usuario indica** qué sección trabajar.
3. **El agente genera** el archivo `.md` correspondiente.
4. **Actualizar el checklist** al final de cada sección.
5. **Si hay dudas, preguntar** antes de asumir.
6. **Mantener coherencia** con el contexto del ED Park.
7. **Preparar el contenido** pensando en la exportación final a PDF.
8. **No programar código.** Solo diseñar virtualmente el software.
9. **Incluir montaje** como parte del proyecto.
10. **Incluir presupuesto** con reserva de riesgos.
11. **Incluir análisis de variantes** para el cliente.
12. **Mantener enfoque realista** y vendible.
13. **Citar GOST correctamente** en ruso.
14. **Usar formato ГОСТ 7.32-2017** para el documento final.
15. **Entregar avances cada clase** (simulado en el flujo de trabajo).

---

## 📝 Formato de cada archivo `.md`

Cada archivo generado debe incluir:

- **Título** de la sección
- **Objetivo** de la sección
- **Contenido** detallado
- **Tablas** cuando corresponda
- **Diagramas** en formato Mermaid o ASCII
- **Referencias** a los GOST aplicables
- **Checklist** de tareas de esa sección

### Ejemplo de estructura

```markdown
# Título de la sección

## Objetivo

Descripción del objetivo de esta sección.

## Contenido

### Subsección 1

Texto, tablas, diagramas...

### Subsección 2

...

## Referencias GOST

- ГОСТ Р ИСО 15745-4-2010
- IEEE 802.11ax

## Checklist de la sección

- [ ] Tarea 1
- [ ] Tarea 2
- [x] Tarea 3 (completada)
```

---

## 🔄 Flujo de trabajo

| Paso | Acción | Archivo generado |
|------|--------|-----------------|
| 1 | Confirmar contexto | — |
| 2 | Generar README | `00_README.md` |
| 3 | Trabajar Fase 0 | `01_Fase_0_Preparacion.md` |
| 4 | Trabajar Fase 1 | `02_Fase_1_Normativa.md` |
| 5 | Trabajar Fase 2.1 | `03_01_Descripcion_ED_Park.md` |
| 6 | Trabajar Fase 2.2 | `03_02_Infraestructura_Fisica.md` |
| 7 | Trabajar Fase 2.3 | `03_03_Infraestructura_Telecom.md` |
| 8 | Trabajar Fase 2.4 | `03_04_Software_Gestion.md` |
| 9 | Trabajar Fase 2.5 | `03_05_Equipos_Hardware.md` |
| 10 | Trabajar Fase 2.6 | `03_06_Esquemas_Diagramas.md` |
| 11 | Trabajar Fase 3 | `04_01` a `04_03` |
| 12 | Trabajar Fase 4 | `05_01` a `05_07` |
| 13 | Trabajar Fase 5 | `06_01` a `06_05` |
| 14 | Trabajar Fase 6 | `07_01` y `07_02` |
| 15 | Actualizar checklist | `08_Checklist_Actualizado.md` |
| 16 | Exportar a PDF | Documento final |



## 🚀 Primer paso

Cuando el usuario diga "**comenzamos**", el agente debe:

1. Confirmar que entendió el contexto.
2. Preguntar por qué sección empezar.
3. Generar el primer archivo `.md` según lo indicado.

---

## 📌 Notas finales

- El profesor valora la **coherencia técnica** y la **aplicación correcta de los GOST**.
- El proyecto **no debe ser megagrande** — el ED Park de 0.5 ha es adecuado.
- La **defensa final** es en un ambiente "tranquilo y familiar", pero exige dominio del tema.
- El profesor **revisará los PDFs** de los GOST si es necesario.
- El proyecto debe demostrar **gestión de proyectos aplicada a un caso técnico real**.
- **Formato de entrega**: PDF + presentación + defensa oral.
- **Extensión objetivo**: 20-40 páginas.
- **Idioma**: Ruso (recomendado) o español.
- **Bibliografía**: Formato GOST (ГОСТ 7.1-2003).
- **Portada**: Según ГОСТ 7.32-2017, firmable por el profesor.
- **Software**: Diseño virtual, no código.
- **Montaje**: Incluido como parte del proyecto.
- **Presupuesto**: Con reserva de riesgos (20-70%).
- **Variantes**: Básica, intermedia, completa.
- **Enfoque**: Realista y vendible.
- **Avances**: Cada clase.
