"""
Visualización del archivo f1_circuits.csv

Este script muestra paso a paso cómo cargar, explorar y visualizar
el contenido del archivo f1_circuits.csv utilizando Python.

"""

# ================================
# 1. Importación de librerías
# ================================

# Importamos la librería pandas, utilizada para cargar y manipular datos en forma tabular
import pandas as pd

# Importamos matplotlib.pyplot para crear gráficos y visualizaciones
import matplotlib.pyplot as plt

# ================================
# 2. Carga del archivo CSV
# ================================

# Leemos el archivo CSV llamado 'f1_circuits.csv'
# El archivo debe estar en la misma carpeta que este script
# El resultado se guarda en un DataFrame llamado 'df'
df = pd.read_csv('f1_circuits.csv')

# Mostramos las primeras 5 filas del DataFrame
# Esto permite verificar que los datos se cargaron correctamente
print("Primeras filas del dataset:
")
print(df.head())

# ================================
# 3. Exploración básica del dataset
# ================================

# Imprimimos información general del DataFrame:
# - Número de filas y columnas
# - Nombre de cada columna
# - Tipo de dato de cada columna
# - Cantidad de valores no nulos
print("
Información general del dataset:
")
df.info()

# ================================
# 4. Visualización gráfica
# ================================

# Creamos una figura y definimos su tamaño para mejorar la visualización
plt.figure(figsize=(10, 5))

# Creamos un gráfico de dispersión (scatter plot)
# Usamos:
# - La columna 'lng' (longitud) en el eje X
# - La columna 'lat' (latitud) en el eje Y
plt.scatter(df['lng'], df['lat'])

# Etiquetamos el eje X con una descripción clara
plt.xlabel('Longitud')

# Etiquetamos el eje Y con una descripción clara
plt.ylabel('Latitud')

# Agregamos un título descriptivo al gráfico
plt.title('Ubicación geográfica de los circuitos de Fórmula 1')

# Mostramos el gráfico en pantalla
plt.show()

# ================================
# Fin del script
# ================================
