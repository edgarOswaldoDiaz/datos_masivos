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


Formulación matemática del análisis de sentimientos

Sea un **corpus de documentos** definido como:

[
 \mathcal{D} = { d_1, d_2, \dots, d_N }
]

donde cada documento ( d_i ) es una secuencia de palabras (tokens):

[
d_i = { w_{i1}, w_{i2}, \dots, w_{iM_i} }
]

---

Tokenización y normalización

Definimos una función de preprocesamiento:

[
\phi: d_i \rightarrow T_i
]

tal que:

[
T_i = { t_{i1}, t_{i2}, \dots, t_{iK_i} }
]

donde ( T_i ) es el conjunto de tokens normalizados del documento ( d_i ) (minúsculas, sin signos de puntuación ni *stopwords*).

---

Léxico de sentimientos

Sea un **léxico de sentimientos** definido como una función:

[
s: V \rightarrow \mathbb{R}
]

donde:

* ( V ) es el vocabulario
* ( s(w) ) asigna un valor de sentimiento a cada palabra

Ejemplos:

* ( s(w) \in {-1, +1} ) (Bing)
* ( s(w) \in [-5, +5] ) (AFINN)

Para palabras que no pertenecen al léxico:

[
s(w) = 0
]

---

Puntaje de sentimiento por documento

El **sentimiento total** del documento ( d_i ) se define como:

[
S(d_i) = \sum_{j=1}^{K_i} s(t_{ij})
]

Este valor representa la **polaridad agregada** del texto.

---

Normalización del sentimiento

Para comparar documentos de distinta longitud, se define el **sentimiento normalizado**:

[
\hat{S}(d_i) = \frac{1}{K_i} \sum_{j=1}^{K_i} s(t_{ij})
]

Esto permite interpretar el sentimiento promedio por palabra.

---

Clasificación del sentimiento

Se define una función de clasificación:

[
C(d_i) =
\begin{cases}
\text{Positivo} & \text{si } \hat{S}(d_i) > \delta \
\text{Negativo} & \text{si } \hat{S}(d_i) < -\delta \
\text{Neutral}  & \text{si } |\hat{S}(d_i)| \le \delta
\end{cases}
]

donde ( \delta \ge 0 ) es un umbral de sensibilidad.

---

Análisis emocional (léxico NRC)

Si el léxico incluye **emociones**, definimos:

[
\mathcal{E} = { e_1, e_2, \dots, e_L }
]

Sea una función:

[
s_e: V \rightarrow {0,1}
]

tal que:

[
s_e(w) =
\begin{cases}
1 & \text{si } w \text{ está asociada a la emoción } e \
0 & \text{en otro caso}
\end{cases}
]

El puntaje emocional del documento es:

[
E_e(d_i) = \sum_{j=1}^{K_i} s_e(t_{ij})
]

Esto genera un **vector de emociones**:

[
\mathbf{E}(d_i) = \left[ E_{e_1}(d_i), E_{e_2}(d_i), \dots, E_{e_L}(d_i) \right]
]

---

Interpretación vectorial del sentimiento

El documento puede representarse como:

[
d_i \rightarrow \left( \hat{S}(d_i), \mathbf{E}(d_i) \right)
]

donde:

* ( \hat{S}(d_i) ) mide la polaridad
* ( \mathbf{E}(d_i) ) mide la distribución emocional

---

Extensión a modelos supervisados (opcional)

En aprendizaje automático, el sentimiento se modela como:

[
\hat{y}_i = f(\mathbf{x}_i)
]

donde:

* ( \mathbf{x}_i ) es el vector de características del documento
* ( f ) es un modelo aprendido
* ( \hat{y}_i \in {\text{Positivo}, \text{Negativo}, \text{Neutral}} )


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
_______________________
Referencias 

> James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). An introduction to statistical learning: With applications in R (2nd ed.). Springer.

> Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep learning. MIT Press. 
