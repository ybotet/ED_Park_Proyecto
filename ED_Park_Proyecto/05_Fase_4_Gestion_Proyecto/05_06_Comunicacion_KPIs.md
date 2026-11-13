# 05_06 - Plan de Comunicación y Seguimiento - Proyecto ED Park

## Objetivo de la sección

Definir el plan de comunicación del proyecto ED Park, establecer los KPIs de seguimiento y control de avance, el método de control de avance (Earned Value), la gestión de cambios y los reportes de avance. Todo coherente con el Pasaporte del Proyecto (05_01), WBS (05_02), Gantt (05_03), Recursos/Presupuesto (05_04) y Riesgos (05_05).

---

## 1. Plan de comunicación

### 1.1 Principios de comunicación

| Principio | Descripción |
|-----------|-------------|
| **Transparencia** | Información veraz, oportuna y accesible a todos los stakeholders según su nivel de autorización |
| **Regularidad** | Cadencia fija de reportes y reuniones (ver calendario 1.3) |
| **Relevancia** | Cada stakeholder recibe información pertinente a su rol e interés (matriz 1.2) |
| **Trazabilidad** | Todas las comunicaciones formales registradas en repositorio del proyecto (SharePoint/Confluence) |
| **Escalamiento** | Rutas claras para decisiones que exceden autoridad del PM (ver 1.4) |

### 1.2 Matriz de comunicación por stakeholder

| Stakeholder | Interés principal | Información que recibe | Formato | Frecuencia | Responsable envío | Canal |
|:------------|:------------------|:----------------------|:--------|:----------:|:-----------------:|:-----:|
| **Cliente / Propietario** | ROI, hitos, presupuesto, riesgos críticos | Reporte ejecutivo, dashboard KPIs, actas comité dirección, solicitudes de decisión | PDF + PPT (10 slides) | Quincenal + hitos | PM | Email + Reunión virtual/presencial |
| **Director del proyecto (PM)** | Control total, desviaciones, recursos, riesgos | Todos los reportes, backlog cambios, registro riesgos, EVM | Dashboard tiempo real + Excel | Diario (dashboard) / Semanal (detalle) | PMO | Jira/Confluence + Teams |
| **Comité de dirección (Cliente + PM + Director técnico)** | Decisiones estratégicas, aprobación cambios > 1M ₽, riesgos Alto/Crítico | Paquete pre-comité: dashboard, RFCs, estado reserva, top 5 riesgos | PDF (20 páginas) | Quincenal (miércoles) | PM | Reunión 90 min + Teams |
| **Equipo técnico (Ingenieros, Desarrolladores, Integrador)** | Especificaciones, avances técnicos, bloqueos, pruebas | Daily standup notes, sprint review, informes PT, especificaciones técnicas | Markdown + Mermaid | Diario (standup) / Sprint (2 sem) | Scrum Master / TL | Jira + Confluence + Teams |
| **Subcontratistas (Civil, Eléctrico/HVAC, AGV, Seguridad)** | Alcance, plazos, pagos, ITP, no conformidades | Órdenes de trabajo, ITP, actas inspección, certificados pago, cambios alcance | PDF firmado | Según hito + semanal | PM + Ingeniero responsable | Email + Procore/SharePoint |
| **Proveedores críticos (AGV, Telecom, SAI)** | Entregas, especificaciones, pruebas FAT/SAT, garantías | Pedidos, specs técnicas, plan de pruebas, actas recepción | PDF + Excel | Según hito de entrega | Compras + Ingeniero responsable | Email + Portal proveedor |
| **Evaluador académico (Profesor)** | Coherencia técnica, GOST, formato, defensa | Avances por clase (simulados), documento final PDF, presentación | PDF (GOST 7.32-2017) | Según calendario académico | PM (como alumno) | Entrega presencial/virtual |
| **Personal operativo (Operarios, Técnicos mantenimiento)** | Formación, manuales, procedimientos, soporte | Plan capacitación, manuales usuario, guías rápido, canal soporte | PDF + Video + Presencial | Fases 1.5–1.6 | Formador + RRHH | Aula + LMS + WhatsApp grupo |
| **Autoridades (Aduanas, MINCOM, ONIT)** | Cumplimiento normativo, documentación técnica | Solicitudes homologación, certificados, declaraciones, planos | PDF oficial + papel | Según trámite | Gestor administrativo | Ventanilla única / Email certificado |
| **Comunidad local / Sindicatos** | Impacto ambiental, empleo, seguridad | Estudio impacto ambiental (resumen), plan seguridad, noticias proyecto | PDF + Carteleria | Hitos públicos | RRHH + Coordinador seguridad | Tablón anuncios + Web municipal |

### 1.3 Calendario de comunicaciones regulares

| Reunión / Reporte | Frecuencia | Día/Hora | Duración | Participantes obligatorios | Entradas | Salidas |
|-------------------|:----------:|:--------:|:--------:|:--------------------------:|:--------:|:-------:|
| **Daily Standup (equipo técnico)** | Diaria (lunes–viernes) | 09:00 | 15 min | Scrum Master, Devs, Ingenieros, Integrador | Tablero Jira, bloqueos | Compromisos día, impedimentos |
| **Reunión semanal PM + TLs** | Semanal | Lunes 10:00 | 60 min | PM, TL Software, TL Telecom, TL Montaje, TL Instalación, Scrum Master | Avance semanal, riesgos nuevos, RFCs pendientes | Decisiones, acciones, actualización Gantt |
| **Comité de dirección (Steering Committee)** | Quincenal | Miércoles 11:00 | 90 min | Cliente (Director ops), PM, Director técnico, Financiero cliente, PMO | Paquete pre-comité (ver 1.2) | Acta con decisiones, RFCs aprobados/rechazados, escalamientos |
| **Reporte ejecutivo cliente** | Quincenal | Viernes 17:00 | — | Cliente (Propietario + Director ops) | Dashboard KPIs, top 5 riesgos, hitos próximos, presupuesto | PDF 5 páginas + dashboard adjunto |
| **Revisión técnica riesgos telecom** | Mensual | 1er martes 15:00 | 60 min | Ingeniero sistemas, Especialista AGV, Proveedor AGV, Integrador | Logs red, site surveys, PT results, KRI telecom | Acciones correctivas, actualización registro riesgos |
| **Revisión ciberseguridad** | Mensual | 2º martes 15:00 | 60 min | Especialista ciberseguridad, CISO cliente, Auditor (si aplica) | Escaneos, SIEM alerts, incidentes, parches | Plan parches, reglas firewall, matriz amenazas actualizada |
| **Sprint Review (Software)** | Cada 2 semanas | Viernes sprint 10:00 | 90 min | PO (PM), Scrum Master, Devs, Stakeholders técnicos | Demo funcional, métricas sprint, backlog refinado | Feedback, aceptación historias, ajustes backlog |
| **Sprint Retrospective** | Cada 2 semanas | Viernes sprint 12:00 | 45 min | Scrum Master, Devs | Métricas flujo, impedimentos, bienestar equipo | 3 mejoras accionables para siguiente sprint |
| **Inspección ITP (Subcontratistas)** | Según plan ITP | Según obra | 30–120 min | Ingeniero responsable, Subcontratista, PM (opcional) | ITP, planos, specs, certificados materiales | Acta inspección (Aprobado / Condicional / Rechazado) |
| **Clase académica (simulada)** | Según calendario | — | 120 min | Profesor, PM (alumno) | Avance fase correspondiente | Feedback profesor, nota parcial |

### 1.4 Escalamiento y autoridad de decisión

| Nivel | Autoridad | Límite económico | Límite plazo | Límite técnico | Ejemplos |
|:-----:|:---------:|:----------------:|:------------:|:--------------:|:---------|
| **Nivel 1 — PM** | Project Manager | ≤ 500,000 ₽ | ≤ 5 días | Cambios dentro de especificación aprobada | Reasignación recursos internos, ajuste prioridades sprint, compra materiales menor |
| **Nivel 2 — Comité Dirección** | PM + Cliente + Director técnico | 500,000 – 5,000,000 ₽ | 5–15 días | Cambios de especificación menor | RFC alcance moderado, cambio proveedor, uso reserva riesgos ≤ 1M ₽ |
| **Nivel 3 — Cliente / Propietario** | Representante legal cliente | > 5,000,000 ₽ | > 15 días | Cambios de arquitectura, exclusiones alcance | Cambio variante, aumento presupuesto, extensión plazo, exclusión hito |
| **Nivel 4 — Evaluador académico** | Profesor (solo ámbito académico) | — | — | Formato, coherencia GOST, defensa | Aprobación documento final, formato presentación, criterios evaluación |

**Proceso de escalamiento (RFC - Request for Change):**
1. **Origen**: Cualquier stakeholder detecta necesidad de cambio → completa formulario RFC en Jira/Confluence
2. **Análisis técnico (48 h)**: TL responsable evalúa impacto en coste, plazo, calidad, riesgos → informe técnico
3. **Análisis económico (24 h)**: PMO evalúa impacto presupuesto, flujo caja, reserva riesgos
4. **Decisión**: Según nivel de autoridad (tabla arriba) → Aprobado / Rechazado / Requiere más info
5. **Implementación**: Si aprobado → actualización WBS, Gantt, presupuesto, baseline, comunicación a afectados
6. **Cierre**: Verificación efectividad → lección aprendida

---

## 2. KPIs de seguimiento (Key Performance Indicators)

### 2.1 KPIs de proyecto (nivel macro)

| KPI | Fórmula | Meta | Frecuencia | Fuente datos | Responsable | Umbral ámbar | Umbral rojo |
|:----|:--------|:----:|:----------:|:------------:|:-----------:|:------------:|:-----------:|
| **SPI (Schedule Performance Index)** | EV / PV | ≥ 1.0 | Quincenal | MS Project / Primavera / Excel EVM | PMO | 0.90–1.0 | < 0.90 |
| **CPI (Cost Performance Index)** | EV / AC | ≥ 1.0 | Quincenal | Contabilidad + EVM | PMO | 0.90–1.0 | < 0.90 |
| **% Hitos cumplidos a tiempo** | Hitos a tiempo / Hitos planificados | 100 % | Mensual | Gantt + Actas hitos | PM | 80–99 % | < 80 % |
| **Desviación presupuesto acumulada** | (AC − PV) / PV × 100 | ≤ 5 % | Quincenal | Contabilidad + EVM | PMO | 5–10 % | > 10 % |
| **Reserva riesgos disponible** | Reserva no comprometida / Reserva total | ≥ 30 % | Quincenal | Registro RFCs + Contabilidad | PM | 20–30 % | < 20 % |
| **Riesgos Alto/Críticos abiertos** | Conteo riesgos nivel ≥ 13 sin mitigación efectiva | 0 | Quincenal | Registro riesgos | PM + Especialista riesgos | 1–2 | > 2 |
| **Calidad entregables (tasa rechazo)** | Entregables rechazados / Entregables presentados | ≤ 5 % | Por hito | Actas revisión / QA | QA Lead | 5–10 % | > 10 % |

### 2.2 KPIs técnicos (telecomunicaciones y automatización)

| KPI | Fórmula | Meta | Frecuencia | Fuente | Responsable | Umbral ámbar | Umbral rojo |
|:----|:--------|:----:|:----------:|:------:|:-----------:|:------------:|:-----------:|
| **Cobertura Wi-Fi (RSSI medio zona A)** | Promedio RSSI 50 puntos medición | ≥ −65 dBm | Semanal (instalación) / Mensual (ops) | Ekahau / NetAlly | Ingeniero sistemas | −65 a −75 dBm | < −75 dBm |
| **Latencia VLAN 10 AGV (P99)** | Percentil 99 latencia ping 64 bytes | < 5 ms | Continuo (SCADA) | Grafana / InfluxDB | Ingeniero sistemas | 5–10 ms | > 10 ms |
| **Jitter VLAN 10** | Desviación estándar latencia | < 1 ms | Continuo | Grafana | Ingeniero sistemas | 1–2 ms | > 2 ms |
| **Disponibilidad red backbone** | Uptime % (excl. ventanas mantenimiento) | ≥ 99.9 % | Mensual | Zabbix / PRTG | Ingeniero sistemas | 99.5–99.9 % | < 99.5 % |
| **Convergencia RSTP** | Tiempo failover anillo núcleo | < 50 ms | Mensual (prueba) | Captura Wireshark | Ingeniero sistemas | 50–100 ms | > 100 ms |
| **PTP offset máximo** | |offset| máx nodos finales | ≤ ±1 µs | Continuo | PTPd / LinuxPTP | Ingeniero sistemas | ±1–10 µs | > 10 µs |
| **V2X PER (Packet Error Rate)** | Paquetes BSM/ICA perdidos / totales | < 1 % | Continuo (AGV) | Logs OBU/RSU | Especialista AGV | 1–5 % | > 5 % |
| **Latencia ICA (Intersection Collision Avoidance)** | P99 tiempo recepción→reacción AGV | < 5 ms | Continuo (pruebas) | Logs AGV + RSU | Especialista AGV | 5–10 ms | > 10 ms |
| **Tasa éxito misiones AGV** | Misiones completadas / Misiones asignadas | ≥ 95 % | Diario (ops) | WMS + Fleet Manager | Especialista AGV | 90–95 % | < 90 % |
| **Tiempo medio entre fallos (MTBF) AGV** | Horas operativas / Nº fallos | ≥ 500 h | Mensual | CMMS / Fleet Manager | Especialista AGV | 300–500 h | < 300 h |

### 2.3 KPIs de software (desarrollo virtual)

| KPI | Fórmula | Meta | Frecuencia | Fuente | Responsable |
|:----|:--------|:----:|:----------:|:------:|:-----------:|
| **Velocity (puntos/sprint)** | Σ Story Points Done / Sprint | Estable ±15 % | Sprint (2 sem) | Jira | Scrum Master |
| **Sprint Burndown** | Puntos restantes vs día sprint | Tendencia a 0 día 10 | Diario | Jira | Scrum Master |
| **Defect Escape Rate** | Bugs producción / Total bugs | ≤ 5 % | Sprint | Jira + SonarQube | QA Lead |
| **Cobertura pruebas unitarias** | Líneas cubiertas / Líneas totales | ≥ 80 % | Sprint | SonarQube | Dev Lead |
| **Deuda técnica (Technical Debt Ratio)** | Coste refactor / Coste desarrollo | ≤ 5 % | Sprint | SonarQube | Dev Lead |
| **Lead Time (Idea → Producción)** | Días desde backlog ready → Done | ≤ 30 días | Mensual | Jira | PM |

### 2.4 KPIs de montaje e instalación

| KPI | Fórmula | Meta | Frecuencia | Fuente | Responsable |
|:----|:--------|:----:|:----------:|:------:|:-----------:|
| **% Avance físico vs plan** | Valor ganado físico / Planificado | SPI ≥ 1.0 | Semanal | ITP + Actas | Ingeniero montaje |
| **No conformidades abiertas > 5 días** | Conteo NC sin cerrar > 5 días | 0 | Semanal | Registro NC | Coordinador calidad |
| **Seguridad: Incidentes LTI** | Lost Time Injuries / 200,000 h | 0 | Mensual | Parte accidentes | Coordinador seguridad |
| **Inspecciones ITP aprobadas 1ª vez** | Aprobadas 1ª / Totales inspeccionadas | ≥ 90 % | Por inspección | Actas ITP | Ingeniero responsable |

---

## 3. Método de control de avance: Earned Value Management (EVM)

### 3.1 Fundamentos aplicados al ED Park

El proyecto utiliza **EVM simplificado** con baseline de coste y plazo aprobados en el Pasaporte (05_01) y WBS (05_02). Se calcula a nivel de **Paquete de Trabajo (Nivel 3 WBS)**.

| Concepto | Definición ED Park | Cálculo |
|----------|-------------------|---------|
| **PV (Planned Value)** | Coste planificado del trabajo programado hasta la fecha | Σ (Presupuesto paquete × % planificado temporal) |
| **EV (Earned Value)** | Coste presupuestado del trabajo realmente completado | Σ (Presupuesto paquete × % avance físico real) |
| **AC (Actual Cost)** | Coste real incurrido en el trabajo completado | Σ Facturas pagadas + Costes internos imputados |
| **BAC (Budget at Completion)** | Presupuesto total aprobado (costo base) | 90,000,000 ₽ (variante intermedia) |
| **EAC (Estimate at Completion)** | Estimación del coste final al terminar | AC + (BAC − EV) / CPI (si CPI estable) |
| **ETC (Estimate to Complete)** | Coste estimado para terminar el trabajo restante | EAC − AC |
| **VAC (Variance at Completion)** | Desviación estimada al final | BAC − EAC |

### 3.2 Reglas de medición de % avance físico (por tipo de paquete)

| Tipo de paquete | Método % avance | Evidencia |
|-----------------|-----------------|-----------|
| **Ingeniería/Diseño** | Hitos de entregables: 0 % / 25 % (borrador) / 50 % (revisado) / 75 % (aprobado cliente) / 100 % (baseline) | PDF firmado en Confluence |
| **Adquisición/Compras** | 0 % / 20 % (PO emitida) / 50 % (en tránsito) / 80 % (recibido almacén) / 100 % (verificado + almacenado) | PO, Albarán, Acta recepción |
| **Obra civil/Montaje** | Medición física in situ (m³ hormigón, m² estantería, uds. equipos) vs BOQ | Topografía, Actas ITP, Fotos georreferenciadas |
| **Instalación telecom** | Por hito: Cableado certificado / Switch configurado / AP montado y asociado / VLAN activa / Servicio probado | Fluke cert, Config backup, Heatmap, Ping test |
| **Software (virtual)** | Story Points Done / Story Points Sprint + % épicas completadas | Jira Sprint Report + Demo grabada |
| **Pruebas/Comisionado** | Casos de prueba passed / Total casos planificados por bloque PT | TestRail / Zephyr + Informe firmado |

### 3.3 Reporting EVM (Dashboard quincenal)

| Métrica | Visualización | Alerta si |
|---------|---------------|-----------|
| **SPI / CPI** | Gauge verde/ámbar/rojo + tendencia 6 periodos | SPI < 0.90 ó CPI < 0.90 |
| **EV vs PV vs AC** | Gráfico líneas acumuladas (S-curve) | AC > PV + 10 % ó EV < PV − 10 % |
| **EAC vs BAC** | Barra comparativa + VAC | VAC < −5 % BAC |
| **Burn rate reserva riesgos** | Barra % consumida + comprometida | > 70 % consumida antes Mes 12 |
| **Top 5 desviaciones WBS** | Tabla: Paquete, PV, EV, AC, SV, CV, % avance | CV < −10 % ó SV < −10 % |

### 3.4 Baseline y control de cambios en EVM

- **Baseline 0**: Aprobado en hito M-02 (Mes 3) — coste 90M ₽, plazo 18 meses
- **Cambios de baseline**: Solo vía RFC aprobado por Comité Dirección (Nivel 2) o Cliente (Nivel 3)
- **Re-baseline**: Si VAC > 10 % BAC ó retraso > 20 días en ruta crítica → nuevo baseline documentado
- **Histórico**: Todas las versiones de baseline archivadas en Confluence con justificación

---

## 4. Gestión de cambios (Change Management)

### 4.1 Tipología de cambios

| Tipo | Descripción | Ejemplos | Nivel autoridad |
|:----:|-------------|:---------|:---------------:|
| **Cambio de alcance (Scope)** | Adición/eliminación/modificación de entregables o funcionalidades | Nueva VLAN, cambio nº AGV, excluir zona C, añadir módulo software | Nivel 2–3 |
| **Cambio de plazo (Schedule)** | Modificación de fechas hitos, duraciones, secuencia | Compresión Fase 1.4, retraso licencia, adelanto entrega AGV | Nivel 2–3 |
| **Cambio de coste (Cost)** | Variación presupuesto paquetes, uso reserva, nuevo contrato | Sobrecoste acero, cambio proveedor AGV, horas extra montaje | Nivel 1–3 |
| **Cambio técnico (Technical)** | Modificación especificaciones, arquitectura, materiales | Cambio Wi-Fi 6E → 7, switch L2 → L3, PLC marca distinta | Nivel 1–2 |
| **Cambio organizacional** | Cambio recursos, roles, subcontratistas, PM | Sustitución TL, nueva subcontrata seguridad, cambio PM | Nivel 2–3 |

### 4.2 Formulario RFC (Request for Change) — Campos obligatorios

| Campo | Descripción |
|-------|-------------|
| RFC-ID | Auto-generado: RFC-YYYYMMDD-XXX |
| Título | Breve (máx 80 chars) |
| Tipo | Alcance / Plazo / Coste / Técnico / Organizacional |
| Origen | Stakeholder / Riesgo / Incidente / Mejora / Regulatorio |
| Descripción detallada | Qué, por qué, qué sucede si no se hace |
| Impacto en alcance | WBS afectados, entregables modificados |
| Impacto en plazo | Días de retraso/adelanto, hitos afectados, ruta crítica |
| Impacto en coste | Δ Coste (₽), partidas afectadas, uso reserva riesgos |
| Impacto en calidad/riesgos | Nuevos riesgos, cambio nivel riesgos existentes |
| Alternativas consideradas | Mínimo 2 (incluyendo "no hacer nada") |
| Recomendación TL | Aprobado / Rechazado / Condicional + justificación |
| Decisión final | Aprobado / Rechazado / Diferido + autoridad + fecha |
| Plan de implementación | Tareas, responsables, fechas, verificación |
| Lección aprendida | (Post-implementación) |

### 4.3 Flujo de trabajo RFC

```mermaid
flowchart TD
    A[Detección necesidad cambio] --> B[Rellenar RFC en Jira]
    B --> C{Análisis impacto\n(48h TL + 24h PMO)}
    C --> D[Nivel 1: ≤500k ₽ / ≤5d\nDecide PM]
    C --> E[Nivel 2: 500k-5M / 5-15d\nComité Dirección]
    C --> F[Nivel 3: >5M / >15d / Arquitectura\nCliente/Propietario]
    D --> G[Aprobado?]
    E --> G
    F --> G
    G -->|Sí| H[Implementar: Actualizar WBS, Gantt, Baseline, Presupuesto]
    G -->|No| I[Rechazado: Comunicar + Archivar]
    G -->|Condicional| J[Requisitos previos → Re-evaluar]
    H --> K[Verificar efectividad (cierre RFC)]
    K --> L[Lección aprendida + Actualizar registro riesgos]
```

### 4.4 Control de cambios en documento final (GOST)

- Cambios en documento final (Fase 5) siguen mismo proceso RFC
- Versiones controladas: `v1.0_borrador`, `v1.1_revisado`, `v2.0_aprobado`, `v2.1_correcciones_profesor`
- Cada versión con `Changelog` en anexo del documento
- Entrega final: `v3.0_final_GOST.pdf` con hash SHA-256 registrado en acta

---

## 5. Reportes de avance

### 5.1 Tipos de reporte

| Reporte | Audiencia | Frecuencia | Formato | Longitud | Contenido clave |
|:--------|:----------|:----------:|:-------:|:--------:|:----------------|
| **Dashboard Ejecutivo** | Cliente, Comité Dirección | Tiempo real (web) + PDF quincenal | Power BI / Grafana + PDF 5 pág | 1 pantalla / 5 pág | SPI, CPI, Top 5 riesgos, Hitos ±2 sem, Budget burn, Decisiones pendientes |
| **Informe Quincenal Formal** | Cliente (Propietario + Director ops) | Quincenal (viernes) | PDF firmado | 10–15 pág | Resumen ejecutivo, Avance por fase (WBS), EVM, Riesgos, Cambios, Próximos hitos, Decisiones requeridas |
| **Informe Mensual Técnico** | Equipo técnico, Subcontratistas, PM | Mensual (1º lunes) | PDF + Anexos Excel | 20–30 pág | Detalle avance paquetes, KPIs técnicos, NCs, ITPs, Pruebas, Consumos materiales, Personal |
| **Acta de Hito** | Comité Dirección, Cliente, PM | Al alcanzar cada hito (M-01 a M-11) | PDF firmado | 3–5 pág | Criterios cumplidos, Evidencias, Firmas, Próximos pasos, Riesgos residuales |
| **Reporte de Incidente / No Conformidad** | PM, Responsable calidad, Cliente (si crítico) | Inmediato (crítico) / 24 h (mayor) / 72 h (menor) | Formulario estándar | 2–4 pág | Descripción, Causa raíz (5 Why / Ishikawa), Acción correctiva, Acción preventiva, Verificación, Cierre |
| **Avance Académico (Simulado)** | Profesor evaluador | Según calendario clases | PDF (formato GOST 7.32-2017 parcial) | Según fase | Sección correspondiente del documento final, Avance checklist, Preguntas al profesor |

### 5.2 Estructura estándar Informe Quincenal Formal

```markdown
# Informe Quincenal ED Park — [Semana X–Y] — [Fecha]

## 1. Resumen Ejecutivo (1 página)
- Estado general: 🟢 Verde / 🟡 Ámbar / 🔴 Rojo
- SPI: X.XX | CPI: X.XX | % Avance global: XX %
- Top 3 logros quincena
- Top 3 riesgos/preocupaciones
- Decisiones requeridas del cliente (sí/no + fecha límite)

## 2. Avance por Fase (WBS Nivel 2)
| Fase | % Plan (PV) | % Real (EV) | SPI | Comentario |
|------|-------------|-------------|-----|------------|
| 1.1 Análisis | 100% | 100% | 1.00 | Completa |
| 1.2 Diseño | 100% | 95% | 0.95 | Pendiente licencia M-03 |
| ... | ... | ... | ... | ... |

## 3. Earned Value Management
- PV acumulado: XX M ₽ | EV: XX M ₽ | AC: XX M ₽
- SV: XX M ₽ (X %) | CV: XX M ₽ (X %)
- EAC: XX M ₽ | VAC: XX M ₽
- Gráfico S-curve (adjunto)

## 4. Hitos
| Hito | Fecha plan | Fecha real/est. | Estado | Comentario |
|------|------------|-----------------|--------|------------|
| M-04 Montaje completado | 2027-11-28 | 2027-12-05 | ⚠️ Riesgo | Retraso licencias |

## 5. Riesgos (Top 5)
| ID | Riesgo | Nivel | Tendencia | Acción esta quincena |
|----|--------|:-----:|:---------:|----------------------|
| R-13 | Licencia municipal | Alto | ⬆️ | Reunión alcalde programada |

## 6. Cambios (RFCs)
| RFC-ID | Título | Tipo | Impacto ₽ | Impacto días | Estado |
|--------|--------|:----:|----------:|-------------:|:------:|
| RFC-20270115-003 | Cambio proveedor SAI | Coste | +800,000 | 0 | Aprobado N2 |

## 7. Próximos 15 días
- Actividades críticas en ruta crítica
- Entregables esperados
- Reuniones clave

## 8. Anexos
- Dashboard EVM completo
- Registro riesgos actualizado
- Log RFCs
- Fotos avance obra (georreferenciadas)
```

### 5.3 Repositorio y control de versiones documentales

| Documento | Herramienta | Estructura carpetas | Naming convention | Retención |
|-----------|-------------|---------------------|-------------------|-----------|
| Reportes formales | SharePoint / Confluence | `/Project_ED_Park/Reports/Quincenal/` | `EDP_Q_YYYYMMDD_vN.pdf` | 10 años post-proyecto |
| Actas reuniones | Confluence | `/Project_ED_Park/Minutes/` | `EDP_MOM_YYYYMMDD_Topic_vN.md` | 10 años |
| RFCs | Jira (Custom Issue Type) | Proyecto `EDP` / Component `Change` | `EDP-RFC-XXXX` | 10 años |
| ITPs / Actas inspección | Procore / SharePoint | `/Project_ED_Park/Quality/ITP/` | `EDP_ITP_PackageID_Seq_vN.pdf` | 10 años |
| Evidencias técnicas (fotos, logs, capturas) | SharePoint / NAS | `/Project_ED_Park/Evidence/Phase_X/` | `EDP_Ev_PhaseX_YYYYMMDD_Desc.ext` | 5 años |
| Documento final (GOST) | Confluence + Entrega física | `/Project_ED_Park/Final_Document/` | `EDP_Final_vN_GOST.pdf` | Permanente |

---

## 6. Comunicación en situaciones de crisis

### 6.1 Definición de crisis

| Nivel | Criterio | Ejemplos |
|:-----:|:---------|:---------|
| **Nivel 1 — Incidente menor** | Afecta 1 paquete, sin impacto hito crítico, coste < 500,000 ₽ | Fallo 1 AP, NC estantería menor, bug software no bloqueante |
| **Nivel 2 — Incidente mayor** | Afecta ruta crítica, hito en riesgo, coste 500,000–5,000,000 ₽ | Retraso licencia > 2 sem, fallo switch núcleo, vulnerabilidad crítica |
| **Nivel 3 — Crisis** | Múltiples hitos en riesgo, coste > 5,000,000 ₽, seguridad personas, reputación | Colisión AGV, incendio, ciberataque exitoso, parada obra por autoridad |

### 6.2 Protocolo de comunicación en crisis

| Acción | Nivel 1 | Nivel 2 | Nivel 3 |
|--------|---------|---------|---------|
| **Detección → Alerta PM** | Inmediata (Teams/llamada) | Inmediata (llamada + SMS) | Inmediata (llamada + SMS + email urgente) |
| **PM → Cliente (Propietario)** | En informe quincenal | < 2 h (llamada + email) | < 30 min (llamada directa Director ops) |
| **PM → Comité Dirección** | Próxima reunión quincenal | < 4 h (convocatoria extraordinaria) | < 1 h (conferencia urgente) |
| **Comunicación externa (prensa, autoridades)** | No requerida | Solo si regulatorio lo exige | PM + Cliente + Jurídico (portavoz único) |
| **Registro** | Jira Incident + Informe quincenal | Acta crisis + RFC si hay cambio | Acta crisis + Informe lecciones + Posible re-baseline |
| **Revisión post-crisis** | En retrospectiva sprint | < 5 días (análisis causa raíz) | < 3 días (informe formal + plan recuperación) |

---

## 7. Referencias normativas

- **ГОСТ Р ИСО 15745-4-2010**. Системы автоматизации производства и их интеграция. Профили. Часть 4. Профили систем управления на основе Ethernet. — М.: Стандартинформ, 2010.
- **ГОСТ Р МЭК 62443-3-3-2016**. Системы и меры по обеспечению кибербезопасности промышленных автоматизированных систем. Часть 3-3. — М.: Стандартинформ, 2016.
- **ГОСТ Р МЭК 61850-3**. Коммуникационные системы и сети в электроэнергетике. Часть 3. — М.: Стандартинформ.
- **ГОСТ 7.32-2017**. Отчет о научно-исследовательской работе. Структура и правила оформления. — М.: Стандартинформ, 2017.
- **ГОСТ 7.1-2003**. Библиографическая запись. Библиографическое описание. — М.: Стандартинформ, 2003.
- **ISO 21500:2021**. Project, programme and portfolio management — Context and concepts (gestión de proyectos).
- **ISO 21502:2020**. Project, programme and portfolio management — Guidance on project management (procesos de comunicación, cambios, reporting).
- **PMI PMBOK 7ª ed.**. Guía de los fundamentos para la dirección de proyectos (EVM, gestión de cambios, comunicación).
- **EIA-748-E**. Earned Value Management Systems (estándar EVMS).
- **ГОСТ Р ИСО 10006-2018**. Руководство по управлению качеством в проектах (calidad en gestión de proyectos).

---

## 8. Checklist de la sección

- [x] Objetivo de la sección definido y alineado con el Pasaporte del Proyecto (05_01)
- [x] Principios de comunicación establecidos (5 principios)
- [x] Matriz de comunicación por stakeholder (10 stakeholders × 7 columnas)
- [x] Calendario de comunicaciones regulares (10 reuniones/reportes con frecuencia, duración, participantes, entradas/salidas)
- [x] Escalamiento y autoridad de decisión (4 niveles con límites económicos, de plazo y técnicos)
- [x] Proceso RFC (Request for Change) completo con diagrama Mermaid
- [x] **KPIs de proyecto (macro)**: 7 indicadores con fórmula, meta, frecuencia, fuente, responsable, umbrales
- [x] **KPIs técnicos (telecom/automatización)**: 10 indicadores con métricas cuantitativas específicas ED Park
- [x] **KPIs de software**: 6 indicadores (velocity, burndown, defect escape, coverage, tech debt, lead time)
- [x] **KPIs de montaje/instalación**: 4 indicadores (avance físico, NCs, seguridad, ITP 1ª vez)
- [x] **Earned Value Management**: Conceptos, reglas de medición % avance por tipo paquete, reporting dashboard, control baseline
- [x] Gestión de cambios: 5 tipologías, formulario RFC (13 campos), flujo trabajo Mermaid
- [x] Reportes de avance: 6 tipos con audiencia, frecuencia, formato, longitud, contenido clave
- [x] Estructura estándar Informe Quincenal Formal (8 secciones + anexos)
- [x] Repositorio y control de versiones documentales (6 tipos documento × herramienta/estructura/naming/retención)
- [x] Comunicación en crisis: 3 niveles, protocolo con tiempos de respuesta, responsable, registro
- [x] Referencias GOST citadas correctamente en ruso (10 estándares + ISO/PMI/EIA)
- [x] Coherencia verificada con 05_01 a 05_05
- [x] Documento revisado por el Project Manager

---

## 9. Conclusión

El plan de comunicación y seguimiento del ED Park establece un marco **estructurado, medible y escalable** para un proyecto de 18 meses, 117M ₽, con 17 tecnologías de telecomunicaciones (Tema Nº 12), 6 AGV con V2X/V2I y entorno regulatorio cubano.

**Pilares clave:**
1. **Matriz de comunicación** adaptada a 10 stakeholders con información relevante, cadencia fija y canales definidos
2. **27 KPIs** distribuidos en 4 dimensiones (proyecto, técnico, software, montaje) con umbrales verde/ámbar/rojo para alerta temprana
3. **EVM integrado** con baseline en M-02, reglas de medición por tipo de paquete y dashboard quincenal para decisiones basadas en datos
4. **Gestión de cambios formal (RFC)** con 4 niveles de autoridad, formulario estandarizado y trazabilidad completa en Jira/Confluence
5. **Reportes estandarizados** (6 tipos) con plantilla quincenal de 8 secciones lista para automatización en Power BI/Grafana
6. **Protocolo de crisis** con 3 niveles y tiempos de respuesta definidos (30 min – 4 h) protegiendo la toma de decisiones bajo presión

La coherencia con el **Pasaporte (05_01)**, **WBS (05_02)**, **Gantt (05_03)**, **Presupuesto (05_04)** y **Riesgos (05_05)** garantiza que la comunicación y el seguimiento no son actividades administrativas aisladas, sino **herramientas de control integrado** que alimentan la toma de decisiones del Comité de Dirección y la rendición de cuentas al cliente y al evaluador académico.

---

*Documento generado como parte del expediente de gestión de proyecto del proyecto ED Park — Fase 5: Gestión de Proyecto*