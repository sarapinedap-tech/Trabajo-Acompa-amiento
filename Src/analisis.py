def estadisticas_basicas(df, columna):
    return {
        'media': df[columna].mean(),
        'mediana': df[columna].median(),
        'moda': df[columna].mode().iloc[0],
        'varianza': df[columna].var(),
        'desviacion_estandar': df[columna].std(),
        'rango': df[columna].max() - df[columna].min()
    }

def tabla_frecuencias(df, columna):
    frecuencia = df[columna].value_counts()
    porcentaje = df[columna].value_counts(normalize=True) * 100
    return frecuencia, porcentaje
