import pandas as pd
import matplotlib.pyplot as plt

# Función para formatear los valores del eje x
def thousands_formatter(x, pos):
    return '{:,.0f}'.format(x / 1000000)

def graph_histogram(df: pd.DataFrame, column: str, n_bins: int, max_value=None, min_value=None):
    fig, ax = plt.subplots(figsize=(14, 5))

    plt.title(f'Distribución de {df[column].name}', size=16, color='white', weight=700)

    plt.grid(visible=True, linewidth=0.1, color='white')
    fig.patch.set_facecolor('#21252b') 
    ax.set_facecolor('#282c34') 


    for group in df['alta'].unique():
        
        filtered_df = df[df['alta']==group]
        
        plt.hist(
            filtered_df[column],
            bins=n_bins,
            alpha=0.5
        )

    plt.xlabel(f'{df[column].name}', size=13, weight=700, color='white')
    plt.xticks(color='white', size=12)

    plt.ylabel(f'Cantidad de clientes', size=13, weight=700, color='white')
    plt.yticks(color='white', size=12)

    if max_value is None:
        max_value = df[column].max()

    if min_value is None:
        min_value = df[column].min()

    plt.xlim(min_value, max_value)
    plt.show()

def adjust_decimal_format(column: pd.Series):
    try:
        new_column = column.apply(lambda x: float(str(x).replace(',', '.').replace('nan', '0')))
        return new_column
    
    except:
        return new_column