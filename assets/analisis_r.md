## 3.1 Análisis de sentimientos en **R**

¿Qué es el análisis de sentimientos?

El **análisis de sentimientos** es una técnica de **Procesamiento de Lenguaje Natural (NLP)** que permite identificar, extraer y cuantificar la **carga emocional** presente en un texto. Su objetivo principal es clasificar opiniones, emociones o actitudes expresadas en lenguaje natural, comúnmente en categorías como:

* **Positivo**
* **Negativo**
* **Neutral**

Y, en enfoques más avanzados:

* Emociones específicas (alegría, enojo, tristeza, miedo, sorpresa, etc.)
* Intensidad del sentimiento
* Polaridad continua (de muy negativo a muy positivo)

En ciencia de datos, esta técnica se utiliza para analizar grandes volúmenes de texto no estructurado proveniente de:

* Redes sociales
* Encuestas abiertas
* Comentarios de usuarios
* Reseñas de productos o servicios
* Noticias y documentos institucionales

Enfoques principales del análisis de sentimientos

En **R**, el análisis de sentimientos se puede abordar principalmente desde dos enfoques:

2.1 Enfoque basado en léxicos

Este enfoque utiliza **diccionarios de palabras** previamente etiquetadas con un valor emocional.

Ejemplo:

* “excelente” → positivo
* “terrible” → negativo

Cada palabra aporta un puntaje y el sentimiento total del texto se obtiene al **agregar los valores individuales**.

Ventajas:

* Fácil de implementar
* No requiere datos etiquetados
* Ideal para fines educativos y análisis exploratorio

Limitaciones:

* No entiende contexto
* Dificultad con sarcasmo o ironía
* Dependencia del idioma y dominio

2.2 Enfoque basado en aprendizaje automático

Aquí se entrenan **modelos supervisados o no supervisados** usando textos previamente etiquetados.

Ejemplos: Comparativa de Modelos de Aprendizaje Automático

| Algoritmo | Concepto Clave | Funcionamiento | Ventajas | Desventajas / Casos de Uso |
| --- | --- | --- | --- | --- |
| **Regresión Logística** | Probabilidad binaria | Utiliza la función sigmoide:  para mapear cualquier valor a un rango entre 0 y 1. | Extremadamente rápido, fácil de interpretar y excelente "línea base" (baseline). | Solo modela relaciones lineales. Mal desempeño si hay mucha complejidad no lineal. |
| **Naive Bayes** | Probabilidad Condicional | Basado en el Teorema de Bayes. Asume que todas las características son **independientes** entre sí (de ahí lo "naive" o ingenuo). | Muy eficiente con grandes volúmenes de datos y texto. Funciona bien con pocas muestras. | La suposición de independencia rara vez se cumple en la realidad. Ideal para **Spam Filters**. |
| **SVM** (Support Vector Machines) | Margen Máximo | Busca el hiperplano que mejor separa las clases maximizando la distancia entre los puntos más cercanos (vectores de soporte). | Muy eficaz en espacios de alta dimensionalidad. Gracias al "Kernel Trick" maneja datos no lineales. | Lento en conjuntos de datos muy grandes. Difícil de tunear (elegir el kernel correcto). |
| **Random Forest** | Ensamble (Bagging) | Crea un "bosque" de múltiples árboles de decisión entrenados con subconjuntos aleatorios de datos y promedia sus votos. | Muy robusto, evita el sobreajuste (overfitting) y maneja bien datos faltantes o valores atípicos. | Puede ser lento en la predicción si el bosque es muy grande. Es una "caja negra" comparado con un solo árbol. |
| **Modelos Avanzados** (Deep Learning) | Representación Jerárquica | Redes neuronales con muchas capas ocultas que aprenden características automáticamente (desde bordes hasta caras). | Rendimiento superior en datos no estructurados (imágenes, audio, texto complejo). | Requieren **muchísimos datos** y una gran potencia de cómputo (GPUs). Muy difíciles de interpretar. |


Ventajas:

* Mejor captura de contexto
* Mayor precisión en dominios específicos

Limitaciones:

* Requiere datasets etiquetados
* Mayor complejidad computacional
* Menor interpretabilidad

> En una materia de **“R para ciencia de datos”**, normalmente se inicia con el **enfoque léxico** y después se introduce el **aprendizaje automático**.

Preparación del texto (Text Mining)

Antes de analizar sentimientos, el texto debe pasar por un proceso de **preprocesamiento**, ya que el lenguaje natural es altamente ruidoso.

Pasos típicos en R:

1. Conversión a minúsculas
2. Eliminación de signos de puntuación
3. Eliminación de números
4. Eliminación de *stopwords* (palabras vacías como “el”, “la”, “y”)
5. Tokenización (separar el texto en palabras)
6. Lematización o stemming (opcional)

Este proceso es crucial porque **impacta directamente en la calidad del análisis**.


Paquetes clave en R para análisis de sentimientos

R cuenta con un ecosistema muy sólido para NLP. Los paquetes más utilizados son:

 `tidytext`

* Integra NLP con el enfoque *tidy data*
* Facilita la tokenización y análisis léxico
* Compatible con `dplyr` y `ggplot2`

 `textdata`

* Proporciona acceso a léxicos predefinidos
* Descarga y gestiona diccionarios de sentimiento

 `tm` y `quanteda`

* Manejo de corpus de texto
* Transformaciones y análisis estadístico del texto

 `syuzhet`

* Enfocado en análisis emocional
* Basado en modelos narrativos y emociones

Léxicos de sentimiento más usados en R

En el enfoque léxico, R permite usar distintos diccionarios, cada uno con un propósito diferente:

AFINN

* Asigna valores numéricos de −5 a +5
* Permite medir intensidad del sentimiento

 Bing

* Clasifica palabras como positivas o negativas
* Simple y directo

 NRC

* Clasifica palabras en:

  * Positivo / Negativo
  * 8 emociones básicas (alegría, miedo, ira, etc.)

La elección del léxico depende del **objetivo del análisis**.

Flujo típico de análisis de sentimientos en R

Un análisis estándar sigue estas etapas:

1. Recolección del texto
2. Limpieza y preprocesamiento
3. Tokenización
4. Asociación con un léxico de sentimiento
5. Agregación de puntajes
6. Interpretación y visualización de resultados

Este flujo permite:

* Analizar sentimiento por documento
* Comparar periodos de tiempo
* Identificar palabras que más influyen en la polaridad

Visualización de resultados

El análisis de sentimientos suele complementarse con visualizaciones como:

* Barras de sentimiento positivo vs negativo
* Nubes de palabras por polaridad
* Evolución temporal del sentimiento
* Distribución de emociones

En R, estas visualizaciones se integran fácilmente con `ggplot2`.

Casos de uso en ciencia de datos

Algunos ejemplos relevantes para una maestría:

* Análisis de opinión ciudadana en encuestas abiertas
* Evaluación de percepción sobre políticas públicas
* Monitoreo de reputación institucional
* Análisis de retroalimentación de usuarios en plataformas digitales
* Estudios sociales basados en texto no estructurado

Retos y consideraciones éticas

Aspectos críticos que deben discutirse en clase:

* Sesgos en los léxicos
* Limitaciones culturales y lingüísticas
* Privacidad de los datos textuales
* Interpretación responsable de resultados

> El análisis de sentimientos **no mide emociones reales**, sino **patrones lingüísticos**.

Conexión con la ciencia de datos

El análisis de sentimientos es un puente entre:

* Estadística
* Programación
* Inteligencia Artificial
* Ciencias Sociales

Nota: En R, permite a los estudiantes **cerrar el ciclo completo**: desde la limpieza del dato hasta la interpretación analítica.


Tú dime 👉
