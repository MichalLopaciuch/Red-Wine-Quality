"""
@author: Michał Łopaciuch
@date: 18.01.21
"""

from os import path
import pandas
import numpy

from src.const import (
    __DATA_SOURCE_FILE__,
    __CONSOLE__
)

from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from src.naivebayes import naive_bayes
from src.knn import knn

__COLUMNS__ = []


def preliminary_informations(df):
    """A function used to collect basic informations about the dataset."""
    __CONSOLE__.log(numpy.where(pandas.isnull(df)),
                    'Null values in dataset')

    mode = []
    for col in df:
        __COLUMNS__.append(col)
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
    # plt.show()


def run():
    """A main function with bussiness logic."""
    df = pandas.read_csv(path.join('data', __DATA_SOURCE_FILE__))
    preliminary_informations(df)
    X, y = df[__COLUMNS__[:-1]], df[__COLUMNS__[-1]]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.33, random_state=0)

    naive_bayes(X_train, X_test, y_train, y_test)
    knn(X_train, X_test, y_train, y_test)
