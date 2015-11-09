# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 00:17:46 2015

@author: babou
"""

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN



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

db = DBSCAN(eps=16).fit(X)

core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print('Estimated number of clusters: %d for DBSCAN' % n_clusters_)


import matplotlib.pyplot as plt
unique_labels = set(labels)
#from mpl_toolkits.mplot3d import Axes3D
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
#unique_labels = set(labels)
#colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
#for k, col in zip(unique_labels, colors):
#    if k == -1:
#        # Black used for noise.
#        col = 'k'
#
#    class_member_mask = (labels == k)
#    
#    xyz = X[class_member_mask & core_samples_mask]
#    plt.plot(xyz[:, 0], xyz[:, 1], xyz[:, 2], 'o', markerfacecolor=col,
#             markeredgecolor='k', markersize=14)
#
#    xyz = X[class_member_mask & ~core_samples_mask]
#    plt.plot(xyz[:, 0], xyz[:, 1], xyz[:, 2],'o', markerfacecolor=col,
#             markeredgecolor='k', markersize=6, alpha=0.3)
#
#plt.title('Estimated number of clusters: %d' % n_clusters_)
#plt.show()



colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = 'k'
    class_member_mask = (labels == k)    
    xy= X[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], xy, 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)
    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=6, alpha=0.3)
plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()
