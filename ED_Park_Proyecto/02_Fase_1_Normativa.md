# Fase 1 — Investigación normativa del proyecto ED Park

## Objetivo de la fase

La presente fase tiene como objetivo establecer la base normativa técnica y documental del proyecto ED Park, a partir de los requisitos del tema académico Nº 12: «Телекоммуникационная инфраструктура». En esta etapa se identifican, clasifican y justifican los estándares, normas profesionales y GOST que regulan la infraestructura industrial, la automatización, la ciberseguridad, la sincronización temporal, la integración de sistemas y la documentación técnica del proyecto.

El proyecto ED Park no es un sistema aislado de telecomunicaciones, sino un complejo logístico con telecom, software, hardware, montaje, puesta en marcha y gestión de proyecto. Por ello, la normativa de la fase 1 debe apoyar todo el ciclo de vida del objeto virtual: desde la infraestructura física y la red, hasta la automatización del almacén, la comunicación entre equipos, la seguridad del sistema y la preparación de la documentación del cliente.

## 1. Alcance normativo de la Fase 1

La base normativa del ED Park incluye los siguientes aspectos:

- industrial Ethernet y redes de comunicación entre equipos;
- Wi‑Fi industrial y redes inalámbricas para almacén y patio;
- sincronización temporal por PTP/IEEE 1588;
- seguridad de la infraestructura industrial (ciberseguridad OT/IT);
- interoperabilidad y arquitectura de automatización;
- integración de sistemas de gestión y control;
- telecontrol y automatización en entornos industriales;
- documentación y bibliografía según normas rusas;
- alineación con requisitos de un proyecto realista y vendible para cliente industrial.

---

## 2. Lista completa de GOST y estándares aplicables

| Nº  | Norma / estándar          | Título en ruso                                                                                                                                                                                                                                                                                        | Año                                                          | Secciones aplicables al proyecto                                                                                          | Por qué aplica al ED Park                                                                                                                                                           |
| --- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | ГОСТ Р ИСО 15745-4-2010   | Системы автоматизации производства и их интеграция. Профили. Часть 4. Профили систем управления на основе Ethernet                                                                                                                                                                                    | 2010                                                         | Arquitectura de red industrial, perfiles de interoperabilidad, integración de sistemas, interfaces de automatización      | El ED Park integra Wi‑Fi industrial, switches, AGV, WMS, sensores IoT y PLC; la norma aporta base para la interoperabilidad del Ethernet industrial y la integración de subsistemas |
| 2   | ГОСТ Р МЭК 61850-3        | Коммуникационные системы и сети в электроэнергетике. Часть 3. Общие требования к коммуникационным системам и сетям                                                                                                                                                                                    | 2010–2019 (Rusia, versión nacional del estándar IEC 61850-3) | Redes de comunicación industrial, equipos de automatización, interoperabilidad, confiabilidad y tolerancia a fallos       | Se usa como referencia para comunicaciones en entornos duros, redes resistentes y arquitecturas de control distribuido en áreas de logística automatizada                           |
| 3   | ГОСТ Р 70982-2023         | Безопасность дорожного движения. Системы связи и управления транспортными средствами. Взаимодействие транспортных средств и инфраструктуры                                                                                                                                                            | 2023                                                         | V2X/V2I, comunicación entre vehículos y infraestructura, control de AGV, seguridad de tráfico                             | El ED Park contempla AGV/AMR, control de movimiento, recorridos automatizados y comunicaciones con infraestructura de logística móvil                                               |
| 4   | ГОСТ Р МЭК 62443-3-3-2016 | Системы и меры по обеспечению кибербезопасности промышленных автоматизированных систем. Часть 3-3. Системные требования к безопасности                                                                                                                                                                | 2016                                                         | Segmentación de redes, control de acceso, gestión de riesgos cibernéticos, seguridad OT, zonas y niveles de seguridad     | Cualquier infraestructura industrial con Wi‑Fi, sensores, servidores, gateways y AGV requiere protección frente a ciberataques y acceso no autorizado                               |
| 5   | ГОСТ IEC 62026-3-2015     | Технологии связи для промышленных систем управления. Сети DeviceNet                                                                                                                                                                                                                                   | 2015                                                         | Bus de campo, dispositivos de automatización, integración de sensores y actuadores                                        | Si se requiere integración de dispositivos con buses de campo o automatización local, DeviceNet es una referencia para dispositivos de bajo nivel                                   |
| 6   | IEEE 802.11ax             | IEEE Standard for Information technology — Telecommunications and information exchange between systems — Local and metropolitan area networks — Specific requirements — Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications — Amendment 1: High Efficiency WLAN | 2019                                                         | Cobertura Wi‑Fi industrial, apuntamiento híbrido Wi‑Fi 6/6E, eficiencia espectral, densidad de usuarios, movilidad de AGV | El almacén y las áreas de patio requieren conectividad inalámbrica alta densidad, baja latencia y alta disponibilidad para móviles, sensores y terminales                           |
| 7   | IEEE 802.3                | IEEE Standard for Ethernet                                                                                                                                                                                                                                                                            | vigente                                                      | Ethernet industrial, switches, backbones, conectividad de servidores y equipos de red                                     | La infraestructura principal del ED Park se basa en Ethernet para la comunicación entre switches, controladores, gateways, servidores y equipos de automatización                   |
| 8   | IEEE 1588 (PTP)           | Precision Time Protocol (PTP)                                                                                                                                                                                                                                                                         | vigente                                                      | Sincronización de tiempo, sincronía de nodos, control industrial en tiempo real, logging y eventos                        | La red del parque requiere sincronización precisa para AGV, sensores, cámaras, controladores y trazabilidad de eventos operativos                                                   |
| 9   | ГОСТ Р МЭК 60870-5-104    | Системы дистанционного управления. Часть 5-104. Протокол передачи данных для телемеханики                                                                                                                                                                                                             | 2013–2019                                                    | Telecontrol, supervisión remota, SCADA, integración de sistemas de supervisión                                            | Si el proyecto incluye supervisión centralizada y telecontrol para infraestructura de logística o energía, se usa como referencia para intercambio de datos con centros de control  |
| 10  | ГОСТ Р МЭК 61131-1        | Программируемые контроллеры. Часть 1. Общие сведения и основные принципы                                                                                                                                                                                                                              | 2011–2014                                                    | Programación de PLC, lógica de control, secuencias de automatización, integración de controladores industriales           | Los AGV, cintas, sensores y sistemas de almacenamiento requieren lógica de control basada en PLC y automación secuencial                                                            |
| 11  | ГОСТ 7.32-2017            | Отчет о научно-исследовательской работе. Структура и правила оформления                                                                                                                                                                                                                               | 2017                                                         | Estructura del documento final, formato del reporte académico, secciones, orden, referencias                              | El proyecto se presenta como documento académico de maestría y debe seguir el formato del informe de investigación                                                                  |
| 12  | ГОСТ 7.1-2003             | Система стандартов по информации, библиотечному и издательскому делу. Библиографическая запись. Библиографическое описание                                                                                                                                                                            | 2003                                                         | Bibliografía, citas, referencias, referencias dentro del documento                                                        | El documento final debe incluir una bibliografía y citas formateadas según la normativa GOST rusa                                                                                   |

---

## 3. Análisis normativo por bloque del proyecto

### 3.1. Telecomunicaciones y Ethernet industrial

La infraestructura de telecomunicaciones del ED Park está basada en varios requisitos normativos:

- IEEE 802.3 regula la capa física y de enlace Ethernet para redes de área local de alta fiabilidad.
- ГОСТ Р ИСО 15745-4-2010 aporta la base para perfiles de automatización industrial con Ethernet.
- ГОСТ Р МЭК 61850-3 es referencia para comunicaciones robustas en entornos de automatización.

Esto aplica a los switches industriales, backbone, enlaces de acceso, servidores de comunicaciones, gateways y equipos de borde.

### 3.2. Wi‑Fi industrial y redes inalámbricas

Para el parque logístico se recomienda un diseño con:

- Wi‑Fi 6/6E según IEEE 802.11ax;
- cobertura en naves, patio de maniobras y muelles;
- capacidad para tráfico de AGV, terminales móviles, escáneres, RFID y sensores.

El estándar IEEE 802.11ax es especialmente pertinente por eficiencia, densidad de usuarios y soporte a entornos industriales con alta demanda.

### 3.3. Automatización, AGV, V2X y sincronización temporal

El ED Park contempla operación automatizada media con AGV/AMR. Para ello se usan:

- ГОСТ Р 70982-2023, que cubre interacción entre vehículos y infraestructura (V2X/V2I);
- IEEE 1588 (PTP), para sincronización precisa de equipos y eventos;
- ГОСТ Р МЭК 61131-1, para controladores lógicos programables en sistemas de automatización.

Esto permite coordinación entre vehículos, sensores, puertas, muelles, rutas, control del almacén y trazabilidad.

### 3.4. Ciberseguridad industrial

La infraestructura del parque integra redes IT y OT; por ello el componente de ciberseguridad es esencial.

- ГОСТ Р МЭК 62443-3-3-2016 define requisitos de seguridad para sistemas industriales.
- Debe aplicarse a VLAN, segmentación, autenticación, control de accesos, políticas de seguridad para gateways, servidores y dispositivos de borde.

### 3.5. Supervisión, telecontrol y integración

Si se usa supervisión centralizada de infraestructura y operación del almacén, se toma como referencia:

- ГОСТ Р МЭК 60870-5-104 para telecontrol y SCADA;
- ГОСТ IEC 62026-3-2015 si se trabaja con buses de campo DeviceNet o integración con dispositivos de automatización industrial.

### 3.6. Documentación académica y bibliográfica

Para el proyecto académico se aplican dos normas técnicas esenciales:

- ГОСТ 7.32-2017 para la estructura y composición del informe final;
- ГОСТ 7.1-2003 para las referencias bibliográficas y la forma de citación.

---

## 4. Formato de citación ГОСТ 7.1-2003

La citación bibliográfica del proyecto debe seguir el formato normativo del sistema GOST para bibliografía. El esquema general es el siguiente:

1. Autor(es).
2. Título del documento.
3. Tipo de documento (si corresponde).
4. Lugar de edición.
5. Editorial.
6. Año de edición.
7. Páginas o volumen.

### Ejemplo de citación general

ГОСТ Р ИСО 15745-4-2010. Системы автоматизации производства и их интеграция. Профили. Часть 4. Профили систем управления на основе Ethernet. — М.: Стандартинформ, 2010. — 48 с.

### Ejemplo de referencia en texto

[1] ГОСТ Р ИСО 15745-2010. Системы автоматизации производства и их интеграция. Профили. Часть 4. Профили систем управления на основе Ethernet. — М.: Стандартинформ, 2010.

### Recomendación para el proyecto

- Todas las normas deben presentarse en la bibliografía final en orden de aparición o alfabético según el criterio del autor.
- Los GOST que se citan en texto y en tablas deben estar en ruso, con número completo y año.
- Para referencias internacionales IEEE, además de la norma técnica, puede incluirse el nombre del estándar y la organización responsable.

---

## 5. Tabla de trazabilidad: equipo → GOST

La siguiente tabla presenta la relación entre los principales equipos y subsistemas del ED Park y los estándares que los respaldan.

| Equipo / subsistema                                | Descripción                                             | GOST / estándar principal                                      | Aplicación específica                                                            |
| -------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Routers y switches industriales                    | Conmutadores de núcleo y acceso para red de almacén     | IEEE 802.3; ГОСТ Р ИСО 15745-4-2010; ГОСТ Р МЭК 62443-3-3-2016 | Ethernet industrial, interoperabilidad, seguridad de la infraestructura          |
| APs Wi‑Fi 6/6E                                     | Puntos de acceso industriales para naves y patio        | IEEE 802.11ax; IEEE 802.3                                      | Cobertura inalámbrica, equilibrio de carga, conectividad para móviles y sensores |
| Red Wi‑Fi mesh / redes inalámbricas                | Cobertura de alta disponibilidad y redundancia          | IEEE 802.11ax; ГОСТ Р МЭК 62443-3-3-2016                       | Densidad de usuarios, continuidad de servicio, seguridad de acceso               |
| PLC y controladores de automación                  | Control de cintas, puertas, AGV, sensores               | ГОСТ Р МЭК 61131-1; ГОСТ Р МЭК 61850-3                         | Lógica de control, automatización y coordinación industrial                      |
| AGV / AMR                                          | Vehículos móviles automatizados para transporte interno | ГОСТ Р 70982-2023; IEEE 802.11ax; IEEE 1588                    | V2X/V2I, navegación, sincronización, comunicación móvil                          |
| RSU / OBU / infraestructura V2I                    | Equipos de comunicación con AGV                         | ГОСТ Р 70982-2023; IEEE 802.11ax                               | Interacción vehículo-infraestructura, control más seguro de rutas                |
| Servidores de la red y edge gateways               | Centros de datos locales de la infraestructura          | ГОСТ Р МЭК 62443-3-3-2016; ГОСТ Р МЭК 61850-3; IEEE 802.3      | Seguridad, integración, procesamiento local, reducción de latencia               |
| Sensores de temperatura, humedad, movimiento e IoT | Monitoreo del entorno y procesos                        | ГОСТ IEC 62026-3-2015; ГОСТ Р МЭК 62443-3-3-2016               | Integración de dispositivos y seguridad de extremo                               |
| Dispositivos de automatización de campo            | Sensores, actuadores y dispositivos de baja capa        | ГОСТ IEC 62026-3-2015; ГОСТ Р ИСО 15745-4-2010                 | Interoperabilidad de periféricos industriales                                    |
| Sistema SCADA / telecontrol                        | Monitoreo y control de operación                        | ГОСТ Р МЭК 60870-5-104; ГОСТ Р МЭК 61850-3                     | Supervisión central, telecontrol y gestión remota                                |
| Sistemas de sincronización temporal                | PTP, relojes maestros y nodos de red                    | IEEE 1588; ГОСТ Р МЭК 61850-3                                  | Timestamps, coordinación y sincronización de eventos                             |
| Red de seguridad y segmentación VLAN               | Separación entre IT y OT                                | ГОСТ Р МЭК 62443-3-3-2016; IEEE 802.3                          | Zonas funcionales, políticas de acceso, prevención de amenazas                   |
| Documentación técnica y bibliográfica              | Informes, planos, referencias y ajustes del proyecto    | ГОСТ 7.32-2017; ГОСТ 7.1-2003                                  | Estructura documental y citación del proyecto                                    |

### Trazabilidad por bloques funcionales

| Bloque funcional             | Equipo clave                      | Norma principal                           | Justificación                             |
| ---------------------------- | --------------------------------- | ----------------------------------------- | ----------------------------------------- |
| Red de transporte            | Switches, fibra, enlaces Ethernet | IEEE 802.3; ГОСТ Р ИСО 15745-4-2010       | Base de la infraestructura operativa      |
| Red inalámbrica              | APs, mesh, equipos móviles        | IEEE 802.11ax                             | Conectividad móvil y alta densidad        |
| Automatización               | PLC, sensores, actuadores         | ГОСТ Р МЭК 61131-1; ГОСТ IEC 62026-3-2015 | Control de procesos y campos industriales |
| AGV / logística automatizada | Vehículos y infraestructura V2I   | ГОСТ Р 70982-2023; IEEE 1588              | Coordinación y seguridad en movimiento    |
| Ciberseguridad               | Firewalls, segmentación, gateways | ГОСТ Р МЭК 62443-3-3-2016                 | Defensa y resiliencia del sistema         |
| Supervisión                  | SCADA, telecontrol                | ГОСТ Р МЭК 60870-5-104                    | Monitoreo operativo y gestión remota      |
| Documentación                | Informe final y bibliografía      | ГОСТ 7.32-2017; ГОСТ 7.1-2003             | Presentación académica y formalización    |

---

## 6. Relevancia de los GOST para el proyecto ED Park

Los estándares incluidos en esta fase no tienen un carácter meramente formal; forman la base técnica del diseño del ED Park. Su uso está justificado porque el proyecto contempla:

- automatización industrial y gestión de flujo en almacén;
- diferentes tipos de conectividad (wired, wireless, industrial Ethernet, red móvil);
- dos o más capas de control y supervisión;
- necesidad de seguridad, trazabilidad y sincronización real;
- uso de equipos de campo, sensores y vehículos automatizados;
- necesidad de documentación formal y bibliográfica según GOST.

Esto permite que la solución propuesta no sea una red teórica aislada, sino un sistema industrial realista, funcional y posible de vender a un cliente con necesidades logísticas y de automatización.

---

## 7. Checklist de la fase

### Checklist de trabajo de la fase 1

- [x] Definir objetivo y alcance de la fase de investigación normativa
- [x] Identificar los estándares clave del proyecto ED Park
- [x] Incluir ГОСТ Р ИСО 15745-4-2010
- [x] Incluir ГОСТ Р МЭК 61850-3
- [x] Incluir ГОСТ Р 70982-2023
- [x] Incluir ГОСТ Р МЭК 62443-3-3-2016
- [x] Incluir ГОСТ IEC 62026-3-2015
- [x] Incluir IEEE 802.11ax
- [x] Incluir IEEE 802.3
- [x] Incluir IEEE 1588 (PTP)
- [x] Incluir ГОСТ Р МЭК 60870-5-104
- [x] Incluir ГОСТ Р МЭК 61131-1
- [x] Incluir ГОСТ 7.32-2017
- [x] Incluir ГОСТ 7.1-2003
- [x] Preparar tabla de análisis de GOST por estándar
- [x] Definir formato de citación bibliográfica según ГОСТ 7.1-2003
- [x] Elaborar tabla de trazabilidad equipo → GOST
- [x] Redactar la justificación técnica de cada estándar para ED Park
- [x] Cerrar la fase con un esquema de trabajo y una base documental coherente

### Checklist de validación del documento

- [x] Título y objetivo definidos
- [x] Tabla completa de normas incluida
- [x] Títulos en ruso presentados para los GOST
- [x] Año de cada estándar indicado
- [x] Relación con el proyecto ED Park explicada
- [x] Formato de citación de GOST 7.1-2003 incluido
- [x] Trazabilidad equipo → GOST incluida
- [x] Checklist de la fase finalizado

---

## 8. Conclusión de la Fase 1

La Fase 1 establece la base regulatoria y técnica del proyecto ED Park. Los estándares seleccionados permiten asegurar que el sistema propuesto sea compatible con buenas prácticas de automatización industrial, telecomunicaciones, ciberseguridad, sincronización temporal y gestión documental. Con esta base, el proyecto puede pasar a la siguiente fase de diseño técnico, donde se asignarán los equipos, se diseñará la topología de red y se definirá la arquitectura funcional del ED Park.

## Referencias de la fase

- ГОСТ 7.32-2017. Отчет о научно-исследовательской работе. Структура и правила оформления. — М.: Стандартинформ, 2017.
- ГОСТ 7.1-2003. Система стандартов по информации, библиотечному и издательскому делу. Библиографическая запись. Библиографическое описание. — М.: Издательство стандартов, 2003.
- ГОСТ Р ИСО 15745-4-2010. Системы автоматизации производства и их интеграция. Профили. Часть 4. Профили систем управления на основе Ethernet. — М.: Стандартинформ, 2010.
- ГОСТ Р МЭК 62443-3-3-2016. Системы и меры по обеспечению кибербезопасности промышленных автоматизированных систем. Часть 3-3. Системные требования к безопасности. — М.: Стандартинформ, 2016.
- IEEE 802.11ax. Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications. — IEEE, 2019.
- IEEE 802.3. Ethernet Standard. — IEEE, edición vigente.
- IEEE 1588. Precision Time Protocol (PTP). — IEEE, edición vigente.
- ГОСТ Р МЭК 61131-1. Программируемые контроллеры. Часть 1. Общие сведения и основные принципы. — М.: Стандартинформ, 2011.
- ГОСТ Р 70982-2023. Безопасность дорожного движения. Системы связи и управления транспортными средствами. Взаимодействие транспортных средств и инфраструктуры. — М.: Стандартинформ, 2023.

