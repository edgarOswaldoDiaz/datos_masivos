# CyberShield Analytics

## Big Data & Cybersecurity Analytics Platform

CyberShield Analytics es una plataforma analítica orientada al procesamiento, transformación y análisis de eventos de ciberseguridad utilizando arquitecturas modernas de Big Data, Data Lakehouse y Machine Learning.

El proyecto implementa procesos ETL/ELT, almacenamiento en formato Parquet y GeoParquet, análisis exploratorio de datos (EDA), regionalización geoespacial y modelos de Machine Learning para clasificación de ataques cibernéticos.

---

# Objetivos del Proyecto

- Implementar una arquitectura Data Lakehouse.
- Procesar datos de ciberseguridad mediante pipelines ETL/ELT.
- Aplicar análisis exploratorio de datos (EDA).
- Construir estructuras geoespaciales utilizando GeoPandas.
- Implementar modelos de Machine Learning para clasificación de ataques.
- Generar datasets optimizados en formatos Parquet y GeoParquet.
- Preparar infraestructura para dashboards y visualización analítica.

---

# Módulos Implementados

## Dashboard Ejecutivo

Panel principal para monitoreo de eventos de ciberseguridad.

Incluye:

- Total de ataques
- Estado más afectado
- Tipo de ataque dominante
- Severidad dominante
- Desempeño de modelos ML

---

## Threat Intelligence

Módulo especializado para análisis de amenazas.

Incluye:

- Attack Type Distribution
- Severity Distribution
- Protocol Analysis
- Traffic Type Analysis
- Network Segment Analysis

---

## Geo Intelligence

Visualización geoespacial de ataques.

Incluye:

- Mapa interactivo de México
- Distribución de ataques por estado
- GeoJSON
- Leaflet

---

## Machine Learning

Monitoreo de desempeño de modelos.

Incluye:

- Best Model KPIs
- Accuracy Comparison
- Precision vs Recall
- Metrics Table

---

## Model Evaluation

Comparación avanzada de modelos.

Incluye:

- Ranking de modelos
- Radar Chart
- Leaderboard

---

## API Monitoring

Monitoreo de disponibilidad de servicios.

Incluye:

- Estado de endpoints
- Disponibilidad
- KPIs de salud de APIs

---

# Dataset

Dataset utilizado:

- Cyber Security Attacks Dataset
- Fuente: Kaggle
- Dataset orientado al análisis de eventos y ataques de ciberseguridad.

---

# Tecnologías Utilizadas

## Infraestructura
- Docker
- Docker Compose
- WSL2
- Jupyter Notebook

## Procesamiento de Datos
- Python
- Pandas
- NumPy
- GeoPandas
- Shapely

## Machine Learning
- Scikit-learn
- Random Forest
- XGBoost
- CatBoost

## Visualización

- AdminLTE
- Bootstrap 5
- ApexCharts
- Leaflet
- OpenStreetMap

## Formatos de Datos
- CSV
- Parquet
- GeoParquet

## Control de Versiones
- Git
- GitHub

---
# Arquitectura del Proyecto

El proyecto implementa una arquitectura basada en Data Lakehouse para procesamiento analítico de eventos de ciberseguridad.

## Flujo General

```text
RAW
 ↓
CLEAN
 ↓
PROCESSED
 ↓
MACHINE LEARNING
 ↓
REST API
 ↓
ANALYTICS DASHBOARDS
```

## Capas del Data Lakehouse

### RAW Layer
Almacenamiento inicial del dataset original proveniente de Kaggle.

### CLEAN Layer
Datos transformados y normalizados mediante procesos ETL/ELT.

### PROCESSED Layer
Datasets preparados para Machine Learning y análisis avanzado.

### GEOSPATIAL Layer
Estructuras GeoDataFrame y GeoParquet para análisis geoespacial.

---

# Root Cause Analysis

El siguiente diagrama Ishikawa resume los factores considerados durante el desarrollo y optimización del modelo de clasificación de ataques cibernéticos.

![Ishikawa Diagram](docs/images/Ishikawa.png)

# Estructura del Proyecto

```text
cybershield-analytics/
│
├── .github/
│
├── api/
│
├── configs/
│
├── dashboard/
│
├── data/
│   ├── raw/
│   ├── clean/
│   ├── processed/
│   └── geoparquet/
│
├── docker/
│   └── Dockerfile.jupyter
│
├── docs/
│   ├── architecture.md
│   ├── etl_pipeline.md
│   ├── geospatial.md
│   └── machine_learning.md
│
├── models/
│
├── notebooks/
│   ├── 01_etl_analysis.ipynb
│   ├── 02_eda_analysis.ipynb
│   ├── 03_ml_preparation.ipynb
│   └── 04_model_training.ipynb
│
├── scripts/
│
├── tests/
│
├── .env
├── .gitignore
├── docker-compose.yml
├── README.md
└── requirements.txt
```

---
# Instalación y Ejecución

## Clonar Repositorio

```bash
git clone https://github.com/USUARIO/cybershield-analytics.git
```

---

## Construir Contenedores

```bash
docker-compose build
```

---

## Levantar Entorno

```bash
docker-compose up -d
```

---

## Acceder a Jupyter Notebook

```text
http://localhost:8888
```

---

## Detener Contenedores

```bash
docker-compose down
```

---
# Machine Learning

El proyecto implementa procesos de preparación y entrenamiento de modelos de Machine Learning orientados a clasificación de ataques cibernéticos.

## Modelos Implementados

### Random Forest

Accuracy: 33.94%

### XGBoost

Accuracy: 32.31%

### CatBoost

Accuracy: 32.45%

### Mejor Modelo

Random Forest

## Pipeline ML

- Selección de features
- Codificación de variables categóricas
- Construcción de dataset ML-ready
- División train/test
- Entrenamiento Random Forest
- Evaluación de métricas
- Matriz de confusión
- Importancia de variables

## Variables Utilizadas

### Features
- protocol
- packet_length
- traffic_type
- anomaly_scores
- severity_level
- network_segment
- mexico_state

### Target
- attack_type

---

# GeoSpatial Analytics

El proyecto incorpora procesamiento geoespacial mediante GeoPandas para regionalización analítica de eventos de ciberseguridad.

## Procesamiento Geoespacial

- Identificación de ubicaciones originales (India)
- Regionalización hacia estados mexicanos
- Generación de coordenadas geográficas
- Construcción de GeoDataFrame
- Exportación GeoParquet
- Validación espacial EPSG:4326

## Formato Espacial

```text
CRS: EPSG:4326
```

---

# REST API

La plataforma expone servicios REST para consumo analítico.

## Endpoints Principales

### Executive KPIs

/analytics/executive-kpis

### Threat Intelligence

/threat/overview

### Geo Intelligence

/geo/attacks-by-state

/geo/mexico-geojson

### Machine Learning

/ml/metrics

/ml/best-model

### Monitoring

/api/status

---
# Equipo del Proyecto

| Integrante | Rol |
|---|---|
| Daniel Ali Romo Chavez | CEO / CIO |
| Claudia Ivett Garcia Vite | Data Scientist |
| Alexis Jaisiel Ortiz Lara | Data Scientist |
| Froylan Alonso Pérez Alanis | DevSecOps Engineer |
| Santiago Cárdenas Laredo | DataSecOps Engineer |
| Paola de Jesus Avila Rivera  | CISO |

---

# Gestión del Proyecto

El proyecto utiliza Jira para administración de tareas, seguimiento de actividades y organización del flujo de trabajo colaborativo.

## Metodología de Trabajo

- Kanban Board
- Organización por épicas
- Seguimiento de ETL/ELT
- Control de Machine Learning
- Gestión de infraestructura Docker
- Seguimiento Data Lakehouse

---

# Estado Actual del Proyecto

## Componentes Implementados

### Infraestructura
- Docker
- Docker Compose
- Jupyter Notebook
- WSL2

### Data Lakehouse
- RAW Layer
- CLEAN Layer
- PROCESSED Layer
- GeoParquet Layer

### ETL / ELT
- Limpieza de datos
- Conversión Parquet
- Validación de nulos
- Normalización de columnas

### GeoSpatial
- GeoDataFrame
- Coordenadas geográficas
- Regionalización México
- Exportación GeoParquet

### Data Science
- EDA
- Visualizaciones
- Métricas descriptivas
- Distribución de ataques

### Machine Learning
- Random Forest
- Feature Engineering
- Train/Test Split
- Classification Report
- Accuracy Metrics

---

# Estado del Desarrollo

```text
Infraestructura        ██████████ 100%
Data Lakehouse         ██████████ 100%
ETL / ELT              ██████████ 100%
GeoSpatial             ██████████ 100%
EDA                    ██████████ 100%
Machine Learning       ██████████ 100%
REST API               ██████████ 100%
Dashboard Ejecutivo    ██████████ 100%
Threat Intelligence    ██████████ 100%
Geo Intelligence       ██████████ 100%
Model Evaluation       ██████████ 100%
API Monitoring         ██████████ 100%

---

# 8. Actualizar Roadmap

Actualmente el roadmap habla de construir dashboard y API. :contentReference[oaicite:2]{index=2}

Eso ya está terminado.

Reemplazar por:

```markdown
# Roadmap

## Futuras Mejoras

- Integración con Apache Superset
- Automatización completa de pipelines
- Entrenamiento incremental de modelos
- Despliegue cloud
- Observabilidad avanzada
- Integración SIEM
- Detección de anomalías en tiempo real
- Streaming analytics

---

# Referencias

## Dataset
- Kaggle Cyber Security Attacks Dataset

## Librerías
- Pandas
- GeoPandas
- NumPy
- Scikit-learn
- Matplotlib

## Herramientas
- Docker
- GitHub
- Jira
- Jupyter Notebook

---

# Licencia

Proyecto académico orientado a análisis de datos, Big Data y ciberseguridad.

---

# Autoría

CyberShield Analytics Team - 2026

---