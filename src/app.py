"""
@author: Michał Łopaciuch
@date: 16.01.21
"""

import matplotlib.pyplot as plt
from src.logger import Logger
from os import path
import pandas
import numpy

__DATA_SOURCE_FILE__ = 'winequality-red.csv'


def run():
    console = Logger()
    df = pandas.read_csv(path.join('data', __DATA_SOURCE_FILE__))
    console.log(numpy.where(pandas.isnull(df)), 'Null values in dataset')
    quantity = []
    for col in df:
        console.log(f'Max: {df[col].max()} Min: {df[col].min()} Mean: {df[col].mean()}',
                    f'Basic info for {col}')
        quantity.append([col, float(df[col].mode())])
    console.log(quantity, 'quantity for pie chart')

    labels = [row[0] for row in quantity]
    sizes = [row[1] for row in quantity]
    explode = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()