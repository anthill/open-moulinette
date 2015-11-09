# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 12:43:38 2015

@author: GILLES Armand
"""

import pandas as pd

distance = pd.read_csv('data/distance_aide_by_année_cluster_com.csv')

commune = pd.read_csv('data/commune_insee.csv', usecols=['COM', 'LIBCOM', 'REG', 'DEP', 'P11_POP'], dtype={'COM' : object})

distance = pd.merge(distance, commune, how='inner', left_on='Codes_Insee', right_on='COM')

usefull_col = ['Codes_Insee', 'LIBCOM', 'REG', 'DEP', 'dist2014', 'P11_POP', ]

distance['dist2010'] = distance.apply(lambda row: pd.np.linalg.norm(row.pca_1_2009 - row.pca_1_2010), axis=1)
distance['dist2011'] = distance.apply(lambda row: pd.np.linalg.norm(row.pca_1_2009 - row.pca_1_2011), axis=1)
distance['dist2012'] = distance.apply(lambda row: pd.np.linalg.norm(row.pca_1_2009 - row.pca_1_2012), axis=1)
distance['dist2013'] = distance.apply(lambda row: pd.np.linalg.norm(row.pca_1_2009 - row.pca_1_2013), axis=1)
distance['dist2014'] = distance.apply(lambda row: pd.np.linalg.norm(row.pca_1_2009 - row.pca_1_2014), axis=1)
