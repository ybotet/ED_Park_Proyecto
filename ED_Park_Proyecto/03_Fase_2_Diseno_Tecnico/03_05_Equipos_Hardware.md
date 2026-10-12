# Equipos y Hardware del ED Park

## Objetivo de la sección

El objetivo de esta sección es definir y justificar la lista completa de equipos hardware del ED Park, organizados por categoría funcional: vehículos automatizados (AGV/AMR), equipos de manutención manual, sistemas de identificación, equipos de pesaje, sensores IoT, servidores físicos, climatización y equipos de telecomunicaciones. Para cada equipo se indica el modelo de referencia (o especificación genérica cuando no se fija fabricante), la cantidad, la función en el parque, el GOST aplicable y el costo estimado unitario y total. La sección cierra con una tabla consolidada de trazabilidad equipo → GOST y el resumen de inversión en hardware.

> ⚠️ **Aclaración: diseño virtual.** Los modelos y precios indicados son referencias de mercado para estimación presupuestaria. No se adquiere ningún equipo real. Los costos se expresan en rublos rusos (₽) a precios de referencia 2024 para el mercado de automatización logística industrial.

---

## 1. AGV / AMR — Vehículos automatizados de guiado autónomo

Los AGV (Automated Guided Vehicles) y AMR (Autonomous Mobile Robots) son los elementos de automatización central del ED Park. Transportan pallets y cajas entre las zonas de recepción, almacenamiento, picking y expedición sin intervención manual directa.

| Atributo | Especificación |
|----------|---------------|
| Cantidad | 6 unidades (variante intermedia; ampliable a 8) |
| Tipo | AGV de contrapeso para palets (capacidad 1,000 kg) |
| Modelo de referencia | STILL RX 20-20 AGV / MiR500 AMR (o equivalente genérico) |
| Carga máxima | 1,000 kg por unidad |
| Velocidad máxima | 6 km/h (cargado) / 8 km/h (vacío) |
| Autonomía de batería | 8 horas de operación continua |
| Sistema de guiado | Cinta magnética en suelo + navegación láser LiDAR |
| Comunicación | Wi-Fi 6E (5 GHz) + 5G privado (backup) + OBU V2X |
| Sensores de seguridad | LiDAR 360°, sensores ultrasónicos, cámara frontal |
| Protocolo de emergencia | Parada en < 500 ms ante obstáculo detectado |
| Sistema operativo embarcado | Linux RT (tiempo real) |
| Cargador | Estación de carga inductiva automática (48 V DC) |

### 1.1 Tabla de AGV

| ID | Modelo de referencia | Cantidad | Función | Zona de operación | Costo unitario (₽) | Costo total (₽) |
|----|---------------------|:--------:|---------|------------------|:-----------------:|:---------------:|
| AGV-01 a AGV-06 | STILL RX 20-20 AGV (o equiv.) | 6 | Transporte de pallets entre zonas | Nave principal + nave recepción + zona AGV | 3,500,000 | 21,000,000 |

### 1.2 GOST aplicable a AGV

- **ГОСТ Р 70982-2023** — comunicaciones V2X/V2I para vehículos autónomos
- **ГОСТ Р МЭК 62443-3-3-2016** — autenticación y cifrado de comunicaciones del AGV
- **ГОСТ Р МЭК 61131-1** — controladores lógicos programables embarcados
- **IEEE 802.11ax** — Wi-Fi 6E para comunicación de control

---

## 2. Carretillas elevadoras

Las carretillas elevadoras manuales (con conductor) complementan a los AGV para operaciones que requieren mayor flexibilidad o para zonas no cubiertas por las rutas automatizadas.

| # | Tipo | Modelo de referencia | Cantidad | Capacidad | Función | Costo unitario (₽) | Costo total (₽) |
|---|------|---------------------|:--------:|:---------:|---------|:-----------------:|:---------------:|
| CE-01/02 | Carretilla contrapeso eléctrica | Toyota 8FBMKT25 (o equiv.) | 2 | 2,500 kg | Carga/descarga en muelles, reposición zona A | 1,200,000 | 2,400,000 |
| CE-03 | Carretilla retráctil eléctrica | Crown RR 5700 (o equiv.) | 1 | 1,600 kg | Almacenamiento en altura, zonas estrechas zona B | 1,400,000 | 1,400,000 |
| CE-04 | Apilador eléctrico | Jungheinrich EJC 110 (o equiv.) | 1 | 1,000 kg | Manipulación en pasillos estrechos zona C | 600,000 | 600,000 |
| **Subtotal carretillas** | | | **4** | | | | **4,400,000** |

### 2.1 GOST aplicable a carretillas

- **ГОСТ Р МЭК 61131-1** — controladores de los sistemas eléctricos de las carretillas
- **ГОСТ Р МЭК 62443-3-3-2016** — si las carretillas se integran con el sistema de gestión de flota

---

## 3. Transpaletas eléctricas

Las transpaletas eléctricas son equipos de corto recorrido para mover pallets dentro de la nave de recepción/expedición, entre muelles y zona de staging.

| # | Tipo | Modelo de referencia | Cantidad | Capacidad | Función | Costo unitario (₽) | Costo total (₽) |
|---|------|---------------------|:--------:|:---------:|---------|:-----------------:|:---------------:|
| TP-01/02 | Transpaleta eléctrica de conductor acompañante | Crown WP 3035 (o equiv.) | 2 | 3,000 kg | Muelles M-01/M-02: descarga a zona staging | 280,000 | 560,000 |
| TP-03/04 | Transpaleta eléctrica de conductor montado | Toyota LWE160 (o equiv.) | 2 | 1,600 kg | Nave recepción: consolidación y staging de salida | 350,000 | 700,000 |
| **Subtotal transpaletas** | | | **4** | | | | **1,260,000** |

---

## 4. Cintas transportadoras

Las cintas transportadoras automatizan el traslado de cajas individuales entre la zona de picking y la zona de consolidación/expedición, reduciendo el trabajo manual en el flujo de paquetes pequeños.

| # | Tipo | Modelo de referencia | Cantidad | Velocidad | Función | Costo unitario (₽) | Costo total (₽) |
|---|------|---------------------|:--------:|:---------:|---------|:-----------------:|:---------------:|
| CT-01 | Cinta transportadora recta (10 m) | Hytrol E-Z Glide (o equiv.) | 1 | 0.3 m/s | Zona picking → consolidación (nave principal) | 450,000 | 450,000 |
| CT-02 | Cinta transportadora con desvío (15 m + 1 desvío) | Interroll DCP (o equiv.) | 1 | 0.5 m/s | Clasificación de paquetes por destino (nave recepción) | 680,000 | 680,000 |
| CT-03 | Cinta de pesaje integrado (5 m) | Mettler Toledo Hi-Speed (o equiv.) | 1 | 0.3 m/s | Verificación de peso antes de expedición | 520,000 | 520,000 |
| **Subtotal cintas** | | | **3** | | | | **1,650,000** |

### 4.1 GOST aplicable a cintas

- **ГОСТ Р МЭК 61131-1** — PLC de control de cintas y desvíos
- **ГОСТ Р ИСО 15745-4-2010** — integración de cintas con el WMS vía Industrial Ethernet

---

## 5. Lectores RFID y código de barras

Los sistemas de identificación automática (AIDC) son el mecanismo de captura de datos del ED Park: registran la entrada, movimiento y salida de cada unidad de inventario sin intervención manual de escritura.

### 5.1 Lectores RFID fijos (pórticos)

| # | Tipo | Modelo de referencia | Cantidad | Función | Ubicación | Costo unitario (₽) | Costo total (₽) |
|---|------|---------------------|:--------:|---------|-----------|:-----------------:|:---------------:|
| RF-01/02 | Pórtico RFID UHF industrial | Zebra FX9600 (o equiv.) | 2 | Lectura automática de pallets a la entrada/salida de la nave principal | Acceso nave principal | 180,000 | 360,000 |
| RF-03/04 | Pórtico RFID UHF en muelles | Zebra FX9600 (o equiv.) | 2 | Captura automática en recepción y expedición | Muelles M-01 y M-03 | 180,000 | 360,000 |
| RF-05/06 | Lector RFID fijo en zona picking | Zebra FX7500 (o equiv.) | 2 | Verificación de unidad extraída en zona de picking | Zona picking nave principal | 120,000 | 240,000 |

### 5.2 Lectores RFID portátiles

| # | Tipo | Modelo de referencia | Cantidad | Función | Costo unitario (₽) | Costo total (₽) |
|---|------|---------------------|:--------:|---------|:-----------------:|:---------------:|
| RF-P01 a RF-P06 | Terminal RFID portátil con pantalla Android | Zebra MC9300 RFID (o equiv.) | 6 | Recepción, picking, inventario manual, devoluciones | 85,000 | 510,000 |

### 5.3 Lectores de código de barras

| # | Tipo | Modelo de referencia | Cantidad | Función | Costo unitario (₽) | Costo total (₽) |
|---|------|---------------------|:--------:|---------|:-----------------:|:---------------:|
| CB-01 a CB-08 | Escáner portátil 1D/2D industrial | Honeywell Granit 1910i (o equiv.) | 8 | Verificación manual de SKU en toda la operación | 18,000 | 144,000 |
| CB-F01/F02 | Escáner fijo de túnel (código barras 1D/2D) | Datalogic Magellan 9800i (o equiv.) | 2 | Lectura automática en cinta transportadora CT-03 | 95,000 | 190,000 |

**Subtotal lectores RFID + código de barras**: **1,804,000 ₽**

### 5.4 GOST aplicable a lectores RFID y CB

- **ГОСТ IEC 62026-3-2015** — integración de dispositivos de identificación con buses industriales
- **ГОСТ Р МЭК 62443-3-3-2016** — seguridad de dispositivos RFID conectados a la red
- **ГОСТ Р ИСО 15745-4-2010** — integración de lectores con el WMS

---

## 6. Básculas digitales

Las básculas industriales verifican el peso de los pallets y bultos en los puntos de recepción, picking y expedición, detectando discrepancias entre el peso declarado y el real.

| # | Tipo | Modelo de referencia | Capacidad | Precisión | Cantidad | Función | Ubicación | Costo unitario (₽) | Costo total (₽) |
|---|------|---------------------|:---------:|:---------:|:--------:|---------|-----------|:-----------------:|:---------------:|
| BA-01/02 | Báscula de plataforma industrial | Mettler Toledo ICS685 (o equiv.) | 3,000 kg | ±0.5 kg | 2 | Verificación de pallets en recepción | Nave recepción, zona verificación | 95,000 | 190,000 |
| BA-03 | Báscula de mesa para paquetes | Mettler Toledo ICS4 (o equiv.) | 30 kg | ±5 g | 1 | Verificación de bultos pequeños en picking | Zona picking | 28,000 | 28,000 |
| BA-04 | Báscula integrada en cinta CT-03 | Mettler Toledo Hi-Speed (incluida en CT-03) | 50 kg | ±10 g | 1 | Pesaje automático en línea antes de expedición | Cinta CT-03 | — | — |
| **Subtotal básculas** | | | | | **3** | | | | **218,000** |

### 6.1 GOST aplicable a básculas

- **ГОСТ Р МЭК 62443-3-3-2016** — seguridad de básculas conectadas a la red WMS
- **ГОСТ Р ИСО 15745-4-2010** — integración de básculas con el WMS vía Industrial Ethernet

---

## 7. Sensores IoT industriales

Los sensores IoT del ED Park monitorean el entorno físico del parque en tiempo real, proporcionando datos al SCADA (M-04) y al edge gateway IoT para gestión de alarmas.

### 7.1 Sensores de temperatura y humedad

| # | Modelo de referencia | Protocolo | Cantidad | Precisión | Función | Ubicación | Costo unitario (₽) | Costo total (₽) |
|---|---------------------|-----------|:--------:|:---------:|---------|-----------|:-----------------:|:---------------:|
| SEN-TH-01…30 | Vaisala HMT120 (o equiv.) | Zigbee / Modbus | 30 | ±0.2 °C / ±2 % HR | Monitoreo T°/HR en zona B (20 uds.) y nave principal (10 uds.) | Zona B + nave principal | 12,000 | 360,000 |

### 7.2 Sensores de presencia y movimiento

| # | Modelo de referencia | Protocolo | Cantidad | Función | Ubicación | Costo unitario (₽) | Costo total (₽) |
|---|---------------------|-----------|:--------:|---------|-----------|:-----------------:|:---------------:|
| SEN-PR-01…20 | Sick PLS101 (o equiv.) | Zigbee / IO-Link | 20 | Detección de presencia en pasillos y zona AGV para seguridad y control de iluminación | Pasillos nave principal + zona AGV | 8,500 | 170,000 |

### 7.3 Detectores de humo e incendio

| # | Modelo de referencia | Protocolo | Cantidad | Función | Ubicación | Costo unitario (₽) | Costo total (₽) |
|---|---------------------|-----------|:--------:|---------|-----------|:-----------------:|:---------------:|
| SEN-FI-01…20 | Hochiki ESP (o equiv.) | Protocolo FAS industrial | 20 | Detección temprana de humo e incendio, integración con SCADA | Distribuidos en toda la superficie cubierta | 5,500 | 110,000 |

### 7.4 Sensores de apertura de puertas/muelles

| # | Modelo de referencia | Protocolo | Cantidad | Función | Ubicación | Costo unitario (₽) | Costo total (₽) |
|---|---------------------|-----------|:--------:|---------|-----------|:-----------------:|:---------------:|
| SEN-DR-01…06 | Sick WL12L (o equiv.) | IO-Link | 6 | Estado de puertas seccionales de muelles (abierta/cerrada) y puertas de nave | Muelles M-01…M-04 + puertas naves | 6,000 | 36,000 |

**Subtotal sensores IoT**: **676,000 ₽**

### 7.5 GOST aplicable a sensores IoT

- **ГОСТ IEC 62026-3-2015** — integración de sensores con buses de campo industriales
- **ГОСТ Р МЭК 62443-3-3-2016** — seguridad de dispositivos IoT conectados a la red
- **ГОСТ Р МЭК 61131-1** — integración de sensores con controladores PLC

---

## 8. Servidores físicos

Los servidores físicos alojan toda la plataforma de software del ED Park en la sala de control. Se describen en detalle en la sección `03_04_Software_Gestion.md`; aquí se especifica el hardware.

| ID | Tipo | Modelo de referencia | Cantidad | Especificación hardware | Función | Costo unitario (₽) | Costo total (₽) |
|----|------|---------------------|:--------:|------------------------|---------|:-----------------:|:---------------:|
| SRV-01 | Servidor rack 2U | Dell PowerEdge R750 (o equiv.) | 1 | 16 cores Xeon, 64 GB RAM, 4 TB SSD RAID-1, 2× 10GbE | WMS, base de datos PostgreSQL, API Gateway | 850,000 | 850,000 |
| SRV-02 | Servidor rack 2U | Dell PowerEdge R750 (o equiv.) | 1 | 12 cores Xeon, 32 GB RAM, 2 TB SSD RAID-1, 2× 10GbE | Control AGV, SCADA, MQTT broker, InfluxDB | 750,000 | 750,000 |
| SRV-03 | Servidor rack 2U (backup) | Dell PowerEdge R550 (o equiv.) | 1 | 8 cores Xeon, 32 GB RAM, 8 TB HDD RAID-5, 2× 1GbE | Hot standby, backups diarios, logs históricos | 550,000 | 550,000 |
| SAI-01/02 | SAI industrial rack | APC Smart-UPS 3000VA RM (o equiv.) | 2 | 3,000 VA, autonomía 15 min, señalización SNMP | Alimentación ininterrumpida para servidores y switches núcleo | 120,000 | 240,000 |
| RACK-01 | Rack de 42U con PDU | APC NetShelter SX 42U (o equiv.) | 1 | 42U, PDU metered, gestión de cable | Alojamiento de servidores, switches núcleo, SAI | 85,000 | 85,000 |
| **Subtotal servidores** | | | **6** | | | | **2,475,000** |

### 8.1 GOST aplicable a servidores

- **ГОСТ Р МЭК 62443-3-3-2016** — seguridad de servidores en zona OT/IT
- **ГОСТ Р МЭК 61850-3** — requisitos de disponibilidad de equipos de comunicación industrial

---

## 9. Equipos de climatización

Los equipos de climatización del ED Park protegen la mercancía sensible de la zona B y garantizan las condiciones de trabajo del personal y de los equipos de la sala de control.

| # | Tipo | Modelo de referencia | Cantidad | Capacidad | Función | Zona | Costo unitario (₽) | Costo total (₽) |
|---|------|---------------------|:--------:|:---------:|---------|------|:-----------------:|:---------------:|
| CLIM-01/02 | Unidad de climatización de precisión | Stulz CyberAir 3PRO (o equiv.) | 2 | 5 kW frío + control HR | Control T° 18–25 °C y HR 40–60 % en zona B | Zona B (nave principal) | 380,000 | 760,000 |
| CLIM-03 | Climatizador industrial de nave | Daikin RZQSG71L3V1B (o equiv.) | 1 | 20 kW frío/calor | Confort térmico general en nave principal (verano Cuba > 35 °C) | Nave principal | 220,000 | 220,000 |
| CLIM-04 | Climatizador industrial de nave | Daikin RZQSG71L3V1B (o equiv.) | 1 | 15 kW frío/calor | Confort térmico en nave recepción/expedición | Nave recepción | 190,000 | 190,000 |
| CLIM-05 | Climatizador sala de control | Mitsubishi Electric SRK50ZSX (o equiv.) | 1 | 5 kW frío | Control T° 20–24 °C para equipos de rack y operadores | Sala de control | 85,000 | 85,000 |
| CLIM-06 | Climatizador oficinas | Mitsubishi Electric SRK35ZSX (o equiv.) | 1 | 3.5 kW frío | Confort térmico en oficinas y sala de reuniones | Oficinas | 65,000 | 65,000 |
| **Subtotal climatización** | | | **6** | | | | **1,320,000** |

### 9.1 GOST aplicable a climatización

- **ГОСТ Р МЭК 62443-3-3-2016** — sensores IoT integrados con la climatización (datos de T°/HR)
- **ГОСТ Р МЭК 61131-1** — controladores PLC de las unidades de climatización de precisión

---

## 10. Impresoras de etiquetas

Las impresoras de etiquetas industriales son equipos de soporte para el flujo operativo: generan etiquetas RFID, códigos de barras y documentos de expedición.

| # | Tipo | Modelo de referencia | Cantidad | Función | Ubicación | Costo unitario (₽) | Costo total (₽) |
|---|------|---------------------|:--------:|---------|-----------|:-----------------:|:---------------:|
| IMP-01…04 | Impresora térmica industrial (etiquetas RFID + CB) | Zebra ZT411 (o equiv.) | 4 | Impresión de etiquetas de ubicación, SKU, albaranes y etiquetas RFID de pallets | Zona picking (2) + nave recepción (2) | 55,000 | 220,000 |

---

## 11. Cámaras IP industriales

Las cámaras industriales cubren dos funciones: videovigilancia de seguridad del parque y apoyo al sistema V2X/V2I para detección de obstáculos y peatones en zonas de circulación de AGV.

| # | Tipo | Modelo de referencia | Cantidad | Resolución | Función | Ubicación | Costo unitario (₽) | Costo total (₽) |
|---|------|---------------------|:--------:|:---------:|---------|-----------|:-----------------:|:---------------:|
| CAM-01…08 | Cámara IP industrial domo (interior) | Axis P3245-V (o equiv.) | 8 | 1080p, IR 10 m | CCTV + detección de personas en zonas de cruce V2X | Intersecciones nave principal (3) + muelles (3) + zona AGV (2) | 28,000 | 224,000 |
| CAM-09…12 | Cámara IP industrial exterior (PTZ) | Axis Q6135-LE (o equiv.) | 4 | 1080p, IR 30 m, PTZ | Videovigilancia del patio y perímetro exterior | Patio (2) + perímetro (2) | 65,000 | 260,000 |
| **Subtotal cámaras** | | | **12** | | | | **484,000** |

---

## 12. PLC y controladores industriales

Los PLC (Programmable Logic Controllers) controlan los equipos electromecánicos del parque: puertas seccionales de muelles, cintas transportadoras y sistemas de climatización de precisión.

| # | Tipo | Modelo de referencia | Cantidad | Función | Protocolo | Costo unitario (₽) | Costo total (₽) |
|---|------|---------------------|:--------:|---------|-----------|:-----------------:|:---------------:|
| PLC-01/02 | PLC industrial modular | Siemens S7-1200 (o equiv.) | 2 | Control de puertas seccionales muelles M-01…M-04 | Modbus RTU → Edge-GW-04 | 85,000 | 170,000 |
| PLC-03 | PLC industrial compacto | Siemens S7-1200 (o equiv.) | 1 | Control de cintas CT-01, CT-02, CT-03 | Modbus RTU → Edge-GW-04 | 75,000 | 75,000 |
| PLC-04 | Controlador de climatización | Honeywell Spyder (o equiv.) | 1 | Control de unidades de precisión zona B (CLIM-01/02) | Modbus TCP → SCADA | 45,000 | 45,000 |
| **Subtotal PLC** | | | **4** | | | | **290,000** |

### 12.1 GOST aplicable a PLC

- **ГОСТ Р МЭК 61131-1** — programación y requisitos de controladores lógicos programables
- **ГОСТ Р ИСО 15745-4-2010** — integración de PLC con la red Industrial Ethernet
- **ГОСТ Р МЭК 61850-3** — comunicaciones de PLC en entornos industriales duros

---

## 13. Equipos de telecomunicaciones (referencia a 03_03)

Los equipos de telecomunicaciones se describen en detalle en la sección `03_03_Infraestructura_Telecom.md`. A continuación se resume la lista con el costo estimado consolidado para el presupuesto global.

| Categoría | Cantidad | Costo estimado (₽) | Referencia |
|-----------|:--------:|:-----------------:|-----------|
| APs Wi-Fi 6/6E (interior + exterior) | 14 | 1,960,000 | Sección 03_03, ítem 1–2 |
| Controlador Wi-Fi (WLC) | 1 | 350,000 | Sección 03_03, ítem 3 |
| eNodeB LTE privado + módems | 1 + 6 | 1,100,000 | Sección 03_03, ítem 4–5 |
| gNB 5G indoor + core 5G + módems | 4 + 1 + 6 | 4,200,000 | Sección 03_03, ítem 6–8 |
| Switches industriales (núcleo + dist. + campo) | 10 | 2,800,000 | Sección 03_03, ítem 9–11 |
| Nodos mesh (fijos + embarcados) | 6 + 6 | 840,000 | Sección 03_03, ítem 12–13 |
| Gateways de protocolo | 4 | 280,000 | Sección 03_03, ítem 14–16 |
| Edge gateways | 4 | 560,000 | Sección 03_03, ítem 17–20 |
| Servidor GPS-PTP Grandmaster | 1 | 420,000 | Sección 03_03, ítem 21 |
| RSU V2X + OBU V2X | 5 + 6 | 1,100,000 | Sección 03_03, ítem 22–23 |
| Sensores IoT Zigbee (T°/HR + presencia) | 50–70 | 510,000 | Sección 03_03, ítem 24–25 |
| Cableado estructurado (fibra OM4 + Cat6A S/FTP) | lote | 650,000 | Sección 03_03 |
| **Subtotal telecom** | | **14,770,000** | Ver 03_03 completo |

---

## 14. Resumen consolidado de inversión en hardware

| Categoría | Cantidad de equipos | Costo total (₽) | % del total hardware |
|-----------|:-------------------:|:---------------:|:-------------------:|
| AGV / AMR | 6 | 21,000,000 | 39.7 % |
| Carretillas elevadoras | 4 | 4,400,000 | 8.3 % |
| Transpaletas eléctricas | 4 | 1,260,000 | 2.4 % |
| Cintas transportadoras | 3 | 1,650,000 | 3.1 % |
| Lectores RFID + código de barras | 20 | 1,804,000 | 3.4 % |
| Básculas digitales | 3 | 218,000 | 0.4 % |
| Sensores IoT industriales | 76 | 676,000 | 1.3 % |
| Servidores físicos + SAI + rack | 6 | 2,475,000 | 4.7 % |
| Climatización | 6 | 1,320,000 | 2.5 % |
| Impresoras de etiquetas | 4 | 220,000 | 0.4 % |
| Cámaras IP industriales | 12 | 484,000 | 0.9 % |
| PLC y controladores | 4 | 290,000 | 0.5 % |
| Equipos de telecomunicaciones | ~145 | 14,770,000 | 27.9 % |
| Montaje, instalación y puesta en marcha | — | 2,400,000 | 4.5 % |
| **TOTAL HARDWARE** | **~293** | **52,967,000** | **100 %** |

> **Nota sobre el presupuesto global**: El costo total de hardware (~52,967,000 ₽) se suma al costo de software (~7,400,000 ₽) y al costo de gestión del proyecto, recursos humanos operativos y reserva de riesgos para obtener el presupuesto global del proyecto. Esto se detalla en la Fase 4 — Gestión del proyecto (`05_04_Recursos_Presupuesto.md`).

---

## 15. Tabla de trazabilidad equipo → GOST

| Equipo | Categoría | GOST / Estándar principal | GOST secundario | Justificación |
|--------|-----------|:------------------------:|:---------------:|---------------|
| AGV / AMR (×6) | Vehículo autónomo | ГОСТ Р 70982-2023 | ГОСТ Р МЭК 62443-3-3-2016 | Comunicaciones V2X y seguridad de control remoto |
| AGV — comunicación Wi-Fi 6E | Red inalámbrica | IEEE 802.11ax | ГОСТ Р МЭК 61850-3 | Conectividad de tiempo real para control de flota |
| AGV — comunicación 5G | Red celular privada | ГОСТ Р МЭК 61850-3 | ГОСТ Р МЭК 62443-3-3-2016 | Canal de backup de misión crítica |
| AGV — OBU V2X | V2X/V2I | ГОСТ Р 70982-2023 | IEEE 802.11p | Interacción con RSU para seguridad en intersecciones |
| Carretillas elevadoras | Manutención | ГОСТ Р МЭК 61131-1 | — | Controladores eléctricos de la carretilla |
| Transpaletas eléctricas | Manutención | ГОСТ Р МЭК 61131-1 | — | Controladores eléctricos de la transpaleta |
| Cintas transportadoras | Automatización | ГОСТ Р МЭК 61131-1 | ГОСТ Р ИСО 15745-4-2010 | PLC de control + integración con WMS vía Industrial Ethernet |
| Lectores RFID fijos (pórticos) | Identificación | ГОСТ IEC 62026-3-2015 | ГОСТ Р МЭК 62443-3-3-2016 | Integración con buses industriales + seguridad de red |
| Terminales RFID portátiles | Identificación | ГОСТ IEC 62026-3-2015 | IEEE 802.11ax | Integración con WMS + conectividad Wi-Fi 6 |
| Escáneres de código de barras | Identificación | ГОСТ IEC 62026-3-2015 | ГОСТ Р ИСО 15745-4-2010 | Integración con WMS |
| Básculas digitales | Pesaje | ГОСТ Р ИСО 15745-4-2010 | ГОСТ Р МЭК 62443-3-3-2016 | Integración con WMS + seguridad de datos |
| Sensores T°/HR Zigbee | IoT ambiental | ГОСТ IEC 62026-3-2015 | ГОСТ Р МЭК 62443-3-3-2016 | Integración con red IoT + seguridad de dispositivos |
| Sensores de presencia | IoT seguridad | ГОСТ IEC 62026-3-2015 | ГОСТ Р МЭК 61131-1 | Integración con PLC de seguridad de zona AGV |
| Detectores de humo/incendio | IoT seguridad | ГОСТ IEC 62026-3-2015 | ГОСТ Р МЭК 62443-3-3-2016 | Integración con SCADA vía protocolo FAS industrial |
| Sensores apertura puertas/muelles | IoT control | ГОСТ Р МЭК 61131-1 | ГОСТ Р ИСО 15745-4-2010 | PLC de control de muelles + integración WMS |
| Servidores físicos (SRV-01/02/03) | IT/OT | ГОСТ Р МЭК 62443-3-3-2016 | ГОСТ Р МЭК 61850-3 | Seguridad de servidores OT + disponibilidad industrial |
| SAI / UPS | Alimentación | ГОСТ Р МЭК 61850-3 | — | Disponibilidad continua de infraestructura crítica |
| Climatización de precisión zona B | Ambiental | ГОСТ Р МЭК 62443-3-3-2016 | ГОСТ Р МЭК 61131-1 | Sensores IoT integrados + PLC de control de T°/HR |
| Climatización naves y oficinas | Ambiental | ГОСТ Р МЭК 61131-1 | — | Control automático de temperatura |
| Impresoras de etiquetas | Periférico | ГОСТ Р ИСО 15745-4-2010 | — | Integración con WMS vía Ethernet |
| Cámaras IP industriales | Seguridad/V2X | ГОСТ Р МЭК 62443-3-3-2016 | ГОСТ Р 70982-2023 | Seguridad de red + detección de obstáculos V2X |
| PLC muelles | Control industrial | ГОСТ Р МЭК 61131-1 | ГОСТ Р ИСО 15745-4-2010 | Programación PLC + integración con SCADA vía Modbus |
| PLC cintas | Control industrial | ГОСТ Р МЭК 61131-1 | ГОСТ Р ИСО 15745-4-2010 | Programación PLC + integración con WMS |
| PLC climatización | Control industrial | ГОСТ Р МЭК 61131-1 | ГОСТ Р МЭК 62443-3-3-2016 | Programación PLC + seguridad datos de proceso |
| APs Wi-Fi 6/6E | Telecom | IEEE 802.11ax | ГОСТ Р МЭК 61850-3 | Conectividad inalámbrica industrial |
| Switches industriales | Telecom | ГОСТ Р ИСО 15745-4-2010 | ГОСТ Р МЭК 61850-3 | Backbone cableado + entornos duros |
| RSU V2X | Telecom V2X | ГОСТ Р 70982-2023 | IEEE 802.11p | Infraestructura fija V2X/V2I |
| Edge gateways | Telecom borde | ГОСТ Р МЭК 62443-3-3-2016 | ГОСТ Р ИСО 15745-4-2010 | Firewall OT + procesamiento local |
| Servidor PTP Grandmaster | Telecom tiempo | IEEE 1588-2019 | ГОСТ Р МЭК 61850-3 | Sincronización precisa de todos los nodos |

---

## 16. Resumen de GOST por número de equipos cubiertos

| GOST / Estándar | Equipos cubiertos | Ámbito |
|----------------|:-----------------:|--------|
| ГОСТ Р МЭК 62443-3-3-2016 | 18 | Ciberseguridad industrial (todos los equipos conectados en red) |
| ГОСТ Р МЭК 61131-1 | 12 | Controladores PLC (AGV, cintas, muelles, climatización, sensores) |
| ГОСТ Р ИСО 15745-4-2010 | 10 | Integración Ethernet industrial (switches, cintas, RFID, PLC, servidores) |
| ГОСТ IEC 62026-3-2015 | 8 | Dispositivos de identificación y campo (RFID, sensores IoT, escáneres) |
| ГОСТ Р 70982-2023 | 4 | V2X/V2I (AGV, OBU, RSU, cámaras V2X) |
| ГОСТ Р МЭК 61850-3 | 8 | Comunicaciones industriales robustas (servidores, SAI, switches, APs) |
| IEEE 802.11ax | 3 | Wi-Fi 6/6E (APs, AGV Wi-Fi, terminales móviles) |
| IEEE 1588-2019 | 2 | Sincronización PTP (servidor Grandmaster, switches BC) |

---

## 17. Referencias normativas de la sección

- **ГОСТ Р 70982-2023**. Безопасность дорожного движения. Системы связи и управления транспортными средствами. Взаимодействие транспортных средств и инфраструктуры. — М.: Стандартинформ, 2023.
- **ГОСТ Р МЭК 62443-3-3-2016**. Системы и меры по обеспечению кибербезопасности промышленных автоматизированных систем. Часть 3-3. Системные требования к безопасности. — М.: Стандартинформ, 2016.
- **ГОСТ Р МЭК 61131-1**. Программируемые контроллеры. Часть 1. Общие сведения и основные принципы. — М.: Стандартинформ, 2011.
- **ГОСТ Р ИСО 15745-4-2010**. Системы автоматизации производства и их интеграция. Профили. Часть 4. Профили систем управления на основе Ethernet. — М.: Стандартинформ, 2010.
- **ГОСТ IEC 62026-3-2015**. Технологии связи для промышленных систем управления. Сети DeviceNet. — М.: Стандартинформ, 2015.
- **ГОСТ Р МЭК 61850-3**. Коммуникационные системы и сети в электроэнергетике. Часть 3. Общие требования. — М.: Стандартинформ.
- **IEEE 802.11ax**. Wireless LAN High Efficiency (HE). — IEEE, 2019.
- **IEEE 1588-2019**. Precision Clock Synchronization Protocol. — IEEE, 2019.
- **ГОСТ 7.32-2017**. Отчет о научно-исследовательской работе. Структура и правила оформления. — М.: Стандартинформ, 2017.

---

## 18. Checklist de la sección

- [x] 2.5.1 Definir AGV/AMR: 6 unidades, modelo, capacidad, guiado, GOST, costo (21,000,000 ₽)
- [x] 2.5.2 Definir carretillas elevadoras: 4 unidades (contrapeso ×2, retráctil ×1, apilador ×1), GOST, costo
- [x] 2.5.3 Definir transpaletas eléctricas: 4 unidades (acompañante ×2, montado ×2), GOST, costo
- [x] 2.5.4 Definir cintas transportadoras: 3 unidades (recta, con desvío, pesaje), GOST, costo
- [x] 2.5.5 Definir lectores RFID: 6 pórticos fijos + 6 terminales portátiles + 10 escáneres CB, GOST, costo
- [x] 2.5.6 Definir básculas digitales: 3 unidades (plataforma ×2, mesa ×1), GOST, costo
- [x] 2.5.7 Definir sensores IoT: 76 unidades (T°/HR ×30, presencia ×20, incendio ×20, puertas ×6), GOST, costo
- [x] 2.5.8 Definir servidores físicos: SRV-01/02/03 + SAI ×2 + rack, GOST, costo
- [x] 2.5.9 Definir climatización: 6 unidades (precisión zona B ×2, naves ×2, sala control ×1, oficinas ×1)
- [x] 2.5.10 Definir impresoras de etiquetas: 4 unidades Zebra ZT411, costo
- [x] 2.5.11 Definir cámaras IP: 12 unidades (interior ×8 + PTZ exterior ×4), GOST, costo
- [x] 2.5.12 Definir PLC y controladores: 4 unidades (muelles ×2, cintas ×1, climatización ×1), GOST, costo
- [x] 2.5.13 Referenciar equipos telecom a sección 03_03 con costo consolidado (14,770,000 ₽)
- [x] 2.5.14 Generar tabla de resumen de inversión por categoría (total ~52,967,000 ₽)
- [x] 2.5.15 Generar tabla de trazabilidad equipo → GOST (29 filas)
- [x] 2.5.16 Generar tabla resumen de GOST por número de equipos cubiertos
- [x] 2.5.17 Referencias normativas (9 GOST + IEEE)
- [x] 2.5.18 Coherencia con infraestructura física (03_02), telecom (03_03) y software (03_04)

---

## 19. Conclusión

La lista de hardware del ED Park comprende aproximadamente 293 unidades de equipo distribuidas en 13 categorías, con un costo total estimado de **52,967,000 ₽**. Los AGV representan la mayor inversión unitaria (39.7 % del total hardware), seguidos de los equipos de telecomunicaciones (27.9 %). Todos los equipos están justificados por su función operativa y respaldados por los estándares GOST e IEEE correspondientes, garantizando la coherencia técnica y normativa del proyecto. Este inventario sirve de base para la planificación del montaje (Fase 3), el cálculo del presupuesto completo (Fase 4) y la elaboración de la tabla de trazabilidad normativa global (sección 03_07).
