# 05_03 - Cronograma Gantt - Proyecto ED Park

## Objetivo de la sección

Definir el cronograma maestro del proyecto ED Park mediante un diagrama de Gantt que visualice la secuencia temporal de todas las tareas, sus duraciones, dependencias, hitos y la ruta crítica. Establece un plazo total de 18 meses como referencia de planificación y control del proyecto.

---

## 1. Fases del proyecto (18 meses)

| Fase | Código | Duración | Periodo estimado | Objetivo |
|------|--------|----------|------------------|----------|
| Análisis | 1.1 | ~3 meses | Nov 2026 – Ene 2027 | Requisitos, normativa, suelo y viabilidad |
| Diseño | 1.2 | ~6 meses | Ene 2027 – Jul 2027 | Arquitectura, ingeniería, licencias |
| Desarrollo | 1.3 | ~7 meses | Mar 2027 – Sep 2027 | Adquisiciones, WMS, sistemas |
| Montaje | 1.4 | ~9 meses | Jul 2027 – Feb 2028 | Construcción e instalación de naves |
| Pruebas | 1.5 | ~3 meses | Ene 2028 – Mar 2028 | Validación técnica y operativa |
| Despliegue | 1.6 | ~2 meses | Feb 2028 – Abr 2028 | Formación, producción y cierre |

> **Plazo total planificado:** 18 meses (nov 2026 – abr/maj 2028), incluyendo margen de contingencia.

---

## 2. Diagrama de Gantt (Mermaid)

```mermaid
gantt
    title Proyecto ED Park - Cronograma Gantt (18 meses)
    dateFormat  YYYY-MM-DD
    axisFormat %b/%y
    todayMarker off

    section Análisis
    1.1.1 Estudio de normativa aplicable       :a1, 2026-11-02, 4w
    1.1.2 Selección y adquisición de suelo     :a2, 2026-11-02, 10w, crit
    1.1.3 Estudio de viabilidad técnica y económica :a3, 2026-12-02, 6w
    1.1.4 Definición de requisitos funcionales :a4, 2026-12-02, 4w, crit
    1.1.5 Estudio de impacto ambiental         :a5, 2026-12-02, 8w

    section Diseño
    1.2.1 Diseño arquitectónico de naves       :b1, 2027-01-04, 6w, crit
    1.2.2 Diseño estructural                   :b2, 2027-02-15, 5w
    1.2.3 Diseño de instalaciones              :b3, 2027-02-15, 5w
    1.2.4 Diseño de muelles y patio            :b4, 2027-02-15, 3w
    1.2.5 Diseño de estanterías y almacenamiento :b5, 2027-02-15, 3w
    1.2.6 Diseño de oficinas y sala de control :b6, 2027-02-15, 3w
    1.2.7 Memoria de seguridad y salud         :b7, 2027-03-22, 3w
    1.2.8 Tramitación de licencias y permisos  :b8, 2027-03-22, 16w, crit

    section Desarrollo
    1.3.1 Adquisición de estanterías y equipos :c1, 2027-03-22, 8w
    1.3.2 Adquisición de carretillas y AGV     :c2, 2027-03-22, 10w
    1.3.3 Desarrollo e implementación de WMS   :c3, 2027-04-12, 12w
    1.3.4 Instalación de red y comunicaciones  :c4, 2027-07-05, 6w
    1.3.5 Instalación de videovigilancia y accesos :c5, 2027-07-05, 6w
    1.3.6 Compra de mobiliario y equipamiento  :c6, 2027-07-05, 6w

    section Montaje
    1.4.1 Obras de cimentación y estructura    :d1, 2027-07-11, 20w, crit
    1.4.2 Instalación de pavimentos y muelles  :d2, 2027-11-01, 8w
    1.4.3 Montaje de instalaciones técnicas    :d3, 2027-11-01, 10w, crit
    1.4.4 Montaje de estanterías y almacenamiento :d4, 2027-11-29, 6w, crit
    1.4.5 Montaje de oficinas y sala de control :d5, 2027-11-29, 6w
    1.4.6 Montaje de zona de carga AGV         :d6, 2028-01-10, 4w

    section Pruebas
    1.5.1 Pruebas de instalaciones técnicas    :e1, 2028-01-10, 4w, crit
    1.5.2 Pruebas de estanterías y capacidad   :e2, 2028-01-10, 2w
    1.5.3 Pruebas de WMS y comunicaciones      :e3, 2028-01-10, 4w
    1.5.4 Pruebas de AGV y zona de carga       :e4, 2028-02-07, 2w
    1.5.5 Pruebas de seguridad y evacuación    :e5, 2028-02-07, 2w
    1.5.6 Puesta en marcha en vacío            :e6, 2028-02-21, 2w, crit

    section Despliegue
    1.6.1 Formación de personal operativo      :f1, 2028-02-21, 4w, crit
    1.6.2 Carga inicial de mercancía           :f2, 2028-03-06, 2w
    1.6.3 Puesta en producción                 :f3, 2028-03-20, 1w, crit
    1.6.4 Entrega y cierre del proyecto        :f4, 2028-03-20, 4w, crit
```

---

## 3. Lista de tareas con detalle

| ID | Nombre | Duración | Inicio | Fin | Predecesoras | Recursos | Hito |
|----|--------|----------|--------|-----|--------------|----------|------|
| 1.1.1 | Estudio de normativa aplicable | 4 semanas | 2026-11-02 | 2026-11-30 | — | Arquitecto, Ingeniero legal | |
| 1.1.2 | Selección y adquisición de suelo | 10 semanas | 2026-11-02 | 2027-01-09 | — | Gestor inmobiliario, Abogado | M1: Terreno adquirido |
| 1.1.3 | Estudio de viabilidad técnica y económica | 6 semanas | 2026-12-02 | 2027-01-13 | 1.1.1 | Consultor financiero, Ingeniero | |
| 1.1.4 | Definición de requisitos funcionales | 4 semanas | 2026-12-02 | 2026-12-30 | 1.1.1 | Analista funcional, Cliente | |
| 1.1.5 | Estudio de impacto ambiental | 8 semanas | 2026-12-02 | 2027-01-27 | 1.1.1 | Consultor ambiental | |
| 1.2.1 | Diseño arquitectónico de naves | 6 semanas | 2027-01-04 | 2027-02-14 | 1.1.4, 1.1.5 | Arquitecto | |
| 1.2.2 | Diseño estructural | 5 semanas | 2027-02-15 | 2027-03-22 | 1.2.1 | Ingeniero estructural | |
| 1.2.3 | Diseño de instalaciones | 5 semanas | 2027-02-15 | 2027-03-22 | 1.2.1 | Ingeniero de instalaciones | |
| 1.2.4 | Diseño de muelles y patio | 3 semanas | 2027-02-15 | 2027-03-08 | 1.2.1 | Ingeniero civil | |
| 1.2.5 | Diseño de estanterías y almacenamiento | 3 semanas | 2027-02-15 | 2027-03-08 | 1.2.1 | Ingeniero logístico | |
| 1.2.6 | Diseño de oficinas y sala de control | 3 semanas | 2027-02-15 | 2027-03-08 | 1.2.1 | Arquitecto | |
| 1.2.7 | Memoria de seguridad y salud | 3 semanas | 2027-03-22 | 2027-04-12 | 1.2.2, 1.2.3 | Coordinador de seguridad | |
| 1.2.8 | Tramitación de licencias y permisos | 16 semanas | 2027-03-22 | 2027-07-11 | 1.2.1, 1.2.7 | Gestor administrativo | M2: Licencia concedida |
| 1.3.1 | Adquisición de estanterías y equipos | 8 semanas | 2027-03-22 | 2027-05-17 | 1.2.5 | Compras, Ingeniero logístico | |
| 1.3.2 | Adquisición de carretillas y AGV | 10 semanas | 2027-03-22 | 2027-05-31 | 1.2.5 | Compras, Ingeniero logístico | |
| 1.3.3 | Desarrollo e implementación de WMS | 12 semanas | 2027-04-12 | 2027-07-04 | 1.1.4 | Desarrollador software, Consultor WMS | |
| 1.3.4 | Instalación de red y comunicaciones | 6 semanas | 2027-07-05 | 2027-08-16 | 1.2.3 | Ingeniero de sistemas | |
| 1.3.5 | Instalación de videovigilancia y accesos | 6 semanas | 2027-07-05 | 2027-08-16 | 1.2.3 | Proveedor seguridad | |
| 1.3.6 | Compra de mobiliario y equipamiento oficinas | 6 semanas | 2027-07-05 | 2027-08-16 | 1.2.6 | Compras, RRHH | |
| 1.4.1 | Obras de cimentación y estructura | 20 semanas | 2027-07-11 | 2027-11-28 | 1.2.8 | Constructor, Ingeniero estructural | M3: Estructura terminada |
| 1.4.2 | Instalación de pavimentos y muelles | 8 semanas | 2027-11-01 | 2027-12-26 | 1.4.1 | Constructor, Ingeniero civil | |
| 1.4.3 | Montaje de instalaciones técnicas | 10 semanas | 2027-11-01 | 2028-01-09 | 1.4.1 | Instalador autorizado | |
| 1.4.4 | Montaje de estanterías y zonas de almacenamiento | 6 semanas | 2027-11-29 | 2028-01-09 | 1.4.1, 1.3.1 | Montador de estanterías | |
| 1.4.5 | Montaje de oficinas y sala de control | 6 semanas | 2027-11-29 | 2028-01-09 | 1.4.1, 1.3.6 | Constructor | |
| 1.4.6 | Montaje de zona de carga AGV | 4 semanas | 2028-01-10 | 2028-02-06 | 1.4.3, 1.3.2 | Ingeniero logístico, Electricista | |
| 1.5.1 | Pruebas de instalaciones técnicas | 4 semanas | 2028-01-10 | 2028-02-06 | 1.4.3 | Ingeniero de instalaciones | |
| 1.5.2 | Pruebas de estanterías y capacidad de carga | 2 semanas | 2028-01-10 | 2028-01-23 | 1.4.4 | Ingeniero estructural | |
| 1.5.3 | Pruebas de WMS y comunicaciones | 4 semanas | 2028-01-10 | 2028-02-06 | 1.4.3, 1.3.3 | Consultor WMS | |
| 1.5.4 | Pruebas de AGV y zona de carga | 2 semanas | 2028-02-07 | 2028-02-20 | 1.4.6, 1.5.3 | Proveedor AGV | |
| 1.5.5 | Pruebas de seguridad y evacuación | 2 semanas | 2028-02-07 | 2028-02-20 | 1.4.5, 1.2.7 | Coordinador de seguridad | |
| 1.5.6 | Puesta en marcha en vacío | 2 semanas | 2028-02-21 | 2028-03-06 | 1.5.1, 1.5.3, 1.5.4 | Equipo operativo | |
| 1.6.1 | Formación de personal operativo | 4 semanas | 2028-02-21 | 2028-03-19 | 1.5.6 | Formador, RRHH | |
| 1.6.2 | Carga inicial de mercancía | 2 semanas | 2028-03-06 | 2028-03-19 | 1.5.6 | Equipo operativo | |
| 1.6.3 | Puesta en producción | 1 semana | 2028-03-20 | 2028-03-26 | 1.6.1, 1.6.2 | Director de operaciones | M4: Producción iniciada |
| 1.6.4 | Entrega y cierre del proyecto | 4 semanas | 2028-03-20 | 2028-04-16 | 1.6.3 | Project Manager | M5: Proyecto cerrado |

---

## 4. Hitos principales

| Hito | ID asociado | Fecha estimada | Descripción |
|------|-------------|----------------|-------------|
| M1 | 1.1.2 | 2027-01-09 | Terreno adquirido y disponible para obra |
| M2 | 1.2.8 | 2027-07-11 | Licencia de obras concedida por el ayuntamiento |
| M3 | 1.4.1 | 2027-11-28 | Estructura de ambas naves terminada |
| M4 | 1.6.3 | 2028-03-26 | Puesta en producción: inicio de operaciones reales |
| M5 | 1.6.4 | 2028-04-16 | Proyecto entregado y cerrado administrativamente |

---

## 5. Ruta crítica identificada

La ruta crítica es la secuencia de tareas que determina la duración mínima del proyecto (sin holgura). Cualquier retraso en estas tareas retrasa directamente la fecha de entrega final.

**Ruta crítica:**
```
1.1.1 Estudio normativa → 1.1.4 Requisitos funcionales → 
1.2.1 Diseño arquitectónico → 1.2.8 Licencias y permisos →
1.4.1 Cimentación y estructura → 1.4.3 Instalaciones técnicas →
1.4.4 Montaje estanterías → 1.5.1 Pruebas instalaciones →
1.5.6 Puesta en marcha en vacío → 1.6.1 Formación personal →
1.6.4 Entrega y cierre
```

**Duración de la ruta crítica:** aproximadamente 17 meses.  
**Margen de contingencia:** ~1 mes dentro de los 18 meses planificados.

Tareas en ruta crítica (marcadas con `crit` en el diagrama): 1.1.2, 1.1.4, 1.2.1, 1.2.8, 1.4.1, 1.4.3, 1.4.4, 1.5.1, 1.5.6, 1.6.1, 1.6.3, 1.6.4.

---

## 6. Checklist de la sección

- [ ] Objetivo de la sección definido y alineado con el WBS (05_02)
- [ ] Diagrama de Gantt completo en Mermaid con las 6 fases
- [ ] Lista de tareas con ID, nombre, duración, inicio, fin, predecesoras, recursos y hito
- [ ] Todas las tareas del WBS (1.1.x a 1.6.x) reflejadas en el cronograma
- [ ] Ruta crítica identificada y señalada en el diagrama y en el texto
- [ ] Hitos principales definidos (M1 a M5) con fechas estimadas
- [ ] Plazo total de 18 meses respetado con margen de contingencia
- [ ] Dependencias entre tareas coherentes con el WBS
- [ ] Recursos asignados a cada tarea
- [ ] Documento revisado por el Project Manager

---
*Documento generado como parte del expediente de gestión de proyecto del proyecto ED Park - Fase 5: Gestión de Proyecto*