#### Caso de uso el estado de ánimo de mi libro o la noticia del día

Este código cargará el texto del libro "seleccionado", analizará los sentimientos de cada palabra utilizando el lexicon de sentimientos bing, contará el número de palabras positivas y negativas, y determinará si el estado de ánimo general del texto es positivo, negativo o neutral.​

```r
# ============================
# 1. Cargar librerías
# ============================
library(tidyverse)
library(tidytext)
library(readr)

# ============================
# 2. Cargar el texto del libro
# ============================
# El archivo debe ser un .txt (por ejemplo: "libro.txt")
texto_libro <- read_lines("libro.txt")

# Convertir el texto a un data frame
libro_df <- tibble(
  linea = texto_libro
)

# ============================
# 3. Tokenización del texto
# ============================
# Separar el texto en palabras individuales
palabras <- libro_df %>%
  unnest_tokens(word, linea)

# ============================
# 4. Cargar el lexicon Bing
# ============================
bing_lexicon <- get_sentiments("bing")

# ============================
# 5. Análisis de sentimientos
# ============================
sentimientos <- palabras %>%
  inner_join(bing_lexicon, by = "word")

# ============================
# 6. Conteo de palabras positivas y negativas
# ============================
conteo_sentimientos <- sentimientos %>%
  count(sentiment)

print(conteo_sentimientos)

# Extraer valores individuales
positivas <- conteo_sentimientos %>%
  filter(sentiment == "positive") %>%
  pull(n)

negativas <- conteo_sentimientos %>%
  filter(sentiment == "negative") %>%
  pull(n)

# Manejo de valores NA
positivas <- ifelse(length(positivas) == 0, 0, positivas)
negativas <- ifelse(length(negativas) == 0, 0, negativas)

# ============================
# 7. Determinar el estado de ánimo general
# ============================
estado_animo <- case_when(
  positivas > negativas ~ "Positivo",
  negativas > positivas ~ "Negativo",
  TRUE ~ "Neutral"
)

# ============================
# 8. Resultados finales
# ============================
resultado <- tibble(
  Palabras_Positivas = positivas,
  Palabras_Negativas = negativas,
  Estado_Animo_General = estado_animo
)

print(resultado)
```

---

## Explicación técnica breve

* **`unnest_tokens()`** divide el texto en unidades léxicas (palabras).
* **Lexicon Bing** clasifica palabras en *positive* o *negative*.
* **`inner_join()`** conserva únicamente las palabras con carga emocional.
* El **estado de ánimo general** se infiere comparando frecuencias absolutas.



