# Fase 0 — Preparación y Encuadre del Proyecto ED Park

## Objetivo de la Sección

Esta fase establece los fundamentos del proyecto, confirmando el tema asignado, releyendo las indicaciones del profesor, definiendo el objeto virtual del proyecto, su alcance, stakeholders, ubicación, características técnicas y estructura física. Proporciona la base conceptual y organizativa para todo el trabajo posterior.

## 0.1 Confirmar tema Nº 12 asignado por sorteo

**Tema confirmado**: **Телекоммуникационная инфраструктура** (Nº 12)

El proyecto debe cubrir todos los aspectos del tema, aplicados al ED Park:

- Промышленный Wi-Fi — red inalámbrica local para entorno industrial
- Wi-Fi 6/6E — IEEE 802.11ax
- Частные LTE-сети — redes LTE privadas
- Private 5G — red corporativa 5G
- Ethernet — tecnología cableada
- Industrial Ethernet — Ethernet industrial determinista
- Беспроводные mesh-сети — redes mesh
- Выделенные сети IoT — redes IoT dedicadas
- Точки доступа — puntos de acceso
- Промышленные коммутаторы — switches industriales
- Резервированные каналы связи — canales redundantes
- Серверы связи — servidores de comunicación
- Шлюзы — gateways
- Edge-шлюзы — edge-gateways
- Системы синхронизации времени — sincronización de tiempo (PTP)
- Каналы связи между машинами — comunicación máquina a máquina (M2M)
- V2X/V2I — comunicación vehículo a todo / vehículo a infraestructura para AGV

## 0.2 Releer indicaciones del profesor

**Requisitos clave del profesor**:

1. **Proyecto virtual, no megagrande** — Enfoque en ED Park (0.5 ha) vs. proyectos masivos
2. **Con base normativa (GOST)** — Citación correcta y aplicación de estándares rusos
3. **Gestión de proyectos completa** — Desde pasaporte hasta defensa
4. **Entrega electrónica** — PDF recomendado + presentación oral + defensa ante el grupo
5. **Fecha de entrega**: Al final del semestre (fecha exacta por confirmar)
6. **Ambiente de defensa**: "tranquilo y familiar", pero con exigencia académica

## 0.3 Definir objeto virtual: ED Park

### 0.3.1 Nombre y tipo del objeto
- **Nombre**: **ED Park**
- **Tipo**: Parque logístico de productos electrónicos
- **Ubicación estratégica**: Matanzas, Cuba (cerca del Puerto de Matanzas) – punto clave para distribución logística regional

### 0.3.2 Características físicas
- **Superficie total**: **0.5 hectáreas (5,000 m²)**
- **Estructura física**: **2 naves** (principal + recepción/expedición) + oficinas, patio de maniobras, aparcamiento, zona AGV, área verde
- **Altura de naves**: Típicamente 6-8 metros para manutención de equipos electrónicos
- **Zonificación**: 
  - Zona A: Recepción y almacenamiento (400 m²)
  - Zona B: Procesamiento y picking (1,500 m²)
  - Zona C: Expedición y devoluciones (2,000 m²)
  - Zona D: Oficinas y apoyo (300 m²)
  - Zona E: Estacionamiento y maniobras (800 m²)

### 0.3.3 Características operativas
- **Mercancía**: Productos electrónicos (consumo, componentes, telecom, industrial)
- **Nivel de automatización**: **Medio** (5-8 AGV/AMR, RFID, WMS, cintas básicas)
- **Personal**: **~38 personas** distribuidas por turnos
- **Capacidad de muelles**: **4-6 muelles de carga**
- **Operaciones principales**: Recepción, almacenamiento, picking, expedición, devoluciones
- **Clientes**: Distribuidores, retailers, empresas de telecom, sector industrial

### 0.3.4 Justificación del objeto virtual
El ED Park representa un objeto de estudio óptimo porque:
- No es "megagrande" — manejable para análisis detallado
- Posee características tecnológicas realistas para parque logístico moderno
- Permite aplicación completa de todos los elementos del Tema Nº 12
- Combina automatización industrial con requisitos de telecomunicaciones avanzados
- Proporciona escenario realista para gestión de proyectos académica

## 0.4 Definir alcance del proyecto

### 0.4.1 Objetivo general
**Implementar una infraestructura de telecomunicaciones completa y moderna en ED Park** que soporte operaciones logísticas automatizadas con altos niveles de confiabilidad, seguridad y eficiencia, basada en estándares GOST e internacionales.

### 0.4.2 Objetivos específicos
1. **Diseñar red backbone** — Ethernet industrial determinista con redundancia
2. **Implementar redes inalámbricas** — Wi-Fi 6/6E industrial y redes LTE/5G privadas
3. **Configurar sistemas de sincronización** — PTP para coordinación precisa de AGV
4. **Establecer redes IoT** — Monitorización de ambiente y equipos
5. **Implementar infraestructura de seguridad** — Ciberseguridad industrial según GOST
6. **Desarrollar documentación de gestión de proyectos** — Pasaporte, WBS, Gantt, riesgos
7. **Preparar presentación** — Defensa ante grupo académico

### 0.4.3 Inclusiones
- Diseño técnico completo de todos los elementos del Tema Nº 12
- Aplicación de estándares GOST relevantes
- Documentación de gestión de proyectos (pasaporte, WBS, Gantt, recursos, riesgos)
- Esquemas y diagramas de topología
- Justificación normativa para cada equipo
- Checklist de progreso

### 0.4.4 Exclusiones
- Construcción de nuevas instalaciones (solo diseño de infraestructura existente)
- Adquisición real de equipos (solo lista de equipos y presupuestos)
- Implementación física (solo diseño y documentación)
- Aspectos legales/regulatorios más allá de los estándares técnicos GOST

## 0.5 Identificar stakeholders

| Stakeholder                         | Rol                 | Intereses                                            | Relevancia |
| ----------------------------------- | ------------------- | ---------------------------------------------------- | ---------- |
| **Profesor**                        | Evaluador académico | Rigor técnico, aplicación GOST, calidad del proyecto | Alta       |
| **Estudiantes del grupo**           | Público de defensa  | Entendibilidad, presentación clara, defensa sólida   | Media      |
| **Usuario final (ED Park)**         | Operador logístico  | Fiabilidad de red, eficiencia, seguridad, ROI        | Alta       |
| **Equipo técnico**                  | Diseñadores         | Estándares aplicables, viabilidad técnica            | Alta       |
| **Autoridades regulatorias**        | Cumplimiento GOST   | Aplicación correcta de estándares rusos              | Media      |
| **Proveedor de telecomunicaciones** | Futuro contratista  | Requisitos de red para licitación                    | Baja       |

### 0.5.1 Mapa de intereses
- **Profesor**: Busca aplicación correcta de GOST, metodología de gestión de proyectos, calidad técnica
- **Operador logístico**: Necesita red confiable que soporte operaciones 24/7
- **Estudiantes**: Aprendizaje de gestión de proyectos y telecomunicaciones industriales

## 0.6 Definir ubicación: Matanzas, Cuba

### 0.6.1 Confirmación geográfica
- **Ciudad**: Matanzas (provincia de Matanzas)
- **País**: Cuba
- **Ubicación estratégica**: Cerca del Puerto de Matanzas – puerto comercial importante en el Caribe

### 0.6.2 Consideraciones técnicas
- **Clima**: Tropical, alta humedad — requiere equipos resistentes a la corrosión
- **Sismicidad**: Baja a moderada — estándar sísmico cubano
- **Fuentes de energía**: Probable red eléctrica industrial trifásica 480V
- **Conectividad**: Acceso a fibra óptica regional, backhaul móvil disponible

### 0.6.3 Implicaciones para el diseño
- **Equipamiento**: Resistente a la humedad y salpicaduras (IP67/IP68)
- **Redundancia**: Considerar respaldo por generadores ante posibles cortes
- **Cobertura móvil**: Asegurar señal 4G/5G suficiente para AGV y IoT

## 0.7 Definir tipo de mercancía: productos electrónicos

### 0.7.1 Categorías de productos
1. **Electrónica de consumo** — Tablets, smartphones, dispositivos IoT
2. **Componentes electrónicos** — Semiconductores, circuitos impresos, sensores
3. **Equipos de telecomunicaciones** — Routers, switches, equipos de red
4. **Equipos industriales** — Controladores PLC, robots industriales, automatización

### 0.7.2 Requisitos logísticos específicos
- **Manipulación delicada** — Requiere AGV con control preciso de posición
- **Seguridad contra ESD** — Zonas con control de estática
- **Rastreabilidad** — RFID y sistemas WMS para lotes sensibles
- **Temperatura controlada** — Para componentes sensibles (20-25°C)

### 0.7.3 Implicaciones para telecomunicaciones
- **Ancho de banda alto** — Para transferencia de archivos grandes (PCB, equipos)
- **Latencia baja** — Para coordinación de AGV en tiempo real
- **Confiabilidad alta** — Para procesamiento de pedidos crítico
- **Cobertura uniforme** — Para toda la superficie del almacén

## 0.8 Definir nivel de automatización: medio

### 0.8.1 Características de automatización
- **AGV/AMR**: 5-8 unidades para transporte interno
- **Sistema WMS**: Gestión de almacén automatizada
- **RFID**: Rastreo en tiempo real de activos y mercancías
- **Cintas transportadoras**: Básicas, para rutas específicas
- **Picking**: Parcialmente automatizado (asistido por voz/pantalla)

### 0.8.2 Capacidad de red
- **Red backbone**: Gigabit Ethernet industrial para coordinación central
- **Red AGV**: Wi-Fi 6/6E para comunicación máquina a máquina (M2M)
- **IoT de sensores**: Red dedicada para monitorización ambiental
- **Redes privadas**: LTE/5G para aplicaciones críticas en tiempo real

### 0.8.3 Requisitos de sincronización de tiempo
- **PTP sincronizado**: Necesario para posicionamiento preciso de AGV (precisión sub-metro)
- **Sincronización de red**: Essential para operaciones coordinadas
- **Registro de tiempo**: Para auditoría y trazabilidad

## 0.9 Definir superficie: 0.5 ha (5,000 m²)

### 0.9.1 Distribución espacial
- **Total**: 5,000 m² construidos
- **Zonas operativas**:
  - Zona de recepción: 400 m²
  - Área de almacenamiento: 2,000 m²
  - Zona de picking: 1,500 m²
  - Área de expedición: 800 m²
  - Oficinas y apoyo: 300 m²

### 0.9.2 Requisitos de cobertura de red
- **Cobertura Wi-Fi**: Mínimo 95% en todas las zonas operativas
- **Capacidad AGV**: Soportar 8 vehículos simultáneos
- **Redundancia**: Canales múltiples por zona crítica
- **Escalabilidad**: Espacio para futuros 50% de expansión

### 0.9.3 Implicaciones de diseño
- **Puntos de acceso**: Distribuidos según densidad de uso
- **Switches industriales**: Ubicados en gabinetes de cableado estructurado
- **Sistemas de cableado**: Categoría 6A+ para backbones, fibra para distribución vertical

## 0.10 Definir estructura física (2 naves + oficinas + patio)

### 0.10.1 Componentes de la estructura
1. **Nave principal**: 2,500 m² — Área central de almacenamiento y procesamiento
2. **Nave secundaria**: 1,500 m² — Recepción y expedición
3. **Oficinas**: 300 m² — Administración y soporte técnico
4. **Patio de maniobras**: 500 m² — Estacionamiento y mantenimiento de AGV
5. **Zona verde**: 200 m² — Área de descanso y reunión

### 0.10.2 Detalles de diseño físico
- **Altura del techo**: 8 metros (nave principal), 6 metros (nave secundaria)
- **Iluminación**: LED industrial, regulable, con sensores de presencia
- **Sistemas de seguridad**: CCTV, control de acceso, alarma de incendios
- **Cableado estructurado**: En conductos separados por zona de riesgo
- **Estación meteorológica**: Para monitorización ambiental en sitio

### 0.10.3 Consideraciones de infraestructura
- **Agua**: Disponible para limpieza y sistemas de extinción de incendios
- **Drenaje**: Drenaje adecuado para equipos electrónicos
- **Acceso de carga**: 4 muelles de carga con gavetas clasificadoras
- **Estacionamiento**: 15 plazas para personal y visitantes

## Checklist de Tareas Completadas (Fase 0)

- [x] 0.1 Confirmar tema Nº 12 asignado por sorteo
- [x] 0.2 Releer indicaciones del profesor
- [x] 0.3 Definir objeto virtual: ED Park
- [x] 0.4 Definir alcance del proyecto
- [x] 0.5 Identificar stakeholders
- [x] 0.6 Definir ubicación: Matanzas, Cuba
- [x] 0.7 Definir tipo de mercancía: productos electrónicos
- [x] 0.8 Definir nivel de automatización: medio
- [x] 0.9 Definir superficie: 0.5 ha (5,000 m²)
- [x] 0.10 Definir estructura física (2 naves + oficinas + patio)

## Checklist de Tareas Pendientes (Fase 0)

- [ ] 0.11 Actualizar checklist principal con estado actual
- [ ] 0.12 Preparar presentación breve de resultados de la Fase 0
- [ ] 0.13 Revisar coherencia con Temas Nº 12 y requisitos del profesor

## Próximos Pasos

Fase 1 comenzará con la investigación normativa GOST, siguiendo el orden establecido en el checklist original:

1. [ ] Buscar ГОСТ Р ИСО 15745-4-2010 (Ethernet industrial)
2. [ ] Buscar ГОСТ Р МЭК 61850-3 (comunicaciones entornos duros)
3. [ ] Buscar ГОСТ Р 70982-2023 (V2X/V2I)
4. [ ] Buscar ГОСТ Р МЭК 62443-3-3-2016 (ciberseguridad industrial)
5. [ ] Buscar IEEE 802.11ax (Wi-Fi 6/6E)
6. [ ] Buscar IEEE 802.3 (Ethernet)
7. [ ] Buscar ГОСТ IEC 62026-3-2015 (DeviceNet) si aplica
8. [ ] Buscar IEEE 1588 (PTP) para sincronización de tiempo
9. [ ] Elaborar tabla de trazabilidad: cada equipo → su GOST
10. [ ] Redactar apartado "Base normativa del proyecto"

El usuario debe indicar qué sección desea generar a continuación.