# Análisis de precios de medicamentos en Colombia usando datos abiertos

## Descripción del proyecto

Este proyecto realiza un análisis exploratorio, estadístico y visual de datos relacionados con medicamentos comercializados en Colombia, con el fin de identificar patrones en los precios y su relación con factores asociados al costo de los medicamentos.

El análisis se enfoca en responder preguntas como:
- ¿Cómo se distribuyen los precios de los medicamentos por tableta?
- ¿Qué principios activos son más frecuentes en el conjunto de datos?
- ¿Existe relación entre el nivel de precio asignado (bajo, medio, alto) y el valor del medicamento?
- ¿Qué variabilidad presentan los precios dentro del mercado farmacéutico colombiano?

Este trabajo se desarrolla en el contexto de las Ciencias Farmacéuticas, apoyando la comprensión de la estructura de precios y su posible impacto en el acceso a medicamentos.

---

## Origen de los datos (obligatorio)

- **Nombre del conjunto de datos:** Medicamentos – precios y características
- **Plataforma:** Datos Abiertos Colombia
- **URL del dataset:**  
  https://www.datos.gov.co/
- **Fecha de descarga:** 2025
- **Descripción del dataset:**  
  El conjunto de datos contiene información sobre medicamentos comercializados en Colombia, incluyendo principio activo, nombre comercial, fabricante, concentración, unidad de dispensación, precio por tableta y una clasificación cualitativa del nivel de precio (bajo, medio o alto).

Los datos fueron descargados en formato CSV y posteriormente procesados para su análisis.

---

## Metodología

### 1. Carga de datos
Los datos se cargaron utilizando la librería **Pandas**, a partir de archivos CSV descargados directamente de la plataforma Datos Abiertos Colombia.

### 2. Limpieza de datos (Notebook 02)
Se realizaron los siguientes procesos:
- Eliminación de registros duplicados.
- Conversión de la columna `precio_por_tableta` a formato numérico.
- Eliminación de registros con valores nulos en el precio.
- Verificación de consistencia en las variables relevantes para el análisis farmacéutico.

Las funciones de limpieza se implementaron en el archivo `src/limpieza.py`.

### 3. Análisis estadístico (Notebook 03)
Se calcularon las siguientes métricas:
- **Medidas de tendencia central:** media, mediana y moda del precio por tableta.
- **Medidas de dispersión:** varianza, desviación estándar y rango.
- **Tablas de frecuencia y porcentajes** para el principio activo.
- Codificación de la variable cualitativa `factoresprecio` en valores numéricos para análisis correlacional.

Las funciones estadísticas se encuentran en `src/analisis.py`.

### 4. Visualizaciones
Se realizaron visualizaciones utilizando **Matplotlib** y **Seaborn**, incluyendo:
- Histograma del precio por tableta.
- Boxplot del precio por tableta.
- Gráfico de barras por principio activo.
- Heatmap de correlación entre precio y factor de precio.

Las funciones de visualización se encuentran en `src/visualizaciones.py`.

---

## Resultados y hallazgos principales

- Los precios de los medicamentos presentan una distribución asimétrica, con presencia de valores atípicos.
- Algunos principios activos concentran una mayor cantidad de registros, lo que sugiere mayor presencia en el mercado.
- Se observa una relación entre la clasificación del factor de precio y el valor monetario del medicamento, lo cual valida la categorización bajo, medio y alto.
- Existe una alta variabilidad en los precios, lo que puede impactar el acceso equitativo a los medicamentos.

---

## Conclusiones

- El análisis permitió identificar patrones claros en la distribución de precios de medicamentos en Colombia.
- Los datos presentan limitaciones, como la ausencia de información clínica o de consumo real.
- Se recomienda complementar este análisis con datos de demanda, EPS o regiones para apoyar decisiones de política pública.
- A futuro, sería útil analizar la evolución temporal de precios y su relación con regulaciones del mercado farmacéutico.

---

## Estructura del repositorio

📁 Apellido_Nombre/
│
├── README.md
├── data/
│ └── raw/
│ └── datos_medicamentos.csv
│
├── notebooks/
│ ├── 01_exploracion.ipynb
│ ├── 02_limpieza.ipynb
│ └── 03_analisis_visualizaciones.ipynb
│
├── src/
│ ├── limpieza.py
│ ├── analisis.py
│ └── visualizaciones.py


---

## Reproducibilidad

El proyecto puede ejecutarse utilizando Python y las librerías:
- pandas
- numpy
- matplotlib
- seaborn

Los notebooks siguen un flujo secuencial y reutilizan funciones definidas en la carpeta `src`.




