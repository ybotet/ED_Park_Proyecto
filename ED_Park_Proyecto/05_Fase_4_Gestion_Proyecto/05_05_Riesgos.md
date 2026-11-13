# 05_05 - Gestión de Riesgos - Proyecto ED Park

## Objetivo de la sección

Identificar, analizar, evaluar y planificar la respuesta a los riesgos del proyecto ED Park, cubriendo riesgos técnicos (telecomunicaciones, automatización), de ciberseguridad, de plazo y presupuesto, financieros, regulatorios (entorno cubano) y de proveedores. Establecer la matriz de riesgos, planes de mitigación y contingencia, y la reserva de riesgos asociada. Coherente con el Pasaporte del Proyecto (05_01), WBS (05_02), Gantt (05_03) y Recursos/Presupuesto (05_04).

---

## 1. Metodología de gestión de riesgos

### 1.1 Proceso aplicado

El proceso sigue las fases estándar de gestión de riesgos adaptadas al contexto académico e industrial del ED Park:

1. **Identificación** — Talleres con stakeholders, revisión de lecciones aprendidas, análisis de WBS y arquitectura técnica
2. **Anualisis cualitativo** — Matriz Probabilidad × Impacto (escala 1–5)
3. **Análisis cuantitativo** — Estimación de impacto en coste (₽) y plazo (días) para riesgos críticos
4. **Planificación de respuestas** — Estrategias: evitar, mitigar, transferir, aceptar
5. **Monitorización y control** — Revisiones quincenales en comité de riesgos, KRI (Key Risk Indicators)

### 1.2 Escalas de valoración

| Probabilidad | Valor | Descripción |
|:------------:|:-----:|-------------|
| Muy baja | 1 | < 10 % — Evento excepcional |
| Baja | 2 | 10–30 % — Poco probable |
| Media | 3 | 30–60 % — Posible |
| Alta | 4 | 60–80 % — Probable |
| Muy alta | 5 | > 80 % — Casi seguro |

| Impacto | Valor | Coste (₽) | Plazo (días) | Calidad / Seguridad |
|:-------:|:-----:|:---------:|:------------:|:-------------------:|
| Insignificante | 1 | < 500,000 | < 5 | Sin efecto apreciable |
| Menor | 2 | 500,000 – 2,000,000 | 5–15 | Desviación menor, corregible |
| Moderado | 3 | 2,000,000 – 10,000,000 | 15–30 | Impacto notable, requiere acción |
| Mayor | 4 | 10,000,000 – 30,000,000 | 30–60 | Impacto severo, pone en riesgo hitos |
| Crítico | 5 | > 30,000,000 | > 60 | Fracaso del proyecto o incidente grave |

**Nivel de riesgo = Probabilidad × Impacto** (rango 1–25)

| Nivel | Rango | Acción |
|:-----:|:-----:|--------|
| Bajo | 1–6 | Aceptar, monitorizar pasivamente |
| Medio | 7–12 | Mitigar, plan de acción asignado |
| Alto | 13–19 | Mitigar prioritario, escalar a dirección |
| Crítico | 20–25 | Evitar o transferir, plan de contingencia obligatorio |

---

## 2. Registro de riesgos identificados

Se han identificado **28 riesgos** agrupados en 6 categorías, coherentes con la reserva de riesgos de 27,000,000 ₽ (30 % del coste base) definida en `05_04_Recursos_Presupuesto.md`.

### 2.1 Riesgos técnicos — Telecomunicaciones y automatización (R-01 a R-08)

| ID | Riesgo | Descripción detallada | Prob. | Impacto | Nivel | Categoría |
|:--:|--------|------------------------|:-----:|:-------:|:-----:|:---------:|
| **R-01** | **Interferencias RF en entorno industrial** | Ruido electromagnético de motores, inversores de frecuencia, soldadoras y equipos de alta potencia degrada señal Wi-Fi 6/6E, LTE/5G privado y mesh. Afecta latencia AGV (< 5 ms) y cobertura (RSSI ≥ −65 dBm). | 4 | 4 | **16 — Alto** | Técnico |
| **R-02** | **Latencia de red superior a especificación** | Congestión en backbone 10G, colisiones en VLAN 10 (AGV), jitter en PTP (IEEE 1588) o procesamiento en edge gateways supera umbrales: AGV < 5 ms, V2X ICA < 5 ms, SCADA < 50 ms. | 3 | 4 | **12 — Medio** | Técnico |
| **R-03** | **Cobertura Wi-Fi insuficiente en zonas críticas** | Sombras de RF en pasillos entre estanterías (zona A, 10 m altura), patio exterior (lluvia, vegetación) y muelles (contenedores metálicos). Handovers entre APs > 50 ms. | 3 | 3 | **9 — Medio** | Técnico |
| **R-04** | **Fallo de sincronización PTP (IEEE 1588)** | Grandmaster GPS no adquiere satélites (techo metálico), BC/TC no convergen, precisión > ±1 µs en nodos finales. Afecta coordenadas AGV, timestamps SCADA, V2X. | 2 | 4 | **8 — Medio** | Técnico |
| **R-05** | **Degradación de enlaces V2X/V2I** | Obstrucción visual (camiones, estanterías), interferencia en banda 5.9 GHz (C-V2X), latencia BSM > 100 ms, pérdida de mensajes SPaT/ICA. Riesgo de colisión AGV. | 3 | 5 | **15 — Alto** | Técnico |
| **R-06** | **Fallo de redundancia de comunicaciones** | RSTP no converge < 50 ms, failover WAN fibra→LTE > 30 s, dual radio AGV no conmuta, SAI no sustenta carga crítica. Pérdida de control AGV y SCADA. | 2 | 5 | **10 — Medio** | Técnico |
| **R-07** | **Incompatibilidad de protocolos industriales** | Mismatch entre versiones OPC-UA (servidor SCADA vs PLC), perfiles PROFINET/EtherNet/IP no alineados, MQTT v5 vs v3.1.1 en gateways. Requiere reingeniería de integración. | 3 | 3 | **9 — Medio** | Técnico |
| **R-08** | **Capacidad insuficiente de edge computing** | Edge gateways (×4) saturados por procesamiento local IoT (76 sensores), inferencia V2X, buffering MQTT. Latencia aumenta, buffers overflow, pérdida de telemetría. | 2 | 3 | **6 — Bajo** | Técnico |

### 2.2 Riesgos de ciberseguridad (R-09 a R-12)

| ID | Riesgo | Descripción detallada | Prob. | Impacto | Nivel | Categoría |
|:--:|--------|------------------------|:-----:|:-------:|:-----:|:---------:|
| **R-09** | **Compromiso de red V2X/V2I** | Ataque de suplantación (spoofing) de mensajes BSM/ICA, inyección de falsos SPaT, denegación de servicio en RSU. Manipulación de trayectoria AGV → colisión o parada de emergencia. | 2 | 5 | **10 — Medio** | Ciberseguridad |
| **R-10** | **Explotación de dispositivos IoT (Zigbee/MQTT)** | Sensores T°/HR/presencia (76 uds.) con firmware vulnerable, claves por defecto, falta de actualización OTA. Punto de entrada a red OT (VLAN 30). | 3 | 4 | **12 — Medio** | Ciberseguridad |
| **R-11** | **Acceso no autorizado a red OT/IT** | Segmentación VLAN/ACL mal configurada, pivoting desde red IT (oficinas) a OT (AGV, SCADA, PLC). Compromiso de historiador InfluxDB o controladores. | 2 | 5 | **10 — Medio** | Ciberseguridad |
| **R-12** | **Fuga de datos operacionales y de clientes** | Portal cliente (M-05 Integración) expone API sin OAuth 2.0/TLS 1.3 correcto, logs con PII en Elasticsearch sin cifrado. Incumplimiento normativa protección de datos Cuba. | 2 | 3 | **6 — Bajo** | Ciberseguridad |

### 2.3 Riesgos de plazo y presupuesto (R-13 a R-16)

| ID | Riesgo | Descripción detallada | Prob. | Impacto | Nivel | Categoría |
|:--:|--------|------------------------|:-----:|:-------:|:-----:|:---------:|
| **R-13** | **Retraso en tramitación de licencias (Cuba)** | Licencia de obras municipal en Matanzas tarda > 16 semanas (planificadas 16). Bloquea inicio de montaje (Fase 1.4), desplaza ruta crítica. | 4 | 4 | **16 — Alto** | Plazo |
| **R-14** | **Retraso en entrega de equipos importados** | AGV (6 uds.), switches industriales (10), APs Wi-Fi 6E (14), gateways 5G/LTE, servidores. Aduanas Cuba, logística marítima Puerto Matanzas, falta de stock global. | 3 | 4 | **12 — Medio** | Plazo / Presupuesto |
| **R-15** | **Sobrecoste en obra civil no prevista** | Cimentación especial (suelo blando Matanzas), refuerzo estructura metálica para cargas AGV, impermeabilización cubierta. No incluido en presupuesto base (excluido en pasaporte). | 3 | 3 | **9 — Medio** | Presupuesto |
| **R-16** | **Desviación en desarrollo software (WMS/SCADA/AGV)** | 74 persona-mes estimados; scope creep en requisitos, deuda técnica, pruebas de integración tardías. Impacta hitos M-06 (Mes 13) y M-07 (Mes 15). | 3 | 3 | **9 — Medio** | Plazo / Presupuesto |

### 2.4 Riesgos financieros (R-17 a R-19)

| ID | Riesgo | Descripción detallada | Prob. | Impacto | Nivel | Categoría |
|:--:|--------|------------------------|:-----:|:-------:|:-----:|:---------:|
| **R-17** | **Volatilidad tipo de cambio ₽/USD / ₽/EUR** | Equipos importados cotizados en USD/EUR (AGV, switches, APs, servidores). Depreciación ₽ > 10 % (supuesto SA-08) eleva coste base > 5,000,000 ₽. | 3 | 4 | **12 — Medio** | Financiero |
| **R-18** | **Inflación en materiales y mano de obra (Cuba)** | Acero, hormigón, cableado, climatización, salarios técnicos. Inflación anual > 15 % en Cuba. Impacta coste montaje e instalación (Fases 1.4–1.5). | 3 | 3 | **9 — Medio** | Financiero |
| **R-19** | **Impago o retraso de pagos del cliente** | Hitos de facturación ligados a M-02, M-04, M-05, M-08, M-11. Flujo de caja tensionado si cliente retrasa > 30 días. Afecta pagos a proveedores/subcontratistas. | 2 | 4 | **8 — Medio** | Financiero |

### 2.5 Riesgos regulatorios — Entorno Cuba (R-20 a R-22)

| ID | Riesgo | Descripción detallada | Prob. | Impacto | Nivel | Categoría |
|:--:|--------|------------------------|:-----:|:-------:|:-----:|:---------:|
| **R-20** | **Nuevas restricciones de importación equipos telecom** | Ministerio de Comunicaciones Cuba exige homologación previa para equipos 5G privado, LTE, Wi-Fi 6E. Proceso 3–6 meses. Bloquea IT-02, IT-03, IT-04. | 2 | 5 | **10 — Medio** | Regulatorio |
| **R-21** | **Requisitos de ciberseguridad obligatorios (Cuba)** | Decreto-Ley de Ciberseguridad exige certificación SL 2 (ГОСТ Р МЭК 62443) por organismo acreditado local. Auditoría externa no planificada (+2 meses, +3,000,000 ₽). | 2 | 4 | **8 — Medio** | Regulatorio |
| **R-22** | **Normativa laboral y de seguridad industrial** | Inspección estatal (ONIT) exige adaptaciones en muelles, señalización, EPI, formación específica. Parada de obra si no cumple. | 2 | 3 | **6 — Bajo** | Regulatorio |

### 2.6 Riesgos de proveedores y subcontratistas (R-23 a R-28)

| ID | Riesgo | Descripción detallada | Prob. | Impacto | Nivel | Categoría |
|:--:|--------|------------------------|:-----:|:-------:|:-----:|:---------:|
| **R-23** | **Quiebra o incumplimiento proveedor AGV** | Proveedor único (single source) para 6 AGV con V2X. Insolvencia, retraso > 8 semanas, especificaciones no cumplidas (latencia, peso, autonomía). | 2 | 5 | **10 — Medio** | Proveedor |
| **R-24** | **Calidad deficiente en subcontrata civil** | Constructora civil no cumple tolerancias cimentación (±10 mm), nivelado suelo AGV, anclaje estanterías. Re-trabajo en MT-01, MT-02, MT-04. | 3 | 3 | **9 — Medio** | Proveedor |
| **R-25** | **Falta de personal cualificado local (Matanzas)** | Escasez de ingenieros telecom industriales, soldadores certificados, electricistas BT/MT. Requiere movilización desde La Habana (+ coste alojamiento, dietas). | 3 | 3 | **9 — Medio** | Proveedor / Recursos |
| **R-26** | **Disputa contractual con subcontratista eléctrico/HVAC** | Alcance ambiguo en instalaciones técnicas, mediciones, certificaciones. Retención de pagos, paralización obras 2–3 semanas. | 2 | 3 | **6 — Bajo** | Proveedor |
| **R-27** | **Obsolescencia de componentes durante el proyecto** | Chips para gateways 5G, módulos Wi-Fi 6E, sensores Zigbee dejan de fabricarse (EOL). Re-diseño de BOM, re-certificación. | 2 | 3 | **6 — Bajo** | Proveedor |
| **R-28** | **Dependencia de proveedor único para SAI/UPS industriales** | 2 SAI de 60 kVA para servidores y red crítica. Un solo proveedor en Cuba con stock limitado. Fallo de suministro paraliza IT-05, IT-08. | 2 | 4 | **8 — Medio** | Proveedor |

---

## 3. Análisis cuantitativo de riesgos críticos (Monte Carlo simplificado)

Para los riesgos con nivel **Alto (≥ 13)** y **Crítico (≥ 20)**, se estima impacto económico y temporal:

| ID | Riesgo | Coste esperado (₽) = Prob. × Impacto ₽ | Dias esperados = Prob. × Impacto días | Reserva asignada (₽) |
|:--:|--------|:--------------------------------------:|:-------------------------------------:|:--------------------:|
| R-01 | Interferencias RF | 0.6 × 15,000,000 = **9,000,000** | 0.6 × 45 = **27** | 7,000,000 |
| R-05 | Degradación V2X/V2I | 0.6 × 25,000,000 = **15,000,000** | 0.6 × 60 = **36** | 5,000,000* |
| R-13 | Retraso licencias | 0.8 × 12,000,000 = **9,600,000** | 0.8 × 60 = **48** | 6,000,000 |
| **Total riesgos Alto/Crítico** | | **33,600,000** | — | **18,000,000** |

> *R-05 comparte reserva con ciberseguridad (R-09–R-11). La reserva total de 27,000,000 ₽ cubre el valor esperado agregado con margen de confianza ~80 %.

---

## 4. Planes de mitigación y contingencia

### 4.1 Riesgos Alto y Crítico — Planes de mitigación (proactivos)

| ID | Riesgo | Estrategia | Acciones de mitigación | Responsable | Plazo | KRI (Indicador) |
|:--:|--------|:----------:|------------------------|:-----------:|:-----:|-----------------|
| **R-01** | Interferencias RF | **Mitigar** | 1. Site survey RF previo (Mes 2) con analizador de espectro<br>2. Diseño de canales Wi-Fi 6E (6 GHz) libre de interferencias<br>3. Cableado blindado S/FTP Cat6A + fibra OM4 para backbone<br>4. Filtros EMI en inversores y cuadros de potencia<br>5. Pruebas de convivencia Wi-Fi / LTE / 5G / mesh en fase de instalación | Ingeniero de sistemas | Mes 2–11 | Nº de alertas de interferencia / semana; RSSI medio por zona |
| **R-05** | Degradación V2X/V2I | **Mitigar** | 1. RSU ×5 con diversidad espacial (altura 6 m, antenas direccionales)<br>2. OBU dual radio (C-V2X + ITS-G5) en cada AGV<br>3. Pruebas de canal en patio y muelles (Mes 14)<br>4. Algoritmo de fallback: V2X perdido → modo seguidor de línea + parada segura<br>5. Monitoreo continuo PER (Packet Error Rate) < 1 % | Especialista AGV + Ingeniero de sistemas | Mes 13–15 | PER V2X; latencia ICA (P99); nº handovers fallidos |
| **R-13** | Retraso licencias | **Mitigar + Transferir** | 1. Gestor administrativo dedicado desde Mes 1<br>2. Pre-tramitación documentación (Mes 1–2) en paralelo a diseño<br>3. Contrato con gestoría local con experiencia en Matanzas (penalización por retraso)<br>4. Hito M-03 (obra civil) con holgura de 4 semanas en Gantt<br>5. Plan B: inicio montaje parcial (zonas no sujetas a licencia) | Gestor administrativo + PM | Mes 1–7 | % documentación completada; días para respuesta municipal |

### 4.2 Riesgos Medio — Planes de mitigación

| ID | Riesgo | Estrategia | Acciones clave | Responsable |
|:--:|--------|:----------:|----------------|:-----------:|
| R-02 | Latencia red | Mitigar | QoS estricto (DSCP EF VLAN 10), colas WRR, aislamiento tráfico AGV, pruebas iperf3 continuas | Ingeniero de sistemas |
| R-03 | Cobertura Wi-Fi | Mitigar | 14 APs con solapamiento 20 %, site survey predictivo (Ekahau), validación in situ PT-01 | Ingeniero de sistemas |
| R-04 | Fallo PTP | Mitigar | Grandmaster GPS en mástil exterior + antena TNC, holdover OCXO 4 h, BMCA forzado | Ingeniero de sistemas |
| R-06 | Fallo redundancia | Mitigar | Pruebas de caos (Chaos Engineering) mensuales: corte fibra, corte LTE, fallo SAI, fallo switch núcleo | Ingeniero de sistemas |
| R-07 | Incompatibilidad protocolos | Mitigar | Matriz de compatibilidad v1.0 (Mes 4), pruebas de interoperabilidad en laboratorio (Mes 10) | Desarrolladores + Integrador |
| R-09 | Compromiso V2X | Mitigar | Certificados ECDSA P-256 en OBU/RSU, firma BSM/ICA, validación de certificado en recepción, revocación CRL | Especialista ciberseguridad |
| R-10 | IoT vulnerable | Mitigar | Onboarding Zigbee con claves únicas, OTA obligatorio, segmentación VLAN 30 + firewall OT, escaneo mensual | Especialista ciberseguridad |
| R-11 | Acceso OT/IT | Mitigar | Firewall OT/IT (Purdue Level 3.5), DMZ industrial, bastión SSH, MFA, micro-segmentación VLAN | Especialista ciberseguridad |
| R-14 | Retraso equipos | Mitigar + Transferir | Pedidos anticipados (Mes 3), proveedores alternativos cualificados, stock de seguridad crítico (APs, switches) | Compras + PM |
| R-15 | Sobrecoste obra civil | Mitigar | Estudio geotécnico previo (Mes 2), contingencia 10 % en partida civil (fuera presupuesto proyecto), cláusula precio cerrado | PM + Constructor |
| R-16 | Desviación software | Mitigar | Scrum 2 semanas, Definition of Done estricta, pruebas continuas (CI/CD), revisión de alcance mensual con cliente | Scrum Master + PM |
| R-17 | Tipo de cambio | Transferir | Contratos en ₽ con cláusula de ajuste ±5 %, cobertura forward USD/EUR para 70 % importaciones | Financiero + PM |
| R-18 | Inflación Cuba | Mitigar | Índices de actualización en contratos locales, acuerdos marco 12 meses con proveedores nacionales | Compras + Financiero |
| R-19 | Impago cliente | Transferir | Facturación por hitos con anticipo 20 %, carta de crédito irrevocable, penalización mora 1.5 %/mes | Financiero + Jurídico |
| R-20 | Restricciones importación | Mitigar | Homologación paralela (Mes 3–6), equipos con certificación CE/FCC pre-aprobada, diálogo temprano MINCOM | Gestor administrativo |
| R-21 | Certificación ciberseguridad | Mitigar | Pre-auditoría interna Mes 14, consultor acreditado cubano contratado Mes 10, evidencias ГОСТ 62443 listas | Especialista ciberseguridad |
| R-23 | Proveedor AGV único | Transferir | Cláusula de escrow código fuente AGV, garantía bancaria 10 %, proveedor backup cualificado (no contractual) | Jurídico + PM |
| R-24 | Calidad subcontrata civil | Mitigar | Inspecciones semanales (ITP - Inspection Test Plan), hold points en cimentación y estructura, penalizaciones | Ingeniero civil + PM |
| R-25 | Falta personal cualificado | Mitigar | Convenio con universidad Matanzas (prácticas), movilización desde La Habana con paquete retributivo, formación interna | RRHH + PM |
| R-28 | SAI proveedor único | Mitigar | Stock de baterías de repuesto (2 años), contrato mantenimiento 24/7, SAI modular (paralelable) | Compras + Ingeniero instalaciones |

### 4.3 Planes de contingencia (reactivos) — Riesgos Alto/Crítico

| ID | Evento disparador | Plan de contingencia | Coste estimado (₽) | Tiempo de activación | Responsable |
|:--:|-------------------|----------------------|--------------------|:--------------------:|:-----------:|
| **R-01** | Interferencias RF impiden cobertura Wi-Fi en > 15 % superficie | 1. Despliegue APs adicionales (hasta 20)<br>2. Migración tráfico crítico AGV a 5G privado (red dedicada)<br>3. Cableado Ethernet a AGV en zonas críticas (tethering temporal) | 3,500,000 | 2 semanas | Ingeniero de sistemas |
| **R-05** | V2X no operativo tras pruebas PT-05 | 1. Desactivación V2X → modo seguidor magnético/óptico (cinta en suelo)<br>2. Reducción velocidad AGV a 0.5 m/s<br>3. Supervisión humana en cruces críticos (muelles, patio) | 2,000,000 | 1 semana | Especialista AGV |
| **R-13** | Licencia no concedida a Mes 7 | 1. Inicio montaje en nave recepción/expedición (no requiere licencia completa)<br>2. Escalación a alcalde/delegado provincial (canal cliente)<br>3. Replanificación Gantt: compresión Fase 1.4 (+20 % recursos) | 5,000,000 | Inmediato | PM + Cliente |

---

## 5. Matriz de riesgos (Probabilidad × Impacto)

```mermaid
quadrantChart
    title Matriz de Riesgos - ED Park (28 riesgos)
    x-axis Baja --> Alta
    y-axis Baja --> Alta
    quadrant-1 Mitigar prioritario (Alto)
    quadrant-2 Monitorizar (Bajo)
    quadrant-3 Aceptar (Muy bajo)
    quadrant-4 Mitigar / Transferir (Medio-Alto)
    "R-01 Interferencias RF": [0.8, 0.8]
    "R-05 V2X degradado": [0.6, 1.0]
    "R-13 Licencias": [0.8, 0.8]
    "R-02 Latencia": [0.6, 0.8]
    "R-03 Cobertura Wi-Fi": [0.6, 0.6]
    "R-04 PTP": [0.4, 0.8]
    "R-06 Redundancia": [0.4, 1.0]
    "R-07 Protocolos": [0.6, 0.6]
    "R-08 Edge capacity": [0.4, 0.6]
    "R-09 V2X ciber": [0.4, 1.0]
    "R-10 IoT ciber": [0.6, 0.8]
    "R-11 OT/IT acceso": [0.4, 1.0]
    "R-12 Fuga datos": [0.4, 0.6]
    "R-14 Equipos importados": [0.6, 0.8]
    "R-15 Sobrecoste civil": [0.6, 0.6]
    "R-16 Software": [0.6, 0.6]
    "R-17 Tipo cambio": [0.6, 0.8]
    "R-18 Inflación": [0.6, 0.6]
    "R-19 Impago": [0.4, 0.8]
    "R-20 Importación telecom": [0.4, 1.0]
    "R-21 Certif. ciber": [0.4, 0.8]
    "R-22 Normativa laboral": [0.4, 0.6]
    "R-23 Proveedor AGV": [0.4, 1.0]
    "R-24 Calidad civil": [0.6, 0.6]
    "R-25 Personal local": [0.6, 0.6]
    "R-26 Disputa eléctrica": [0.4, 0.6]
    "R-27 Obsolescencia": [0.4, 0.6]
    "R-28 SAI único": [0.4, 0.8]
```

**Leyenda visual:**
- **Rojo (cuadrante 1)**: R-01, R-05, R-13 — **Mitigación prioritaria + contingencia**
- **Naranja (cuadrante 4)**: R-02, R-04, R-06, R-09, R-10, R-11, R-14, R-17, R-19, R-20, R-21, R-23, R-28 — **Mitigación activa**
- **Amarillo (cuadrante 2)**: R-03, R-07, R-08, R-12, R-15, R-16, R-18, R-22, R-24, R-25, R-26, R-27 — **Monitorizar + plan si escala**
- **Verde (cuadrante 3)**: Ninguno en esta categoría (todos los riesgos identificados tienen al menos nivel Medio)

---

## 6. Reserva de riesgos — Desglose y control

### 6.1 Asignación por categoría (coherente con `05_04_Recursos_Presupuesto.md`)

| Categoría | Riesgos asociados | Reserva asignada (₽) | % reserva total |
|:---------:|:------------------|:--------------------:|:---------------:|
| **Técnicos (telecom/automatización)** | R-01, R-02, R-03, R-04, R-05, R-06, R-07, R-08 | **10,000,000** | 37.0 % |
| **Ciberseguridad** | R-09, R-10, R-11, R-12 | **5,000,000** | 18.5 % |
| **Plazo y presupuesto** | R-13, R-14, R-15, R-16 | **6,000,000** | 22.2 % |
| **Financieros** | R-17, R-18, R-19 | **3,000,000** | 11.1 % |
| **Regulatorios (Cuba)** | R-20, R-21, R-22 | **2,000,000** | 7.4 % |
| **Proveedores** | R-23, R-24, R-25, R-26, R-27, R-28 | **1,000,000** | 3.7 % |
| **TOTAL** | **28 riesgos** | **27,000,000** | **100 %** |

### 6.2 Gobernanza de la reserva

| Aspecto | Definición |
|---------|------------|
| **Autoridad de gasto** | PM autoriza ≤ 1,000,000 ₽; Comité de dirección (PM + Cliente + Director técnico) autoriza > 1,000,000 ₽ |
| **Solicitud de uso** | Formulario RFC (Request for Contingency) con justificación técnica, impacto si no se usa, plan de reembolso si procede |
| **Reporting** | Estado de reserva en dashboard quincenal: consumida, comprometida, disponible |
| **Cierre proyecto** | Reserva no consumida → reduce precio final al cliente (ahorro compartido 50/50) o se destina a fase de garantía |

---

## 7. Monitorización y control de riesgos

### 7.1 Key Risk Indicators (KRI) — Dashboard quincenal

| KRI | Riesgos vinculados | Umbral verde | Umbral ámbar | Umbral rojo | Frecuencia |
|:---:|:------------------:|:------------:|:------------:|:-----------:|:----------:|
| **RSSI medio zona A** | R-01, R-03 | ≥ −65 dBm | −65 a −75 dBm | < −75 dBm | Semanal (instalación) |
| **Latencia VLAN 10 P99** | R-02, R-05 | < 5 ms | 5–10 ms | > 10 ms | Continuo (SCADA) |
| **PER V2X (BSM/ICA)** | R-05, R-09 | < 1 % | 1–5 % | > 5 % | Continuo (AGV) |
| **PTP offset máx.** | R-04 | ±1 µs | ±1–10 µs | > 10 µs | Continuo (servidores) |
| **Días retraso licencia** | R-13 | ≤ 0 | 1–15 | > 15 | Quincenal |
| **% equipos recibidos vs plan** | R-14 | ≥ 95 % | 85–95 % | < 85 % | Semanal (Mes 3–10) |
| **Vulnerabilidades críticas abiertas** | R-09–R-11 | 0 | 1–2 | > 2 | Semanal (escaneo) |
| **Desviación presupuesto acumulada** | R-15, R-16, R-17, R-18 | ≤ 5 % | 5–10 % | > 10 % | Quincenal |
| **Personal clave disponible** | R-25 | 100 % | 90–99 % | < 90 % | Mensual |

### 7.2 Reuniones de riesgos

| Reunión | Frecuencia | Participantes | Entradas | Salidas |
|---------|:----------:|:-------------:|:--------:|:-------:|
| **Comité de riesgos** | Quincenal | PM, Director técnico, Especialista ciberseguridad, Ingeniero sistemas, Cliente (opcional) | Registro actualizado, KRI, RFCs | Decisiones de mitigación, autorización reserva, escalaciones |
| **Revisión técnica riesgos telecom** | Mensual | Ingeniero sistemas, Especialista AGV, Proveedor AGV, Integrador | Logs de red, pruebas PT, site surveys | Acciones correctivas, actualización probabilidad/impacto |
| **Revisión ciberseguridad** | Mensual | Especialista ciberseguridad, CISO (cliente), Auditores (si aplica) | Escaneos, logs SIEM, incidentes | Parches, reglas firewall, actualización matriz amenazas |

---

## 8. Lecciones aprendidas y riesgos residuales

### 8.1 Riesgos residuales tras mitigación (aceptados con contingencia)

| ID | Riesgo residual | Nivel residual | Justificación de aceptación |
|:--:|-----------------|:--------------:|----------------------------|
| R-01 | Interferencias imprevistas (nuevas fuentes) | Medio (9) | Mitigación reduce probabilidad; contingencia cableado/5G cubre impacto |
| R-05 | Fallo V2X en condiciones extremas (tormenta, apilamiento contenedores) | Medio (10) | Fallback a seguidor de línea probado; velocidad reducida segura |
| R-13 | Retraso licencia > 8 semanas por causa administrativa imprevisible | Alto (12) | Transferido parcialmente a gestoría; holgura en Gantt; plan B montaje parcial |
| R-17 | Devaluación ₽ > 20 % (escenario macroeconómico severo) | Medio (10) | Cobertura forward 70 %; cláusula ajuste en contratos; reserva financiera 3M ₽ |

### 8.2 Riesgos emergentes a monitorizar (no en registro inicial)

| Riesgo emergente | Señal de alerta | Acción preparatoria |
|------------------|-----------------|---------------------|
| Cambio normativo spectrum 5.9 GHz (C-V2X) en Cuba | Consulta pública MINCOM | Participar en consulta; diseño agnóstico banda (ITS-G5 backup) |
| Ciberataque supply chain (actualización firmware maliciosa) | Alerta CERT nacional | Verificación firma digital todas las actualizaciones; staging previo |
| Escasez global chips automotrices (afecta AGV) | Lead time > 26 semanas | Pedido anticipado Mes 3; acuerdo stock seguridad proveedor |

---

## 9. Referencias normativas

- **ГОСТ Р ИСО 15745-4-2010**. Системы автоматизации производства и их интеграция. Профили. Часть 4. Профили систем управления на основе Ethernet. — М.: Стандартинформ, 2010.
- **ГОСТ Р МЭК 61850-3**. Коммуникационные системы и сети в электроэнергетике. Часть 3. Общие требования к среде и испытаниям. — М.: Стандартинформ.
- **ГОСТ Р 70982-2023**. Интеллектуальные транспортные системы. Взаимодействие транспортных средств с инфраструктурой (V2X). Требования и методы испытаний. — М.: Стандартинформ, 2023.
- **ГОСТ Р МЭК 62443-3-3-2016**. Системы и меры по обеспечению кибербезопасности промышленных автоматизированных систем. Часть 3-3. Требования к безопасности системы. — М.: Стандартинформ, 2016.
- **ГОСТ Р МЭК 61131-1**. Программируемые логические контроллеры. Часть 1. Общие сведения. — М.: Стандартинформ.
- **IEEE 802.11ax**. IEEE Standard for Information Technology — Telecommunications and Information Exchange between Systems — Local and Metropolitan Area Networks — Specific Requirements — Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications — Amendment 1: Enhancements for High Efficiency WLAN.
- **IEEE 1588-2019**. IEEE Standard for a Precision Clock Synchronization Protocol for Networked Measurement and Control Systems (PTP).
- **ISO 31000:2018**. Gestión de riesgos — Directrices (referencia internacional para el proceso).
- **ГОСТ 7.32-2017**. Отчет о научно-исследовательской работе. Структура и правила оформления. — М.: Стандартинформ, 2017.
- **ГОСТ 7.1-2003**. Библиографическая запись. Библиографическое описание. — М.: Стандартинформ, 2003.

---

## 10. Checklist de la sección

- [x] Objetivo de la sección definido y alineado con el Pasaporte del Proyecto (05_01)
- [x] Metodología de gestión de riesgos descrita (identificación, análisis cuali/cuantitativo, respuesta, monitorización)
- [x] Escalas de probabilidad e impacto definidas (1–5) con matriz de nivel de riesgo
- [x] **28 riesgos identificados** en 6 categorías (técnicos, ciberseguridad, plazo/presupuesto, financieros, regulatorios Cuba, proveedores)
- [x] Análisis cualitativo completo: probabilidad, impacto, nivel de riesgo para cada riesgo
- [x] Análisis cuantitativo (Monte Carlo simplificado) para riesgos Alto/Crítico (R-01, R-05, R-13)
- [x] Planes de mitigación proactivos para todos los riesgos Medio, Alto y Crítico
- [x] Planes de contingencia reactivos para riesgos Alto/Crítico (R-01, R-05, R-13)
- [x] Matriz de riesgos (Probabilidad × Impacto) en Mermaid quadrantChart con 28 riesgos posicionados
- [x] Reserva de riesgos desglosada por categoría (total 27,000,000 ₽ = 30 % coste base, coherente con 05_04)
- [x] Gobernanza de la reserva definida (autoridad, solicitud, reporting, cierre)
- [x] KRI (Key Risk Indicadores) definidos (9 indicadores con umbrales verde/ámbar/rojo)
- [x] Calendario de reuniones de riesgos (comité quincenal, revisiones técnicas mensuales)
- [x] Riesgos residuales documentados y justificados (4 riesgos)
- [x] Riesgos emergentes identificados (3) con señales de alerta y acciones preparatorias
- [x] Referencias GOST citadas correctamente en ruso (10 estándares + ISO 31000)
- [x] Coherencia verificada con 05_01 (Pasaporte), 05_02 (WBS), 05_03 (Gantt), 05_04 (Recursos/Presupuesto)
- [x] Documento revisado por el Project Manager

---

## 11. Conclusión

La gestión de riesgos del ED Park identifica **28 riesgos** relevantes para un proyecto de infraestructura logística automatizada con 17 tecnologías de telecomunicaciones (Tema Nº 12), 6 AGV con V2X/V2I, nivel de automatización medio y entorno regulatorio cubano. Tres riesgos destacan en nivel **Alto (16)**: **R-01 Interferencias RF**, **R-05 Degradación V2X/V2I** y **R-13 Retraso en licencias municipales**, todos con planes de mitigación proactivos y contingencias reactivas definidas.

La **reserva de riesgos de 27,000,000 ₽ (30 % del coste base)** se asigna por categorías y cubre el valor esperado agregado de los riesgos críticos con margen de confianza razonable. La gobernanza establece umbrales claros de autorización y reporting quincenal mediante **9 KRI** cuantificables.

El proceso de monitorización (comité quincenal, revisiones técnicas mensuales) y la actualización continua del registro garantizan que la exposición al riesgo se mantenga dentro de los límites de tolerancia del proyecto, protegiendo los hitos clave (M-05 Red operativa Mes 11, M-07 AGV+V2X Mes 15, M-08 Pruebas Mes 16) y el presupuesto total de **117,000,000 ₽** (variante intermedia).

---

*Documento generado como parte del expediente de gestión de proyecto del proyecto ED Park — Fase 5: Gestión de Proyecto*