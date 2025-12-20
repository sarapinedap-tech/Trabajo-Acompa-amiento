import pandas as pd

def cargar_datos_limpios(ruta):
    """
    Carga el archivo limpio desde CSV
    """
    df = pd.read_csv(ruta)
    return df

def limpiar_datos(df):
    """
    Aplica los mismos pasos de limpieza del notebook 02
    """
    df = df.copy()

    # Eliminar duplicados
    df = df.drop_duplicates()

    # Convertir precio a numérico
    df['precio_por_tableta'] = pd.to_numeric(
        df['precio_por_tableta'],
        errors='coerce'
    )

    # Eliminar registros sin precio
    df = df.dropna(subset=['precio_por_tableta'])

    return df