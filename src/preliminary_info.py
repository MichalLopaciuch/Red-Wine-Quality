"""
@author: Michał Łopaciuch
@date: 18.01.21
"""
from src.const import __CONSOLE__
import matplotlib.pyplot as plt
import seaborn as sns
import pandas
import numpy


def preliminary_informations(df):
    """A function used to collect basic informations about the dataset."""
    __CONSOLE__.log(numpy.where(pandas.isnull(df)),
                    'Null values in dataset')
    mode = []
    for col in df:
        __CONSOLE__.log(f'Max: {df[col].max()} Min: {df[col].min()} Mean: {df[col].mean()}',
                        f'Basic info for {col}')
        if col not in ['free sulfur dioxide', 'quality']:
            mode.append([col, float(df[col].mode())])
    __CONSOLE__.log(mode, 'mode for pie chart')

    labels, sizes = [row[0] for row in mode], [row[1] for row in mode]

    y_pos = numpy.arange(len(labels))
    plt.bar(y_pos, sizes, align='center', alpha=0.5)
    plt.xticks(y_pos, labels)
    plt.title('Component')
    plt.ylabel('Mode')
    with open('docs/mode.png', 'wb') as f:
        plt.savefig(f)
    sns.countplot(x='quality', data=df)
    with open('docs/quality.png', 'wb') as f:
        plt.savefig(f)
    corr = df.corr()
    plt.subplots(figsize=(15, 10))
    sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns,
                annot=True, cmap=sns.diverging_palette(220, 20, as_cmap=True))
    with open('docs/corr.png', 'wb') as f:
        plt.savefig(f)
