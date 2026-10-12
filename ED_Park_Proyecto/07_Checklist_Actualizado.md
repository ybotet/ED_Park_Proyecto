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
- [x] 2.1.8 Redactar descripción narrativa del parque
- [x] 2.1.9 Describir flujos operativos diarios
- [x] 2.1.10 Describir la experiencia del cliente

### 2.2 Infraestructura física

- [x] 2.2.1 Describir naves y su distribución interna (nave principal 2,000 m² + nave recepción/expedición 1,100 m²)
- [x] 2.2.2 Describir muelles de carga (4 posiciones hidráulicas, capacidad 6,000 kg, ampliables a 6)
- [x] 2.2.3 Describir patio de maniobras (700 m², circulación antihoraria, radio de giro ≥ 13 m)
- [x] 2.2.4 Describir zonas de almacenamiento (Zona A convencional, Zona B temperatura controlada, Zona C alta rotación)
- [x] 2.2.5 Describir zonas de picking y embalaje (350 m², 8 mesas, 10 terminales WMS, 2 pórticos RFID)
- [x] 2.2.6 Describir oficinas y sala de control (250 m², NOC, servidores rack, videovigilancia, SAI)

### 2.3 Infraestructura de telecomunicaciones

- [x] 2.3.1 Tecnología 1: Промышленный Wi-Fi — definición, aplicación, equipos, GOST, justificación
- [x] 2.3.2 Tecnología 2: Wi-Fi 6/6E (IEEE 802.11ax) — 14 APs, controlador WLC, parámetros de rendimiento
- [x] 2.3.3 Tecnología 3: Частные LTE-сети — eNodeB, módems AGV, cobertura exterior
- [x] 2.3.4 Tecnología 4: Private 5G — gNB ×4, core UPF+AMF, módems 5G para AGV
- [x] 2.3.5 Tecnología 5: Ethernet (IEEE 802.3) — backbone fibra OM4 10G + Cat6A S/FTP
- [x] 2.3.6 Tecnología 6: Industrial Ethernet — jerarquía 3 niveles (núcleo/distribución/campo)
- [x] 2.3.7 Tecnología 7: Беспроводные mesh-сети — 6 nodos mesh fijos + embarcados en AGV
- [x] 2.3.8 Tecnología 8: Выделенные сети IoT — Zigbee, 30–40 sensores T°/HR, VLAN IoT dedicada
- [x] 2.3.9 Tecnología 9: Точки доступа — planificación RF, 14 APs, solapamiento 20 %
- [x] 2.3.10 Tecnología 10: Промышленные коммутаторы — 10 switches en 3 niveles jerárquicos
- [x] 2.3.11 Tecnología 11: Резервированные каналы — RSTP + WAN dual fibra/LTE + SAI + dual radio AGV
- [x] 2.3.12 Tecnología 12: Серверы связи — SRV-01 WMS, SRV-02 AGV/SCADA, SRV-03 backup
- [x] 2.3.13 Tecnología 13: Шлюзы — 4 gateways (Zigbee→MQTT, RFID→TCP, Modbus→OPC-UA)
- [x] 2.3.14 Tecnología 14: Edge-шлюзы — 4 edge gateways (IoT, AGV, seguridad OT, muelles)
- [x] 2.3.15 Tecnología 15: PTP (IEEE 1588) — jerarquía GM→BC→TC→OC, precisión < 1 µs
- [x] 2.3.16 Tecnología 16: M2M — MQTT v5 + OPC-UA + Modbus TCP, arquitectura publisher/subscriber
- [x] 2.3.17 Tecnología 17: V2X/V2I — RSU ×5, OBU ×5–8, mensajes BSM/SPaT/ICA/MAP
- [x] 2.3.18 Tabla consolidada de ~130–155 equipos telecom (27 tipos)
- [x] 2.3.19 Diagrama de topología de red completa (Mermaid)
- [x] 2.3.20 Esquema de cobertura Wi-Fi (14 APs en planta, Mermaid)
- [x] 2.3.21 Esquema de redundancia (RSTP + WAN dual + SAI, Mermaid)
- [x] 2.3.22 Esquema V2X/V2I (sequenceDiagram BSM/ICA/SPaT, Mermaid)
- [x] 2.3.23 Esquema de sincronización PTP (GM→BC→TC→OC, Mermaid)
- [x] 2.3.24 Tabla de parámetros de rendimiento (latencia, disponibilidad, cobertura)
- [x] 2.3.25 Tabla de segmentación VLAN y QoS (8 VLANs con DSCP)
- [x] 2.3.26 Tabla de ciberseguridad (ГОСТ МЭК 62443 SL 2, 9 medidas)
- [x] 2.3.27 Referencias normativas (10 GOST + IEEE citados en formato ГОСТ 7.1-2003)

### 2.4 Software de gestión (diseño, no código)

- [x] 2.4.1 Definir M-01 WMS (10 req. funcionales, tecnología Spring Boot/PostgreSQL, integración MQTT/REST)
- [x] 2.4.2 Definir M-02 Control de AGV (10 req., ROS 2, latencia < 50 ms, parada emergencia < 500 ms)
- [x] 2.4.3 Definir M-03 V2X/V2I (mensajes BSM/SPaT/ICA/MAP, latencia ICA < 5 ms)
- [x] 2.4.4 Definir M-04 SCADA (8 req., Ignition/WinCC, OPC-UA, InfluxDB, 2,000 tags)
- [x] 2.4.5 Definir M-05 Integración (API Gateway, OAuth 2.0, EDI, webhooks, portal cliente)
- [x] 2.4.6 Definir M-06 UI (5 perfiles, React 18, app móvil React Native, WebSocket)
- [x] 2.4.7 Definir ciberseguridad SL 2 (ГОСТ МЭК 62443, 10 medidas: RBAC, TLS 1.3, ECDSA, auditoría)
- [x] 2.4.8 Estimar equipo de desarrollo (13 roles: arquitecto, backend ×3, frontend ×2, DevOps, QA ×2, seguridad, SM)
- [x] 2.4.9 Definir metodología Scrum (sprints 2 semanas, 9 hitos, 15 meses de desarrollo)
- [x] 2.4.10 Estimar plazos y costo (74 persona-mes, ~7,400,000 ₽, hitos MS-01 a MS-09)
- [x] 2.4.11 Generar diagrama de arquitectura de software (Mermaid — 6 módulos + bus + datos + campo)
- [x] 2.4.12 Generar diagrama de flujo de datos — proceso de picking (Mermaid flowchart)
- [x] 2.4.13 Generar diagrama de flujo de datos — monitoreo SCADA (Mermaid flowchart)
- [x] 2.4.14 Generar diagrama de integración de sistemas (Mermaid — ED Park ↔ ERP/TMS/campo)

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

**Total de tareas completadas**: 78/170 (45.9%)

**Fases completadas**:
- ✅ Fase 0 — Preparación y encuadre (13/13 tareas)
- ✅ Fase 1 — Investigación normativa (12/12 tareas)
- ✅ Fase 2.1 — Descripción del ED Park (10/10 tareas, archivo `03_01`)
- ✅ Fase 2.2 — Infraestructura física (6/6 tareas, archivo `03_02`)
- ✅ Fase 2.3 — Infraestructura de telecomunicaciones (27/27 tareas, archivo `03_03`)
- ✅ Fase 2.4 — Software de gestión — diseño virtual (14/14 tareas, archivo `03_04`)

**Archivos generados**:
- ✅ `00_README.md` — Documentación general del proyecto
- ✅ `01_Fase_0_Preparacion.md` — Fase 0 completa
- ✅ `02_Fase_1_Normativa.md` — Base normativa (12 GOST + IEEE)
- ✅ `03_Fase_2_Diseno_Tecnico/03_01_Descripcion_ED_Park.md` — Descripción del objeto virtual
- ✅ `03_Fase_2_Diseno_Tecnico/03_02_Infraestructura_Fisica.md` — Infraestructura física (5,000 m²)
- ✅ `03_Fase_2_Diseno_Tecnico/03_03_Infraestructura_Telecom.md` — 17 tecnologías Tema Nº 12
- ✅ `03_Fase_2_Diseno_Tecnico/03_04_Software_Gestion.md` — Diseño virtual del software (6 módulos)
- ✅ `07_Checklist_Actualizado.md` — Checklist actualizado

**Documentación completada en Fase 2.4**:
- 6 módulos de software: M-01 WMS, M-02 AGV, M-03 V2X/V2I, M-04 SCADA, M-05 Integración, M-06 UI
- Equipo de 13 roles con responsabilidades y fases de actividad
- Metodología Scrum (sprints 2 semanas, 9 hitos en 15 meses)
- Estimación: 74 persona-mes, ~7,400,000 ₽
- Ciberseguridad SL 2 (ГОСТ МЭК 62443, 10 medidas)
- 4 diagramas Mermaid: arquitectura, flujo picking, flujo SCADA, integración sistemas

**Próximo paso recomendado**: Generar `03_05_Equipos_Hardware.md` — Lista completa de equipos hardware (AGV, carretillas, cintas, RFID, sensores, servidores, climatización) con modelos, cantidades, GOST y costo estimado.