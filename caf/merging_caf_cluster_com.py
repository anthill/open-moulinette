# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 02:11:33 2015

@author: GILLES Armand
"""

import pandas as pd
import matplotlib.pyplot as plt
import glob
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


def get_color(x):
    return colors[x]

ref_cluster = pd.read_csv('data/ref_com_cluster.csv')

caf_files = glob.glob('data/caf_*')

distance = pd.DataFrame()

min_max = MinMaxScaler()

for path_file in caf_files:
    my_year = path_file[-8:-4]
    print my_year
    df = pd.read_csv(path_file, dtype={'Codes_Insee' : object})
    df.fillna(0, inplace=True)
    df = pd.merge(df, ref_cluster, how='inner', left_on='Codes_Insee' ,right_on='COM')
    
#    df = df[df.DEP == '76']
#    df = df.head(len(df) / 4)

    features = [u'ALL_PRIM',u'rsa_NB_allocataires']
#               u'NB_allocataire_RSA', u'Dont_RSA_jeune', u'RSA_SOCLE_non_Majore',
#               u'RSA_SOCLE_Majore', u'RSA_activite']
    
    # Standardization
    df[features] = min_max.fit_transform(df[features])
               
    # PCA Transformation
               
    X = df[features].values
    pca = PCA(n_components=2).fit(X)
    X_pca = pca.transform(X)
#    X = X_pca; print "PCA transformation"; pca_bool = 1
    
    df["pca_1"] = X[:, 0]
    df["pca_2"] = X[:, 1]
    
    if (my_year == "2009"):
    
        k_means = KMeans(init='k-means++', n_clusters=3, n_init=10).fit(X)
    
        k_means_labels = k_means.labels_
        k_means_cluster_centers = k_means.cluster_centers_
        k_means_labels_unique = np.unique(k_means_labels)
        
        df['cluster_caf'] = pd.Series(k_means_labels)
        df[['Codes_Insee', 'cluster_caf']].to_csv('data/ref_caf_cluster.csv')
        print "Create Ref cluster CAF 2009"
        print df.cluster_caf.value_counts()
    else:
        ref_caf_cluster = pd.read_csv('data/ref_caf_cluster.csv')
        df = pd.merge(df, ref_caf_cluster, how='inner', on='Codes_Insee')
        print df.cluster_caf.value_counts()
    
    colors = ['#7fff00','#ff00ff','#00bfff','#ff8c00']
    df['color'] = df.cluster.apply(lambda x: get_color(x))
    # Reverse standardization
    df[features] = min_max.inverse_transform(df[features])
    
    if ("2009" == my_year):
        
        distance = df[['Codes_Insee', 'cluster', 'pca_1', 'pca_1']]
        distance.rename(columns={'pca_1':'pca_1_2009'}, inplace=True)
        distance.rename(columns={'pca_2':'pca_2_2009'}, inplace=True)
    else:
        dist_features = ['Codes_Insee', "pca_1", "pca_2"]
        distance = pd.merge(distance, df[dist_features], how='inner', on='Codes_Insee')
        distance.rename(columns={'pca_1':'pca_1_'+my_year}, inplace=True)
        distance.rename(columns={'pca_2':'pca_2_'+my_year}, inplace=True)
    
    dico_city = {#'88190' : 'Frizon'} # DEP 88
                #'85095' : 'Froidfond'} # DEP 85 vieux
                 '57242' : 'Gandrange'} #, ArcelorMittal DEP 57
                 #'91659' : 'Villabe'}#, # Jeune DEP 91 
                 #'78440' : 'Les Mureaux'} #, # city
                 #'03082' : 'Commentry'}
    city_key = dico_city.keys()
    
    plt.figure(figsize=(10,8))
    plt.xlim(-0.2, 1.2)
    plt.ylim(-0.2, 1.2)
    for k, col in zip(range(df.cluster_caf.max() + 1), colors):
        my_members = df.cluster.values == k
        plt.scatter(X[my_members, 0], X[my_members, 1], color=col,
                 marker='.', alpha=0.3)
        
    for com in city_key:
        anno = df[df.Codes_Insee == com]
        plt.annotate(dico_city.get(com), xy=(anno.pca_1, anno.pca_2),
                         xytext=(anno.pca_1 +0.4, anno.pca_2 + 0.1), arrowprops=dict(arrowstyle="->", connectionstyle="angle"))
    plt.title('Les types de ville et les aides de la caf %s' % my_year)
    plt.xlabel('De plus en plus de naissance')
    plt.ylabel('De plus en plus de personne touchant le RSA')
    plt.show()

distance.to_csv('data/distance_aide_by_année_cluster_com.csv', encoding='utf-8', index=False)
    