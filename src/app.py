"""
@author: Michał Łopaciuch
@date: 18.01.21
"""
from src.const import __DATA_SOURCE_FILE__
from os import path
import pandas

from src.preliminary_info import preliminary_informations
from sklearn.model_selection import train_test_split
from src.dtc import decision_tree_classifier as dtc
from src.naivebayes import nvb
from src.knn import knn


def run():
    """A main function with bussiness logic."""
    df = pandas.read_csv(path.join('data', __DATA_SOURCE_FILE__))
    preliminary_informations(df)
    __COLUMNS__ = df.columns
    X, y = df[__COLUMNS__[:-1]], df[__COLUMNS__[-1]]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=1)

    nvb(X_train, X_test, y_train, y_test)
    knn(X_train, X_test, y_train, y_test)
    dtc(X_train, X_test, y_train, y_test)
