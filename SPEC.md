# SPEC.md — Especificación de Requisitos del Proyecto ED Park

## 🎯 Propósito

Este archivo define **qué debe construirse** en el proyecto ED Park, incluyendo requisitos funcionales, técnicos, normativos y criterios de aceptación. Complementa a `AGENT.md` (que define el rol y flujo de trabajo del agente) y a `PROMPTS.md` (que contiene los prompts por sección).

---

## 1. Visión general del proyecto

| Aspecto | Detalle |
|---------|---------|
| **Nombre** | Implementación del Proyecto de Automatización y Telecomunicaciones ED Park |
| **Objeto virtual** | ED Park |
| **Tipo** | Parque logístico de productos electrónicos |
| **Ubicación** | Matanzas, Cuba |
| **Superficie** | 0.5 ha (5,000 m²) |
| **Plazo** | 18 meses |
| **Presupuesto** | 117,000,000 ₽ (variante intermedia) |
| **Nivel de automatización** | Medio (5-8 AGV/AMR) |
| **Personal** | ~38 personas |

---

## 2. Alcance

### 2.1 Incluye

- Diseño de la infraestructura física (virtual)
- Diseño de la infraestructura de telecomunicaciones (17 tecnologías del Tema Nº 12)
- Diseño virtual del software de gestión
- Definición y selección de equipos (hardware)
- Planificación del montaje e instalación
- Planificación de la puesta en marcha
- Gestión del proyecto completa
- Análisis de variantes para el cliente
- Documentación según ГОСТ

### 2.2 NO incluye

- Construcción real del parque
- Compra real de equipos
- Programación real de software
- Integración real con sistemas externos
- Certificación oficial de sistemas
- Mantenimiento post-venta

---

## 3. Requisitos de telecomunicaciones (Tema Nº 12)

### 3.1 Tecnologías requeridas (17)

| # | Tecnología | Aplicación en ED Park | GOST |
|---|-----------|----------------------|------|
| 1 | Промышленный Wi-Fi | Cobertura en naves y patio | IEEE 802.11 |
| 2 | Wi-Fi 6/6E | Alta densidad de dispositivos | IEEE 802.11ax |
| 3 | Частные LTE-сети | Cobertura exterior | ГОСТ Р МЭК 61850-3 |
| 4 | Private 5G | Baja latencia para AGV | ГОСТ Р МЭК 61850-3 |
| 5 | Ethernet | Backbone cableado | IEEE 802.3 |
| 6 | Industrial Ethernet | Comunicación con PLCs | ГОСТ Р ИСО 15745-4-2010 |
| 7 | Mesh | Red de respaldo | IEEE 802.11s |
| 8 | IoT dedicado | Sensores temperatura/humedad | ГОСТ Р МЭК 62443 |
| 9 | Точки доступа | Distribución | IEEE 802.11 |
| 10 | Промышленные коммутаторы | Entornos duros | ГОСТ Р МЭК 61850-3 |
| 11 | Резервированные каналы | Redundancia | IEEE 802.1w |
| 12 | Серверы связи | WMS, control de flota | IEEE 802.3 |
| 13 | Шлюзы | Entre protocolos | ГОСТ Р МЭК 61131-1 |
| 14 | Edge-шлюзы | Procesamiento local | ГОСТ Р МЭК 62443 |
| 15 | PTP | Sincronización | IEEE 1588 |
| 16 | M2M | AGV ↔ AGV | ГОСТ Р 70982-2023 |
| 17 | V2X/V2I | Vehículos autónomos | ГОСТ Р 70982-2023 |

### 3.2 Requisitos de rendimiento

| Parámetro | Requisito |
|-----------|-----------|
| Latencia Wi-Fi | < 20 ms |
| Latencia 5G privado | < 10 ms |
| Cobertura Wi-Fi | 100% de naves y patio |
| Disponibilidad de red | 99.9% |
| Redundancia | < 1 s |
| Sincronización PTP | < 1 µs |
| Capacidad IoT | > 500 dispositivos |
| Ancho de banda backbone | > 10 Gbps |

### 3.3 Ciberseguridad

- Cumplimiento de ГОСТ Р МЭК 62443-3-3-2016
- Segmentación VLAN
- Cifrado de comunicaciones V2X
- Autenticación de dispositivos IoT
- Monitoreo de tráfico anómalo
- Plan de respuesta a incidentes

---

## 4. Requisitos de software (diseño virtual)

### 4.1 Módulos requeridos

| # | Módulo | Función |
|---|--------|---------|
| 1 | WMS | Gestión de almacén, inventario, pedidos |
| 2 | Control de AGV | Rutas, tráfico, carga |
| 3 | Integración V2X/V2I | Comunicación vehículo-infraestructura |
| 4 | SCADA | Monitoreo y control |
| 5 | Integración | Con ERP, TMS del cliente |
| 6 | Interfaz de usuario | Dashboard, operaciones, reportes |

### 4.2 Requisitos

- **NO** código real
- **SÍ** arquitectura, módulos, interfaces, flujos
- **SÍ** equipo de desarrollo, metodología, plazos
- **SÍ** costo estimado
- **SÍ** ciberseguridad

### 4.3 Equipo de desarrollo estimado

| Rol | Cantidad |
|-----|----------|
| Arquitecto de software | 1 |
| Desarrolladores backend | 3 |
| Desarrolladores frontend | 2 |
| Ingeniero de integración | 1 |
| QA / Tester | 2 |
| DevOps | 1 |
| **TOTAL** | **10** |

---

## 5. Requisitos de equipamiento

### 5.1 Telecom

| Equipo | Cantidad |
|--------|----------|
| Puntos de acceso Wi-Fi 6/6E | 12-16 |
| Switches industriales | 6-8 |
| Gateways | 3-4 |
| Edge-gateways | 4-6 |
| Servidores | 2-3 |
| RSU (V2X) | 4-6 |
| OBU (V2X) | 5-8 |
| PTP | 2 |
| LTE/5G privado | 1-2 |

### 5.2 Operación

| Equipo | Cantidad |
|--------|----------|
| AGV/AMR | 5-8 |
| Carretillas | 4 |
| Transpaletas | 4 |
| Cintas | 2-3 |
| RFID | 6-8 |
| Código de barras | 10-12 |
| Básculas | 3-4 |
| Sensores IoT | 50-100 |
| Servidores | 3-4 |
| Climatización | 4-6 |

### 5.3 Requisitos

- GOST aplicable a cada equipo
- Adecuados para entorno industrial
- Resistentes a condiciones de Cuba
- Compatibles entre sí
- Permitir expansión

---

## 6. Requisitos de montaje e instalación

### 6.1 Montaje

- Estanterías
- Cintas transportadoras
- Muelles
- Sensores
- AGV

### 6.2 Instalación

- Cableado
- Switches
- Puntos de acceso
- Gateways
- Servidores
- VLAN y QoS
- Redundancia
- Software

### 6.3 Puesta en marcha

- Cobertura Wi-Fi
- Latencia
- Redundancia
- V2X/V2I
- PTP
- Ciberseguridad
- Integración
- AGV
- Capacitación

---

## 7. Requisitos de gestión

### 7.1 Pasaporte

- Nombre
- Objetivos
- Alcance
- Stakeholders
- Criterios de éxito
- Restricciones
- Supuestos
- Exclusiones
- Entregables
- Hitos
- Presupuesto
- Plazo (18 meses)

### 7.2 WBS

- Nivel 1: Proyecto
- Nivel 2: Fases
- Nivel 3: Paquetes
- Nivel 4: Tareas
- Codificación WBS
- Diagrama Mermaid

### 7.3 Gantt

- Diagrama completo
- ID, nombre, duración
- Predecesoras
- Recursos
- Hitos
- Ruta crítica
- 18 meses

### 7.4 Recursos y presupuesto

- RRHH
- Materiales
- Costo base
- Reserva (30%)
- Precio costo
- Precio venta
- RACI
- Contratación
- Subcontratistas

### 7.5 Riesgos

- Técnicos
- Ciberseguridad
- Plazo
- Financieros
- Regulatorios
- Proveedores
- Matriz

### 7.6 Comunicación

- Plan
- KPIs
- Control
- Cambios
- Reuniones
- Reportes

### 7.7 Variantes

- Básica
- Intermedia
- Completa
- Comparación
- Recomendación

---

## 8. Requisitos de documentación

### 8.1 Formato

- ГОСТ 7.32-2017
- ГОСТ 7.1-2003
- PDF final
- Markdown trabajo

### 8.2 Estructura

01. Portada
02. Índice
03. Introducción
04. Descripción ED Park
05. Base normativa
06. Diseño técnico
07. Plan software
08. Plan montaje
09. Gestión
10. Conclusiones
11. Bibliografía
12. Anexos


### 8.3 Portada

- Título
- Estudiante
- Profesor
- Asignatura
- Institución
- Ciudad y año
- Firma profesor

### 8.4 Extensión

- 20-40 páginas
- Anexos ilimitados

### 8.5 Idioma

- Ruso o español
- GOST en ruso

---

## 9. Criterios de aceptación

### 9.1 Contenido

- [ ] Todos los `.md` generados
- [ ] GOST citados correctamente
- [ ] Trazabilidad completa
- [ ] 17 tecnologías cubiertas
- [ ] Software diseñado
- [ ] Montaje planificado
- [ ] Gestión completa
- [ ] Variantes incluidas
- [ ] ГОСТ 7.32-2017

### 9.2 Calidad

- [ ] Coherencia técnica
- [ ] Coherencia gestión
- [ ] Presupuesto realista
- [ ] Plazos realistas
- [ ] Riesgos mitigados
- [ ] Enfoque vendible

### 9.3 Formato

- [ ] Portada ГОСТ
- [ ] Índice
- [ ] Bibliografía ГОСТ
- [ ] PDF exportado
- [ ] 20-40 páginas

### 9.4 Presentación

- [ ] Slides
- [ ] Resumen oral
- [ ] Q&A
- [ ] Defensa ensayada

---

## 10. Restricciones

- **NO** código real
- **NO** construcción real
- **NO** compra real
- **NO** contratación real
- **NO** integración real
- **NO** certificación oficial
- **NO** > 40 páginas
- **NO** fuentes no confiables
- **NO** omitir GOST
- **NO** ignorar realismo

---

## 11. Validación

### 11.1 Por sección

Validación del usuario antes de continuar.

### 11.2 Por fase

Revisión de completitud, coherencia, GOST, calidad.

### 11.3 Final

Revisión completa, formato, bibliografía, anexos.

### 11.4 Profesor

Avances cada clase, retroalimentación, firma final.

---

## 12. Definición de "Done"

1. Todos los `.md` generados y validados.
2. PDF exportado.
3. Portada lista para firma.
4. Presentación preparada.
5. Checklist 100%.
6. Profesor firmó.
