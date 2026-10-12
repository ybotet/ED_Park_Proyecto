## 📌 Prompt de Inicialización (usar una sola vez)

```
He cargado el archivo AGENT.md en la raíz del proyecto. 
Léelo completo y confirma que entendiste:

1. El contexto académico
2. El objeto virtual (ED Park)
3. El alcance completo (telecom + software + hardware + montaje)
4. Las reglas de trabajo
5. La estructura de archivos
6. El checklist

Luego dime: ¿estás listo para comenzar?
```

---

## 📌 FASE 0 — Preparación y encuadre

### Prompt para generar `00_README.md`

```
Genera el archivo 00_README.md del proyecto.

Debe incluir:
- Título del proyecto: "ED Park — Implementación de Sistema Completo"
- Descripción breve del proyecto
- Objetivo general
- Alcance (qué incluye y qué NO)
- Estructura del repositorio
- Cómo navegar los archivos
- Estado actual del proyecto (checklist resumido)
- Autor y fecha

Formato: Markdown limpio, profesional, listo para exportar a PDF.
```

### Prompt para generar `01_Fase_0_Preparacion.md`

```
Genera el archivo 01_Fase_0_Preparacion.md.

Debe incluir:
- Objetivo de la fase
- Confirmación del tema Nº 12
- Resumen de las indicaciones del profesor (clases 12 y 19 sept)
- Descripción del objeto virtual ED Park (tabla completa)
- Alcance del proyecto (sistema completo: telecom + software + hardware + montaje)
- Stakeholders identificados (tabla con rol, interés, influencia)
- Variantes para el cliente (básica, intermedia, completa) — descripción inicial
- Experiencia del cliente (cómo usará el sistema)
- Checklist de la fase

Usa tablas, listas y formato ГОСТ 7.32-2017.
Cita los GOST aplicables si corresponde.
```

---

## 📌 FASE 1 — Investigación normativa

### Prompt para generar `02_Fase_1_Normativa.md`

```
Genera el archivo 02_Fase_1_Normativa.md.

Debe incluir:
- Objetivo de la fase
- Lista completa de GOST y estándares aplicables (tabla)
- Para cada GOST:
  - Número completo
  - Título en ruso
  - Año
  - Secciones aplicables al proyecto
  - Por qué aplica al ED Park
- Formato de citación ГОСТ 7.1-2003
- Tabla de trazabilidad: equipo → GOST
- Checklist de la fase

Los GOST a incluir son:
- ГОСТ Р ИСО 15745-4-2010
- ГОСТ Р МЭК 61850-3
- ГОСТ Р 70982-2023
- ГОСТ Р МЭК 62443-3-3-2016
- ГОСТ IEC 62026-3-2015
- IEEE 802.11ax
- IEEE 802.3
- IEEE 1588 (PTP)
- ГОСТ Р МЭК 60870-5-104
- ГОСТ Р МЭК 61131-1
- ГОСТ 7.32-2017
- ГОСТ 7.1-2003

Genera la tabla de trazabilidad completa.
```

---

## 📌 FASE 2 — Diseño técnico del sistema completo

### Prompt para generar `03_01_Descripcion_ED_Park.md`

```
Genera el archivo 03_01_Descripcion_ED_Park.md.

Debe incluir:
- Objetivo de la sección
- Descripción narrativa del ED Park (2-3 párrafos)
- Ubicación y justificación estratégica
- Superficie y distribución (tabla)
- Tipo de mercancía y requisitos especiales
- Nivel de automatización (descripción detallada)
- Estructura física (diagrama ASCII o Mermaid)
- Flujos operativos diarios (recepción, almacenamiento, picking, expedición, devoluciones)
- Personal necesario (tabla por rol)
- Experiencia del cliente (cómo interactúa con el sistema)
- Checklist de la sección

Usa diagramas Mermaid o ASCII para la estructura física.
```

### Prompt para generar `03_02_Infraestructura_Fisica.md`

```
Genera el archivo 03_02_Infraestructura_Fisica.md.

Debe incluir:
- Objetivo de la sección
- Descripción de las 2 naves (principal + recepción/expedición)
- Distribución interna de cada nave
- Muelles de carga (cantidad, ubicación, capacidad)
- Patio de maniobras (superficie, función)
- Zonas de almacenamiento (estanterías, temperatura controlada)
- Zonas de picking y embalaje
- Oficinas y sala de control
- Zona de carga de AGV
- Aparcamiento
- Área verde y expansión
- Diagrama de planta (ASCII o Mermaid)
- Checklist de la sección

Incluye medidas, capacidades y justificación técnica.
```

### Prompt para generar `03_03_Infraestructura_Telecom.md`

```
Genera el archivo 03_03_Infraestructura_Telecom.md.

Este es el archivo central del tema Nº 12. Debe incluir:
- Objetivo de la sección
- Descripción de cada tecnología:
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
  - Системы синхронизации времени (PTP)
  - Каналы связи между машинами (M2M)
  - V2X/V2I
- Para cada tecnología:
  - Definición
  - Aplicación en el ED Park
  - Equipos específicos
  - GOST aplicable
  - Justificación técnica
- Lista completa de equipos de telecom (tabla)
- Diagrama de topología de red (Mermaid)
- Esquema de cobertura Wi-Fi
- Esquema de redundancia
- Esquema V2X/V2I
- Esquema de sincronización PTP
- Checklist de la sección

Usa tablas, diagramas Mermaid y referencias a GOST.
```

### Prompt para generar `03_04_Software_Gestion.md`

```
Genera el archivo 03_04_Software_Gestion.md.

IMPORTANTE: Este archivo describe el DISEÑO VIRTUAL del software, NO código.

Debe incluir:
- Objetivo de la sección
- Aclaración: no se programa, se diseña virtualmente
- Módulos de software a desarrollar:
  - WMS (Warehouse Management System)
  - Sistema de control de AGV
  - Sistema de integración V2X/V2I
  - SCADA
  - Módulos de integración con sistemas del cliente
  - Interfaz de usuario (concepto)
- Para cada módulo:
  - Función
  - Requisitos
  - Tecnología sugerida
  - Integración con otros módulos
  - GOST aplicable (ciberseguridad, etc.)
- Equipo de desarrollo necesario (tabla por rol)
- Metodología de desarrollo (Agile, Scrum, etc.)
- Plazos estimados
- Requisitos de ciberseguridad (ГОСТ Р МЭК 62443-3-3-2016)
- Diagrama de arquitectura de software (Mermaid)
- Diagrama de flujo de datos (Mermaid)
- Diagrama de integración de sistemas (Mermaid)
- Checklist de la sección

Recuerda: NO código, solo diseño y planificación.
```

### Prompt para generar `03_05_Equipos_Hardware.md`

```
Genera el archivo 03_05_Equipos_Hardware.md.

Debe incluir:
- Objetivo de la sección
- Lista completa de equipos (tabla):
  - AGV/AMR (5-8 unidades)
  - Carretillas elevadoras
  - Transpaletas eléctricas
  - Cintas transportadoras
  - Lectores RFID y código de barras
  - Básculas digitales
  - Sensores IoT
  - Servidores físicos
  - Equipos de climatización
  - Equipos de telecom (referencia a 03_03)
- Para cada equipo:
  - Modelo sugerido (o genérico)
  - Cantidad
  - Función
  - GOST aplicable
  - Costo estimado (si aplica)
- Tabla de trazabilidad equipo → GOST
- Checklist de la sección

Usa tablas detalladas.
```

### Prompt para generar `03_06_Esquemas_Diagramas.md`

```
Genera el archivo 03_06_Esquemas_Diagramas.md.

Debe incluir todos los diagramas del proyecto en formato Mermaid:

1. Diagrama de topología de red (mesh, estrella, redundante)
2. Esquema de ubicación física de equipos en el plano
3. Esquema de segmentación VLAN y QoS
4. Esquema de redundancia de canales
5. Esquema de arquitectura V2X/V2I para AGV
6. Esquema de cobertura Wi-Fi en las 2 naves y patio
7. Esquema de sincronización de tiempo (PTP)
8. Diagrama de arquitectura del software
9. Diagrama de flujo de datos
10. Diagrama de integración de sistemas

Para cada diagrama:
- Título
- Descripción
- Código Mermaid
- Interpretación

Usa Mermaid para todos los diagramas.
```

### Prompt para generar `03_07_Trazabilidad_GOST.md`

```
Genera el archivo 03_07_Trazabilidad_GOST.md.

Debe incluir:
- Objetivo de la sección
- Tabla de trazabilidad completa: equipo/tecnología → GOST → sección → justificación
- Para cada equipo del proyecto:
  - Nombre
  - Categoría
  - GOST aplicable (número completo)
  - Sección específica del GOST
  - Justificación de por qué aplica
- Resumen por GOST: cuántos equipos aplican a cada estándar
- Checklist de la sección

Esta tabla es fundamental para demostrar coherencia normativa.
```

---

## 📌 FASE 3 — Plan de montaje e instalación

### Prompt para generar `04_01_Plan_Montaje.md`

```
Genera el archivo 04_01_Plan_Montaje.md.

Debe incluir:
- Objetivo de la sección
- Tareas de montaje de equipos (tabla):
  - Montaje de estanterías
  - Montaje de cintas transportadoras
  - Instalación de muelles
  - Montaje de sensores
  - Montaje de AGV (puesta en servicio)
- Para cada tarea:
  - Descripción
  - Duración estimada
  - Recursos necesarios
  - Dependencias
  - GOST aplicable
- Cronograma de montaje (Gantt simplificado)
- Riesgos de montaje
- Checklist de la sección
```

### Prompt para generar `04_02_Plan_Instalacion.md`

```
Genera el archivo 04_02_Plan_Instalacion.md.

Debe incluir:
- Objetivo de la sección
- Tareas de instalación de red (tabla):
  - Cableado estructurado
  - Instalación de switches
  - Instalación de puntos de acceso
  - Instalación de gateways
  - Instalación de servidores
  - Configuración de VLAN
  - Configuración de QoS
  - Configuración de redundancia
- Tareas de instalación de software:
  - Instalación de WMS
  - Instalación de SCADA
  - Instalación de sistema de control de AGV
  - Integración de sistemas
- Para cada tarea:
  - Descripción
  - Duración estimada
  - Recursos necesarios
  - Dependencias
  - GOST aplicable
- Cronograma de instalación (Gantt simplificado)
- Riesgos de instalación
- Checklist de la sección
```

### Prompt para generar `04_03_Puesta_Marcha_Pruebas.md`

```
Genera el archivo 04_03_Puesta_Marcha_Pruebas.md.

Debe incluir:
- Objetivo de la sección
- Tareas de puesta en marcha:
  - Pruebas de cobertura Wi-Fi
  - Pruebas de latencia
  - Pruebas de redundancia
  - Pruebas de V2X/V2I
  - Pruebas de sincronización PTP
  - Pruebas de ciberseguridad
  - Pruebas de integración de software
  - Pruebas de AGV
- Para cada prueba:
  - Descripción
  - Criterios de aceptación
  - Métricas
  - Duración estimada
- Plan de validación
- Plan de capacitación del personal
- Checklist de la sección
```

---

## 📌 FASE 4 — Gestión del proyecto

### Prompt para generar `05_01_Pasaporte_Proyecto.md`

```
Genera el archivo 05_01_Pasaporte_Proyecto.md.

Debe incluir:
- Nombre del proyecto
- Objetivo general y objetivos específicos
- Alcance detallado (qué incluye y qué NO)
- Stakeholders y sus intereses (tabla)
- Criterios de éxito
- Restricciones (presupuesto, plazo, normativa)
- Supuestos del proyecto
- Exclusiones del proyecto
- Entregables principales
- Hitos clave
- Presupuesto preliminar
- Plazo estimado (18 meses)
- Checklist de la sección

Usa el formato de pasaporte de proyecto visto en clase.
```

### Prompt para generar `05_02_WBS_EDT.md`

```
Genera el archivo 05_02_WBS_EDT.md.

Debe incluir:
- Objetivo de la sección
- EDT/WBS completa (estructura de desglose de trabajo)
- Nivel 1: Proyecto ED Park
- Nivel 2: Fases (Análisis, Diseño, Desarrollo, Montaje, Pruebas, Despliegue)
- Nivel 3: Paquetes de trabajo
- Nivel 4: Tareas específicas
- Para cada tarea:
  - Código WBS
  - Nombre
  - Descripción
  - Duración
  - Recursos
  - Dependencias
  - Entregable
- Diagrama WBS en Mermaid
- Checklist de la sección

Usa codificación WBS estándar (1.0, 1.1, 1.1.1, etc.).
```

### Prompt para generar `05_03_Gantt.md`

```
Genera el archivo 05_03_Gantt.md.

Debe incluir:
- Objetivo de la sección
- Diagrama de Gantt completo (Mermaid)
- Lista de tareas con:
  - ID
  - Nombre
  - Duración
  - Inicio
  - Fin
  - Predecesoras
  - Recursos
  - Hito (si aplica)
- Ruta crítica identificada
- Hitos principales
- Fases del proyecto
- Checklist de la sección

Usa Mermaid gantt para el diagrama.
Plazo total: 18 meses.
```

### Prompt para generar `05_04_Recursos_Presupuesto.md`

```
Genera el archivo 05_04_Recursos_Presupuesto.md.

Debe incluir:
- Objetivo de la sección
- Recursos humanos (tabla por rol):
  - Director de proyecto
  - Jefe de operaciones
  - Ingenieros de red
  - Desarrolladores de software
  - Técnicos de montaje
  - Operarios
  - Personal administrativo
- Recursos materiales (tabla):
  - Equipos de telecom
  - Equipos de hardware
  - Materiales de montaje
  - Software (licencias)
- Presupuesto preliminar:
  - Costo base
  - Reserva de riesgos (20-70%)
  - Precio de costo
  - Precio de venta
- Matriz RACI
- Plan de contratación
- Subcontratistas (si aplica)
- Checklist de la sección

Usa tablas detalladas con costos estimados.
```

### Prompt para generar `05_05_Riesgos.md`

```
Genera el archivo 05_05_Riesgos.md.

Debe incluir:
- Objetivo de la sección
- Identificación de riesgos:
  - Técnicos (interferencias, latencia, cobertura)
  - Ciberseguridad (V2X, IoT, red)
  - Plazo y presupuesto
  - Financieros (tipo de cambio, inflación)
  - Regulatorios en Cuba
  - Proveedores
- Para cada riesgo:
  - ID
  - Descripción
  - Categoría
  - Probabilidad (alta, media, baja)
  - Impacto (alto, medio, bajo)
  - Nivel de riesgo (matriz)
  - Estrategia de mitigación
  - Plan de contingencia
  - Responsable
- Matriz de riesgos (probabilidad vs impacto)
- Reserva de riesgos en presupuesto
- Checklist de la sección

Usa tablas detalladas.
```

### Prompt para generar `05_06_Comunicacion_KPIs.md`

```
Genera el archivo 05_06_Comunicacion_KPIs.md.

Debe incluir:
- Objetivo de la sección
- Plan de comunicación:
  - Stakeholders
  - Información a comunicar
  - Frecuencia
  - Canal
  - Responsable
- KPIs de seguimiento:
  - KPI
  - Descripción
  - Fórmula
  - Meta
  - Frecuencia de medición
- Método de control de avance
- Gestión de cambios
- Reuniones periódicas
- Reportes de avance
- Checklist de la sección

Usa tablas detalladas.
```

### Prompt para generar `05_07_Analisis_Variantes.md`

```
Genera el archivo 05_07_Analisis_Variantes.md.

Debe incluir:
- Objetivo de la sección
- Variante básica:
  - Descripción
  - Alcance
  - Costo estimado
  - Plazo
  - Ventajas
  - Desventajas
- Variante intermedia (recomendada):
  - Descripción
  - Alcance
  - Costo estimado
  - Plazo
  - Ventajas
  - Desventajas
- Variante completa:
  - Descripción
  - Alcance
  - Costo estimado
  - Plazo
  - Ventajas
  - Desventajas
- Tabla comparativa
- Recomendación con justificación
- Checklist de la sección

Enfoque: realista y vendible al cliente.
```

---

## 📌 FASE 5 — Documento final

### Prompt para generar `06_01_Portada_GOST.md`

```
Genera el archivo 06_01_Portada_GOST.md.

Debe incluir:
- Portada según ГОСТ 7.32-2017
- Título del proyecto
- Nombre del estudiante
- Nombre del profesor
- Nombre de la asignatura
- Nombre de la institución
- Ciudad y año
- Espacio para firma del profesor
- Formato limpio y profesional

La portada debe ser firmable por el profesor.
```

### Prompt para generar `06_02_Introduccion.md`

```
Genera el archivo 06_02_Introduccion.md.

Debe incluir:
- Justificación del proyecto
- Objetivo general
- Objetivos específicos
- Alcance
- Metodología
- Estructura del documento
- Checklist de la sección
```

### Prompt para generar `06_03_Conclusiones.md`

```
Genera el archivo 06_03_Conclusiones.md.

Debe incluir:
- Resumen de lo realizado
- Cumplimiento de objetivos
- Aportes del proyecto
- Lecciones aprendidas
- Trabajo futuro
- Checklist de la sección
```

### Prompt para generar `06_04_Bibliografia.md`

```
Genera el archivo 06_04_Bibliografia.md.

Debe incluir:
- Lista completa de GOST citados (formato ГОСТ 7.1-2003)
- Lista de estándares IEEE
- Lista de libros y artículos consultados
- Lista de recursos web
- Orden alfabético
- Checklist de la sección

Formato:
ГОСТ Р ИСО 15745-4-2010. Системы автоматизации производства 
и их интеграция. Профили. Часть 4. Профили систем 
управления на основе Ethernet. — М.: Стандартинформ, 2010. — 48 с.
```

### Prompt para generar `06_05_Anexos.md`

```
Genera el archivo 06_05_Anexos.md.

Debe incluir:
- Anexo A: Diagramas y esquemas
- Anexo B: Tablas de equipos
- Anexo C: Tablas de trazabilidad GOST
- Anexo D: Presupuesto detallado
- Anexo E: Matriz de riesgos
- Anexo F: WBS completa
- Anexo G: Gantt completo
- Checklist de la sección
```

---

## 📌 FASE 6 — Presentación y defensa

### Prompt para generar `07_01_Slides.md`

```
Genera el archivo 07_01_Slides.md.

Debe incluir:
- Estructura de la presentación (10-15 min)
- Diapositiva 1: Portada
- Diapositiva 2: Introducción
- Diapositiva 3: Objeto virtual ED Park
- Diapositiva 4: Base normativa
- Diapositiva 5: Infraestructura de telecom
- Diapositiva 6: Software de gestión
- Diapositiva 7: Equipos
- Diapositiva 8: Plan de montaje
- Diapositiva 9: Gestión del proyecto
- Diapositiva 10: Presupuesto
- Diapositiva 11: Riesgos
- Diapositiva 12: Análisis de variantes
- Diapositiva 13: Conclusiones
- Diapositiva 14: Preguntas

Para cada diapositiva:
- Título
- Contenido
- Notas del presentador
```

### Prompt para generar `07_02_Q&A.md`

```
Genera el archivo 07_02_Q&A.md.

Debe incluir:
- Preguntas anticipadas del profesor
- Respuestas preparadas
- Preguntas sobre:
  - Elección de tecnología
  - Justificación de GOST
  - Presupuesto y riesgos
  - Plazos
  - Software
  - Montaje
  - Variantes
  - Ciberseguridad
- Checklist de la sección
```

---

## 📌 Prompt para actualizar el checklist

```
Actualiza el archivo 08_Checklist_Actualizado.md.

Marca todas las tareas completadas hasta ahora.
Muestra el progreso general del proyecto.
Indica qué tareas quedan pendientes.
Sugiere el siguiente paso.
```

---

## 📌 Prompt para exportar a PDF

```
Genera el documento final consolidado en formato Markdown.

Debe incluir:
- Portada según ГОСТ 7.32-2017
- Índice
- Todas las secciones en orden
- Bibliografía
- Anexos

Luego indícame cómo exportarlo a PDF con formato académico.
```

---

## 🎯 Resumen de prompts por fase

| Fase | Prompt                  | Archivo                            |
| ---- | ----------------------- | ---------------------------------- |
| 0    | Inicialización          | `00_README.md`                     |
| 0    | Preparación             | `01_Fase_0_Preparacion.md`         |
| 1    | Normativa               | `02_Fase_1_Normativa.md`           |
| 2.1  | Descripción ED Park     | `03_01_Descripcion_ED_Park.md`     |
| 2.2  | Infraestructura física  | `03_02_Infraestructura_Fisica.md`  |
| 2.3  | Infraestructura telecom | `03_03_Infraestructura_Telecom.md` |
| 2.4  | Software gestión        | `03_04_Software_Gestion.md`        |
| 2.5  | Equipos hardware        | `03_05_Equipos_Hardware.md`        |
| 2.6  | Esquemas diagramas      | `03_06_Esquemas_Diagramas.md`      |
| 2.7  | Trazabilidad GOST       | `03_07_Trazabilidad_GOST.md`       |
| 3.1  | Plan montaje            | `04_01_Plan_Montaje.md`            |
| 3.2  | Plan instalación        | `04_02_Plan_Instalacion.md`        |
| 3.3  | Puesta marcha           | `04_03_Puesta_Marcha_Pruebas.md`   |
| 4.1  | Pasaporte               | `05_01_Pasaporte_Proyecto.md`      |
| 4.2  | WBS/EDT                 | `05_02_WBS_EDT.md`                 |
| 4.3  | Gantt                   | `05_03_Gantt.md`                   |
| 4.4  | Recursos/presupuesto    | `05_04_Recursos_Presupuesto.md`    |
| 4.5  | Riesgos                 | `05_05_Riesgos.md`                 |
| 4.6  | Comunicación/KPIs       | `05_06_Comunicacion_KPIs.md`       |
| 4.7  | Análisis variantes      | `05_07_Analisis_Variantes.md`      |
| 5.1  | Portada GOST            | `06_01_Portada_GOST.md`            |
| 5.2  | Introducción            | `06_02_Introduccion.md`            |
| 5.3  | Conclusiones            | `06_03_Conclusiones.md`            |
| 5.4  | Bibliografía            | `06_04_Bibliografia.md`            |
| 5.5  | Anexos                  | `06_05_Anexos.md`                  |
| 6.1  | Slides                  | `07_01_Slides.md`                  |
| 6.2  | Q&A                     | `07_02_Q&A.md`                     |
| —    | Checklist               | `08_Checklist_Actualizado.md`      |