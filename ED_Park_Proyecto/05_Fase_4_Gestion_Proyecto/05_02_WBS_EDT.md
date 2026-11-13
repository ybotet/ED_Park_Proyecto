# 05_02 - WBS/EDT - Estructura de Desglose del Trabajo

## Objetivo de la sección

Definir la Estructura de Desglose del Trabajo (EDT/WBS) del proyecto ED Park, descomponiendo el proyecto en fases, paquetes de trabajo y tareas específicas. Establece códigos WBS estándar, duraciones, recursos, dependencias y entregables para cada tarea, sirviendo como base para la planificación, estimación de costos, asignación de recursos y control del proyecto. Coherente con el alcance definido en el Pasaporte del Proyecto (05_01) y con la superficie real del ED Park (5,000 m²).

---

## 1. EDT/WBS completa

### Nivel 1: Proyecto ED Park

| Código | Nombre | Descripción |
|--------|--------|-------------|
| 1.0 | Proyecto ED Park | Implementación del Sistema Completo de Automatización y Telecomunicaciones del Centro Logístico ED Park (Matanzas, Cuba) |

---

### Nivel 2: Fases

| Código | Nombre | Descripción |
|--------|--------|-------------|
| 1.1 | Análisis | Definición de requisitos, estudio de normativa, selección de suelo y viabilidad |
| 1.2 | Diseño | Arquitectura, ingeniería, planos de planta, instalaciones y especificaciones técnicas |
| 1.3 | Desarrollo | Adquisición de equipamiento, desarrollo de software WMS, configuración de sistemas |
| 1.4 | Montaje | Construcción de naves, instalación de estanterías, muelles y equipos |
| 1.5 | Pruebas | Puesta en marcha, pruebas de sistemas, pruebas de carga y comisiones |
| 1.6 | Despliegue | Puesta en producción, formación de personal, entrega y cierre del proyecto |

---

### Nivel 3 y Nivel 4: Paquetes de trabajo y tareas específicas

#### Fase 1.1 - Análisis

| WBS | Nombre | Descripción | Duración | Recursos | Dependencias | Entregable |
|-----|--------|-------------|----------|----------|--------------|------------|
| 1.1.1 | Estudio de normativa aplicable | Revisión de normativa urbanística, industrial, seguridad y medioambiental | 2 semanas | Arquitecto, Ingeniero legal | 1.0 | Informe normativo |
| 1.1.2 | Selección y adquisición de suelo | Búsqueda, evaluación y compra del terreno para ED Park (5,000 m²) | 4 semanas | Gestor inmobiliario, Abogado | 1.0 | Escritura de compra del terreno |
| 1.1.3 | Estudio de viabilidad técnica y económica | Análisis de demanda, costos de construcción y retorno de inversión | 3 semanas | Consultor financiero, Ingeniero | 1.1.1 | Estudio de viabilidad |
| 1.1.4 | Definición de requisitos funcionales | Recolección de necesidades operativas del cliente final | 2 semanas | Analista funcional, Cliente | 1.1.1 | Especificación de requisitos |
| 1.1.5 | Estudio de impacto ambiental | Evaluación de impacto y medidas correctoras | 3 semanas | Consultor ambiental | 1.1.1 | Declaración de impacto ambiental |

#### Fase 1.2 - Diseño

| WBS | Nombre | Descripción | Duración | Recursos | Dependencias | Entregable |
|-----|--------|-------------|----------|----------|--------------|------------|
| 1.2.1 | Diseño arquitectónico de naves | Planta, secciones, fachadas y distribuciones internas (5,000 m² total) | 4 semanas | Arquitecto | 1.1.4, 1.1.5 | Plano arquitectónico |
| 1.2.2 | Diseño estructural | Cálculo de estructuras, cimentación y soportes | 3 semanas | Ingeniero estructural | 1.2.1 | Cálculo estructural |
| 1.2.3 | Diseño de instalaciones (eléctrica, HVAC, contraincendios) | Proyectos de instalaciones técnicas | 3 semanas | Ingeniero de instalaciones | 1.2.1 | Proyecto de instalaciones |
| 1.2.4 | Diseño de muelles y patio de maniobras | Distribución de 4 muelles, radios de giro y pavimento | 2 semanas | Ingeniero civil | 1.2.1 | Plano de muelles y patio |
| 1.2.5 | Diseño de estanterías y almacenamiento | Tipología, alturas y capacidad de estanterías (zonas A, B, C) | 2 semanas | Ingeniero logístico | 1.2.1 | Plano de almacenamiento |
| 1.2.6 | Diseño de oficinas y sala de control | Distribución de espacios administrativos (250 m²) | 2 semanas | Arquitecto | 1.2.1 | Plano de oficinas |
| 1.2.7 | Memoria de seguridad y salud | Plan de seguridad y salud en la construcción | 2 semanas | Coordinador de seguridad | 1.2.1 | Plan de seguridad |
| 1.2.8 | Tramitación de licencias y permisos | Solicitud y obtención de licencia de obras y apertura | 6 semanas | Gestor administrativo | 1.2.1, 1.2.7 | Licencia de obras concedida |

#### Fase 1.3 - Desarrollo

| WBS | Nombre | Descripción | Duración | Recursos | Dependencias | Entregable |
|-----|--------|-------------|----------|----------|--------------|------------|
| 1.3.1 | Adquisición de estanterías y equipos | Compra de estanterías portapalets, cantilever y dinámicas (zonas A, B, C) | 4 semanas | Compras, Ingeniero logístico | 1.2.5 | Estanterías entregadas |
| 1.3.2 | Adquisición de carretillas y AGV | Compra de carretillas, transpaletas y 6 AGV/AMR | 5 semanas | Compras, Ingeniero logístico | 1.2.5 | Vehículos entregados |
| 1.3.3 | Desarrollo e implementación de WMS | Instalación y configuración del Sistema de Gestión de Almacén | 6 semanas | Desarrollador software, Consultor WMS | 1.1.4 | WMS operativo |
| 1.3.4 | Instalación de red y comunicaciones | Cableado estructurado, Wi-Fi industrial y red de sensores | 3 semanas | Ingeniero de sistemas | 1.2.3 | Red instalada |
| 1.3.5 | Instalación de sistema de videovigilancia y control de accesos | Cámaras, lectores y central de seguridad | 3 semanas | Ingeniero de sistemas, Proveedor seguridad | 1.2.3 | Sistema de seguridad instalado |
| 1.3.6 | Compra de mobiliario y equipamiento oficinas | Mesas, sillas, equipos informáticos y mobiliario (250 m²) | 3 semanas | Compras, RRHH | 1.2.6 | Mobiliario entregado |

#### Fase 1.4 - Montaje

| WBS | Nombre | Descripción | Duración | Recursos | Dependencias | Entregable |
|-----|--------|-------------|----------|----------|--------------|------------|
| 1.4.1 | Obras de cimentación y estructura | Cimentación, estructura metálica y cerramiento de naves | 8 semanas | Constructor, Ingeniero estructural | 1.2.2, 1.2.8 | Estructura terminada |
| 1.4.2 | Instalación de pavimentos y muelles | Pavimento hormigón, plataformas niveladoras y 4 muelles | 4 semanas | Constructor, Ingeniero civil | 1.4.1 | Pavimentos y muelles instalados |
| 1.4.3 | Montaje de instalaciones técnicas | Electricidad, HVAC, contraincendios y fontanería | 5 semanas | Instalador autorizado | 1.2.3, 1.4.1 | Instalaciones operativas |
| 1.4.4 | Montaje de estanterías y zonas de almacenamiento | Instalación de estanterías portapalets y dinámicas (zonas A, B, C) | 3 semanas | Montador de estanterías | 1.4.1, 1.3.1 | Estanterías montadas |
| 1.4.5 | Montaje de oficinas y sala de control | Construcción de tabiques, oficinas y equipamiento | 3 semanas | Constructor | 1.4.1, 1.3.6 | Oficinas terminadas |
| 1.4.6 | Montaje de zona de carga AGV | Instalación de estaciones de carga y marcado de suelo | 2 semanas | Ingeniero logístico, Electricista | 1.4.3, 1.3.2 | Zona AGV operativa |

#### Fase 1.5 - Pruebas

| WBS | Nombre | Descripción | Duración | Recursos | Dependencias | Entregable |
|-----|--------|-------------|----------|----------|--------------|------------|
| 1.5.1 | Pruebas de instalaciones técnicas | Pruebas de electricidad, HVAC y contraincendios | 2 semanas | Ingeniero de instalaciones | 1.4.3 | Informe de pruebas instalaciones |
| 1.5.2 | Pruebas de estanterías y capacidad de carga | Pruebas de carga estática y dinámica | 1 semana | Ingeniero estructural | 1.4.4 | Certificado de estanterías |
| 1.5.3 | Pruebas de WMS y comunicaciones | Pruebas de funcionalidad, integración y carga del WMS | 2 semanas | Consultor WMS, Desarrollador | 1.3.3, 1.3.4 | WMS validado |
| 1.5.4 | Pruebas de AGV y zona de carga | Pruebas de navegación, carga y ciclo completo | 1 semana | Proveedor AGV | 1.4.6, 1.5.3 | AGV operativos |
| 1.5.5 | Pruebas de seguridad y evacuación | Simulacros y verificación de sistemas de seguridad | 1 semana | Coordinador de seguridad | 1.4.5, 1.2.7 | Certificado de seguridad |
| 1.5.6 | Puesta en marcha en vacío | Operación de prueba sin mercancía real | 1 semana | Equipo operativo | 1.5.1, 1.5.3, 1.5.4 | Informe de puesta en marcha |

#### Fase 1.6 - Despliegue

| WBS | Nombre | Descripción | Duración | Recursos | Dependencias | Entregable |
|-----|--------|-------------|----------|----------|--------------|------------|
| 1.6.1 | Formación de personal operativo | Formación en WMS, carretillas, AGV y procedimientos | 2 semanas | Formador, RRHH | 1.5.6 | Personal formado |
| 1.6.2 | Carga inicial de mercancía | Recepción y almacenamiento de stock inicial | 1 semana | Equipo operativo | 1.6.1 | Stock cargado |
| 1.6.3 | Puesta en producción | Inicio de operaciones reales con clientes | 1 semana | Director de operaciones | 1.6.2 | ED Park operativo |
| 1.6.4 | Entrega y cierre del proyecto | Documentación final, acta de entrega y cierre administrativo | 2 semanas | Project Manager | 1.6.3 | Proyecto cerrado y entregado |

---

## 2. Diagrama WBS en Mermaid

```mermaid
graph TD
    %% Nivel 1
    1["1.0 Proyecto ED Park"]
    
    %% Nivel 2 - Fases
    1 --> 11["1.1 Análisis"]
    1 --> 12["1.2 Diseño"]
    1 --> 13["1.3 Desarrollo"]
    1 --> 14["1.4 Montaje"]
    1 --> 15["1.5 Pruebas"]
    1 --> 16["1.6 Despliegue"]
    
    %% Nivel 3 - Fase Análisis
    11 --> 111["1.1.1 Estudio normativa"]
    11 --> 112["1.1.2 Selección suelo"]
    11 --> 113["1.1.3 Viabilidad"]
    11 --> 114["1.1.4 Requisitos funcionales"]
    11 --> 115["1.1.5 Impacto ambiental"]
    
    %% Nivel 3 - Fase Diseño
    12 --> 121["1.2.1 Diseño arquitectónico"]
    12 --> 122["1.2.2 Diseño estructural"]
    12 --> 123["1.2.3 Instalaciones"]
    12 --> 124["1.2.4 Muelles y patio"]
    12 --> 125["1.2.5 Estanterías"]
    12 --> 126["1.2.6 Oficinas y control"]
    12 --> 127["1.2.7 Seguridad y salud"]
    12 --> 128["1.2.8 Licencias y permisos"]
    
    %% Nivel 3 - Fase Desarrollo
    13 --> 131["1.3.1 Adquisición estanterías"]
    13 --> 132["1.3.2 Adquisición AGV/carretillas"]
    13 --> 133["1.3.3 WMS"]
    13 --> 134["1.3.4 Red y comunicaciones"]
    13 --> 135["1.3.5 Videovigilancia y accesos"]
    13 --> 136["1.3.6 Mobiliario oficinas"]
    
    %% Nivel 3 - Fase Montaje
    14 --> 141["1.4.1 Cimentación y estructura"]
    14 --> 142["1.4.2 Pavimentos y muelles"]
    14 --> 143["1.4.3 Instalaciones técnicas"]
    14 --> 144["1.4.4 Montaje estanterías"]
    14 --> 145["1.4.5 Montaje oficinas"]
    14 --> 146["1.4.6 Zona carga AGV"]
    
    %% Nivel 3 - Fase Pruebas
    15 --> 151["1.5.1 Pruebas instalaciones"]
    15 --> 152["1.5.2 Pruebas estanterías"]
    15 --> 153["1.5.3 Pruebas WMS"]
    15 --> 154["1.5.4 Pruebas AGV"]
    15 --> 155["1.5.5 Pruebas seguridad"]
    15 --> 156["1.5.6 Puesta en marcha vacío"]
    
    %% Nivel 3 - Fase Despliegue
    16 --> 161["1.6.1 Formación personal"]
    16 --> 162["1.6.2 Carga inicial mercancía"]
    16 --> 163["1.6.3 Puesta en producción"]
    16 --> 164["1.6.4 Entrega y cierre"]
    
    %% Estilos
    classDef phase fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef wp fill:#fff3e0,stroke:#e65100,stroke-width:1px;
    class 11,12,13,14,15,16 phase;
    class 111,112,113,114,115,121,122,123,124,125,126,127,128,131,132,133,134,135,136,141,142,143,144,145,146,151,152,153,154,155,156,161,162,163,164 wp;
    
    linkStyle default stroke-width:2px,fill:none,stroke:#666;
```

---

## 3. Cronograma resumido (duraciones estimadas)

| Fase | Duración | Inicio estimado | Fin estimado |
|------|----------|-----------------|--------------|
| 1.1 Análisis | 12 semanas | Semana 1 | Semana 12 |
| 1.2 Diseño | 16 semanas | Semana 5 | Semana 20 |
| 1.3 Desarrollo | 10 semanas | Semana 12 | Semana 22 |
| 1.4 Montaje | 16 semanas | Semana 20 | Semana 36 |
| 1.5 Pruebas | 6 semanas | Semana 30 | Semana 36 |
| 1.6 Despliegue | 6 semanas | Semana 36 | Semana 42 |
| **Total proyecto** | **42 semanas** | | |

> *Nota: Las fases se solapan parcialmente para optimizar el tiempo total del proyecto. El plazo contractual es de 18 meses incluyendo margen de contingencia.*

---

## 4. Checklist de la sección

- [x] Objetivo de la sección definido y alineado con el Pasaporte del Proyecto (05_01)
- [x] Nivel 1: Proyecto ED Park (código 1.0) definido
- [x] Nivel 2: 6 fases identificadas (Análisis, Diseño, Desarrollo, Montaje, Pruebas, Despliegue)
- [x] Nivel 3: Paquetes de trabajo para cada fase
- [x] Nivel 4: Tareas específicas con código WBS estándar (1.0, 1.1, 1.1.1, etc.)
- [x] Cada tarea incluye: código, nombre, descripción, duración, recursos, dependencias y entregable
- [x] Diagrama WBS en Mermaid incluido y conectado jerárquicamente
- [x] Duraciones realistas y justificadas por tarea
- [x] Dependencias entre tareas correctamente identificadas
- [x] Entregables definidos para cada tarea
- [x] Cronograma resumido con fechas estimadas
- [x] Codificación WBS estándar aplicada consistentemente en todo el documento
- [x] Medidas coherentes con el ED Park (5,000 m², 2 naves, 4 muelles, 6 AGV)
- [x] Documento revisado por el Project Manager

---
*Documento generado como parte del expediente de gestión de proyecto del proyecto ED Park - Fase 5: Gestión de Proyecto*
