import matplotlib.pyplot as plt
import seaborn as sns


def histograma_precio(df):
    sns.histplot(df['precio_por_tableta'], kde=True)
    plt.title('Distribución del precio por tableta')
    plt.xlabel('Precio por tableta')
    plt.ylabel('Frecuencia')
    plt.show()


def boxplot_precio(df):
    sns.boxplot(x=df['precio_por_tableta'])
    plt.title('Boxplot del precio por tableta')
    plt.show()


def barras_principio_activo(df):
    sns.countplot(y='principio_activo', data=df)
    plt.title('Distribución por principio activo')
    plt.show()


def heatmap_correlacion_precio_factor(df):
    corr = df[['precio_por_tableta', 'factoresprecio_num']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlación entre precio y factor de precio')
    plt.show()

