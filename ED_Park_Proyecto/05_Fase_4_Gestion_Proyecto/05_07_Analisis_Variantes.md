# 05_07 - Análisis de Variantes - Proyecto ED Park

## Objetivo de la sección

Analizar y comparar tres alternativas de solución técnico-económicas para la implementación del sistema completo del parque logístico ED Park, con el fin de recomendar la opción más adecuada para el cliente según su nivel de exigencia operativa, presupuesto disponible, plazo de ejecución y riesgo tecnológico. La variante recomendada debe equilibrar capacidad operativa, nivel de automatización, cobertura de telecomunicaciones, seguridad y rentabilidad del proyecto.

La presente sección se alinea con el Pasaporte del Proyecto (05_01), la estimación de recursos y presupuesto (05_04) y el cronograma general (05_03). El enfoque es realista, técnico y vendible para un cliente industrial que desea una solución viable sin sobre-invertir en capacidades no justificadas por su nivel actual de operación.

---

## 1. Variante básica

### 1.1 Descripción

La variante básica está orientada a una solución funcional, suficiente para operar un parque logístico con flujo de mercancías moderado, automatización media y conectividad estable, pero sin profundizar en la digitalización completa ni en la máxima capacidad de sincronización de procesos.

En esta opción se prioriza:
- infraestructura mínima pero robusta;
- redes Wi-Fi 6/6E y Ethernet industrial para operación segura;
- automatización ligera de AGV/AMR con alcance reducido;
- WMS básico con trazabilidad de inventario y recepciones;
- integración limitada con sistemas externos;
- menor nivel de redundancia y menos densidad de sensores IoT.

Es una solución adecuada para un cliente que quiere iniciar con una operación eficiente y escalable, sin entrar de forma inmediata en una automatización de alto costo.

### 1.2 Alcance

- Superficie operativa: 5,000 m² con una nave principal y una nave secundaria reducida
- 2-3 muelles de carga operativos
- 3-4 AGV/AMR máximo
- Wi-Fi industrial + Wi-Fi 6/6E en zonas críticas
- Ethernet industrial con redundancia simple
- WMS básico con recepción, almacenamiento, picking y expedición
- RFID parcial, sin integración completa con V2X/V2I
- Solución IoT limitada con sensores clave para temperatura, presencia y seguridad
- Red IP con seguridad mínima, pero suficiente según operación
- Montaje y puesta en servicio con pruebas funcionales básicas

### 1.3 Costo estimado

- Costo base estimado: 87,750,000 ₽
- Reserva de riesgos (25%): 21,937,500 ₽
- Presupuesto total estimado: 109,687,500 ₽

### 1.4 Plazo

- Duración estimada: 12-14 meses
- Actividades clave:
  - diseño y aprobación: 2-3 meses
  - instalación y montaje: 5-6 meses
  - pruebas y puesta en marcha: 2-3 meses
  - ajuste operativo: 1-2 meses

### 1.5 Ventajas

- Menor inversión inicial
- Menor carga financiera al cliente
- Implementación más rápida
- Adecuada para una operación logística con requerimientos no muy exigentes
- Menor complejidad de integración y mantenimiento
- Permite iniciar la operación con buen nivel de eficiencia

### 1.6 Desventajas

- Menor capacidad de crecimiento
- Limitaciones en automatización y velocidad operativa
- Menor nivel de supervisión en tiempo real
- Reducción de resiliencia frente a fallos de red o equipos
- Menos competitividad frente a clientes con exigencias más avanzadas
- Menor capacidad de soportar operación de alta densidad o multiproducto

---

## 2. Variante intermedia (recomendada)

### 2.1 Descripción

La variante intermedia es la solución recomendada para el cliente, porque combina una automatización funcional con una infraestructura tecnológica moderna y una buena relación costo-beneficio. Permite operar el parque con alta eficiencia, reduciendo errores, mejorando trazabilidad y ofreciendo espacio para crecimiento futuro sin imponer una inversión excesiva.

Esta variante incluye:
- infraestructura telecom completa según el Tema Nº 12;
- Wi-Fi 6/6E, redes LTE/5G privadas y Ethernet industrial robusto;
- WMS completo, SCADA, integración con AGV y supervisión central;
- 4 a 6 AGV/AMR;
- IoT detallado y sensores de seguridad en zonas críticas;
- redundancia de canales y control de sincronización PTP;
- V2X/V2I parcial con enfoque operativo realista.

Es la opción con mejor equilibrio entre tecnología, costo, complejidad y valor para el cliente.

### 2.2 Alcance

- Superficie completa de 5,000 m²
- 2 naves, oficinas, patio de maniobras, zona AGV y muelles de carga
- 4-6 AGV/AMR con carga variable
- Wi-Fi industrial + Wi-Fi 6/6E + LTE/5G privadas
- Ethernet industrial y redundancia con RSTP y enlaces duales
- WMS, SCADA, control de AGV, integración con ERP/TMS y UI
- Redes IoT para temperatura, presencia, puertas, incendio y localización
- Sistema de supervisión y trazabilidad integral
- V2X/V2I operativo en puntos críticos del patio y muelles
- Capacidad de expansión a 15-20% sin cambios mayores

### 2.3 Costo estimado

- Costo base estimado: 117,000,000 ₽
- Reserva de riesgos (30%): 35,100,000 ₽
- Presupuesto total estimado: 152,100,000 ₽

### 2.4 Plazo

- Duración estimada: 16-18 meses
- Fases:
  - diseño técnico y aprobación: 3-4 meses
  - adquisición y preparación: 3-4 meses
  - montaje e instalación: 5-6 meses
  - pruebas: 2-3 meses
  - puesta en marcha: 1-2 meses

### 2.5 Ventajas

- Mejora operativa real y visible en recepción, almacenamiento y expedición
- Mejor trazabilidad de inventario y reducción de errores
- Mayor automatización sin generar una inversión excesiva
- Redundancia y mayor disponibilidad del sistema
- Mayor capacidad de crecimiento y adaptación
- Mejor perfil para presentación al cliente y defensa académica
- Equilibrio óptimo entre riesgo, costo y beneficios

### 2.6 Desventajas

- Requiere mayor coordinación técnica y gestión de proveedores
- Mayor complejidad de integración entre sistemas
- Necesidad de contar con personal bien capacitado
- Coste más elevado que la variante básica
- Exige mayor control de riesgos y seguimiento de indicadores

---

## 3. Variante completa

### 3.1 Descripción

La variante completa representa la solución más avanzada y del más alto nivel tecnológico. Está diseñada para un parque logístico que requiere máxima automatización, alta disponibilidad y una infraestructura de telecomunicaciones de última generación.

Incluye:
- automatización total de procesos críticos;
- 6-8 AGV/AMR con control avanzado y movilidad coordinada;
- Wi-Fi 6/6E, LTE privado, 5G privado, mesh y V2X/V2I con máxima cobertura;
- WMS, SCADA, control de AGV, integración industrial profunda y alta seguridad cibernética;
- sensores IoT avanzados y análisis de datos en tiempo real;
- capacidades de expansión y evolución tecnológica con pocos límites.

Es una solución muy atractiva para un cliente con alta exigencia operativa y capacidad financiera, pero no siempre es la más prudente si la operación aún no necesita todo ese nivel.

### 3.2 Alcance

- Superficie completa con máxima capacidad operativa
- 6-8 AGV/AMR, integración completa de flujos de carga y movimiento
- Wi-Fi 6/6E + LTE privado + 5G privado + mesh + V2X/V2I completo
- Supervisión central de todos los procesos y zonas
- Sensores IoT de alta densidad y monitoreo continuo
- Red de telecomunicaciones con alta redundancia y QoS segmentado
- Integración profunda con ERP, TMS, WMS, sistemas de control y cliente
- Seguridad cibernética avanzada según nivel industrial
- Requerimientos de mantenimiento más elevados y mayor especialización

### 3.3 Costo estimado

- Costo base estimado: 146,250,000 ₽
- Reserva de riesgos (35%): 51,187,500 ₽
- Presupuesto total estimado: 197,437,500 ₽

### 3.4 Plazo

- Duración estimada: 20-22 meses
- Fases:
  - diseño formal y aprobación: 4-5 meses
  - adquisición y logística: 4-5 meses
  - montaje e instalación: 7-8 meses
  - pruebas avanzadas: 3-4 meses
  - puesta en marcha y ajuste: 2 meses

### 3.5 Ventajas

- Máxima automatización y rendimiento operativo
- Excelente nivel de trazabilidad, disponibilidad y control
- Solución muy competitiva para clientes con alto volumen de operación
- Preparación tecnológica para expansión futura
- Mejor nivel de seguridad y robustez operativa
- Excelente valor de presentación para escenarios avanzados

### 3.6 Desventajas

- Mayor inversión inicial y mayor riesgo financiero
- Requiere mayores recursos humanos, técnicos y de mantenimiento
- Complejidad de integración y operación más alta
- Tiempo de ejecución más largo
- Posible sobreinversión si el volumen operacional real no lo requiere
- Mayor exigencia en gestión de riesgos, control y soporte técnico

---

## 4. Tabla comparativa

| Criterio | Variante básica | Variante intermedia | Variante completa |
|---------|-----------------|--------------------|-------------------|
| Objetivo | Operación funcional y segura | Equilibrio técnico-económico | Máxima automatización y tecnología |
| Nivel de automatización | Baja a media | Media | Alta |
| Cantidad AGV/AMR | 2-4 | 4-6 | 6-8 |
| Telecomunicaciones | Wi-Fi + Ethernet básico | Wi-Fi + LTE/5G + Ethernet industrial | Wi-Fi + LTE + 5G + mesh + V2X/V2I completo |
| WMS / SCADA / Integración | Básico | Completo | Muy completo |
| Sensores IoT | Limitado | Adecuado | Alto |
| Redundancia | Simple | Media | Alta |
| Riesgo tecnológico | Medio | Medio | Alto |
| Tiempo estimado | 12-14 meses | 16-18 meses | 20-22 meses |
| Costo base | 87,750,000 ₽ | 117,000,000 ₽ | 146,250,000 ₽ |
| Reserva de riesgos | 25% | 30% | 35% |
| Presupuesto total | 109,687,500 ₽ | 152,100,000 ₽ | 197,437,500 ₽ |
| Adecuación para cliente | Inicio / operación menor | Solución equilibrada | Cliente exigente / alto volumen |
| Escalabilidad | Moderada | Buena | Excelente |
| Valor para el cliente | Bueno | Muy bueno | Excelente |

---

## 5. Recomendación con justificación

Se recomienda la variante intermedia como la solución óptima para el ED Park.

### Justificación

1. Equilibrio entre inversión y beneficio:
   - No es tan limitada como la variante básica, ni tan costosa como la completa.
   - Permite cubrir los requerimientos operativos reales del parque sin sobreinversión.

2. Adecuación al nivel de automatización previsto:
   - El proyecto contempla un nivel de automatización medio con 5-8 AGV/AMR, RFID, WMS, cintas básicas, control de flujo y supervisión.
   - La variante intermedia es coherente con este nivel y con la carga logística del entorno.

3. Mejor relación costo-beneficio:
   - Proporciona cobertura funcional de telecomunicaciones, redundancia y control operativo sin elevar el presupuesto a niveles difíciles de justificar para un parque de 0.5 ha.

4. Mayor capacidad de crecimiento:
   - Permite expansión futura sin cambiar completamente la arquitectura, lo que la hace más vendible para un cliente que quiere empezar con una plataforma sólida y escalable.

5. Menor riesgo operativo:
   - La variante completa puede generar complejidad técnica, coordinación, mantenimiento y riesgo financiero que exceden el nivel de operación planeado en este proyecto.

6. Coherencia con la propuesta académica:
   - El proyecto exige una solución realista, técnica, normativa y viable desde el punto de vista del cliente.
   - La variante intermedia es la más acreditada para defender con rigor técnico y económico.

### Conclusión
La variante intermedia es la más recomendable porque ofrece:
- tecnología suficiente para operar con eficiencia;
- buenos niveles de seguridad y redundancia;
- mejor relación costo/beneficio;
- capacidad de crecimiento;
- mayor plausibilidad para un cliente industrial real.

---

## 6. Checklist de la sección

- [x] Objetivo de la sección definido y alineado con el Pasaporte del Proyecto (05_01)
- [x] Descripción general de la variante básica
- [x] Alcance de la variante básica definido
- [x] Costo estimado de la variante básica establecido
- [x] Plazo de la variante básica estimado
- [x] Ventajas y desventajas de la variante básica registradas
- [x] Descripción general de la variante intermedia
- [x] Alcance de la variante intermedia definido
- [x] Costo estimado de la variante intermedia establecido
- [x] Plazo de la variante intermedia estimado
- [x] Ventajas y desventajas de la variante intermedia registradas
- [x] Descripción general de la variante completa
- [x] Alcance de la variante completa definido
- [x] Costo estimado de la variante completa establecido
- [x] Plazo de la variante completa estimado
- [x] Ventajas y desventajas de la variante completa registradas
- [x] Tabla comparativa elaborada
- [x] Recomendación técnica y económica incluida
- [x] Enfoque realista y vendible al cliente aplicado
- [x] Coherencia con presupuesto y cronograma del proyecto verificada
- [x] Documento completado según formato académico y de proyecto

---

*Documento generado como parte del análisis de alternativas del proyecto ED Park — Fase 4: Gestión del Proyecto.*