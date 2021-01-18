"""
@author: Michał Łopaciuch
@date: 18.01.21
"""
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from src.const import __CONSOLE__


def knn(X_train, X_test, y_train, y_test):
    for n in [3, 5, 11]:
        l = f'knn: {n}'
        knn = KNeighborsClassifier(n_neighbors=n)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        a = knn.score(X_test, y_test)
        __CONSOLE__.log(a, l)
        __CONSOLE__.log(f'\n{confusion_matrix(y_test, y_pred)}',
                        'knn confusion matrix')
