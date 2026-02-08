#### Minería de Datos en (X) antes Twitter:​

​La minería de datos en Twitter implica el uso de técnicas computacionales para extraer información útil y significativa de los datos generados en la plataforma. Esto puede incluir la extracción de texto de tweets, identificación de temas, detección de tendencias y, crucialmente, análisis de sentimientos. ​

​El análisis de sentimientos se refiere a la tarea de determinar la actitud emocional expresada en un texto, ya sea positiva, negativa o neutral. En el contexto de Twitter, esto puede aplicarse para comprender cómo se sienten las personas sobre un tema específico, un producto, un evento o incluso una marca.

- Herramientas y técnicas:​ ​Para llevar a cabo la minería de datos en Twitter para análisis de sentimientos, se emplean una variedad de herramientas y técnicas. Estas pueden incluir algoritmos de aprendizaje automático, procesamiento del lenguaje natural (NLP), y técnicas específicas de análisis de sentimientos como el análisis léxico basado en diccionarios o modelos de aprendizaje profundo. ​

- ​Las API proporcionadas por Twitter permiten a los investigadores y desarrolladores acceder a grandes cantidades de datos en tiempo real, facilitando así el proceso de recopilación de datos para el análisis.

- Aplicaciones y beneficios:​ ​Las aplicaciones de la minería de datos en Twitter para análisis de sentimientos son diversas y van desde la investigación académica hasta la toma de decisiones empresariales. Por ejemplo, las empresas pueden utilizar esta técnica para evaluar la percepción del consumidor sobre sus productos o servicios, identificar problemas potenciales y tomar medidas correctivas de manera proactiva. Los gobiernos pueden monitorear el sentimiento público sobre políticas específicas o eventos importantes, lo que les permite adaptar sus estrategias de comunicación y políticas en consecuencia.​

- ​Limitaciones y desafíos:​ ​A pesar de sus numerosos beneficios, la minería de datos en Twitter para análisis de sentimientos enfrenta varios desafíos y limitaciones. Por un lado, la naturaleza ruidosa y a menudo ambigua de los tweets puede dificultar la precisión del análisis de sentimientos, especialmente en contextos donde el sarcasmo, la ironía o el lenguaje coloquial son comunes. Además, la representatividad de los datos puede ser un problema, ya que los usuarios de Twitter no son necesariamente una muestra representativa de la población en general.

#### **Proceso completo para utilizar la API de la red social X (antes Twitter)**,

Antes de tocar la API, esto es **clave** (y muchas veces lo primero que revisa X):

* ¿Qué quieres hacer?

  * Análisis de opinión pública
  * Monitoreo de tendencias
  * Recolección de datos para Data Science / IA
  * Publicación automática de contenido
* ¿Qué datos necesitas?

  * Tweets (posts)
  * Usuarios
  * Métricas de interacción
* ¿Con qué frecuencia?

  * Tiempo real
  * Histórico
* ¿Para qué contexto?

  * Académico
  * Investigación
  * Institucional
  * Comercial

**Tip legal/data**: define desde aquí si manejarás datos personales, porque eso impacta privacidad, consentimiento y almacenamiento (algo muy alineado con tu perfil.

Crear una cuenta de desarrollador en X

1. Tener una cuenta activa en X.
2. Ir al **portal de desarrolladores de X**.
3. Solicitar acceso como desarrollador:

   * Describe claramente el **caso de uso**
   * Sé específico y honesto (X rechaza solicitudes vagas)
4. Elegir el tipo de acceso:

   * **Free**
   * **Basic**
   * **Pro / Enterprise**

Cada plan define:

* Número de solicitudes (rate limits)
* Acceso a endpoints históricos
* Uso comercial o no

Crear un proyecto y una aplicación

Una vez aprobado:

1. Crear un **Project**.
2. Dentro del proyecto, crear una **App**.
3. La App genera las credenciales necesarias para autenticarte.

Esto separa:

* Propósito del proyecto
* Aplicaciones técnicas específicas

Obtener credenciales y tipos de autenticación

X usa principalmente **OAuth**. Dependiendo de lo que hagas, usarás:

Credenciales típicas

* API Key
* API Key Secret
* Bearer Token
* Access Token
* Access Token Secret

Tipos de autenticación

* **OAuth 2.0 Bearer Token**

  * Lectura de datos públicos
  * Ideal para análisis y minería de datos
* **OAuth 1.0a**

  * Publicar tweets
  * Acciones en nombre de un usuario

**Buena práctica de seguridad**:

* Nunca subas claves a repositorios
* Usa variables de entorno
* Rota credenciales periódicamente

Identificar los endpoints que vas a usar

La API de X está organizada por **endpoints REST**.

Ejemplos comunes:

* Buscar tweets por palabras clave
* Obtener tweets de un usuario
* Obtener métricas (likes, retweets, replies)
* Publicar un tweet

Cada endpoint define:

* Método HTTP (GET / POST)
* Parámetros
* Límites de uso
* Nivel de acceso requerido

Diseñar el flujo del proceso (arquitectura)

Aquí es donde ya suena a **ciencia de datos / ingeniería**

Flujo típico:

1. Autenticación contra la API
2. Solicitud de datos (request)
3. Recepción de respuesta (JSON)
4. Validación y limpieza
5. Almacenamiento:

   * Base de datos
   * Data Lake
6. Análisis / visualización / modelos
7. Auditoría y control de uso

Ideal si documentas:

* Origen del dato
* Fecha
* Endpoint
* Versión de la API

Consumo de la API (peticiones)

A nivel lógico:

* Construyes la solicitud HTTP
* Agregas encabezados de autenticación
* Envías parámetros de búsqueda
* Manejas la respuesta

Consideraciones importantes:

* **Rate limits** (si te pasas, te bloquean temporalmente)
* Manejo de errores (401, 403, 429, 500)
* Paginación de resultados
* Reintentos controlados

Gestión y almacenamiento de datos

Importante desde el punto de vista legal y ético:

* Almacenar solo lo necesario
* Evitar duplicados
* Controlar versiones
* Anonimizar cuando sea posible
* Definir tiempos de retención

💡 En proyectos institucionales:

* Registrar metadatos
* Clasificar sensibilidad
* Aplicar controles de acceso

Cumplimiento legal y políticas de X

No es opcional

Debes cumplir:

* **Developer Policy de X**
* Restricciones de redistribución
* Eliminación de datos cuando X lo solicite
* Respeto a privacidad de usuarios

Si el proyecto es académico o gubernamental:

* Documenta finalidad
* Justifica interés público
* Aplica principios de minimización

Monitoreo, auditoría y mantenimiento

Finalmente:

* Monitorea uso de la API
* Revisa cambios de versión
* Actualiza tokens
* Ajusta consultas según necesidades
* Documenta incidentes

Esto te salva cuando:

* Cambia la API
* Hay auditorías
* Escala el proyecto




