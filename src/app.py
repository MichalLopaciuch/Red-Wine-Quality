"""
@author: Michał Łopaciuch
@date: 18.01.21
"""

import numpy
import pandas
from os import path
from src.const import (
    __DATA_SOURCE_FILE__,
    __CONSOLE__
)
import matplotlib.pyplot as plt


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
        print(col, float(df[col].mode()))
    __CONSOLE__.log(mode, 'mode for pie chart')

    labels, sizes = [row[0] for row in mode], [row[1] for row in mode]

    y_pos = numpy.arange(len(labels))
    plt.bar(y_pos, sizes, align='center', alpha=0.5)
    plt.xticks(y_pos, labels)
    plt.title('Component')
    plt.ylabel('Mode')

    plt.show()


def run():
    """A main function with bussiness logic."""
    df = pandas.read_csv(path.join('data', __DATA_SOURCE_FILE__))
    preliminary_informations(df)
