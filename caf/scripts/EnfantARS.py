# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 13:47:48 2015

@author: GILLES Armand
"""

import pandas as pd
import glob

df = pd.read_csv('source/EnfantARS2009.csv', sep=";")

df.columns = ['Communes', 'Codes_Insee', 'NB_enfant_ARS_2009', 
              'ARS_5A10_2009', 'ARS_11A14_2009',
              'ARS_15A17_2009']

files = glob.glob('source/EnfantARS*')

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
        list_col.append(col+"_ARS") # ARS = EnfantARS
    else:
        list_col.append(col)
df.columns = list_col

df.to_csv('data/full_EnfantARS.csv', encoding='utf-8', index=False)

## Features 
#NB_enfant_ARS_2009', u'ARS_5A10_2009',
#       u'ARS_11A14_2009', u'ARS_15A17_2009', u'NB_enfant_ARS_2010',
#       u'ARS_5A10_2010', u'ARS_11A14_2010', u'ARS_15A17_2010',
#       u'NB_enfant_ARS_2011', u'ARS_5A10_2011', u'ARS_11A14_2011',
#       u'ARS_15A17_2011', u'NB_enfant_ARS_2012', u'ARS_5A10_2012',
#       u'ARS_11A14_2012', u'ARS_15A17_2012', u'NB_enfant_ARS_2013',
#       u'ARS_5A10_2013', u'ARS_11A14_2013', u'ARS_15A17_2013',
#       u'NB_enfant_ARS_2014', u'ARS_5A10_2014', u'ARS_11A14_2014',
#       u'ARS_15A17_2014'

