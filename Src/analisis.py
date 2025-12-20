import pandas as pd

def info_general(df):
    """
    Información básica del dataset (equivalente a df.info() y df.describe())
    """
    info = df.info()
    descripcion = df.describe(include='all')
    return info, descripcion

def estadisticas_precio(df):
    """
    Medidas estadísticas usadas en el análisis
    """
    return {
        'media': df['precio_por_tableta'].mean(),
        'mediana': df['precio_por_tableta'].median(),
        'moda': df['precio_por_tableta'].mode().iloc[0],
        'varianza': df['precio_por_tableta'].var(),
        'desviacion_estandar': df['precio_por_tableta'].std(),
        'rango': df['precio_por_tableta'].max() - df['precio_por_tableta'].min()
    }

def tabla_frecuencia_principio_activo(df):
    """
    Tabla de frecuencias y porcentajes
    """
    frecuencia = df['principio_activo'].value_counts()
    porcentaje = df['principio_activo'].value_counts(normalize=True) * 100
    return frecuencia, porcentaje

def codificar_factoresprecio(df):
    """
    Convierte factoresprecio (Bajo, Medio, Alto) a valores numéricos
    """
    mapa = {
        'Bajo': 1,
        'Medio': 2,
        'Alto': 3
    }

    df = df.copy()
    df['factoresprecio_num'] = df['factoresprecio'].map(mapa)

    return df