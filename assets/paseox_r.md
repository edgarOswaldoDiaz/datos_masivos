
#### Un paseo por el software R

R es un software libre y un lenguaje de programación especializado en el análisis estadístico, la manipulación de datos y la visualización gráfica, ampliamente utilizado en ciencia de datos, investigación académica e industria. Su principal fortaleza radica en la gran cantidad de paquetes disponibles, desarrollados por una comunidad global, que permiten abordar problemas complejos de análisis de datos de forma flexible y reproducible.

Desde el punto de vista conceptual, R trabaja principalmente con **objetos**, como vectores, matrices, data frames y listas, lo que facilita el manejo estructurado de la información. El data frame es especialmente relevante en ciencia de datos, ya que representa tablas de datos similares a las que se utilizan en bases de datos o archivos CSV. Además, R promueve el análisis reproducible, ya que todo el proceso —desde la carga de datos hasta los resultados— puede documentarse mediante scripts.

El entorno de desarrollo más utilizado es **RStudio**, que proporciona una interfaz amigable con editor de scripts, consola, visualización de gráficos y manejo de archivos, lo cual reduce la curva de aprendizaje para estudiantes. R permite integrar estadística clásica, análisis exploratorio, modelos predictivos y técnicas modernas como machine learning, todo dentro de un mismo ecosistema.

Otro aspecto clave es la capacidad de R para generar visualizaciones de alta calidad mediante paquetes como `ggplot2`, que facilitan la exploración y comunicación de resultados. En ciencia de datos, esto es esencial para identificar patrones, tendencias y anomalías en los datos.

En resumen, R no solo es una herramienta técnica, sino una plataforma integral para el análisis de datos, ideal para formar profesionales capaces de extraer conocimiento a partir de grandes volúmenes de información.

Ejemplo práctico: análisis exploratorio sencillo en R

**Objetivo:** Analizar un conjunto de datos básico para comprender su estructura.

```r
# Crear un data frame con información ficticia
datos <- data.frame(
  edad = c(22, 25, 30, 28, 35),
  ingreso = c(12000, 15000, 20000, 18000, 25000)
)

# Visualizar los datos
print(datos)

# Calcular estadísticas básicas
summary(datos)
```

**Explicación:**
En este ejemplo se crea un `data frame` llamado `datos` que contiene edades e ingresos mensuales. La función `print()` permite visualizar la tabla, mientras que `summary()` genera estadísticas descriptivas como mínimos, máximos y medias. Este tipo de análisis exploratorio es uno de los primeros pasos en cualquier proyecto de ciencia de datos y muestra cómo R facilita la comprensión inicial de la información antes de aplicar modelos más avanzados.


Básicos de R

```r
# Comentarios
x <- 5          # Asignación
x = 5           # También válido (menos recomendado)

ls()            # Listar objetos en memoria
rm(x)           # Eliminar objeto
rm(list = ls()) # Limpiar todo
```



Tipos de datos básicos

```r
numeric    # 10, 3.14
integer    # 5L
character  # "texto"
logical    # TRUE / FALSE
```

```r
class(x)       # Tipo de dato
is.numeric(x)  # Verificar tipo
as.numeric(x)  # Convertir tipo
```

Estructuras de datos

Vectores

```r
v <- c(1, 2, 3, 4)
length(v)
mean(v)
sum(v)
```

Matrices

```r
m <- matrix(1:6, nrow = 2)
dim(m)
```

Listas

```r
l <- list(nombre = "Ana", edad = 30)
l$nombre
```

Data Frames (clave en Ciencia de Datos)

```r
df <- data.frame(
  edad = c(20, 25, 30),
  ingreso = c(10000, 15000, 20000)
)

head(df)
str(df)
summary(df)
```

Carga y guardado de datos

```r
setwd("ruta/del/directorio")

read.csv("archivo.csv")
read.table("archivo.txt")

write.csv(df, "salida.csv")
```

Indexación y filtrado

```r
df[1, ]        # Fila 1
df[, 2]        # Columna 2
df$edad        # Columna por nombre

df[df$edad > 25, ]  # Filtrado
```

Operaciones y funciones

```r
+  -  *  /  ^

mean()
median()
sd()
min()
max()
```

```r
apply(df, 2, mean)  # Aplicar función por columnas
```

Control de flujo

```r
if (x > 5) {
  print("Mayor a 5")
} else {
  print("Menor o igual a 5")
}
```

```r
for (i in 1:5) {
  print(i)
}
```

```r
while (x < 10) {
  x <- x + 1
}
```

Funciones propias

```r
mi_funcion <- function(x) {
  return(x^2)
}

mi_funcion(4)
```

Visualización básica

```r
plot(df$edad, df$ingreso)
hist(df$edad)
boxplot(df$ingreso)
```

ggplot2 

```r
library(ggplot2)

ggplot(df, aes(x = edad, y = ingreso)) +
  geom_point() +
  geom_line()
```

Estadística y modelos

```r
cor(df$edad, df$ingreso)

modelo <- lm(ingreso ~ edad, data = df)
summary(modelo)
```

Manejo de paquetes

```r
install.packages("dplyr")
library(dplyr)
```

Manipulación con dplyr (IMPRESCINDIBLE)

```r
df %>%
  filter(edad > 25) %>%
  select(edad, ingreso) %>%
  arrange(desc(ingreso)) %>%
  mutate(ingreso_anual = ingreso * 12)
```

Ayuda y documentación

```r
help(mean)
?mean
example(mean)
```

