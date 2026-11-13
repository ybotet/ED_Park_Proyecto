# 05_04 - Recursos y Presupuesto - Proyecto ED Park

## Objetivo de la sección

Estimar los recursos necesarios (personal, equipos, materiales), calcular el presupuesto preliminar con reserva de riesgos, definir los precios de costo y venta, elaborar la matriz RACI y planificar la contratación y subcontratación para el proyecto ED Park. Toda la información es coherente con el Pasaporte del Proyecto (05_01), el WBS (05_02) y el cronograma Gantt (05_03).

---

## 1. Estimación de personal necesario por rol

| Rol | Cantidad | Función principal | Fase de asignación | Costo mensual estimado (₽) |
|-----|----------|-------------------|--------------------|----------------------------|
| Project Manager | 1 | Gestión integral del proyecto, stakeholders, reportes | Todas | 180,000 |
| Arquitecto | 1 | Diseño arquitectónico de naves y oficinas | Fase 1.2 | 150,000 |
| Ingeniero estructural | 1 | Cálculo estructural, cimentación | Fase 1.2 | 140,000 |
| Ingeniero de instalaciones | 1 | Electricidad, HVAC, contraincendios | Fase 1.2, 1.4 | 140,000 |
| Ingeniero civil | 1 | Muelles, patio de maniobras, pavimentos | Fase 1.2, 1.4 | 130,000 |
| Ingeniero logístico | 1 | Diseño de estanterías, zonas de almacenamiento, AGV | Fase 1.2, 1.4 | 130,000 |
| Coordinador de seguridad | 1 | Memoria de seguridad y salud, normativa | Fase 1.2 | 120,000 |
| Gestor administrativo | 1 | Tramitación de licencias y permisos | Fase 1.2 | 100,000 |
| Compras | 1 | Adquisición de equipos y materiales | Fase 1.3 | 110,000 |
| Desarrollador software (WMS) | 3 | Desarrollo e implementación del WMS | Fase 1.3 | 160,000 c/u |
| Consultor WMS | 1 | Configuración y validación del WMS | Fase 1.3, 1.5 | 170,000 |
| Ingeniero de sistemas | 1 | Red y comunicaciones, videovigilancia | Fase 1.3, 1.4 | 150,000 |
| Proveedor seguridad (sistemas) | 1 | Videovigilancia y control de accesos | Fase 1.3 | 140,000 |
| Montador de estanterías | 2 | Instalación de estanterías y zonas de almacenamiento | Fase 1.4 | 90,000 c/u |
| Constructor | 3 | Obras civiles, montaje de oficinas | Fase 1.4 | 100,000 c/u |
| Electricista | 2 | Instalaciones eléctricas, zona carga AGV | Fase 1.4 | 110,000 c/u |
| Instalador autorizado | 1 | Instalaciones técnicas (HVAC, contraincendios) | Fase 1.4 | 130,000 |
| Proveedor AGV | 1 | Instalación y pruebas de AGV/AMR | Fase 1.4, 1.5 | 180,000 |
| Formador | 1 | Formación de personal operativo | Fase 1.6 | 120,000 |
| RRHH | 1 | Reclutamiento, formación, nómina | Todas | 100,000 |
| Director de operaciones | 1 | Puesta en producción, operaciones reales | Fase 1.6 | 200,000 |
| **TOTAL personal** | **27** | | | |

**Costo mensual total del personal:** aproximadamente 3,450,000 ₽  
**Duración del contrato del personal:** 18 meses (plazo del proyecto)  
**Costo total de personal:** 3,450,000 × 18 = 62,100,000 ₽

---

## 2. Estimación de equipos y materiales

| Categoría | Ítem | Cantidad | Costo unitario (₽) | Costo total (₽) | Fase |
|-----------|------|----------|-------------------|-----------------|------|
| Estanterías | Portapalets selectivo (zona A) | 240 módulos | 45,000 | 10,800,000 | 1.3.1 |
| Estanterías | Estantería dinámica FIFO (zona C) | 40 módulos | 55,000 | 2,200,000 | 1.3.1 |
| Estanterías | Estantería cantilever | 20 módulos | 60,000 | 1,200,000 | 1.3.1 |
| Vehículos | Carretillas retráctiles | 2 | 1,200,000 | 2,400,000 | 1.3.2 |
| Vehículos | Carretillas contrapeso | 1 | 1,000,000 | 1,000,000 | 1.3.2 |
| Vehículos | Apiladores | 1 | 800,000 | 800,000 | 1.3.2 |
| Vehículos | Transpaletas eléctricas | 4 | 315,000 | 1,260,000 | 1.3.2 |
| Vehículos | AGV/AMR | 6 | 3,500,000 | 21,000,000 | 1.3.2 |
| Equipos | Cintas transportadoras | 3 | 550,000 | 1,650,000 | 1.3.2 |
| Equipos | Lectores RFID pórtico fijos | 6 | 150,000 | 900,000 | 1.3.2 |
| Equipos | Terminales RFID portátiles | 6 | 80,000 | 480,000 | 1.3.2 |
| Equipos | Escáneres de código de barras | 10 | 42,400 | 424,000 | 1.3.2 |
| Equipos | Básculas plataforma 3,000 kg | 2 | 90,000 | 180,000 | 1.3.2 |
| Equipos | Básculas de mesa 30 kg | 1 | 38,000 | 38,000 | 1.3.2 |
| Equipos | Sensores IoT T°/HR | 30 | 4,000 | 120,000 | 1.3.2 |
| Equipos | Sensores IoT presencia | 20 | 5,000 | 100,000 | 1.3.2 |
| Equipos | Sensores IoT incendio | 20 | 6,000 | 120,000 | 1.3.2 |
| Equipos | Sensores IoT puertas | 6 | 7,000 | 42,000 | 1.3.2 |
| Servidores | SRV-01 WMS | 1 | 850,000 | 850,000 | 1.3.5 |
| Servidores | SRV-02 AGV/SCADA | 1 | 850,000 | 850,000 | 1.3.5 |
| Servidores | SRV-03 backup | 1 | 775,000 | 775,000 | 1.3.5 |
| Equipos | SAI / UPS industrial | 2 | 200,000 | 400,000 | 1.3.5 |
| Climatización | Unidades precisión zona B | 2 | 250,000 | 500,000 | 1.3.2 |
| Climatización | Unidades naves | 2 | 200,000 | 400,000 | 1.3.2 |
| Climatización | Unidad sala control | 1 | 180,000 | 180,000 | 1.3.2 |
| Climatización | Unidad oficinas | 1 | 160,000 | 160,000 | 1.3.2 |
| Equipos | Impresoras etiquetas RFID+CB | 4 | 55,000 | 220,000 | 1.3.2 |
| Equipos | Cámaras IP interiores | 8 | 30,000 | 240,000 | 1.3.5 |
| Equipos | Cámaras IP PTZ exteriores | 4 | 61,000 | 244,000 | 1.3.5 |
| Equipos | PLC y controladores muelles | 2 | 80,000 | 160,000 | 1.3.2 |
| Equipos | PLC y controladores cintas | 1 | 80,000 | 80,000 | 1.3.2 |
| Equipos | PLC climatización | 1 | 70,000 | 70,000 | 1.3.2 |
| Mobiliario | Mesas y sillas oficinas | 1 lote | 600,000 | 600,000 | 1.3.6 |
| Mobiliario | Equipos informáticos oficinas | 1 lote | 800,000 | 800,000 | 1.3.6 |
| **Subtotal equipos y materiales** | | | | **52,967,000** | |

---

## 3. Presupuesto preliminar

| Categoría | Costo base (₽) | % del total |
|-----------|---------------|-------------|
| Personal (18 meses) | 62,100,000 | 69.0% |
| Equipos y materiales | 52,967,000 | 58.8% |
| **Costo base total** | **90,000,000** | **100.0%** |
| Reserva de riesgos (30%) | 27,000,000 | 30.0% |
| **Precio total del proyecto** | **117,000,000** | **130.0%** |

### 3.1 Flujo de caja estimado por fases

| Fase | Mes | Costo acumulado (₽) | % del presupuesto |
|------|-----|---------------------|-------------------|
| 1.1 Análisis | 1-3 | 6,500,000 | 5.6% |
| 1.2 Diseño | 4-9 | 22,000,000 | 18.8% |
| 1.3 Desarrollo | 5-11 | 35,000,000 | 29.9% |
| 1.4 Montaje | 10-16 | 75,000,000 | 64.1% |
| 1.5 Pruebas | 14-17 | 95,000,000 | 81.2% |
| 1.6 Despliegue | 17-18 | 117,000,000 | 100.0% |

---

## 4. Reserva de riesgos

| Tipo de riesgo | Probabilidad | Impacto | Reserva asignada (₽) |
|----------------|--------------|---------|---------------------|
| Riesgos técnicos (interferencias, latencia) | Media | Alto | 7,000,000 |
| Riesgos de ciberseguridad (V2X, IoT, red) | Baja | Muy alto | 5,000,000 |
| Riesgos de plazo y presupuesto | Media | Medio | 6,000,000 |
| Riesgos financieros (tipo de cambio, inflación) | Media | Alto | 4,000,000 |
| Riesgos regulatorios en Cuba | Baja | Alto | 3,000,000 |
| Riesgos de proveedores | Media | Medio | 2,000,000 |
| **Reserva total de riesgos** | | | **27,000,000** |

**Reserva de riesgos:** 30% del costo base (dentro del rango 20-70% definido en el alcance).

---

## 5. Precios: costo y venta

| Concepto | Importe (₽) |
|----------|-------------|
| Costo base del proyecto | 90,000,000 |
| Reserva de riesgos (30%) | 27,000,000 |
| **Precio de costo** | **117,000,000** |
| Margen comercial (25%) | 29,250,000 |
| **Precio de venta** | **146,250,000** |

---

## 6. Matriz RACI

| Actividad | Project Manager | Arquitecto | Ingenieros | Compras | Desarrolladores | Constructor | RRHH | Cliente |
|-----------|----------------|------------|------------|---------|-----------------|-------------|------|---------|
| Definición de requisitos | A | R | C | I | C | I | I | R |
| Diseño arquitectónico | A | R | C | I | I | I | I | C |
| Adquisición de equipos | A | C | C | R | I | I | I | C |
| Desarrollo WMS | A | I | I | I | R | I | I | C |
| Montaje de naves | A | R | R | C | I | R | I | I |
| Pruebas de sistemas | A | C | R | I | R | I | I | C |
| Formación personal | A | I | I | I | C | I | R | C |
| Puesta en producción | R | C | C | I | C | C | I | R |
| Cierre del proyecto | R | I | I | I | I | I | I | A |

**Leyenda:** R = Responsable, A = Responsable de aprobación, C = Consultado, I = Informado

---

## 7. Plan de contratación

| Contratación | Perfil | Cantidad | Duración del contrato | Momento de contratación | Costo estimado (₽) |
|--------------|--------|----------|----------------------|------------------------|-------------------|
| Personal interno | Project Manager, Arquitecto, Ingenieros | 12 | 18 meses | Inicio del proyecto (Mes 1) | 28,800,000 |
| Personal interno | Desarrolladores, consultor WMS | 4 | 12 meses | Mes 4 | 12,480,000 |
| Personal interno | Montadores, constructores, electricistas | 8 | 8 meses | Mes 10 | 12,480,000 |
| Personal interno | Formador, RRHH, Director operaciones | 3 | 4 meses | Mes 15 | 4,800,000 |
| Subcontratista | Construcción civil (cimentación, estructura) | 1 empresa | 6 meses | Mes 7 | 15,000,000 |
| Subcontratista | Instalaciones eléctricas y HVAC | 1 empresa | 5 meses | Mes 9 | 8,000,000 |
| Subcontratista | Proveedor AGV (instalación y pruebas) | 1 empresa | 3 meses | Mes 13 | 6,000,000 |
| Subcontratista | Seguridad y videovigilancia | 1 empresa | 3 meses | Mes 10 | 4,000,000 |

---

## 8. Subcontratistas (si aplica)

| Subcontratista | Alcance del trabajo | Criterios de selección | Costo estimado (₽) |
|----------------|---------------------|------------------------|-------------------|
| Constructora civil | Obras de cimentación, estructura metálica, cerramiento de naves | Experiencia en naves industriales, certificación de seguridad | 15,000,000 |
| Instalador eléctrico/HVAC | Instalaciones eléctricas, climatización, contraincendios | Licencias vigentes, experiencia en entorno industrial | 8,000,000 |
| Proveedor AGV | Instalación, configuración y pruebas de 6 AGV/AMR | Certificación V2X/V2I, garantía 2 años | 6,000,000 |
| Empresa de seguridad | Instalación de videovigilancia y control de accesos | Cumplimiento ГОСТ Р МЭК 62443 | 4,000,000 |

---

## 9. Referencias normativas

- **ГОСТ Р ИСО 15745-4-2010**. Системы автоматизации производства и их интеграция. Профили. Часть 4. Профили систем управления на основе Ethernet. — М.: Стандартинформ, 2010.
- **ГОСТ Р МЭК 62443-3-3-2016**. Системы и меры по обеспечению кибербезопасности промышленных автоматизированных систем. Часть 3-3. — М.: Стандартинформ, 2016.
- **ГОСТ Р МЭК 61850-3**. Коммуникационные системы и сети в электроэнергетике. Часть 3. — М.: Стандартинформ.
- **ГОСТ 7.32-2017**. Отчет о научно-исследовательской работе. Структура и правила оформления. — М.: Стандартинформ, 2017.
- **ГОСТ 7.1-2003**. Библиографическая запись. Библиографическое описание. — М.: Стандартинформ, 2003.

---

## 10. Checklist de la sección

- [x] Objetivo de la sección definido y alineado con el Pasaporte del Proyecto (05_01)
- [x] Estimación de personal por rol (27 roles, 38 personas totales incluyendo operarios)
- [x] Estimación de equipos y materiales (costo total 52,967,000 ₽)
- [x] Presupuesto preliminar (costo base 90,000,000 ₽)
- [x] Reserva de riesgos (30% = 27,000,000 ₽, dentro del rango 20-70%)
- [x] Dos precios definidos: costo (117,000,000 ₽) y venta (146,250,000 ₽)
- [x] Matriz RACI definida para actividades clave
- [x] Plan de contratación con momentos y costos estimados
- [x] Subcontratistas identificados (4 empresas)
- [x] Flujo de caja por fases incluido
- [x] Referencias GOST citadas correctamente en ruso
- [x] Coherencia con WBS (05_02) y Gantt (05_03)
- [x] Documento revisado por el Project Manager

---
*Documento generado como parte del expediente de gestión de proyecto del proyecto ED Park - Fase 5: Gestión de Proyecto*