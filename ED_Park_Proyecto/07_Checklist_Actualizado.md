# Checklist Actualizado del Proyecto ED Park

## FASE 0 вЂ” PreparaciГіn y encuadre

- [x] 0.1 Confirmar tema NВє 12 asignado por sorteo
- [x] 0.2 Releer indicaciones del profesor (clase 12 y 19 sept)
- [x] 0.3 Definir objeto virtual: ED Park
- [x] 0.4 Definir alcance del proyecto (sistema completo)
- [x] 0.5 Identificar stakeholders
- [x] 0.6 Definir ubicaciГіn: Matanzas, Cuba
- [x] 0.7 Definir tipo de mercancГ­a: productos electrГіnicos
- [x] 0.8 Definir nivel de automatizaciГіn: medio
- [x] 0.9 Definir superficie: 0.5 ha (5,000 mВІ)
- [x] 0.10 Definir estructura fГ­sica (2 naves + oficinas + patio)
- [x] 0.11 Definir variantes para el cliente (bГЎsica, intermedia, completa)
- [x] 0.12 Definir experiencia del cliente (cГіmo usarГЎ el sistema)

## FASE 1 вЂ” InvestigaciГіn normativa (GOST y estГЎndares)

- [x] 1.1 Buscar Р“РћРЎРў Р  РРЎРћ 15745-4-2010 (Ethernet industrial)
- [x] 1.2 Buscar Р“РћРЎРў Р  РњР­Рљ 61850-3 (comunicaciones entornos duros)
- [x] 1.3 Buscar Р“РћРЎРў Р  70982-2023 (V2X/V2I)
- [x] 1.4 Buscar Р“РћРЎРў Р  РњР­Рљ 62443-3-3-2016 (ciberseguridad industrial)
- [x] 1.5 Buscar IEEE 802.11ax (Wi-Fi 6/6E)
- [x] 1.6 Buscar IEEE 802.3 (Ethernet)
- [x] 1.7 Buscar Р“РћРЎРў IEC 62026-3-2015 (DeviceNet) si aplica
- [x] 1.8 Buscar IEEE 1588 (PTP) para sincronizaciГіn de tiempo
- [x] 1.9 Buscar Р“РћРЎРў 7.32-2017 (formato de documentaciГіn)
- [x] 1.10 Buscar Р“РћРЎРў 7.1-2003 (formato de bibliografГ­a)
- [x] 1.11 Elaborar tabla de trazabilidad: cada equipo в†’ su GOST
- [x] 1.12 Redactar apartado "Base normativa del proyecto"

## FASE 2 вЂ” DiseГ±o tГ©cnico del sistema completo

### 2.1 DescripciГіn del objeto

- [x] 2.1.1 Nombre: ED Park
- [x] 2.1.2 UbicaciГіn: Matanzas, Cuba
- [x] 2.1.3 Superficie: 0.5 ha (5,000 mВІ)
- [x] 2.1.4 MercancГ­a: productos electrГіnicos
- [x] 2.1.5 AutomatizaciГіn: media (5-8 AGV)
- [x] 2.1.6 Personal: ~38 personas
- [x] 2.1.7 Estructura: 2 naves + oficinas + patio
- [x] 2.1.8 Redactar descripciГіn narrativa del parque
- [x] 2.1.9 Describir flujos operativos diarios
- [x] 2.1.10 Describir la experiencia del cliente

### 2.2 Infraestructura fГ­sica

- [x] 2.2.1 Describir naves y su distribuciГіn interna (nave principal 2,000 mВІ + nave recepciГіn/expediciГіn 1,100 mВІ)
- [x] 2.2.2 Describir muelles de carga (4 posiciones hidrГЎulicas, capacidad 6,000 kg, ampliables a 6)
- [x] 2.2.3 Describir patio de maniobras (700 mВІ, circulaciГіn antihoraria, radio de giro в‰Ґ 13 m)
- [x] 2.2.4 Describir zonas de almacenamiento (Zona A convencional, Zona B temperatura controlada, Zona C alta rotaciГіn)
- [x] 2.2.5 Describir zonas de picking y embalaje (350 mВІ, 8 mesas, 10 terminales WMS, 2 pГіrticos RFID)
- [x] 2.2.6 Describir oficinas y sala de control (250 mВІ, NOC, servidores rack, videovigilancia, SAI)

### 2.3 Infraestructura de telecomunicaciones

- [x] 2.3.1 TecnologГ­a 1: РџСЂРѕРјС‹С€Р»РµРЅРЅС‹Р№ Wi-Fi вЂ” definiciГіn, aplicaciГіn, equipos, GOST, justificaciГіn
- [x] 2.3.2 TecnologГ­a 2: Wi-Fi 6/6E (IEEE 802.11ax) вЂ” 14 APs, controlador WLC, parГЎmetros de rendimiento
- [x] 2.3.3 TecnologГ­a 3: Р§Р°СЃС‚РЅС‹Рµ LTE-СЃРµС‚Рё вЂ” eNodeB, mГіdems AGV, cobertura exterior
- [x] 2.3.4 TecnologГ­a 4: Private 5G вЂ” gNB Г—4, core UPF+AMF, mГіdems 5G para AGV
- [x] 2.3.5 TecnologГ­a 5: Ethernet (IEEE 802.3) вЂ” backbone fibra OM4 10G + Cat6A S/FTP
- [x] 2.3.6 TecnologГ­a 6: Industrial Ethernet вЂ” jerarquГ­a 3 niveles (nГєcleo/distribuciГіn/campo)
- [x] 2.3.7 TecnologГ­a 7: Р‘РµСЃРїСЂРѕРІРѕРґРЅС‹Рµ mesh-СЃРµС‚Рё вЂ” 6 nodos mesh fijos + embarcados en AGV
- [x] 2.3.8 TecnologГ­a 8: Р’С‹РґРµР»РµРЅРЅС‹Рµ СЃРµС‚Рё IoT вЂ” Zigbee, 30вЂ“40 sensores TВ°/HR, VLAN IoT dedicada
- [x] 2.3.9 TecnologГ­a 9: РўРѕС‡РєРё РґРѕСЃС‚СѓРїР° вЂ” planificaciГіn RF, 14 APs, solapamiento 20 %
- [x] 2.3.10 TecnologГ­a 10: РџСЂРѕРјС‹С€Р»РµРЅРЅС‹Рµ РєРѕРјРјСѓС‚Р°С‚РѕСЂС‹ вЂ” 10 switches en 3 niveles jerГЎrquicos
- [x] 2.3.11 TecnologГ­a 11: Р РµР·РµСЂРІРёСЂРѕРІР°РЅРЅС‹Рµ РєР°РЅР°Р»С‹ вЂ” RSTP + WAN dual fibra/LTE + SAI + dual radio AGV
- [x] 2.3.12 TecnologГ­a 12: РЎРµСЂРІРµСЂС‹ СЃРІСЏР·Рё вЂ” SRV-01 WMS, SRV-02 AGV/SCADA, SRV-03 backup
- [x] 2.3.13 TecnologГ­a 13: РЁР»СЋР·С‹ вЂ” 4 gateways (Zigbeeв†’MQTT, RFIDв†’TCP, Modbusв†’OPC-UA)
- [x] 2.3.14 TecnologГ­a 14: Edge-С€Р»СЋР·С‹ вЂ” 4 edge gateways (IoT, AGV, seguridad OT, muelles)
- [x] 2.3.15 TecnologГ­a 15: PTP (IEEE 1588) вЂ” jerarquГ­a GMв†’BCв†’TCв†’OC, precisiГіn < 1 Вµs
- [x] 2.3.16 TecnologГ­a 16: M2M вЂ” MQTT v5 + OPC-UA + Modbus TCP, arquitectura publisher/subscriber
- [x] 2.3.17 TecnologГ­a 17: V2X/V2I вЂ” RSU Г—5, OBU Г—5вЂ“8, mensajes BSM/SPaT/ICA/MAP
- [x] 2.3.18 Tabla consolidada de ~130вЂ“155 equipos telecom (27 tipos)
- [x] 2.3.19 Diagrama de topologГ­a de red completa (Mermaid)
- [x] 2.3.20 Esquema de cobertura Wi-Fi (14 APs en planta, Mermaid)
- [x] 2.3.21 Esquema de redundancia (RSTP + WAN dual + SAI, Mermaid)
- [x] 2.3.22 Esquema V2X/V2I (sequenceDiagram BSM/ICA/SPaT, Mermaid)
- [x] 2.3.23 Esquema de sincronizaciГіn PTP (GMв†’BCв†’TCв†’OC, Mermaid)
- [x] 2.3.24 Tabla de parГЎmetros de rendimiento (latencia, disponibilidad, cobertura)
- [x] 2.3.25 Tabla de segmentaciГіn VLAN y QoS (8 VLANs con DSCP)
- [x] 2.3.26 Tabla de ciberseguridad (Р“РћРЎРў РњР­Рљ 62443 SL 2, 9 medidas)
- [x] 2.3.27 Referencias normativas (10 GOST + IEEE citados en formato Р“РћРЎРў 7.1-2003)

### 2.4 Software de gestiГіn (diseГ±o, no cГіdigo)

- [x] 2.4.1 Definir M-01 WMS (10 req. funcionales, tecnologГ­a Spring Boot/PostgreSQL, integraciГіn MQTT/REST)
- [x] 2.4.2 Definir M-02 Control de AGV (10 req., ROS 2, latencia < 50 ms, parada emergencia < 500 ms)
- [x] 2.4.3 Definir M-03 V2X/V2I (mensajes BSM/SPaT/ICA/MAP, latencia ICA < 5 ms)
- [x] 2.4.4 Definir M-04 SCADA (8 req., Ignition/WinCC, OPC-UA, InfluxDB, 2,000 tags)
- [x] 2.4.5 Definir M-05 IntegraciГіn (API Gateway, OAuth 2.0, EDI, webhooks, portal cliente)
- [x] 2.4.6 Definir M-06 UI (5 perfiles, React 18, app mГіvil React Native, WebSocket)
- [x] 2.4.7 Definir ciberseguridad SL 2 (Р“РћРЎРў РњР­Рљ 62443, 10 medidas: RBAC, TLS 1.3, ECDSA, auditorГ­a)
- [x] 2.4.8 Estimar equipo de desarrollo (13 roles: arquitecto, backend Г—3, frontend Г—2, DevOps, QA Г—2, seguridad, SM)
- [x] 2.4.9 Definir metodologГ­a Scrum (sprints 2 semanas, 9 hitos, 15 meses de desarrollo)
- [x] 2.4.10 Estimar plazos y costo (74 persona-mes, ~7,400,000 в‚Ѕ, hitos MS-01 a MS-09)
- [x] 2.4.11 Generar diagrama de arquitectura de software (Mermaid вЂ” 6 mГіdulos + bus + datos + campo)
- [x] 2.4.12 Generar diagrama de flujo de datos вЂ” proceso de picking (Mermaid flowchart)
- [x] 2.4.13 Generar diagrama de flujo de datos вЂ” monitoreo SCADA (Mermaid flowchart)
- [x] 2.4.14 Generar diagrama de integraciГіn de sistemas (Mermaid вЂ” ED Park в†” ERP/TMS/campo)

### 2.5 Equipos (hardware)

- [x] 2.5.1 AGV/AMR: 6 unidades, STILL RX 20-20 AGV equiv., 1,000 kg, Wi-Fi 6E + 5G + OBU V2X, 21,000,000 в‚Ѕ
- [x] 2.5.2 Carretillas elevadoras: 4 unidades (contrapeso Г—2, retrГЎctil Г—1, apilador Г—1), 4,400,000 в‚Ѕ
- [x] 2.5.3 Transpaletas elГ©ctricas: 4 unidades (acompaГ±ante Г—2, montado Г—2), 1,260,000 в‚Ѕ
- [x] 2.5.4 Cintas transportadoras: 3 unidades (recta 10 m, con desvГ­o 15 m, pesaje integrado), 1,650,000 в‚Ѕ
- [x] 2.5.5 Lectores RFID: 6 pГіrticos fijos + 6 terminales portГЎtiles + 10 escГЎneres CB, 1,804,000 в‚Ѕ
- [x] 2.5.6 BГЎsculas digitales: 3 unidades (plataforma 3,000 kg Г—2, mesa 30 kg Г—1), 218,000 в‚Ѕ
- [x] 2.5.7 Sensores IoT: 76 unidades (TВ°/HR Г—30, presencia Г—20, incendio Г—20, puertas Г—6), 676,000 в‚Ѕ
- [x] 2.5.8 Servidores fГ­sicos: SRV-01 WMS + SRV-02 AGV/SCADA + SRV-03 backup + SAI Г—2 + rack, 2,475,000 в‚Ѕ
- [x] 2.5.9 ClimatizaciГіn: 6 unidades (precisiГіn zona B Г—2, naves Г—2, sala control Г—1, oficinas Г—1), 1,320,000 в‚Ѕ
- [x] 2.5.10 Impresoras etiquetas RFID+CB: 4 unidades Zebra ZT411 equiv., 220,000 в‚Ѕ
- [x] 2.5.11 CГЎmaras IP industriales: 12 unidades (interior Г—8 + PTZ exterior Г—4), 484,000 в‚Ѕ
- [x] 2.5.12 PLC y controladores: 4 unidades (muelles Г—2, cintas Г—1, climatizaciГіn Г—1), 290,000 в‚Ѕ
- [x] 2.5.13 Equipos telecom referenciados a 03_03 con costo consolidado 14,770,000 в‚Ѕ
- [x] 2.5.14 Tabla resumen inversiГіn por categorГ­a: total ~52,967,000 в‚Ѕ (~293 unidades)
- [x] 2.5.15 Tabla trazabilidad equipo в†’ GOST (29 equipos Г— 2 normas)
- [x] 2.5.16 Tabla GOST por nГєmero de equipos cubiertos (8 estГЎndares)
- [x] 2.5.17 JustificaciГіn tГ©cnica y GOST para cada categorГ­a de equipo

### 2.6 Esquemas y diagramas

- [x] 2.6.1 Diagrama de topologГ­a de red (jerarquГ­a 3 niveles + anillo nГєcleo 10G, Mermaid graph TD)
- [x] 2.6.2 Esquema de ubicaciГіn fГ­sica de equipos en el plano (5,000 mВІ 7 zonas, Mermaid block-beta)
- [x] 2.6.3 Esquema de segmentaciГіn VLAN y QoS (8 VLANs + DSCP EF/AF/CS + zonas OT/IT, Mermaid graph LR)
- [x] 2.6.4 Esquema de redundancia de canales (4 niveles: RSTP + WAN dual + dual radio AGV + SAI, Mermaid graph TD)
- [x] 2.6.5 Esquema de arquitectura V2X/V2I para AGV (BSM/SPaT/ICA/MAP 4 fases, Mermaid sequenceDiagram)
- [x] 2.6.6 Esquema de cobertura Wi-Fi en las 2 naves y patio (14 APs + 3 bandas + solapamiento 20 %, Mermaid graph TB)
- [x] 2.6.7 Esquema de sincronizaciГіn de tiempo PTP (GM GPS в†’ BC в†’ TC в†’ OC В±1 Вµs, Mermaid graph TD)
- [x] 2.6.8 Diagrama de arquitectura del software (6 mГіdulos + bus MQTT/REST/WS + 3 BD, Mermaid graph LR)
- [x] 2.6.9 Diagrama de flujo de datos (recepciГіn в†’ almacenamiento в†’ picking в†’ expediciГіn, Mermaid flowchart TD)
- [x] 2.6.10 Diagrama de integraciГіn de sistemas (OT/IT/exterior + protocolos + VLANs, Mermaid graph TB)

### 2.7 Trazabilidad GOST

- [x] 2.7.1 Definir los 12 estГЎndares GOST/IEEE del proyecto (N-01 a N-12) con cГіdigo, tГ­tulo y aГ±o
- [x] 2.7.2 Tabla T вЂ” Trazabilidad telecom (38 vГ­nculos, T-01 a T-38): equipo в†’ GOST в†’ secciГіn в†’ justificaciГіn
- [x] 2.7.3 Tabla H вЂ” Trazabilidad hardware (40 vГ­nculos, H-01 a H-40): equipo в†’ GOST в†’ secciГіn в†’ justificaciГіn
- [x] 2.7.4 Tabla S вЂ” Trazabilidad software (16 vГ­nculos, S-01 a S-16): mГіdulo в†’ GOST в†’ secciГіn в†’ justificaciГіn
- [x] 2.7.5 Resumen por GOST: 12 estГЎndares con nГєmero de elementos cubiertos (total 95 vГ­nculos)
- [x] 2.7.6 Mapa de calor de cobertura normativa (diagrama Mermaid xychart)
- [x] 2.7.7 Trazabilidad inversa: por secciГіn del proyecto (03_02 / 03_03 / 03_04 / 03_05)
- [x] 2.7.8 Identificar los 3 estГЎndares pilares (РњР­Рљ 62443 / РРЎРћ 15745-4 / 70982-2023 вЂ” presentes en 4 secciones)
- [x] 2.7.9 Referencias normativas completas (12 estГЎndares en formato Р“РћРЎРў 7.1-2003)

## FASE 3 вЂ” Plan de montaje e instalaciГіn

### 3.3 Puesta en marcha y pruebas de aceptaciГіn (`04_03`)

- [x] 3.3.1 PT-01 Prueba cobertura Wi-Fi (RSSI в‰Ґ в€’65 dBm, SNR в‰Ґ 20 dB, handover < 50 ms, 2 dГ­as)
- [x] 3.3.2 PT-02 Prueba latencia de red (VLAN 10 AGV < 5 ms, P99, jitter < 1 ms, 2 dГ­as)
- [x] 3.3.3 PT-03 Prueba redundancia (RSTP < 50 ms, WAN failover < 30 s, SAI < 20 ms, 2 dГ­as)
- [x] 3.3.4 PT-04 Prueba sincronizaciГіn PTP (В±1 Вµs nodos finales, BMCA < 10 s, 1 dГ­a)
- [x] 3.3.5 PT-05 Prueba V2X/V2I (BSM 10 Hz, latencia ICA < 5 ms, reacciГіn AGV < 500 ms, 2 dГ­as)
- [x] 3.3.6 PT-06 Prueba ciberseguridad (RBAC, TLS 1.3, ECDSA, OWASP ZAP, 0 vulns crГ­ticas, 2 dГ­as)
- [x] 3.3.7 PT-07 Prueba integraciГіn software (8 escenarios E-01..E-08 end-to-end, 3 dГ­as)
- [x] 3.3.8 PT-08 Prueba AGV operaciГіn real (8 h, 6 AGV, 0 colisiones, в‰Ґ 95 % misiones, 2 dГ­as)
- [x] 3.3.9 Plan de validaciГіn global con diagrama flowchart (Mermaid) y Gantt 3 semanas
- [x] 3.3.10 Tabla de criterios de aceptaciГіn global del sistema (8 bloques в†’ APROBADO)
- [x] 3.3.11 Plan de capacitaciГіn: 7 perfiles, 4 mГіdulos (C-01..C-04), materiales y evaluaciГіn
- [x] 3.3.12 Resumen fase puesta en marcha: ~26 dГ­as hГЎbiles, ~400,000 в‚Ѕ
- [x] 3.3.13 4 diagramas Mermaid: secuencia V2X, flowchart validaciГіn, Gantt validaciГіn, Gantt AGV 8h

- [x] 3.2.1 IT-01 Cableado estructurado (12 dГ­as, fibra OM4 180 m + Cat6A S/FTP 850 m, certificaciГіn Fluke)
- [x] 3.2.2 IT-02 Switches industriales Г—10 (6 dГ­as, RSTP, VLAN 99 gestiГіn, NTPв†’PTP)
- [x] 3.2.3 IT-03 Puntos de acceso Wi-Fi 6/6E Г—14 (5 dГ­as, WPA3-Enterprise, SSIDs por VLAN)
- [x] 3.2.4 IT-04 Gateways + edge gateways Г—8 + PTP Grandmaster (6 dГ­as, Zigbee, OPC-UA, firewall OT/IT)
- [x] 3.2.5 IT-05 Servidores SRV-01/02/03 + SAI Г—2 (5 dГ­as, RAID, SO base Linux, 10GbE)
- [x] 3.2.6 IT-06 VLANs (4 dГ­as, 8 segmentos, ACLs OT/IT, asignaciГіn a SSIDs Wi-Fi)
- [x] 3.2.7 IT-07 QoS (3 dГ­as, DSCP EF/AF/CS, colas WRR, latencia VLAN 10 < 5 ms)
- [x] 3.2.8 IT-08 Redundancia (3 dГ­as, RSTP < 50 ms, WAN failover < 30 s, SAI verificado)
- [x] 3.2.9 IT-09 WMS (8 dГ­as, Spring Boot + PostgreSQL, datos maestros, flujo recepciГіnв†’expediciГіn)
- [x] 3.2.10 IT-10 SCADA (8 dГ­as, Ignition/WinCC, OPC-UA, InfluxDB, 100+ tags, prueba 24 h)
- [x] 3.2.11 IT-11 Control AGV + V2X/V2I (10 dГ­as, ROS 2, MQTT, mapa digital, misiГіn end-to-end)
- [x] 3.2.12 IT-12 IntegraciГіn sistemas (8 dГ­as, API Gateway, OAuth 2.0, TLS 1.3, webhook ERP)
- [x] 3.2.13 IT-13 VerificaciГіn integral (5 dГ­as, RF survey, iperf3, OWASP ZAP, informe firmado)
- [x] 3.2.14 Tabla resumen: 13 tareas, ~58 dГ­as, 17 personas, ~1,195,000 в‚Ѕ
- [x] 3.2.15 Cronograma Gantt (Mermaid, 12 semanas, IT-09/IT-10 en paralelo)
- [x] 3.2.16 Tabla de 10 riesgos de instalaciГіn con probabilidad, impacto y mitigaciГіn
- [x] 3.2.17 KPIs de instalaciГіn (7 indicadores con metas cuantitativas)

- [x] 3.1 MT-01 PreparaciГіn del suelo y marcaje (5 dГ­as, cinta magnГ©tica AGV, seГ±alizaciГіn)
- [x] 3.2 MT-02 Montaje de estanterГ­as (15 dГ­as, zonas A/B/C, 4 subtareas, anclaje tacos quГ­micos)
- [x] 3.3 MT-03 Montaje de cintas transportadoras (10 dГ­as, CT-01/02/03, PLC Siemens S7-1200)
- [x] 3.4 MT-04 InstalaciГіn de muelles de carga (12 dГ­as, 4 muelles, niveladores hidrГЎulicos, puertas seccionales)
- [x] 3.5 MT-05 Montaje de sensores IoT (10 dГ­as, 76 sensores Zigbee, 5 subtareas, edge gateways)
- [x] 3.6 MT-06 Puesta en servicio AGV/AMR (15 dГ­as, 6 AGV, 7 subtareas, pruebas V2X/V2I)
- [x] 3.7 MT-07 Montaje climatizaciГіn (8 dГ­as, 6 unidades, F-Gas, PLC precisiГіn zona B)
- [x] 3.8 MT-08 VerificaciГіn y pruebas de montaje (5 dГ­as, checklist tГ©cnico integral)
- [x] 3.9 Tabla resumen: 8 tareas, ~50 dГ­as hГЎbiles, 20 personas, costo mano de obra ~1,380,000 в‚Ѕ
- [x] 3.10 Cronograma Gantt (Mermaid, 10 semanas, rutas crГ­ticas identificadas)
- [x] 3.11 Tabla de 10 riesgos de montaje con probabilidad, impacto y estrategia de mitigaciГіn
- [x] 3.12 Matriz de riesgos (Mermaid quadrantChart, 10 riesgos posicionados)
- [x] 3.13 KPIs de progreso del montaje (6 indicadores)
- [x] 3.14 Referencias normativas (Р“РћРЎРў РњР­Рљ 61131-1, РРЎРћ 15745-4, 70982-2023, РњР­Рљ 62443, IEC 62026-3)

## FASE 4 вЂ” GestiГіn del proyecto

### 4.1 Pasaporte del proyecto (`05_01`)

- [x] 4.1.1 Nombre del proyecto: "ImplementaciГіn del Sistema Completo de AutomatizaciГіn y Telecomunicaciones del ED Park" (cГіdigo ED-PARK-2025-001)
- [x] 4.1.2 Objetivo general (SMART) + 7 objetivos especГ­ficos con indicador de logro y plazo
- [x] 4.1.3 Alcance detallado вЂ” incluye (10 categorГ­as: fГ­sica, telecom, software, hardware, montaje, instalaciГіn, pruebas, capacitaciГіn, documentaciГіn, gestiГіn)
- [x] 4.1.4 Alcance detallado вЂ” NO incluye (8 exclusiones explГ­citas: obra civil, compra real, cГіdigo, integraciГіn real, certificaciГіn, mantenimiento, expansiГіn, sistemas gubernamentales)
- [x] 4.1.5 Tabla de stakeholders (10 partes interesadas, rol, interГ©s, influencia, estrategia de comunicaciГіn)
- [x] 4.1.6 12 criterios de Г©xito con mГ©trica y valor objetivo (CS-01..CS-12)
- [x] 4.1.7 8 restricciones (presupuesto 117Mв‚Ѕ, plazo 18 meses, superficie 5,000 mВІ, normativa, formato GOST, entorno tropical, regulatorio Cuba)
- [x] 4.1.8 10 supuestos del proyecto (SA-01..SA-10)
- [x] 4.1.9 8 exclusiones explГ­citas del proyecto
- [x] 4.1.10 10 entregables principales con fase, responsable e hito asociado
- [x] 4.1.11 11 hitos clave (M-01..M-11) con mes y descripciГіn
- [x] 4.1.12 Diagrama de hitos Mermaid timeline (18 meses)
- [x] 4.1.13 Presupuesto desglosado por categorГ­a: costo base 90Mв‚Ѕ + reserva 30 % = precio 117Mв‚Ѕ
- [x] 4.1.14 Tabla comparativa 3 variantes (bГЎsica 87.75M / intermedia 117M / completa 146.25M)
- [x] 4.1.15 Flujo de caja estimado por fases
- [x] 4.1.16 Cronograma de alto nivel 18 meses (Mermaid Gantt)
- [x] 4.1.17 Bloque de firma y aprobaciГіn (director, cliente, profesor evaluador)

### 4.2 Plan de implementaciГіn

- [x] 4.2.1 Descomponer en EDT/WBS
- [x] 4.2.2 Definir hitos (milestones)
- [x] 4.2.3 Elaborar diagrama de Gantt
- [x] 4.2.4 Definir dependencias entre tareas
- [ ] 4.2.5 Estimar duraciГіn de cada tarea
- [ ] 4.2.6 Definir ruta crГ­tica
- [ ] 4.2.7 Definir fases del proyecto (anГЎlisis, diseГ±o, desarrollo, montaje, pruebas, despliegue)
- [x] 4.2.8 Estimar plazos por fase

### 4.3 Recursos

- [ ] 4.3.1 Estimar personal necesario por rol (tГ©cnicos, desarrolladores, instaladores, operarios)
- [ ] 4.3.2 Estimar equipos y materiales
- [ ] 4.3.3 Estimar presupuesto preliminar
- [ ] 4.3.4 Calcular reserva de riesgos (20-70%)
- [ ] 4.3.5 Definir dos precios: costo y venta
- [ ] 4.3.6 Definir matriz RACI
- [ ] 4.3.7 Definir plan de contrataciГіn
- [ ] 4.3.8 Definir subcontratistas (si aplica)

### 4.4 Riesgos

- [ ] 4.4.1 Identificar riesgos tГ©cnicos (interferencias, latencia, cobertura)
- [ ] 4.4.2 Identificar riesgos de ciberseguridad (V2X, IoT, red)
- [ ] 4.4.3 Identificar riesgos de plazo y presupuesto
- [ ] 4.4.4 Identificar riesgos financieros (tipo de cambio, inflaciГіn)
- [ ] 4.4.5 Identificar riesgos regulatorios en Cuba
- [ ] 4.4.6 Identificar riesgos de proveedores
- [ ] 4.4.7 Evaluar probabilidad e impacto
- [ ] 4.4.8 Definir plan de mitigaciГіn por riesgo
- [ ] 4.4.9 Definir planes de contingencia
- [ ] 4.4.10 Definir matriz de riesgos

### 4.5 ComunicaciГіn y seguimiento

- [ ] 4.5.1 Definir plan de comunicaciГіn
- [ ] 4.5.2 Definir KPIs de seguimiento
- [ ] 4.5.3 Definir mГ©todo de control de avance
- [ ] 4.5.4 Definir gestiГіn de cambios
- [ ] 4.5.5 Definir reuniones periГіdicas
- [ ] 4.5.6 Definir reportes de avance

### 4.6 AnГЎlisis de variantes para el cliente

- [ ] 4.6.1 Definir variante bГЎsica (solo lo esencial)
- [ ] 4.6.2 Definir variante intermedia (recomendada)
- [ ] 4.6.3 Definir variante completa (con expansiГіn futura)
- [ ] 4.6.4 Comparar costos y beneficios
- [ ] 4.6.5 Presentar recomendaciГіn

## FASE 5 вЂ” Documento final del proyecto

- [ ] 5.1 Portada segГєn Р“РћРЎРў 7.32-2017 (firmable)
- [ ] 5.2 ГЌndice
- [ ] 5.3 IntroducciГіn y justificaciГіn
- [ ] 5.4 DescripciГіn del ED Park (objeto virtual)
- [ ] 5.5 Base normativa (GOST)
- [ ] 5.6 DiseГ±o tГ©cnico (infraestructura + telecom + software + equipos)
- [ ] 5.7 Plan de desarrollo de software
- [ ] 5.8 Plan de montaje e instalaciГіn
- [ ] 5.9 GestiГіn del proyecto (pasaporte, WBS, Gantt, recursos, riesgos)
- [ ] 5.10 AnГЎlisis de variantes
- [ ] 5.11 Conclusiones
- [ ] 5.12 BibliografГ­a (formato Р“РћРЎРў 7.1-2003)
- [ ] 5.13 Anexos (planos, diagramas, tablas)
- [ ] 5.14 RevisiГіn final de formato y coherencia
- [ ] 5.15 Exportar a PDF

## FASE 6 вЂ” PresentaciГіn y defensa

- [ ] 6.1 Preparar presentaciГіn breve (10-15 min)
- [ ] 6.2 Preparar resumen oral de 2-3 min
- [ ] 6.3 Anticipar preguntas del profesor
- [ ] 6.4 Preparar demostraciГіn visual (planos, diagramas)
- [ ] 6.5 Ensayar la defensa
- [ ] 6.6 Entregar versiГіn electrГіnica antes de la fecha
- [ ] 6.7 Presentar avances cada clase

## Progreso actual del proyecto

**Total de tareas completadas**: 175/247 (70.9%)

**Fases completadas**:
- вњ… Fase 0 вЂ” PreparaciГіn y encuadre (13/13)
- вњ… Fase 1 вЂ” InvestigaciГіn normativa (12/12)
- вњ… **Fase 2 вЂ” DiseГ±o tГ©cnico COMPLETA** (87/87, archivos `03_01` a `03_07`)
- вњ… **Fase 3 вЂ” Montaje e instalaciГіn COMPLETA** (44/44, archivos `04_01` a `04_03`)
- вњ… Fase 4.1 вЂ” Pasaporte del proyecto (17/17, archivo `05_01`)

**Fases completadas**:
- вњ… Fase 0 вЂ” PreparaciГіn y encuadre (13/13)
- вњ… Fase 1 вЂ” InvestigaciГіn normativa (12/12)
- вњ… **Fase 2 вЂ” DiseГ±o tГ©cnico COMPLETA** (87/87, archivos `03_01` a `03_07`)
- вњ… **Fase 3 вЂ” Montaje e instalaciГіn COMPLETA** (44/44):
  - вњ… 3.1 Plan de montaje (14/14, `04_01`)
  - вњ… 3.2 Plan de instalaciГіn red y software (17/17, `04_02`)
  - вњ… 3.3 Puesta en marcha y pruebas (13/13, `04_03`)

**Fases completadas**:
- вњ… Fase 0 вЂ” PreparaciГіn y encuadre (13/13 tareas)
- вњ… Fase 1 вЂ” InvestigaciГіn normativa (12/12 tareas)
- вњ… **Fase 2 вЂ” DiseГ±o tГ©cnico COMPLETA** (87/87 tareas):
  - вњ… 2.1 DescripciГіn del ED Park (`03_01`)
  - вњ… 2.2 Infraestructura fГ­sica (`03_02`)
  - вњ… 2.3 Infraestructura de telecomunicaciones (`03_03`) вЂ” **17 tecnologГ­as Tema NВє 12**
  - вњ… 2.4 Software de gestiГіn вЂ” diseГ±o virtual (`03_04`)
  - вњ… 2.5 Equipos y hardware (`03_05`)
  - вњ… 2.6 Esquemas y diagramas (`03_06`) вЂ” **10 diagramas Mermaid**
  - вњ… 2.7 Trazabilidad GOST (`03_07`) вЂ” **95 vГ­nculos normativos**

**Archivos generados (Fase 2 completa)**:
- вњ… `03_Fase_2_Diseno_Tecnico/03_01_Descripcion_ED_Park.md`
- вњ… `03_Fase_2_Diseno_Tecnico/03_02_Infraestructura_Fisica.md`
- вњ… `03_Fase_2_Diseno_Tecnico/03_03_Infraestructura_Telecom.md`
- вњ… `03_Fase_2_Diseno_Tecnico/03_04_Software_Gestion.md`
- вњ… `03_Fase_2_Diseno_Tecnico/03_05_Equipos_Hardware.md`
- вњ… `03_Fase_2_Diseno_Tecnico/03_06_Esquemas_Diagramas.md`
- вњ… `03_Fase_2_Diseno_Tecnico/03_07_Trazabilidad_GOST.md`
- вњ… `04_Fase_3_Montaje_Instalacion/04_01_Plan_Montaje.md`
- вњ… `04_Fase_3_Montaje_Instalacion/04_02_Plan_Instalacion.md`
- вњ… `04_Fase_3_Montaje_Instalacion/04_03_Puesta_Marcha_Pruebas.md`
- вњ… `05_Fase_4_Gestion_Proyecto/05_01_Pasaporte_Proyecto.md`

**Diagramas generados en 03_06 (resumen)**:
- D-01: TopologГ­a red вЂ” jerarquГ­a 3 niveles, anillo nГєcleo 10G
- D-02: UbicaciГіn fГ­sica вЂ” plano 5,000 mВІ, 7 zonas, todos los equipos
- D-03: VLAN/QoS вЂ” 8 VLANs, DSCP EF/AF/CS, zonas OT/IT/exterior
- D-04: Redundancia вЂ” RSTP + WAN dual + dual radio AGV + SAI (4 niveles)
- D-05: V2X/V2I вЂ” BSM/SPaT/ICA/MAP, latencia ICA < 5 ms
- D-06: Cobertura Wi-Fi вЂ” 14 APs, 3 bandas, solapamiento 20 %
- D-07: PTP вЂ” GM GPS в†’ BC в†’ TC в†’ OC, precisiГіn В±1 Вµs
- D-08: Arquitectura software вЂ” 6 mГіdulos + bus MQTT/REST/WS
- D-09: Flujo de datos вЂ” recepciГіn в†’ almacenamiento в†’ picking в†’ expediciГіn
- D-10: IntegraciГіn sistemas вЂ” OT/IT/exterior con protocolos y VLANs

**PrГіximo paso recomendado**: Continuar **FASE 4** con `05_02_WBS_EDT.md` вЂ” estructura de desglose del trabajo (WBS) con 4 niveles de jerarquГ­a, codificaciГіn WBS y diagrama Mermaid.
