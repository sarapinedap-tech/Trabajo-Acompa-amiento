import matplotlib.pyplot as plt
import seaborn as sns

def histograma(df, columna, titulo):
    sns.histplot(df[columna], kde=True)
    plt.title(titulo)
    plt.xlabel(columna)
    plt.ylabel('Frecuencia')
    plt.show()

def boxplot(df, columna, titulo):
    sns.boxplot(x=df[columna])
    plt.title(titulo)
    plt.show()

def barras_categoria(df, columna, titulo):
    sns.countplot(y=columna, data=df)
    plt.title(titulo)
    plt.show()

def heatmap_correlacion(df, columnas, titulo):
    corr = df[columnas].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title(titulo)
    plt.show()
