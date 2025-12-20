import pandas as pd

def limpiar_datos(df):
    df = df.copy()
    df = df.drop_duplicates()
    df['precio_por_tableta'] = pd.to_numeric(df['precio_por_tableta'], errors='coerce')
    df = df.dropna(subset=['precio_por_tableta'])
    return df
