# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 13:47:48 2015

@author: GILLES Armand
"""

import pandas as pd
import glob

df = pd.read_csv('source/RsaPersCom2009.csv', sep=";")

df.columns = ['Communes', 'Codes_Insee', 'NB_Pers_par_Foyer_Alloc_2009', 
              'NB_Pers_couv_RSA_2009', 'RSA_SOCLE_non_Majore_Pers_couv_2009',
              'RSA_SOCLE_Majore_Pers_couv_2009', 'RSA_activite_Pers_couv_2009']

files = glob.glob('source/RsaPersCom*')

for path_file in files:
    year = str(path_file[-8:-4])
    if (year != '2009'):
        df_temp = pd.read_csv(path_file, sep=';')
        
        # Rename Col with year
        year_col = ['Communes', 'Codes_Insee']
        features_col = []
        for col in df_temp.columns[2:]:
            year_col.append(col +"_"+ year)
            features_col.append(col +"_"+ year)
        
        # Adding key for mergeing
        features_col.append('Codes_Insee')
        df_temp.columns = year_col
        df = pd.merge(df, df_temp[features_col], how='inner', on='Codes_Insee')


# Rename col to have unique name in futur merge
list_col = []
for col in df.columns:
    if col[0:15] in 'NB_Pers_par_Foyer': 
        list_col.append(col+"_RPC") # RPC = RsaPersCom
    else:
        list_col.append(col)
df.columns = list_col

df.to_csv('data/full_RsaPersCom.csv', encoding='utf-8', index=False)

## Features 
#u'NB_Pers_par_Foyer_Alloc_2009_RPC',
#       u'NB_Pers_couv_RSA_2009', u'RSA_SOCLE_non_Majore_Pers_couv_2009',
#       u'RSA_SOCLE_Majore_Pers_couv_2009', u'RSA_activite_Pers_couv_2009',
#       u'NB_Pers_par_Foyer_Alloc_2010_RPC', u'NB_Pers_couv_RSA_2010',
#       u'RSA_SOCLE_non_Majore_Pers_couv_2010',
#       u'RSA_SOCLE_Majore_Pers_couv_2010', u'RSA_activite_Pers_couv_2010',
#       u'NB_Pers_par_Foyer_Alloc_2011_RPC', u'NB_Pers_couv_RSA_2011',
#       u'RSA_SOCLE_non_Majore_Pers_couv_2011',
#       u'RSA_SOCLE_Majore_Pers_couv_2011', u'RSA_activite_Pers_couv_2011',
#       u'NB_Pers_par_Foyer_Alloc_2012_RPC', u'NB_Pers_couv_RSA_2012',
#       u'RSA_SOCLE_non_Majore_Pers_couv_2012',
#       u'RSA_SOCLE_Majore_Pers_couv_2012', u'RSA_activite_Pers_couv_2012',
#       u'NB_Pers_par_Foyer_Alloc_2013_RPC', u'NB_Pers_couv_RSA_2013',
#       u'RSA_SOCLE_non_Majore_Pers_couv_2013',
#       u'RSA_SOCLE_Majore_Pers_couv_2013', u'RSA_activite_Pers_couv_2013',
#       u'NB_Pers_par_Foyer_Alloc_2014_RPC', u'NB_Pers_couv_RSA_2014',
#       u'RSA_SOCLE_non_Majore_Pers_couv_2014',
#       u'RSA_SOCLE_Majore_Pers_couv_2014', u'RSA_activite_Pers_couv_2014'

