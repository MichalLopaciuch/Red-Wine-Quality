"""
@author: Michał Łopaciuch
@date: 18.01.21
"""
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from src.const import __CONSOLE__


def naive_bayes(X_train, X_test, y_train, y_test):
    gnb = GaussianNB()
    y_pred = gnb.fit(X_train, y_train).predict(X_test)
    __CONSOLE__.log(f'mislabeled points out of a total {X_test.shape[0]} points : {(y_test != y_pred).sum()}',
                    'Gaussian Naive Bayes mislabeled')
    __CONSOLE__.log(f'{accuracy_score(y_test, y_pred)}',
                    'Gaussian Naive Bayes accuracy')
