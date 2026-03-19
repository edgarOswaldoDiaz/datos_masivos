#### Caso 2 ...
# Nombre de la empresa: Frodalex Systems

## Enfoque organizacional
La propuesta de sistema para el despacho es implementar una estrategia integral de gestión y explotación avanzada de datos legales, con el objetivo de optimizar los procesos y la gestión interna, mejorar la toma de decisiones estratégicas y aumentar la eficiencia operativa.
- Administración de expedientes
- Seguimiento de casos
- Gestión de audiencias
- Control documental legal

## Fuentes de datos 
Para el desarrollo de la herramienta, se deben de proporcionar fuentes de datos como lo son:
- Sistemas internos de gestión
- Jurisprudencias y legislaciones
- Documentos legales como contratos, demandas y sentencias
- Normativas y boletines oficiales
- APIs de sistemas judiciales
Dado a que estos contienen información delicada, es necesario llevar un control y resguardo con respecto a todos los documentos, así como una firma de responsabilidad de todos los involucrados en el desarrollo así como monitoreo del uso de estos.

```mermaid
flowchart TD
A[Business Process Management<br/>Roles jurídicos<br/>Automatización<br/>Flujos de trabajo]
B[Fuentes de datos<br/>Expedientes<br/>Jurisprudencia<br/>Legislaciones<br/>Contratos<br/>Documentos legales<br/>Sistemas internos]
C[Integración y preparación<br/>ELT / ETL<br/>Data Engineering<br/>Data Quality<br/>Catalogación]
D[Data Lakehouse<br/>Data Lake - documentos legales<br/>Data Warehouse - datos estructurados<br/>Metadatos]
E[Business Intelligence<br/>Reportes<br/>Visualización]
F[Business Analytics<br/>Descriptivo<br/>Predictivo<br/>Prescriptivo<]
G[Data Science<br/>ML / NLP<br/>Clasificación de documentos]
H[Agentes inteligentes legales<br/>LLMs especializados<br/>RAG sobre documentos<br/>Automatización de análisis<br/>Asistencia a abogados]
I[Soporte a la toma de decisiones<br/>Estrategias legales optimizadas<br/>Predicción de resultados<br/>Automatización de procesos]
J[Gobernanza, seguridad y ética<br/>Privacidad legal<br/>Confidencialidad<br/>Cumplimiento normativo<br/>Auditoría<br/>Control de acceso<br/>Mitigación de sesgos]
%% Flujo
A --> B
B --> C
C --> D
%% Ramificaciones
D --> E
D --> F
D --> G
%% Continuidad
G --> H
H --> I
%% Gobernanza
J -.-> A
J -.-> B
J -.-> C
J -.-> D
J -.-> G
J -.-> I
```
