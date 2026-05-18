# Técnicas para generación de datos sintéticos 

¿Por qué usar datos sintéticos en el INEGI?

- Contar con una alternativa para cubrir la demanda de información con alta desagregación (microdatos).
- Habilitar la portabilidad de la información para automatizar procesos.
- Contribuir al marco de protección en la privacidad y confidencialidad estadística. 
- Administrar el acceso a la información, dentro del entorno de gobernanza.

### Diagrama para seleccionar que método definir para el proyecto 

![Diagrama](/assets/recursos/diagrama_datos_sinteticos.jpg)


### Métodos para generar datos sintéticos.

- Datos simulados: archivos ficticios: se enfoca en mantener la estructura, pero no el valor analítico de los datos originales.

- Ofuscación estadística preservando la información (IPSO)​: ajusta un “modelo de regresión”, con los datos originales y utiliza tal modelo para generar datos sintéticos.

- Pseudo probabilidad: incorpora los pesos del diseño de selección para estimar la “distribución”, de la población.

- Especificación totalmente condicional (FCS)​: divide la “distribución multidimensional”, de los datos originales en una serie de “distribuciones univariadas condicionales”.

- Red generativa antagónica (GAN)​: Crea un par de redes de “aprendizaje profundo”, que compiten para crear y detectar datos sintéticos. 

### Método Fully Conditional Specification (FCS)

Conceptualmente las características de los datos originales se obtienen de la distribución conjunta de todas las variables de las tablas originales, estas distribuciones no son conocidas a priori, por lo que se estiman usando modelación. El modelaje de distribuciones conjuntas en un solo paso es complejo, por lo que FCS descompone la distribución conjunta en una serie de distribuciones condicionales univariadas.

𝒇𝑿𝟏,𝑿𝟐,… ,𝑿𝒑 = 𝒇𝑿𝟏×𝒇𝑿𝟐|𝑿𝟏×⋯× 𝒇𝑿𝒑|𝑿𝟏,𝑿𝟐,…, 𝑿𝒑

- Model the univariate distribution 𝒇𝑿𝟏 based on the original data
- Generate values from the non conditional model in order to obtain synthetic 𝑿𝟏 values
- Model the conditional distribution 𝒇𝑿𝟐|𝑿𝟏based on the original data
- Generate values from the model using 𝑿𝟏,𝒔𝒚𝒏 values as input to obtain synthetic 𝑿𝟐 values
- Repeat 3 and 4 until the last variable 𝑿𝒑

Es decir, el método avanza generando una variable a la vez, condicionado a las variables previas.

Esto se implementa en dos pasos. 

- Primero, FCS modela la distribución conjunta de cada variable utilizando los datos originales. 
- Segundo, se generan valores sintéticos para cada variable utilizando su modelo utilizando como entrada los valores producidos en las variables anteriores.

### Método Information Preserving Statistical Obfuscation (IPSO) 

En este método los datos originales se consideran estar conformados por dos subconjuntos de variables: la matriz X es información no confidencial y la matriz Y es información confidencial.
Este método asume la normalidad multivariada en la distribución de un modelo de regresión lineal don la matriz X es la componente independiente y Y es la dependiente.
Se ajusta el modelo 𝒀= 𝛽𝑿+ 𝜀en los datos originales para obtener  y se calcula . Se agrega ruido normalmente distribuido a  para crear los valores sintéticos Y′.

𝑌 = 𝑋  𝛽 + Σ

IPSO añade un pasos extra para forzar la igualdad  o .

𝜷𝒐𝒓𝒊𝒈𝒊𝒏𝒂𝒍 = 𝜷 𝒔𝒚𝒏𝒕𝒉𝒆𝒕𝒊𝒄 and 𝜮 𝒐𝒓𝒊𝒈𝒊𝒏𝒂𝒍 = 𝜮 𝒔𝒚𝒏𝒕𝒉𝒆𝒕𝒊𝒄

### Método Generative Adversarial Networks (GAN)      

La idea detrás de las GAN es crear dos modelos de redes neuronales. Uno es llamado el generador el cual recibe valores aleatorios y los transforma en un registro. 
El otro modelo es llamado el discriminador, recibe un registro y trata de discernir si es real o sintético. 
Estos dos modelos son entrenados de manera iterativa con el objetivo de vencer a su contraparte hasta que se logra un equilibrio entre ambos. 
El generador es entrenado para poder crear registros que parezcan reales, mientras el discriminador es entrenado para encontrar las sutiles diferencias entre los datos reales y generados.

___________

> Naciones Unidas. (2023). Synthetic data for official statistics: A starter guide. UNECE. https://unece.org/statistics/publications/synthetic-data-official-statistics-starter-guide

