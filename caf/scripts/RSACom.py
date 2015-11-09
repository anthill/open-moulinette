# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 13:47:48 2015

@author: GILLES Armand
"""

import pandas as pd
import glob

df = pd.read_csv('source/RSACom2009.csv', sep=";")

df.columns = ['Communes', 'Codes_Insee', 'NB_allocataires_2009', 
              'NB_allocataire_RSA_2009', 'Dont_RSA_jeune_2009',
              'RSA_SOCLE_non_Majore_2009', 'RSA_SOCLE_Majore_2009',
              'RSA_activite_2009']

files = glob.glob('source/RSACom*')

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
    if "nb_allocataires" in col.lower(): # NB_Allocataires (2009) != NB_allocataires (2010)
        list_col.append(col+"_RSAC") # RSAC = RSACom
    else:
        list_col.append(col)
df.columns = list_col

df.to_csv('data/full_RSACom.csv', encoding='utf-8', index=False)

## Features 
#u'NB_allocataires_2009_RSAC',
#       u'NB_allocataire_RSA_2009', u'Dont_RSA_jeune_2009',
#       u'RSA_SOCLE_non_Majore_2009', u'RSA_SOCLE_Majore_2009',
#       u'RSA_activite_2009', u'NB_allocataires_2010_RSAC',
#       u'NB_allocataire_RSA_2010', u'Dont_RSA_jeune_2010',
#       u'RSA_SOCLE_non_Majore_2010', u'RSA_SOCLE_Majore_2010',
#       u'RSA_activite_2010', u'NB_allocataires_2011_RSAC',
#       u'NB_allocataire_RSA_2011', u'Dont_RSA_jeune_2011',
#       u'RSA_SOCLE_non_Majore_2011', u'RSA_SOCLE_Majore_2011',
#       u'RSA_activite_2011', u'NB_allocataires_2012_RSAC',
#       u'NB_allocataire_RSA_2012', u'Dont_RSA_jeune_2012',
#       u'RSA_SOCLE_non_Majore_2012', u'RSA_SOCLE_Majore_2012',
#       u'RSA_activite_2012', u'NB_allocataires_2013_RSAC',
#       u'NB_allocataire_RSA_2013', u'Dont_RSA_jeune_2013',
#       u'RSA_SOCLE_non_Majore_2013', u'RSA_SOCLE_Majore_2013',
#       u'RSA_activite_2013', u'NB_allocataires_2014_RSAC',
#       u'NB_allocataire_RSA_2014', u'Dont_RSA_jeune_2014',
#       u'RSA_SOCLE_non_Majore_2014', u'RSA_SOCLE_Majore_2014',
#       u'RSA_activite_2014'

