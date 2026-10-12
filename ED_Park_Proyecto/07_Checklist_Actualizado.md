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

- [x] 2.5.1 AGV/AMR: 6 unidades, STILL RX 20-20 AGV equiv., 1,000 kg, Wi-Fi 6E + 5G + OBU V2X, 21,000,000 ₽
- [x] 2.5.2 Carretillas elevadoras: 4 unidades (contrapeso ×2, retráctil ×1, apilador ×1), 4,400,000 ₽
- [x] 2.5.3 Transpaletas eléctricas: 4 unidades (acompañante ×2, montado ×2), 1,260,000 ₽
- [x] 2.5.4 Cintas transportadoras: 3 unidades (recta 10 m, con desvío 15 m, pesaje integrado), 1,650,000 ₽
- [x] 2.5.5 Lectores RFID: 6 pórticos fijos + 6 terminales portátiles + 10 escáneres CB, 1,804,000 ₽
- [x] 2.5.6 Básculas digitales: 3 unidades (plataforma 3,000 kg ×2, mesa 30 kg ×1), 218,000 ₽
- [x] 2.5.7 Sensores IoT: 76 unidades (T°/HR ×30, presencia ×20, incendio ×20, puertas ×6), 676,000 ₽
- [x] 2.5.8 Servidores físicos: SRV-01 WMS + SRV-02 AGV/SCADA + SRV-03 backup + SAI ×2 + rack, 2,475,000 ₽
- [x] 2.5.9 Climatización: 6 unidades (precisión zona B ×2, naves ×2, sala control ×1, oficinas ×1), 1,320,000 ₽
- [x] 2.5.10 Impresoras etiquetas RFID+CB: 4 unidades Zebra ZT411 equiv., 220,000 ₽
- [x] 2.5.11 Cámaras IP industriales: 12 unidades (interior ×8 + PTZ exterior ×4), 484,000 ₽
- [x] 2.5.12 PLC y controladores: 4 unidades (muelles ×2, cintas ×1, climatización ×1), 290,000 ₽
- [x] 2.5.13 Equipos telecom referenciados a 03_03 con costo consolidado 14,770,000 ₽
- [x] 2.5.14 Tabla resumen inversión por categoría: total ~52,967,000 ₽ (~293 unidades)
- [x] 2.5.15 Tabla trazabilidad equipo → GOST (29 equipos × 2 normas)
- [x] 2.5.16 Tabla GOST por número de equipos cubiertos (8 estándares)
- [x] 2.5.17 Justificación técnica y GOST para cada categoría de equipo

### 2.6 Esquemas y diagramas

- [x] 2.6.1 Diagrama de topología de red (jerarquía 3 niveles + anillo núcleo 10G, Mermaid graph TD)
- [x] 2.6.2 Esquema de ubicación física de equipos en el plano (5,000 m² 7 zonas, Mermaid block-beta)
- [x] 2.6.3 Esquema de segmentación VLAN y QoS (8 VLANs + DSCP EF/AF/CS + zonas OT/IT, Mermaid graph LR)
- [x] 2.6.4 Esquema de redundancia de canales (4 niveles: RSTP + WAN dual + dual radio AGV + SAI, Mermaid graph TD)
- [x] 2.6.5 Esquema de arquitectura V2X/V2I para AGV (BSM/SPaT/ICA/MAP 4 fases, Mermaid sequenceDiagram)
- [x] 2.6.6 Esquema de cobertura Wi-Fi en las 2 naves y patio (14 APs + 3 bandas + solapamiento 20 %, Mermaid graph TB)
- [x] 2.6.7 Esquema de sincronización de tiempo PTP (GM GPS → BC → TC → OC ±1 µs, Mermaid graph TD)
- [x] 2.6.8 Diagrama de arquitectura del software (6 módulos + bus MQTT/REST/WS + 3 BD, Mermaid graph LR)
- [x] 2.6.9 Diagrama de flujo de datos (recepción → almacenamiento → picking → expedición, Mermaid flowchart TD)
- [x] 2.6.10 Diagrama de integración de sistemas (OT/IT/exterior + protocolos + VLANs, Mermaid graph TB)

### 2.7 Trazabilidad GOST

- [x] 2.7.1 Definir los 12 estándares GOST/IEEE del proyecto (N-01 a N-12) con código, título y año
- [x] 2.7.2 Tabla T — Trazabilidad telecom (38 vínculos, T-01 a T-38): equipo → GOST → sección → justificación
- [x] 2.7.3 Tabla H — Trazabilidad hardware (40 vínculos, H-01 a H-40): equipo → GOST → sección → justificación
- [x] 2.7.4 Tabla S — Trazabilidad software (16 vínculos, S-01 a S-16): módulo → GOST → sección → justificación
- [x] 2.7.5 Resumen por GOST: 12 estándares con número de elementos cubiertos (total 95 vínculos)
- [x] 2.7.6 Mapa de calor de cobertura normativa (diagrama Mermaid xychart)
- [x] 2.7.7 Trazabilidad inversa: por sección del proyecto (03_02 / 03_03 / 03_04 / 03_05)
- [x] 2.7.8 Identificar los 3 estándares pilares (МЭК 62443 / ИСО 15745-4 / 70982-2023 — presentes en 4 secciones)
- [x] 2.7.9 Referencias normativas completas (12 estándares en formato ГОСТ 7.1-2003)

## FASE 3 — Plan de montaje e instalación

### 3.3 Puesta en marcha y pruebas de aceptación (`04_03`)

- [x] 3.3.1 PT-01 Prueba cobertura Wi-Fi (RSSI ≥ −65 dBm, SNR ≥ 20 dB, handover < 50 ms, 2 días)
- [x] 3.3.2 PT-02 Prueba latencia de red (VLAN 10 AGV < 5 ms, P99, jitter < 1 ms, 2 días)
- [x] 3.3.3 PT-03 Prueba redundancia (RSTP < 50 ms, WAN failover < 30 s, SAI < 20 ms, 2 días)
- [x] 3.3.4 PT-04 Prueba sincronización PTP (±1 µs nodos finales, BMCA < 10 s, 1 día)
- [x] 3.3.5 PT-05 Prueba V2X/V2I (BSM 10 Hz, latencia ICA < 5 ms, reacción AGV < 500 ms, 2 días)
- [x] 3.3.6 PT-06 Prueba ciberseguridad (RBAC, TLS 1.3, ECDSA, OWASP ZAP, 0 vulns críticas, 2 días)
- [x] 3.3.7 PT-07 Prueba integración software (8 escenarios E-01..E-08 end-to-end, 3 días)
- [x] 3.3.8 PT-08 Prueba AGV operación real (8 h, 6 AGV, 0 colisiones, ≥ 95 % misiones, 2 días)
- [x] 3.3.9 Plan de validación global con diagrama flowchart (Mermaid) y Gantt 3 semanas
- [x] 3.3.10 Tabla de criterios de aceptación global del sistema (8 bloques → APROBADO)
- [x] 3.3.11 Plan de capacitación: 7 perfiles, 4 módulos (C-01..C-04), materiales y evaluación
- [x] 3.3.12 Resumen fase puesta en marcha: ~26 días hábiles, ~400,000 ₽
- [x] 3.3.13 4 diagramas Mermaid: secuencia V2X, flowchart validación, Gantt validación, Gantt AGV 8h

- [x] 3.2.1 IT-01 Cableado estructurado (12 días, fibra OM4 180 m + Cat6A S/FTP 850 m, certificación Fluke)
- [x] 3.2.2 IT-02 Switches industriales ×10 (6 días, RSTP, VLAN 99 gestión, NTP→PTP)
- [x] 3.2.3 IT-03 Puntos de acceso Wi-Fi 6/6E ×14 (5 días, WPA3-Enterprise, SSIDs por VLAN)
- [x] 3.2.4 IT-04 Gateways + edge gateways ×8 + PTP Grandmaster (6 días, Zigbee, OPC-UA, firewall OT/IT)
- [x] 3.2.5 IT-05 Servidores SRV-01/02/03 + SAI ×2 (5 días, RAID, SO base Linux, 10GbE)
- [x] 3.2.6 IT-06 VLANs (4 días, 8 segmentos, ACLs OT/IT, asignación a SSIDs Wi-Fi)
- [x] 3.2.7 IT-07 QoS (3 días, DSCP EF/AF/CS, colas WRR, latencia VLAN 10 < 5 ms)
- [x] 3.2.8 IT-08 Redundancia (3 días, RSTP < 50 ms, WAN failover < 30 s, SAI verificado)
- [x] 3.2.9 IT-09 WMS (8 días, Spring Boot + PostgreSQL, datos maestros, flujo recepción→expedición)
- [x] 3.2.10 IT-10 SCADA (8 días, Ignition/WinCC, OPC-UA, InfluxDB, 100+ tags, prueba 24 h)
- [x] 3.2.11 IT-11 Control AGV + V2X/V2I (10 días, ROS 2, MQTT, mapa digital, misión end-to-end)
- [x] 3.2.12 IT-12 Integración sistemas (8 días, API Gateway, OAuth 2.0, TLS 1.3, webhook ERP)
- [x] 3.2.13 IT-13 Verificación integral (5 días, RF survey, iperf3, OWASP ZAP, informe firmado)
- [x] 3.2.14 Tabla resumen: 13 tareas, ~58 días, 17 personas, ~1,195,000 ₽
- [x] 3.2.15 Cronograma Gantt (Mermaid, 12 semanas, IT-09/IT-10 en paralelo)
- [x] 3.2.16 Tabla de 10 riesgos de instalación con probabilidad, impacto y mitigación
- [x] 3.2.17 KPIs de instalación (7 indicadores con metas cuantitativas)

- [x] 3.1 MT-01 Preparación del suelo y marcaje (5 días, cinta magnética AGV, señalización)
- [x] 3.2 MT-02 Montaje de estanterías (15 días, zonas A/B/C, 4 subtareas, anclaje tacos químicos)
- [x] 3.3 MT-03 Montaje de cintas transportadoras (10 días, CT-01/02/03, PLC Siemens S7-1200)
- [x] 3.4 MT-04 Instalación de muelles de carga (12 días, 4 muelles, niveladores hidráulicos, puertas seccionales)
- [x] 3.5 MT-05 Montaje de sensores IoT (10 días, 76 sensores Zigbee, 5 subtareas, edge gateways)
- [x] 3.6 MT-06 Puesta en servicio AGV/AMR (15 días, 6 AGV, 7 subtareas, pruebas V2X/V2I)
- [x] 3.7 MT-07 Montaje climatización (8 días, 6 unidades, F-Gas, PLC precisión zona B)
- [x] 3.8 MT-08 Verificación y pruebas de montaje (5 días, checklist técnico integral)
- [x] 3.9 Tabla resumen: 8 tareas, ~50 días hábiles, 20 personas, costo mano de obra ~1,380,000 ₽
- [x] 3.10 Cronograma Gantt (Mermaid, 10 semanas, rutas críticas identificadas)
- [x] 3.11 Tabla de 10 riesgos de montaje con probabilidad, impacto y estrategia de mitigación
- [x] 3.12 Matriz de riesgos (Mermaid quadrantChart, 10 riesgos posicionados)
- [x] 3.13 KPIs de progreso del montaje (6 indicadores)
- [x] 3.14 Referencias normativas (ГОСТ МЭК 61131-1, ИСО 15745-4, 70982-2023, МЭК 62443, IEC 62026-3)

## FASE 4 — Gestión del proyecto

### 4.1 Pasaporte del proyecto (`05_01`)

- [x] 4.1.1 Nombre del proyecto: "Implementación del Sistema Completo de Automatización y Telecomunicaciones del ED Park" (código ED-PARK-2025-001)
- [x] 4.1.2 Objetivo general (SMART) + 7 objetivos específicos con indicador de logro y plazo
- [x] 4.1.3 Alcance detallado — incluye (10 categorías: física, telecom, software, hardware, montaje, instalación, pruebas, capacitación, documentación, gestión)
- [x] 4.1.4 Alcance detallado — NO incluye (8 exclusiones explícitas: obra civil, compra real, código, integración real, certificación, mantenimiento, expansión, sistemas gubernamentales)
- [x] 4.1.5 Tabla de stakeholders (10 partes interesadas, rol, interés, influencia, estrategia de comunicación)
- [x] 4.1.6 12 criterios de éxito con métrica y valor objetivo (CS-01..CS-12)
- [x] 4.1.7 8 restricciones (presupuesto 117M₽, plazo 18 meses, superficie 5,000 m², normativa, formato GOST, entorno tropical, regulatorio Cuba)
- [x] 4.1.8 10 supuestos del proyecto (SA-01..SA-10)
- [x] 4.1.9 8 exclusiones explícitas del proyecto
- [x] 4.1.10 10 entregables principales con fase, responsable e hito asociado
- [x] 4.1.11 11 hitos clave (M-01..M-11) con mes y descripción
- [x] 4.1.12 Diagrama de hitos Mermaid timeline (18 meses)
- [x] 4.1.13 Presupuesto desglosado por categoría: costo base 90M₽ + reserva 30 % = precio 117M₽
- [x] 4.1.14 Tabla comparativa 3 variantes (básica 87.75M / intermedia 117M / completa 146.25M)
- [x] 4.1.15 Flujo de caja estimado por fases
- [x] 4.1.16 Cronograma de alto nivel 18 meses (Mermaid Gantt)
- [x] 4.1.17 Bloque de firma y aprobación (director, cliente, profesor evaluador)

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

**Total de tareas completadas**: 175/247 (70.9%)

**Fases completadas**:
- ✅ Fase 0 — Preparación y encuadre (13/13)
- ✅ Fase 1 — Investigación normativa (12/12)
- ✅ **Fase 2 — Diseño técnico COMPLETA** (87/87, archivos `03_01` a `03_07`)
- ✅ **Fase 3 — Montaje e instalación COMPLETA** (44/44, archivos `04_01` a `04_03`)
- ✅ Fase 4.1 — Pasaporte del proyecto (17/17, archivo `05_01`)

**Fases completadas**:
- ✅ Fase 0 — Preparación y encuadre (13/13)
- ✅ Fase 1 — Investigación normativa (12/12)
- ✅ **Fase 2 — Diseño técnico COMPLETA** (87/87, archivos `03_01` a `03_07`)
- ✅ **Fase 3 — Montaje e instalación COMPLETA** (44/44):
  - ✅ 3.1 Plan de montaje (14/14, `04_01`)
  - ✅ 3.2 Plan de instalación red y software (17/17, `04_02`)
  - ✅ 3.3 Puesta en marcha y pruebas (13/13, `04_03`)

**Fases completadas**:
- ✅ Fase 0 — Preparación y encuadre (13/13 tareas)
- ✅ Fase 1 — Investigación normativa (12/12 tareas)
- ✅ **Fase 2 — Diseño técnico COMPLETA** (87/87 tareas):
  - ✅ 2.1 Descripción del ED Park (`03_01`)
  - ✅ 2.2 Infraestructura física (`03_02`)
  - ✅ 2.3 Infraestructura de telecomunicaciones (`03_03`) — **17 tecnologías Tema Nº 12**
  - ✅ 2.4 Software de gestión — diseño virtual (`03_04`)
  - ✅ 2.5 Equipos y hardware (`03_05`)
  - ✅ 2.6 Esquemas y diagramas (`03_06`) — **10 diagramas Mermaid**
  - ✅ 2.7 Trazabilidad GOST (`03_07`) — **95 vínculos normativos**

**Archivos generados (Fase 2 completa)**:
- ✅ `03_Fase_2_Diseno_Tecnico/03_01_Descripcion_ED_Park.md`
- ✅ `03_Fase_2_Diseno_Tecnico/03_02_Infraestructura_Fisica.md`
- ✅ `03_Fase_2_Diseno_Tecnico/03_03_Infraestructura_Telecom.md`
- ✅ `03_Fase_2_Diseno_Tecnico/03_04_Software_Gestion.md`
- ✅ `03_Fase_2_Diseno_Tecnico/03_05_Equipos_Hardware.md`
- ✅ `03_Fase_2_Diseno_Tecnico/03_06_Esquemas_Diagramas.md`
- ✅ `03_Fase_2_Diseno_Tecnico/03_07_Trazabilidad_GOST.md`
- ✅ `04_Fase_3_Montaje_Instalacion/04_01_Plan_Montaje.md`
- ✅ `04_Fase_3_Montaje_Instalacion/04_02_Plan_Instalacion.md`
- ✅ `04_Fase_3_Montaje_Instalacion/04_03_Puesta_Marcha_Pruebas.md`
- ✅ `05_Fase_4_Gestion_Proyecto/05_01_Pasaporte_Proyecto.md`

**Diagramas generados en 03_06 (resumen)**:
- D-01: Topología red — jerarquía 3 niveles, anillo núcleo 10G
- D-02: Ubicación física — plano 5,000 m², 7 zonas, todos los equipos
- D-03: VLAN/QoS — 8 VLANs, DSCP EF/AF/CS, zonas OT/IT/exterior
- D-04: Redundancia — RSTP + WAN dual + dual radio AGV + SAI (4 niveles)
- D-05: V2X/V2I — BSM/SPaT/ICA/MAP, latencia ICA < 5 ms
- D-06: Cobertura Wi-Fi — 14 APs, 3 bandas, solapamiento 20 %
- D-07: PTP — GM GPS → BC → TC → OC, precisión ±1 µs
- D-08: Arquitectura software — 6 módulos + bus MQTT/REST/WS
- D-09: Flujo de datos — recepción → almacenamiento → picking → expedición
- D-10: Integración sistemas — OT/IT/exterior con protocolos y VLANs

**Próximo paso recomendado**: Continuar **FASE 4** con `05_02_WBS_EDT.md` — estructura de desglose del trabajo (WBS) con 4 niveles de jerarquía, codificación WBS y diagrama Mermaid.