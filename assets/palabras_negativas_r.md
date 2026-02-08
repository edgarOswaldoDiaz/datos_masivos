#### Ejemplo en R: Uso de palabras de opinión negativa

```r
# ============================
# 1. Cargar librerías
# ============================
library(tidyverse)
library(tidytext)

# ============================
# 2. Texto de ejemplo
# ============================
texto <- tibble(
  documento = c(
    "El servicio fue terrible y la experiencia muy mala",
    "El sistema es lento, ineficiente y frustrante",
    "La aplicación falló y el soporte fue decepcionante"
  )
)

# ============================
# 3. Tokenización del texto
# ============================
palabras <- texto %>%
  unnest_tokens(word, documento)

# ============================
# 4. Cargar lexicon Bing
# ============================
bing <- get_sentiments("bing")

# ============================
# 5. Filtrar SOLO palabras negativas
# ============================
palabras_negativas <- palabras %>%
  inner_join(bing, by = "word") %>%
  filter(sentiment == "negative")

print(palabras_negativas)
```

Conteo de palabras negativas

```r
conteo_negativas <- palabras_negativas %>%
  count(word, sort = TRUE)

print(conteo_negativas)
```

Visualización de palabras negativas más frecuentes

```r
ggplot(conteo_negativas, aes(x = reorder(word, n), y = n)) +
  geom_col() +
  coord_flip() +
  labs(
    title = "Palabras de opinión negativa",
    x = "Palabra",
    y = "Frecuencia"
  ) +
  theme_minimal()
```

¿Qué muestra este código?

- Identifica **palabras con carga emocional negativa**
- Usa un **lexicon estándar** ampliamente citado
- Permite analizar **opiniones negativas** en textos (quejas, reseñas, reportes)
- Es escalable a corpus más grandes (libros, redes sociales, documentos)
