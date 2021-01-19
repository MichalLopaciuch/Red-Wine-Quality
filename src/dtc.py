"""
@author: Michał Łopaciuch
@date: 18.01.21
"""
from sklearn.tree import DecisionTreeClassifier
from src.const import __CONSOLE__


def decision_tree_classifier(X_train, X_test, y_train, y_test):
    dtc = DecisionTreeClassifier()
    dtc.fit(X_train, y_train)
    __CONSOLE__.log(dtc.score(X_test, y_test), 'dtc score')
