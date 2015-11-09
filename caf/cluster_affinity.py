# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 00:24:06 2015

@author: GILLES Armand
"""

import pandas as pd
import numpy as np
from sklearn.cluster import AffinityPropagation

test = pd.read_csv('data/commune_insee.csv')

df = test[test.DEP.isin(['76', '27'])].reset_index(drop=True)

features = df.columns.tolist()

# unusefull col
for col in ["LIBCOM","REG","DEP"]:
    features.remove(col)

# key
features.remove('COM')

df.fillna(value=0, inplace=True)

X = df[features].values

# PCA Transformation
from sklearn.decomposition import PCA

pca = PCA(n_components=2).fit(X)
X_pca = pca.transform(X)
X = X_pca; print "PCA transformation"; pca_bool = 1
af = AffinityPropagation(preference=-200, max_iter=300, verbose=True).fit(X)

cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_

vn_clusters_ = len(cluster_centers_indices)        


print('Estimated number of clusters: %d for AffinityPropagation' % n_clusters_)



# Plot result
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#
#from itertools import cycle
#
#colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
#fig = plt.figure().gca(projection='3d')
#
#if pca_bool == 0: # If no PCA transforamtion DO classic feature name
#    fig.set_xlabel('Number of entries by day')
#    fig.set_ylabel('Number of differents station')
#    fig.set_zlabel('Mean time by run')
#else: # If PCA transformation rename axes.
#    fig.set_xlabel('First PCA direction')
#    fig.set_ylabel('Seconde PCA direction')
#    fig.set_zlabel('Three PCA direction')
#
#for k, col in zip(range(n_clusters_), colors):
#    class_members = labels == k
#    cluster_center = X[cluster_centers_indices[k]]
#    fig.plot(X[class_members, 0], X[class_members, 1], X[class_members, 2], col + '.')
#   # fig.plot(cluster_center[0], cluster_center[1], cluster_center[2], 'o', markerfacecolor=col,
#   #          markeredgecolor='k', markersize=14)
#    for x in X[class_members]:
#        fig.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], [cluster_center[2], x[2]], col)
#
#plt.title('Estimated number of clusters: %d' % n_clusters_)
#plt.show()


import matplotlib.pyplot as plt
from itertools import cycle
plt.close('all')
plt.figure(1)
plt.clf()
colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    class_members = labels == k
    cluster_center = X[cluster_centers_indices[k]]
    plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
    plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)
    for x in X[class_members]:
        plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)
plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()
