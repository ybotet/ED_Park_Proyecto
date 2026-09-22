# Checklist Actualizado del Proyecto ED Park

## FASE 0 — Preparación y encuadre

- [x] 0.1 Confirmar tema Nº 12 asignado por sorteo
- [x] 0.2 Releer indicaciones del profesor (clase 12 y 19 sept)
- [x] 0.3 Definir objeto virtual: ED Park
- [x] 0.4 Definir alcance del proyecto (sistema completo)
- [x] 0.5 Identificar stakeholders
- [x] 0.6 Definir ubicación: Matanzas, Cuba
- [x] 0.7 Definir tipo de mercancía: productos electrónicos
- [x] 0.8 Definir nivel de automatización: medio
- [x] 0.9 Definir superficie: 0.5 ha (5,000 m²)
- [x] 0.10 Definir estructura física (2 naves + oficinas + patio)
- [x] 0.11 Definir variantes para el cliente (básica, intermedia, completa)
- [x] 0.12 Definir experiencia del cliente (cómo usará el sistema)

## FASE 1 — Investigación normativa (GOST y estándares)

- [x] 1.1 Buscar ГОСТ Р ИСО 15745-4-2010 (Ethernet industrial)
- [x] 1.2 Buscar ГОСТ Р МЭК 61850-3 (comunicaciones entornos duros)
- [x] 1.3 Buscar ГОСТ Р 70982-2023 (V2X/V2I)
- [x] 1.4 Buscar ГОСТ Р МЭК 62443-3-3-2016 (ciberseguridad industrial)
- [x] 1.5 Buscar IEEE 802.11ax (Wi-Fi 6/6E)
- [x] 1.6 Buscar IEEE 802.3 (Ethernet)
- [x] 1.7 Buscar ГОСТ IEC 62026-3-2015 (DeviceNet) si aplica
- [x] 1.8 Buscar IEEE 1588 (PTP) para sincronización de tiempo
- [x] 1.9 Buscar ГОСТ 7.32-2017 (formato de documentación)
- [x] 1.10 Buscar ГОСТ 7.1-2003 (formato de bibliografía)
- [x] 1.11 Elaborar tabla de trazabilidad: cada equipo → su GOST
- [x] 1.12 Redactar apartado "Base normativa del proyecto"

## FASE 2 — Diseño técnico del sistema completo

### 2.1 Descripción del objeto

- [x] 2.1.1 Nombre: ED Park
- [x] 2.1.2 Ubicación: Matanzas, Cuba
- [x] 2.1.3 Superficie: 0.5 ha (5,000 m²)
- [x] 2.1.4 Mercancía: productos electrónicos
- [x] 2.1.5 Automatización: media (5-8 AGV)
- [x] 2.1.6 Personal: ~38 personas
- [x] 2.1.7 Estructura: 2 naves + oficinas + patio
- [ ] 2.1.8 Redactar descripción narrativa del parque
- [ ] 2.1.9 Describir flujos operativos diarios
- [ ] 2.1.10 Describir la experiencia del cliente

### 2.2 Infraestructura física

- [ ] 2.2.1 Describir naves y su distribución interna
- [ ] 2.2.2 Describir muelles de carga
- [ ] 2.2.3 Describir patio de maniobras
- [ ] 2.2.4 Describir zonas de almacenamiento
- [ ] 2.2.5 Describir zonas de picking y embalaje
- [ ] 2.2.6 Describir oficinas y sala de control

### 2.3 Infraestructura de telecomunicaciones

- [ ] 2.3.1 Listar puntos de acceso Wi-Fi 6/6E
- [ ] 2.3.2 Listar switches industriales (Industrial Ethernet)
- [ ] 2.3.3 Listar gateways y Edge-gateways
- [ ] 2.3.4 Listar servidores de comunicación
- [ ] 2.3.5 Listar equipos V2X/V2I (RSU, OBU) para AGV
- [ ] 2.3.6 Listar sistemas de sincronización de tiempo (PTP)
- [ ] 2.3.7 Listar canales redundantes (LTE privado, mesh)
- [ ] 2.3.8 Listar redes IoT dedicadas (sensores temperatura, humedad)
- [ ] 2.3.9 Listar equipos de red para AGV (Wi-Fi 6, 5G privado)
- [ ] 2.3.10 Justificar cada equipo con su GOST

### 2.4 Software de gestión (diseño, no código)

- [ ] 2.4.1 Definir WMS (Warehouse Management System)
- [ ] 2.4.2 Definir sistema de control de AGV
- [ ] 2.4.3 Definir sistema de integración V2X/V2I
- [ ] 2.4.4 Definir sistema de monitoreo y control (SCADA)
- [ ] 2.4.5 Definir módulos de integración con sistemas del cliente
- [ ] 2.4.6 Definir interfaz de usuario (concepto)
- [ ] 2.4.7 Definir requisitos de ciberseguridad
- [ ] 2.4.8 Estimar equipo de desarrollo necesario
- [ ] 2.4.9 Definir metodología de desarrollo
- [ ] 2.4.10 Estimar plazos de desarrollo

### 2.5 Equipos (hardware)

- [ ] 2.5.1 Listar AGV/AMR (5-8 unidades)
- [ ] 2.5.2 Listar carretillas elevadoras
- [ ] 2.5.3 Listar transpaletas eléctricas
- [ ] 2.5.4 Listar cintas transportadoras
- [ ] 2.5.5 Listar lectores RFID y código de barras
- [ ] 2.5.6 Listar básculas digitales
- [ ] 2.5.7 Listar sensores IoT
- [ ] 2.5.8 Listar servidores físicos
- [ ] 2.5.9 Listar equipos de climatización (para electrónica)
- [ ] 2.5.10 Justificar cada equipo

### 2.6 Esquemas y diagramas

- [ ] 2.6.1 Diagrama de topología de red (mesh, estrella, redundante)
- [ ] 2.6.2 Esquema de ubicación física de equipos en el plano
- [ ] 2.6.3 Esquema de segmentación VLAN y QoS
- [ ] 2.6.4 Esquema de redundancia de canales
- [ ] 2.6.5 Esquema de arquitectura V2X/V2I para AGV
- [ ] 2.6.6 Esquema de cobertura Wi-Fi en las 2 naves y patio
- [ ] 2.6.7 Esquema de sincronización de tiempo (PTP)
- [ ] 2.6.8 Diagrama de arquitectura del software
- [ ] 2.6.9 Diagrama de flujo de datos
- [ ] 2.6.10 Diagrama de integración de sistemas

## FASE 3 — Plan de montaje e instalación

- [ ] 3.1 Planificar tareas de montaje de equipos
- [ ] 3.2 Planificar tareas de instalación de red
- [ ] 3.3 Planificar tareas de instalación de software
- [ ] 3.4 Planificar tareas de puesta en marcha
- [ ] 3.5 Planificar tareas de pruebas y validación
- [ ] 3.6 Definir recursos para montaje
- [ ] 3.7 Definir plazos de montaje
- [ ] 3.8 Definir riesgos de montaje

## FASE 4 — Gestión del proyecto

### 4.1 Pasaporte del proyecto

- [ ] 4.1.1 Nombre del proyecto: "Implementación de sistema completo en ED Park"
- [ ] 4.1.2 Objetivo general y objetivos específicos
- [ ] 4.1.3 Alcance detallado
- [ ] 4.1.4 Stakeholders y sus intereses
- [ ] 4.1.5 Criterios de éxito
- [ ] 4.1.6 Restricciones (presupuesto, plazo, normativa)
- [ ] 4.1.7 Supuestos del proyecto
- [ ] 4.1.8 Exclusiones del proyecto

### 4.2 Plan de implementación

- [ ] 4.2.1 Descomponer en EDT/WBS
- [ ] 4.2.2 Definir hitos (milestones)
- [ ] 4.2.3 Elaborar diagrama de Gantt
- [ ] 4.2.4 Definir dependencias entre tareas
- [ ] 4.2.5 Estimar duración de cada tarea
- [ ] 4.2.6 Definir ruta crítica
- [ ] 4.2.7 Definir fases del proyecto (análisis, diseño, desarrollo, montaje, pruebas, despliegue)
- [ ] 4.2.8 Estimar plazos por fase

### 4.3 Recursos

- [ ] 4.3.1 Estimar personal necesario por rol (técnicos, desarrolladores, instaladores, operarios)
- [ ] 4.3.2 Estimar equipos y materiales
- [ ] 4.3.3 Estimar presupuesto preliminar
- [ ] 4.3.4 Calcular reserva de riesgos (20-70%)
- [ ] 4.3.5 Definir dos precios: costo y venta
- [ ] 4.3.6 Definir matriz RACI
- [ ] 4.3.7 Definir plan de contratación
- [ ] 4.3.8 Definir subcontratistas (si aplica)

### 4.4 Riesgos

- [ ] 4.4.1 Identificar riesgos técnicos (interferencias, latencia, cobertura)
- [ ] 4.4.2 Identificar riesgos de ciberseguridad (V2X, IoT, red)
- [ ] 4.4.3 Identificar riesgos de plazo y presupuesto
- [ ] 4.4.4 Identificar riesgos financieros (tipo de cambio, inflación)
- [ ] 4.4.5 Identificar riesgos regulatorios en Cuba
- [ ] 4.4.6 Identificar riesgos de proveedores
- [ ] 4.4.7 Evaluar probabilidad e impacto
- [ ] 4.4.8 Definir plan de mitigación por riesgo
- [ ] 4.4.9 Definir planes de contingencia
- [ ] 4.4.10 Definir matriz de riesgos

### 4.5 Comunicación y seguimiento

- [ ] 4.5.1 Definir plan de comunicación
- [ ] 4.5.2 Definir KPIs de seguimiento
- [ ] 4.5.3 Definir método de control de avance
- [ ] 4.5.4 Definir gestión de cambios
- [ ] 4.5.5 Definir reuniones periódicas
- [ ] 4.5.6 Definir reportes de avance

### 4.6 Análisis de variantes para el cliente

- [ ] 4.6.1 Definir variante básica (solo lo esencial)
- [ ] 4.6.2 Definir variante intermedia (recomendada)
- [ ] 4.6.3 Definir variante completa (con expansión futura)
- [ ] 4.6.4 Comparar costos y beneficios
- [ ] 4.6.5 Presentar recomendación

## FASE 5 — Documento final del proyecto

- [ ] 5.1 Portada según ГОСТ 7.32-2017 (firmable)
- [ ] 5.2 Índice
- [ ] 5.3 Introducción y justificación
- [ ] 5.4 Descripción del ED Park (objeto virtual)
- [ ] 5.5 Base normativa (GOST)
- [ ] 5.6 Diseño técnico (infraestructura + telecom + software + equipos)
- [ ] 5.7 Plan de desarrollo de software
- [ ] 5.8 Plan de montaje e instalación
- [ ] 5.9 Gestión del proyecto (pasaporte, WBS, Gantt, recursos, riesgos)
- [ ] 5.10 Análisis de variantes
- [ ] 5.11 Conclusiones
- [ ] 5.12 Bibliografía (formato ГОСТ 7.1-2003)
- [ ] 5.13 Anexos (planos, diagramas, tablas)
- [ ] 5.14 Revisión final de formato y coherencia
- [ ] 5.15 Exportar a PDF

## FASE 6 — Presentación y defensa

- [ ] 6.1 Preparar presentación breve (10-15 min)
- [ ] 6.2 Preparar resumen oral de 2-3 min
- [ ] 6.3 Anticipar preguntas del profesor
- [ ] 6.4 Preparar demostración visual (planos, diagramas)
- [ ] 6.5 Ensayar la defensa
- [ ] 6.6 Entregar versión electrónica antes de la fecha
- [ ] 6.7 Presentar avances cada clase

## Progreso actual del proyecto

**Total de tareas completadas**: 25/149 (16.8%)

**Fases completadas**: Fase 0 (13/13 tareas completadas), Fase 1 (12/12 tareas completadas)

**Archivos generados**:
- ✅ `00_README.md` — Documentación general del proyecto
- ✅ `01_Fase_0_Preparacion.md` — Documentación completa de la Fase 0
- ✅ `02_Fase_1_Normativa.md` — Base normativa y trazabilidad del proyecto
- ✅ `07_Checklist_Actualizado.md` — Checklist actualizado

**Documentación completada**:
- Definición del alcance completo del proyecto
- Identificación completa de stakeholders
- Tres variantes de oferta (básica, intermedia, completa)
- Descripción detallada de la experiencia del cliente
- Diagramas de flujo y esquemas de interfaz
- Matriz de intereses de stakeholders
- Esquema de estrategia de comunicación
- Recomendación de precios y beneficios
- Base normativa completa con GOST e IEEE aplicables
- Tabla de trazabilidad equipo → GOST
- Formato de citación bibliográfica según ГОСТ 7.1-2003

**Próximo paso recomendado**: Iniciar la FASE 2 — Diseño técnico del sistema completo (infraestructura física y telecom, software y equipos)