# -*- coding: utf-8 -*-
"""KNN practic.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1X-Uo-hC2I1W8Ookt4cy_ZJON2PY-io6t
"""

import pandas as pd
from google.colab import drive
drive.mount('/content/drive')

ds= pd.read_csv('/content/drive/MyDrive/Colab Notebooks/loan_approval_dataset.csv')

ds.head()

ds.isnull().sum()

ds.describe()

x=ds.drop('Loan_Approved',axis=1)
y=ds['Loan_Approved']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.fit_transform(x_test)

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)

y_pred=knn.predict(x_test)

from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
print(accuracy_score(y_test,y_pred))

print(confusion_matrix(y_test,y_pred))

print(classification_report(y_test,y_pred))