# Esquemas y Diagramas del ED Park

## Objetivo de la sección

Esta sección consolida en un único documento de referencia visual los diez diagramas principales del proyecto ED Park. Cada diagrama se presenta con su título, una descripción de su propósito, el código Mermaid correspondiente y una interpretación que explica los elementos clave y las decisiones de diseño que refleja. Los diagramas cubren la red de telecomunicaciones, la distribución física de equipos, la segmentación lógica de red, la redundancia, el sistema V2X/V2I, la cobertura Wi-Fi, la sincronización PTP, la arquitectura de software, el flujo de datos y la integración de sistemas.

> Esta sección es el documento de referencia visual del proyecto. Los diagramas aquí presentados sintetizan el diseño técnico completo descrito en las secciones `03_02` a `03_05`.

---

## Diagrama 1 — Topología de red

**Título**: Topología de red del ED Park — arquitectura jerárquica con redundancia

**Descripción**: Representa la estructura completa de la red de telecomunicaciones del ED Park en tres niveles jerárquicos (núcleo, distribución y campo), con la topología en anillo redundante en el núcleo, los enlaces de fibra óptica entre niveles, los puntos de acceso Wi-Fi 6/6E, las small cells 5G privado y la conexión WAN dual (fibra ISP + LTE backup).

```mermaid
graph TD
    subgraph WAN["WAN — acceso exterior"]
        ISP[Fibra ISP\n1 Gbps]
        LTE_W[LTE backup\n100 Mbps]
    end

    subgraph NUCLEO["Núcleo — Sala de control"]
        FW[Firewall / Router\nperimetral]
        SW_C1[SW-C1\nSwitch núcleo 10G]
        SW_C2[SW-C2\nSwitch núcleo 10G]
        SRV1[SRV-01\nWMS]
        SRV2[SRV-02\nAGV / SCADA]
        SRV3[SRV-03\nBackup]
        WLC[WLC\nControlador Wi-Fi]
        GM[Grandmaster\nPTP GPS]
        LTE_ENB[eNodeB\nLTE privado]
        CORE5G[Core 5G NPN]
        EDGE_SEC[Edge-GW-03\nSeguridad OT]
    end

    subgraph NAVE_P["Distribución — Nave principal"]
        SW_D1[SW-D1 1G]
        SW_D2[SW-D2 1G]
        AP1[AP-1] & AP2[AP-2] & AP3[AP-3]
        AP4[AP-4] & AP5[AP-5] & AP6[AP-6]
        GNB1[gNB-1 5G] & GNB2[gNB-2 5G]
        EDGE_IOT[Edge-GW-01 IoT]
        RSU1[RSU-1] & RSU2[RSU-2]
    end

    subgraph NAVE_R["Distribución — Nave recepción"]
        SW_D3[SW-D3 1G]
        SW_D4[SW-D4 1G]
        AP7[AP-7] & AP8[AP-8]
        AP9[AP-9] & AP10[AP-10]
        GNB3[gNB-3 5G] & GNB4[gNB-4 5G]
        EDGE_MU[Edge-GW-04 Muelles]
        RSU3[RSU-3] & RSU4[RSU-4]
    end

    subgraph CAMPO["Campo — Patio y zona AGV"]
        SW_F1[SW-F1 campo AGV]
        SW_F2[SW-F2 campo muelles]
        AP11[AP-11 ext] & AP12[AP-12 ext]
        AP13[AP-13 ext] & AP14[AP-14 ext]
        MESH1[MESH-1] & MESH2[MESH-2]
        EDGE_AGV[Edge-GW-02 AGV]
        RSU5[RSU-5]
    end

    ISP --> FW
    LTE_W -.->|failover| FW
    FW --> SW_C1
    SW_C1 <-->|anillo fibra OM4 10G| SW_C2
    SW_C1 --> SRV1 & SRV2 & SRV3 & WLC & GM & LTE_ENB & CORE5G & EDGE_SEC
    SW_C2 --> SW_D1 & SW_D3 & SW_F1
    SW_D1 --> SW_D2
    SW_D1 --> AP1 & AP2 & AP3 & GNB1 & EDGE_IOT & RSU1 & RSU2
    SW_D2 --> AP4 & AP5 & AP6 & GNB2
    SW_D3 --> SW_D4
    SW_D3 --> AP7 & AP8 & GNB3 & EDGE_MU & RSU3 & RSU4
    SW_D4 --> AP9 & AP10 & GNB4
    SW_F1 --> SW_F2
    SW_F1 --> AP11 & AP12 & MESH1 & EDGE_AGV & RSU5
    SW_F2 --> AP13 & AP14 & MESH2
```

**Interpretación**: El núcleo forma un anillo de fibra OM4 a 10 Gbps entre SW-C1 y SW-C2, eliminando el punto único de fallo en la capa más crítica. Cada nave tiene su propio par de switches de distribución conectados a ambos switches de núcleo (conexión dual upstream). Los switches de campo en el exterior dependen del SW-C2 pero cuentan con MESH como respaldo inalámbrico. Los gNB de 5G privado y los APs Wi-Fi 6 se conectan a los switches de distribución de su nave, garantizando cobertura celular y Wi-Fi independiente por zona.

---

## Diagrama 2 — Ubicación física de equipos en el plano

**Título**: Plano de distribución de equipos del ED Park (vista en planta esquemática)

**Descripción**: Muestra la posición relativa de los principales equipos de red, sensores, AGV y PLC sobre el plano del parque, organizado por zonas físicas. Permite visualizar la lógica de despliegue de la infraestructura sobre la planta de 5,000 m².

```mermaid
block-beta
    columns 7

    space:1
    VERDE["Área verde 300 m²\n[MESH-1] [MESH-2]"]:3
    space:1
    space:2

    AP_OF["[AP-11]\n[AP-12]"]:1
    OFIC["OFICINAS + SALA CONTROL 250 m²\n[SW-C1][SW-C2][SRV-01..03]\n[WLC][GM-PTP][EDGE-SEC]"]:2
    AGV_Z["ZONA AGV 300 m²\n[SW-F1][EDGE-AGV]\n[RSU-5][Est.carga ×6]"]:2
    AP_EXT["[AP-13]\n[AP-14]"]:1
    space:1

    AP_Z["[AP-1..6]\n[GNB-1..2]"]:1
    NAVE_P["NAVE PRINCIPAL 2,000 m²\n— Zona A: estant. convecc. [RFID-pórtico ×2]\n— Zona B: T°control [EDGE-IOT][Sens.T°/HR ×20]\n— Zona C: alta rotación\n— Picking: [RFID-fijo ×2][básc.×3]\n[RSU-1][RSU-2][PLC-cintas]"]:4
    space:1
    space:1

    AP_R["[AP-7..10]\n[GNB-3..4]"]:1
    NAVE_R["NAVE RECEPCIÓN/EXPEDICIÓN 1,100 m²\n— Muelles M-01..M-04 [PLC-muelles ×2]\n— Verificación [básc.plat.×2][RFID-pórtico ×2]\n— Staging entrada/salida\n[EDGE-MU][RSU-3][RSU-4]\n[Cinta CT-01..CT-03]"]:4
    space:1
    space:1

    AP_PT["[AP-11ext]\n[AP-12ext]"]:1
    PATIO["PATIO MANIOBRAS 700 m²\n[Cámaras PTZ ×4][barreras]\n[AGV-1..6 en tránsito]"]:4
    space:1
    APARCA:1

    space:1
    MUELLES["MUELLES  M-01  M-02  M-03  M-04\n[SW-F2][Sens.puertas ×6]"]:5
    space:1
```

**Interpretación**: Los switches de núcleo y los servidores se concentran en la sala de control (zona segura, climatizada, acceso restringido). Los edge gateways se distribuyen por zonas funcionales: Edge-GW-01 en zona B (IoT), Edge-GW-02 en zona AGV, Edge-GW-04 en muelles. Las RSU V2X se ubican en los puntos de mayor riesgo de colisión: intersecciones de pasillos y muelles. Los APs se posicionan en el techo de cada nave y en mástiles en el exterior para garantizar cobertura continua.

---

## Diagrama 3 — Segmentación VLAN y QoS

**Título**: Arquitectura de segmentación lógica — VLANs y políticas QoS del ED Park

**Descripción**: Muestra las ocho VLANs del ED Park, su función, los dispositivos que las componen y la prioridad QoS asignada a cada segmento. La separación lógica entre OT (operación) e IT (negocio) es el principio central de seguridad de la red.

```mermaid
graph LR
    subgraph FIREWALL["Firewall perimetral\n+ Edge-GW-03 IDS/IPS OT"]
        FW_NODE[" "]
    end

    subgraph OT["Zona OT — control industrial"]
        VLAN10["VLAN 10 — AGV-CONTROL\nPrioridad: MÁXIMA DSCP EF\nAGV OBU · RSU V2X · Edge-GW-02\nLatencia: < 5 ms"]
        VLAN20["VLAN 20 — INDUSTRIAL-CTRL\nPrioridad: ALTA DSCP AF41\nPLC muelles · PLC cintas · Edge-GW-04\nLatencia: < 20 ms"]
        VLAN40["VLAN 40 — IOT-SENSORS\nPrioridad: MEDIA DSCP AF21\nSensores T°/HR · presencia · puertas\nRetención: 90 días"]
    end

    subgraph IT["Zona IT — negocio y gestión"]
        VLAN30["VLAN 30 — WMS-SERVERS\nPrioridad: ALTA DSCP AF31\nSRV-01 · SRV-02 · SRV-03\nDisponibilidad: 99.9 %"]
        VLAN50["VLAN 50 — WIFI-OPERARIOS\nPrioridad: MEDIA DSCP AF11\nTerminales mano · tabletas · escáneres\nUsuarios: hasta 30"]
        VLAN60["VLAN 60 — CAMERAS-CCTV\nPrioridad: NORMAL DSCP CS0\nCámaras IP interior · exterior\nAncho de banda: 4 Mbps/cámara"]
        VLAN70["VLAN 70 — ADMIN-OFICINAS\nPrioridad: NORMAL DSCP CS0\nPCs · impresoras · teléfonos"]
    end

    subgraph MGMT["Gestión de red"]
        VLAN99["VLAN 99 — MGMT\nPrioridad: ALTA DSCP CS6\nInterfaces mgmt switches · APs · WLC"]
    end

    subgraph EXTERIOR["Zona exterior / clientes"]
        EXT[ERP cliente · TMS · Portal web]
    end

    VLAN10 <-->|"ACL: solo MQTT/V2X"| VLAN20
    VLAN20 <-->|"ACL: solo OPC-UA"| VLAN30
    VLAN40 -->|"MQTT → broker SRV-02"| VLAN30
    VLAN30 <-->|"REST API interna"| VLAN50
    VLAN30 -->|"API Gateway TLS 1.3\nOAuth 2.0"| EXTERIOR
    FIREWALL <-->|"Segmentación OT/IT"| OT
    FIREWALL <-->|"Segmentación IT/Exterior"| IT
    VLAN99 -.->|"Acceso mgmt restringido"| OT
    VLAN99 -.->|"Acceso mgmt restringido"| IT
```

**Interpretación**: La VLAN 10 (AGV-CONTROL) recibe máxima prioridad QoS (DSCP EF — Expedited Forwarding) para garantizar latencia < 5 ms en los comandos de navegación. Las VLANs OT (10, 20, 40) están separadas de las IT (30, 50, 60, 70) por el Edge-GW-03 que actúa como firewall OT con ACLs estrictas. El tráfico exterior pasa por el API Gateway con TLS 1.3 y OAuth 2.0, sin acceso directo a las VLANs internas. La VLAN 99 de gestión está aislada y solo accesible desde la sala de control.

---

## Diagrama 4 — Redundancia de canales de comunicación

**Título**: Arquitectura de redundancia a cuatro niveles del ED Park

**Descripción**: Ilustra las cuatro capas de redundancia implementadas en la infraestructura de comunicaciones: backbone en anillo (RSTP), WAN dual (fibra + LTE), doble radio para AGV (Wi-Fi 6 + 5G privado) y alimentación ininterrumpida (SAI + generador).

```mermaid
graph TD
    subgraph NIVEL_1["Nivel 1 — Backbone en anillo RSTP"]
        C1[SW-C1 10G] <-->|"Primario\nfibra OM4 10G\nRSTP < 50 ms"| C2[SW-C2 10G]
        C1 <-.->|"Backup\nanillo cerrado"| C2
    end

    subgraph NIVEL_2["Nivel 2 — WAN dual"]
        FIBRA["Fibra ISP 1 Gbps\n↑↓ primario"]
        LTE_BK["LTE backup 100 Mbps\nfailover < 30 s"]
        FIBRA -->|normal| C1
        LTE_BK -.->|failover automático| C1
    end

    subgraph NIVEL_3["Nivel 3 — AGV doble radio"]
        AGV_N[AGV-1..6]
        WIFI6["Wi-Fi 6E 5 GHz\nprimario < 5 ms"]
        G5["5G privado\nbackup < 1 ms"]
        AGV_N <-->|primario| WIFI6
        AGV_N <-.->|backup activo| G5
        WIFI6 --> C2
        G5 --> CORE5G[Core 5G NPN]
        CORE5G --> C1
    end

    subgraph NIVEL_4["Nivel 4 — Alimentación ininterrumpida"]
        RED_E["Red eléctrica\nprincipal"]
        SAI1["SAI-1 UPS\n3,000 VA / 15 min"]
        SAI2["SAI-2 UPS\n3,000 VA / 15 min"]
        GEN["Generador\nemergencia 20 kVA"]
        RED_E --> SAI1 & SAI2
        GEN -.->|"arranque < 10 s"| SAI1
        SAI1 --> C1 & SRV1[SRV-01] & SRV2[SRV-02]
        SAI2 --> C2 & SRV3[SRV-03]
    end

    classDef primary fill:#d4edda,stroke:#28a745
    classDef backup fill:#fff3cd,stroke:#ffc107,stroke-dasharray:5 5
    class FIBRA,WIFI6,RED_E primary
    class LTE_BK,G5,GEN backup
```

**Interpretación**: El tiempo de recuperación ante fallo del backbone es < 50 ms (RSTP). El failover WAN tarda < 30 s (detección + conmutación LTE). Los AGV nunca pierden conectividad: si Wi-Fi 6E cae, 5G privado asume en < 100 ms (handover). Los SAI garantizan 15 minutos de operación para arranque ordenado del generador. El generador cubre una parada eléctrica total indefinida. Disponibilidad resultante de la red: 99.9 %.

---

## Diagrama 5 — Arquitectura V2X/V2I para AGV

**Título**: Sistema V2X/V2I del ED Park — flujo de mensajes y coordinación de vehículos

**Descripción**: Muestra el flujo completo de mensajes V2X entre los AGV (OBU), las unidades de infraestructura fija (RSU) y el servidor V2X, incluyendo los cuatro tipos de mensaje (BSM, SPaT, ICA, MAP) y el proceso de coordinación en intersecciones y muelles.

```mermaid
sequenceDiagram
    participant AGV1 as AGV-1 (OBU)
    participant AGV2 as AGV-2 (OBU)
    participant RSU1 as RSU-1 (intersección nave P)
    participant SRV as Servidor V2X (SRV-02)
    participant RSU3 as RSU-3 (muelle M-01)
    participant CAM as Cámara IP + visión

    Note over AGV1,RSU1: Fase 1 — Transmisión de posición (10 Hz)
    AGV1->>RSU1: BSM: pos(4.2,12.1) v=1.2m/s dir=N
    AGV2->>RSU1: BSM: pos(4.0,8.3) v=0.9m/s dir=N
    RSU1->>SRV: Reenvío BSM AGV-1 y AGV-2

    Note over SRV,RSU1: Fase 2 — Detección de riesgo de colisión
    CAM->>SRV: Detección visual: 2 AGV en trayectoria convergente
    SRV->>SRV: Cálculo TTC (Time to Collision) = 2.3 s
    SRV->>RSU1: ICA: alerta colisión inminente zona (4.1, 10.0)
    RSU1->>AGV1: ICA: reducir velocidad, ceder paso
    RSU1->>AGV2: ICA: detener en posición actual

    Note over AGV1,AGV2: Fase 3 — Maniobra de seguridad
    AGV1->>AGV1: Reducir v → 0.3 m/s
    AGV2->>AGV2: Detener (v=0)
    AGV1->>RSU1: BSM: pos(4.2,10.5) v=0.3m/s
    Note over AGV1,AGV2: Cruce completado sin colisión

    Note over RSU3,AGV1: Fase 4 — Acceso a muelle
    RSU3->>AGV1: SPaT: puerta M-01 ABIERTA, acceso habilitado
    AGV1->>RSU3: ACK avanzando a M-01
    SRV->>AGV1: MAP: ruta actualizada → zona staging entrada

    Note over SRV: Registro de todos los mensajes con timestamp PTP ±1 µs
```

**Interpretación**: El sistema V2X opera en cuatro fases: transmisión continua de posición (BSM a 10 Hz), detección de riesgo por el servidor V2X con apoyo de visión artificial, generación de alertas ICA para maniobra de seguridad, y sincronización con la infraestructura de muelles (SPaT). La latencia máxima desde detección hasta envío de ICA es < 5 ms, suficiente para detener un AGV a 6 km/h con una distancia de seguridad > 0.8 m. Todos los mensajes se registran con timestamp PTP para auditoría.

---

## Diagrama 6 — Cobertura Wi-Fi en las 2 naves y patio

**Título**: Plan de cobertura Wi-Fi 6/6E del ED Park — 14 puntos de acceso

**Descripción**: Representa la distribución de los 14 puntos de acceso Wi-Fi 6/6E del ED Park sobre el plano en planta, con los radios de cobertura estimados, el solapamiento entre celdas y la asignación de canales para evitar interferencias.

```mermaid
graph TB
    subgraph PLANTA["Planta del ED Park — Vista esquemática de cobertura"]

        subgraph NP["NAVE PRINCIPAL 2,000 m²\nAltura libre 8 m — APs en techo h=7 m"]
            AP1C(("AP-1\nCh 36\n25m"))
            AP2C(("AP-2\nCh 40\n25m"))
            AP3C(("AP-3\nCh 44\n25m"))
            AP4C(("AP-4\nCh 36\n25m"))
            AP5C(("AP-5\nCh 40\n25m"))
            AP6C(("AP-6\nCh 44\n25m"))
            AP1C -.-|"solapamiento\n≥ 20 %"| AP2C
            AP2C -.-|"solapamiento\n≥ 20 %"| AP3C
            AP4C -.-|"solapamiento\n≥ 20 %"| AP5C
            AP5C -.-|"solapamiento\n≥ 20 %"| AP6C
            AP1C -.-|"solapamiento\n≥ 20 %"| AP4C
            AP2C -.-|"solapamiento\n≥ 20 %"| AP5C
            AP3C -.-|"solapamiento\n≥ 20 %"| AP6C
        end

        subgraph NR["NAVE RECEPCIÓN 1,100 m²\nAltura libre 7 m — APs en techo h=6 m"]
            AP7C(("AP-7\nCh 36\n22m"))
            AP8C(("AP-8\nCh 40\n22m"))
            AP9C(("AP-9\nCh 44\n22m"))
            AP10C(("AP-10\nCh 36\n22m"))
            AP7C -.-|"solapamiento\n≥ 20 %"| AP8C
            AP8C -.-|"solapamiento\n≥ 20 %"| AP9C
            AP9C -.-|"solapamiento\n≥ 20 %"| AP10C
            AP7C -.-|"solapamiento\n≥ 20 %"| AP10C
        end

        subgraph EXT["EXTERIOR — Patio y zona AGV\nAPs en mástil h=4 m"]
            AP11C(("AP-11\nCh 149\n40m\next"))
            AP12C(("AP-12\nCh 153\n40m\next"))
            AP13C(("AP-13\nCh 157\n40m\next"))
            AP14C(("AP-14\nCh 161\n40m\next"))
            AP11C -.-|"solapamiento"| AP12C
            AP12C -.-|"solapamiento"| AP13C
            AP13C -.-|"solapamiento"| AP14C
        end

        NP -.-|"handover\nseamless"| NR
        NR -.-|"handover\nseamless"| EXT
        NP -.-|"handover\nseamless"| EXT
    end

    subgraph PARAMS["Parámetros de diseño RF"]
        P1["Radio cobertura interior: ~25 m\n(obstáculos metálicos, h=7 m)"]
        P2["Radio cobertura exterior: ~40 m\n(línea de vista, h=4 m)"]
        P3["Solapamiento mínimo: 20 %\n(condición para handover sin pérdida)"]
        P4["Bandas utilizadas:\n2.4 GHz (legacy) + 5 GHz (operarios)\n6 GHz (AGV — canal exclusivo)"]
        P5["Seguridad: WPA3-Enterprise\n802.1X + certificados X.509"]
    end
```

**Interpretación**: La nave principal (2,000 m²) requiere 6 APs en disposición 2×3 para garantizar cobertura total con solapamiento ≥ 20 % entre celdas adyacentes. La nave de recepción (1,100 m²) requiere 4 APs en disposición 2×2. El exterior se cubre con 4 APs de mayor potencia (27 dBm) montados en mástiles. La banda de 6 GHz (Wi-Fi 6E) se asigna exclusivamente a los AGV, eliminando interferencias con otros dispositivos. El solapamiento del 20 % garantiza handover sin pérdida de paquetes para AGV en movimiento a 6 km/h.

---

## Diagrama 7 — Sincronización de tiempo PTP

**Título**: Jerarquía de sincronización PTP (IEEE 1588) del ED Park

**Descripción**: Muestra la jerarquía completa del protocolo PTP desde el reloj maestro GPS (Grandmaster) hasta los relojes ordinarios en los nodos finales (AGV, servidores, PLC), con los roles de cada dispositivo y la precisión alcanzada en cada nivel.

```mermaid
graph TD
    GPS_ANT["🛰 Antena GPS exterior\nReferencia UTC global"]

    subgraph GM_LEVEL["Grandmaster Clock — Nivel 0"]
        GM["Meinberg LANTIME M300\nGrandmaster PTP GPS\nPrecisión: ±50 ns\nProtocolo: PTP v2.1 IEEE 1588-2019"]
    end

    subgraph BC_LEVEL["Boundary Clock — Nivel 1\nSwitches núcleo"]
        BC1["SW-C1\nBoundary Clock\n±100 ns\nDomain: 0"]
        BC2["SW-C2\nBoundary Clock\n±100 ns\nDomain: 0\n(backup BC)"]
    end

    subgraph TC_LEVEL["Transparent Clock — Nivel 2\nSwitches distribución y campo"]
        TC1["SW-D1\nTransparent Clock\n±500 ns"]
        TC2["SW-D2\nTransparent Clock\n±500 ns"]
        TC3["SW-D3\nTransparent Clock\n±500 ns"]
        TC4["SW-D4\nTransparent Clock\n±500 ns"]
        TC5["SW-F1\nTransparent Clock\n±500 ns"]
    end

    subgraph OC_LEVEL["Ordinary Clock — Nivel 3\nNodos finales"]
        OC1["SRV-01 WMS\nNIC Intel I210\n±1 µs"]
        OC2["SRV-02 AGV/SCADA\nNIC Intel I210\n±1 µs"]
        OC3["AGV-1..6\nControlador embarcado\n±1 µs"]
        OC4["PLC muelles ×2\n±1 µs"]
        OC5["RSU V2X ×5\n±1 µs"]
        OC6["Cámaras IP ×12\n±1 µs"]
    end

    GPS_ANT -->|"señal GPS 1PPS\n±20 ns"| GM
    GM -->|"PTP Announce\nSync / Follow_Up\nDelay_Req / Resp"| BC1
    GM -.->|"PTP backup\n(GM falla → BC1 asume)"| BC2
    BC1 -->|"PTP Sync"| TC1 & TC3
    BC2 -->|"PTP Sync"| TC2 & TC4 & TC5
    TC1 -->|"PTP transparente"| OC1 & OC3
    TC2 -->|"PTP transparente"| OC2
    TC3 -->|"PTP transparente"| OC4 & OC5
    TC4 -->|"PTP transparente"| OC6
    TC5 -->|"PTP transparente"| OC3

    BC1 <-->|"BMCA\n(Best Master\nClock Algorithm)"| BC2

    style GM fill:#ff9900,color:#000,font-weight:bold
    style BC1 fill:#4da6ff,color:#000
    style BC2 fill:#4da6ff,color:#000
    style GPS_ANT fill:#90ee90,color:#000
```

**Interpretación**: El Grandmaster sincroniza su reloj interno con GPS (precisión ±20 ns), propagando PTP a los Boundary Clocks de los switches de núcleo (±100 ns). Los Transparent Clocks en los switches de distribución y campo no modifican los timestamps PTP sino que corrigen el retardo de transit (±500 ns al final). Los nodos finales (AGV, servidores, PLC, RSU) mantienen sincronización ±1 µs, suficiente para correlacionar eventos entre sistemas y coordinar AGV en intersecciones sin ambigüedad de posición. Si el GM falla, el BC1 asume el rol de maestro mediante el algoritmo BMCA.

---

## Diagrama 8 — Arquitectura del software

**Título**: Arquitectura de la plataforma de software del ED Park — 6 módulos integrados

**Descripción**: Representa la arquitectura completa del software de gestión del ED Park, mostrando los seis módulos principales, el bus de integración (MQTT + REST + WebSocket), la capa de datos, los clientes de usuario y la conexión con la infraestructura física de campo.

```mermaid
graph LR
    subgraph USUARIOS["Usuarios"]
        U1["👤 Supervisor\nPC sala control"]
        U2["📱 Operario\nTerminal mano"]
        U3["🔧 Técnico\nTablet"]
        U4["🌐 Cliente\nNavegador web"]
    end

    subgraph UI_MOD["M-06 Interfaz de usuario"]
        WEB["Portal web\nReact 18 + TypeScript"]
        APP["App móvil\nReact Native"]
    end

    subgraph BUS["Bus de integración — SRV-02"]
        MQTT_B["MQTT Broker v5\nMosquitto"]
        REST_GW["REST API Gateway\nOpenAPI 3.0"]
        WS_SRV["WebSocket\nsocket.io"]
    end

    subgraph MODULOS["Módulos de negocio"]
        M01["M-01 WMS\nSpring Boot\nSRV-01"]
        M02["M-02 Control AGV\nROS 2 / Python\nSRV-02"]
        M03["M-03 V2X/V2I\nProcesador mensajes\nSRV-02"]
        M04["M-04 SCADA\nIgnition / WinCC\nSRV-02"]
        M05["M-05 Integración\nKong API Gateway\nSRV-01"]
    end

    subgraph DATOS["Capa de datos"]
        DB1[("PostgreSQL\nWMS + pedidos")]
        DB2[("InfluxDB\nSCADA + T°")]
        DB3[("TimescaleDB\nAGV + misiones")]
        BK[("SRV-03\nBackup diario")]
    end

    subgraph CAMPO["Campo"]
        AGV_F["AGV ×6\nOBU + LiDAR"]
        RSU_F["RSU ×5\nV2X fijos"]
        PLC_F["PLC ×4\nmuelles + cintas"]
        IOT_F["Sensores IoT ×76\nZigbee T°/HR"]
        EGW_F["Edge GW ×4\nMQTT + OPC-UA"]
    end

    subgraph EXTERNO["Externo"]
        ERP["ERP cliente"]
        TMS["TMS cliente"]
    end

    U1 & U3 --> WEB
    U2 --> APP
    U4 --> WEB
    WEB & APP --> REST_GW & WS_SRV
    REST_GW --> M01 & M04 & M05
    MQTT_B --> M02 & M03
    WS_SRV --> M01 & M02 & M04
    M01 --> DB1
    M02 --> DB3
    M04 --> DB2
    M03 --> DB3
    DB1 & DB2 & DB3 --> BK
    M02 <-->|"MQTT 5G/Wi-Fi"| AGV_F
    M03 <-->|"MQTT V2X"| RSU_F
    M04 <-->|"OPC-UA via EGW"| EGW_F
    EGW_F <-->|Zigbee| IOT_F
    EGW_F <-->|"Modbus RTU"| PLC_F
    M05 <-->|"REST / EDI"| ERP & TMS
    M01 <-->|"MQTT interno"| M02
    M02 <-->|"MQTT interno"| M03
    M04 <-->|"REST interno"| M01
    M05 <-->|"REST interno"| M01
```

**Interpretación**: La arquitectura separa explícitamente los módulos de tiempo real (M-02, M-03 — en SRV-02) de los módulos de negocio (M-01 — en SRV-01) y de integración externa (M-05). El bus de integración permite que los módulos se comuniquen sin acoplamiento directo: MQTT para tráfico de tiempo real (AGV, sensores), REST para operaciones transaccionales (WMS, integración), WebSocket para actualizaciones en tiempo real del dashboard. La capa de datos usa tres motores especializados: PostgreSQL para datos relacionales (inventario), InfluxDB para series temporales de proceso (SCADA) y TimescaleDB para telemetría de AGV.

---

## Diagrama 9 — Flujo de datos principal

**Título**: Flujo de datos del proceso de recepción, almacenamiento y expedición

**Descripción**: Muestra el flujo completo de datos desde la llegada de mercancía al muelle hasta la confirmación de expedición al cliente, pasando por todos los sistemas (SCADA, WMS, AGV, V2X, integración). Es el diagrama de flujo de datos operativo central del ED Park.

```mermaid
flowchart TD
    PROV["🚛 Camión en patio\nproveedor / transportista"]

    subgraph RECEPCION["RECEPCIÓN"]
        MUELLE["Muelle M-01 o M-02\nSPaT: puerta ABIERTA"]
        DESCARGA["Descarga de mercancía\noperario + transpaleta"]
        VERIF["Verificación:\n• Escaneo RFID pórtico\n• Pesaje báscula plataforma\n• Inspección visual"]
        REG_WMS["Registro en WMS M-01:\n• Albarán vs. orden de compra\n• Asignación de ubicación\n• Generación etiqueta RFID pallet"]
    end

    subgraph ALMACENAMIENTO["ALMACENAMIENTO"]
        STAGING["Zona staging entrada"]
        AGV_TR["AGV asignado\npor M-02 Control AGV"]
        V2X_RUTA["Ruta calculada + V2X\ncoordinación intersecciones"]
        UBIC["Pallet depositado en\nZona A / B / C\nWMS actualiza stock"]
    end

    subgraph PICKING["PICKING Y PREPARACIÓN"]
        ORDEN["Orden de pedido\ncliente vía M-05"]
        PICK_TASK["WMS genera ruta\nde picking optimizada"]
        AGV_PICK["AGV trae pallet\na zona de picking"]
        PICK_OP["Operario: extrae unidades\n+ escáner RFID confirmación"]
        EMBAL["Embalaje + pesaje mesa\n+ impresión etiqueta envío"]
    end

    subgraph EXPEDICION["EXPEDICIÓN"]
        CONSOLID["Consolidación por\nruta o cliente"]
        STAGING_OUT["Zona staging salida"]
        MUELLE_EXP["Muelle M-03 o M-04\nSPaT: puerta ABIERTA"]
        DESPACHO["Carga en camión\n+ cierre pedido WMS"]
        NOTIF["Webhook → ERP cliente\nconfirmación despacho"]
    end

    subgraph MONITOREO["MONITOREO TRANSVERSAL"]
        SCADA_M["SCADA M-04:\n• T°/HR zona B\n• Estado muelles\n• Alertas"]
        PTP_M["PTP IEEE 1588:\ntimestamp ±1 µs\nen todos los eventos"]
        LOG["Logs auditables\nSRV-03 backup"]
    end

    PROV --> MUELLE
    MUELLE --> DESCARGA --> VERIF --> REG_WMS
    REG_WMS --> STAGING --> AGV_TR
    AGV_TR <-->|"BSM / ICA"| V2X_RUTA
    V2X_RUTA --> UBIC
    UBIC -->|"pedido recibido"| ORDEN
    ORDEN --> PICK_TASK --> AGV_PICK --> PICK_OP --> EMBAL
    EMBAL --> CONSOLID --> STAGING_OUT --> MUELLE_EXP --> DESPACHO --> NOTIF
    SCADA_M -.->|"alertas T°"| REG_WMS
    SCADA_M -.->|"control puertas"| MUELLE & MUELLE_EXP
    PTP_M -.->|"timestamp"| VERIF & UBIC & PICK_OP & DESPACHO
    LOG -.->|"registro"| REG_WMS & UBIC & DESPACHO
```

**Interpretación**: El flujo de datos sigue el ciclo operativo completo: recepción (datos de proveedor → WMS), almacenamiento (WMS → AGV → ubicación física), picking (pedido cliente → WMS → AGV → operario) y expedición (WMS → muelle → confirmación cliente). El SCADA monitorea transversalmente el proceso controlando las condiciones ambientales y el estado de los muelles. El PTP garantiza que todos los eventos del flujo tengan timestamps coherentes para trazabilidad de lote completa. Todos los datos se replican en SRV-03 para auditoría.

---

## Diagrama 10 — Integración de sistemas

**Título**: Mapa de integración de sistemas del ED Park — interfaces internas y externas

**Descripción**: Muestra todas las interfaces de integración entre los módulos internos del ED Park y los sistemas externos (ERP, TMS, portal cliente), incluyendo los protocolos, el tipo de integración (síncrona/asíncrona) y las VLANs que atraviesan.

```mermaid
graph TB
    subgraph INTERNO["ED Park — Sistemas internos"]
        subgraph OT_INT["Zona OT (VLAN 10/20/40)"]
            M02_I["M-02\nControl AGV"]
            M03_I["M-03\nV2X/V2I"]
            M04_I["M-04\nSCADA"]
        end

        subgraph IT_INT["Zona IT (VLAN 30/50)"]
            M01_I["M-01\nWMS"]
            M05_I["M-05\nIntegración"]
            M06_I["M-06\nUI"]
        end

        FW_OT["Firewall OT/IT\nEdge-GW-03"]
    end

    subgraph CAMPO_INT["Infraestructura física"]
        AGV_INT["AGV ×6\nOBU V2X"]
        RSU_INT["RSU ×5\nV2X fijos"]
        PLC_INT["PLC ×4\nmuelles + cintas"]
        IOT_INT["Sensores IoT ×76"]
        EGW_INT["Edge GW ×4"]
    end

    subgraph EXTERNO_INT["Sistemas externos del cliente"]
        ERP_INT["ERP cliente\n(SAP / 1C)"]
        TMS_INT["TMS cliente"]
        PORTAL_INT["Portal web\ncliente"]
        EMAIL_INT["Email / SMS\nnotificaciones"]
    end

    subgraph PROTOCOLOS["Protocolos de integración"]
        P_MQTT["MQTT v5\nasíncrono\nQoS 1"]
        P_OPCUA["OPC-UA\nsíncrono\ngarantizado"]
        P_REST["REST / JSON\nHTTPS TLS 1.3\nsíncrono"]
        P_EDI["EDI X12 / EDIFACT\no REST/JSON\ncliente ERP legacy"]
        P_WH["Webhooks HTTPS\nasíncrono\neventos"]
    end

    M02_I <-->|"MQTT v5\nVLAN 10"| AGV_INT
    M03_I <-->|"MQTT V2X\nVLAN 10"| RSU_INT
    M04_I <-->|"OPC-UA via EGW\nVLAN 20"| EGW_INT
    EGW_INT <-->|"Zigbee"| IOT_INT
    EGW_INT <-->|"Modbus RTU"| PLC_INT

    M02_I <-->|"MQTT interno\nVLAN 30"| M01_I
    M03_I <-->|"MQTT interno\nVLAN 30"| M02_I
    M04_I <-->|"REST API\nVLAN 30"| M01_I
    M01_I <-->|"REST API\nVLAN 30"| M05_I
    M06_I <-->|"REST + WebSocket\nVLAN 50"| M01_I
    M06_I <-->|"REST + WebSocket\nVLAN 50"| M04_I

    OT_INT <-->|"ACL estricta\nfirewall OT/IT"| FW_OT
    FW_OT <-->|"tráfico permitido"| IT_INT

    M05_I <-->|"REST / EDI\nTLS 1.3 + OAuth 2.0"| ERP_INT
    M05_I <-->|"REST / JSON\nTLS 1.3"| TMS_INT
    M05_I -->|"Webhooks HTTPS"| PORTAL_INT
    M04_I -->|"SMTP / SMS API"| EMAIL_INT

    classDef ot fill:#fff3cd,stroke:#ffc107
    classDef it fill:#d4edda,stroke:#28a745
    classDef ext fill:#d1ecf1,stroke:#17a2b8
    class M02_I,M03_I,M04_I,AGV_INT,RSU_INT,PLC_INT,IOT_INT,EGW_INT ot
    class M01_I,M05_I,M06_I it
    class ERP_INT,TMS_INT,PORTAL_INT,EMAIL_INT ext
```

**Interpretación**: El mapa de integración muestra tres zonas claramente separadas: OT (naranja) con los módulos de control en tiempo real y la infraestructura física, IT (verde) con los módulos de negocio y la interfaz de usuario, y exterior (azul) con los sistemas del cliente. La separación OT/IT la implementa el Edge-GW-03 con ACLs que solo permiten el tráfico estrictamente necesario (MQTT desde M-02 a M-01 para confirmaciones de misión, REST desde M-04 a M-01 para alertas SCADA). Toda la integración externa pasa por M-05 con TLS 1.3 y OAuth 2.0, sin acceso directo a las zonas internas.

---

## Resumen de diagramas

| # | Diagrama | Tipo Mermaid | Sección origen | Elementos clave |
|---|----------|:------------:|---------------|-----------------|
| 1 | Topología de red | `graph TD` | `03_03` | Anillo núcleo 10G, 3 niveles jerárquicos, 14 APs, 4 gNB |
| 2 | Ubicación física de equipos | `block-beta` | `03_02` + `03_03` | 5,000 m² en 7 zonas, posición de todos los equipos |
| 3 | Segmentación VLAN y QoS | `graph LR` | `03_03` | 8 VLANs, DSCP EF/AF/CS, zonas OT/IT/exterior |
| 4 | Redundancia de canales | `graph TD` | `03_03` | 4 niveles: RSTP + WAN dual + dual radio + SAI |
| 5 | V2X/V2I para AGV | `sequenceDiagram` | `03_03` + `03_04` | BSM / SPaT / ICA / MAP, latencia < 5 ms |
| 6 | Cobertura Wi-Fi | `graph TB` | `03_03` | 14 APs, 3 bandas, solapamiento 20 %, WPA3 |
| 7 | Sincronización PTP | `graph TD` | `03_03` | GM GPS → BC → TC → OC, precisión ±1 µs |
| 8 | Arquitectura del software | `graph LR` | `03_04` | 6 módulos, bus MQTT/REST/WS, 3 bases de datos |
| 9 | Flujo de datos | `flowchart TD` | `03_04` | Recepción → almacenamiento → picking → expedición |
| 10 | Integración de sistemas | `graph TB` | `03_04` + `03_05` | OT/IT/exterior, protocolos, VLANs, firewall |

---

## Referencias normativas de la sección

- **ГОСТ Р ИСО 15745-4-2010** — Topología Industrial Ethernet (D-01, D-10)
- **ГОСТ Р МЭК 61850-3** — Requisitos de disponibilidad de red (D-01, D-04)
- **ГОСТ Р 70982-2023** — V2X/V2I, mensajes BSM/SPaT/ICA/MAP (D-05)
- **ГОСТ Р МЭК 62443-3-3-2016** — Segmentación VLAN, zonas OT/IT, ciberseguridad (D-03, D-10)
- **IEEE 802.11ax** — Planificación de cobertura Wi-Fi 6/6E (D-06)
- **IEEE 1588-2019 (PTP v2.1)** — Jerarquía de sincronización GM/BC/TC/OC (D-07)
- **ГОСТ 7.32-2017** — Formato del documento de diseño técnico

---

## Checklist de la sección

- [x] D-01 Diagrama de topología de red (jerarquía 3 niveles + anillo núcleo, Mermaid graph TD)
- [x] D-02 Esquema de ubicación física de equipos en el plano (5,000 m², Mermaid block-beta)
- [x] D-03 Esquema de segmentación VLAN y QoS (8 VLANs + DSCP + zonas OT/IT, Mermaid graph LR)
- [x] D-04 Esquema de redundancia de canales (4 niveles: RSTP + WAN + dual radio + SAI, Mermaid graph TD)
- [x] D-05 Esquema V2X/V2I para AGV (BSM/SPaT/ICA/MAP + fases, Mermaid sequenceDiagram)
- [x] D-06 Esquema de cobertura Wi-Fi (14 APs + 3 bandas + solapamiento 20 %, Mermaid graph TB)
- [x] D-07 Esquema de sincronización PTP (GM → BC → TC → OC ±1 µs, Mermaid graph TD)
- [x] D-08 Diagrama de arquitectura del software (6 módulos + bus + datos + campo, Mermaid graph LR)
- [x] D-09 Diagrama de flujo de datos (recepción → almacenamiento → picking → expedición, Mermaid flowchart)
- [x] D-10 Diagrama de integración de sistemas (OT/IT/exterior + protocolos + VLANs, Mermaid graph TB)
- [x] Cada diagrama incluye: título, descripción, código Mermaid e interpretación
- [x] Tabla resumen de 10 diagramas con tipo Mermaid, sección origen y elementos clave
- [x] Referencias normativas de la sección
- [x] Coherencia visual con todas las secciones del diseño técnico (03_02 a 03_07)
