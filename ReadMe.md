# Análisis de precios de medicamentos en Colombia usando datos abiertos

## Descripción del proyecto

Este proyecto realiza un análisis exploratorio, estadístico y visual de datos relacionados con medicamentos comercializados en Colombia, con el fin de identificar patrones en los precios equivalentes por tableta o cápsula de diferentes alternativas en el mercado, para un mismo medicamento.

El análisis se enfoca en responder preguntas como:
- ¿Cómo se distribuyen los precios de los medicamentos por tableta?
- ¿Qué principios activos son más frecuentes en el conjunto de datos?
- ¿Existe relación entre el nivel de precio asignado (bajo, medio, alto) y el valor del medicamento?
- ¿Qué variabilidad presentan los precios dentro del mercado farmacéutico colombiano?

Este trabajo se desarrolla en el contexto de las Ciencias Farmacéuticas, apoyando la comprensión de la estructura de precios y su posible impacto en el acceso a medicamentos.

---

## Origen de los datos 

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

- **Significado de los datos:**  
  El análisis por unidad de dispensación mostró que la forma farmacéutica más frecuente es la tableta, representando aproximadamente el 47 % del total de registros, por lo cual el resto de análisis se enfocó principalmente en esta forma farmacéutica. Después de las tabletas les siguen los frascos (17,7 %) y cápsulas (11,9 %). Esta distribución refleja la predominancia de las formas sólidas orales, las cuales suelen asociarse con procesos de fabricación estandarizados y menores costos de producción.

Al continuar con este enfoque de análisis, se evidenció que la alta frecuencia de una forma farmacéutica no implica necesariamente homogeneidad en el precio pues los costos por unidad de tableta variaron notoramiente lo que podría deberse a variables como concentración del principio ctivo, fabricante, indicación terapéutica o variables que no están en el conjunto de datos pero que pueden afectar los costos como principios activos de estrecho margen terapéutico, para patologías poco frecuentes, de control especial, etc. 
En la dispersión del precio por unidad, se observa que algunas formas farmacéuticas menos frecuentes, como ampollas, viales y jeringas prellenadas, presentan una mayor variabilidad de precios, lo que sugiere la influencia de factores adicionales como esterilidad, complejidad tecnológica, condiciones de almacenamiento y uso clínico especializado. En contraste, las tabletas y cápsulas tienden a concentrar una mayor proporción de precios en rangos bajos y medios, lo que puede explicarse por economías de escala, competencia entre fabricantes y una mayor disponibilidad de alternativas terapéuticas.

Este comportamiento evidencia que la forma farmacéutica es un factor relevante en la variabilidad del precio, pero debe analizarse en conjunto con otras características del medicamento para comprender completamente la estructura de costos en el mercado farmacéutico colombianp .Los datos analizados reflejan la estructura de precios de medicamentos comercializados, permitiendo observar cómo varía el costo por tableta según el principio activo y la clasificación del factor de precio. El precio por tableta se utiliza como un indicador económico relevante para evaluar accesibilidad y posibles barreras al acceso a medicamentos.

- **Patrones encontrados:**  
  Se identificó una distribución desigual de los precios, con concentración de valores en rangos bajos y presencia de precios elevados en algunos medicamentos específicos. El análisis por principio activo mostró que ciertos medicamentos aparecen con mayor frecuencia en el conjunto de datos, lo que sugiere una mayor oferta o uso en el mercado.  
  Además, la correlación entre el precio por tableta y la variable `factoresprecio` codificada evidenció una relación positiva, indicando que los medicamentos clasificados como de precio alto presentan, en general, valores monetarios mayores.

- **Hallazgos inesperados:**  
  Se observaron valores atípicos en el precio por tableta que superan ampliamente el promedio del conjunto de datos, lo cual no es uniforme entre todos los principios activos. Esto sugiere que factores adicionales, como fabricante, concentración o presentación, podrían influir de manera significativa en el precio y no están completamente capturados por la clasificación del factor de precio.


## Conclusiones

- **Qué se descubrió:**  
  El análisis de los datos permitió identificar una alta variabilidad en el precio por tableta de los medicamentos analizados. Se evidenció que algunos principios activos concentran una mayor presencia en el mercado y que la clasificación cualitativa del factor de precio (bajo, medio y alto) guarda relación con el valor económico del medicamento, lo cual respalda su utilidad como indicador general de costo.

- **Limitaciones de los datos:**  
  El conjunto de datos no incluye información sobre consumo real, volumen de ventas, ni características clínicas de los pacientes. Además, la variable de factor de precio es una clasificación cualitativa, lo que limita la precisión de los análisis cuantitativos. No se cuenta con una dimensión temporal suficientemente detallada para evaluar cambios en los precios a lo largo del tiempo.

- **Recomendaciones para políticas de salud o gestión farmacéutica:**  
  Los resultados sugieren la necesidad de fortalecer estrategias de regulación y monitoreo de precios de medicamentos, especialmente en aquellos con alta variabilidad de costos. La información analizada puede servir como apoyo para procesos de gestión farmacéutica orientados a mejorar el acceso y la equidad en la disponibilidad de medicamentos.

- **Análisis futuro útil:**  
  Para futuros estudios, sería relevante incorporar datos de consumo por región, EPS o institución de salud, así como analizar la evolución temporal de los precios. También sería útil relacionar los precios con indicadores de demanda y cobertura para evaluar el impacto económico en el sistema de salud.










