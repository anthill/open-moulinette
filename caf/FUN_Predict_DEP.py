# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 12:33:33 2015

@author: babou
"""
import pandas as pd
import numpy as np
import matplotlib as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import  train_test_split


df = pd.read_csv('data/commune_insee.csv')
df = df[df.DEP.isin(['76', '33', '13'])].reset_index(drop=True)
df = df.ix[:, 3:]

LE = LabelEncoder()
OHE = OneHotEncoder(sparse=False)

df['DEP'] = LE.fit_transform(df.DEP.values)
#df['DEP'] = OHE.fit_transform(df.DEP.values)

feature_label = df.columns[1:]
X, y = df.iloc[:, 1:].values, df.iloc[:, 0].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=12345)

STS = StandardScaler()

X_train_std = STS.fit_transform(X_train)
X_test_std = STS.transform(X_test)

from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(n_estimators=10000,
                                random_state=1234,
                                n_jobs=-1)

forest.fit(X_train_std, y_train)
importances = forest.feature_importances_
indices = np.argsort(importances)[::-1] # pour rendre l'inverse

result = []
for f in range(X_train.shape[1]):
    print ("%2d) %-*s %f" %(f+1, 30,
                            feature_label[f],
                            importances[indices[f]]))
    result.append({feature_label[f] : importances[indices[f]]})

graph = pd.DataFrame(result)
graph.plot(kind='bar', align='center')

print ("training : ", forest.score(X_train, y_train))
