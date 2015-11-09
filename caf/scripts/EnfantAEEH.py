# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 13:47:48 2015

@author: GILLES Armand
"""

import pandas as pd
import glob

df = pd.read_csv('source/EnfantAEEH2009.csv', sep=";")

df.columns = ['Communes', 'Codes_Insee', 'NB_enfant_AEEH_2009']

files = glob.glob('source/EnfantAEEH*')

# Warning no file for 2010, waiting fix from CAF

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
    if "nb_allocataires" in col.lower(): 
        list_col.append(col+"_AEEH") # AEEH = EnfantAEEH
    else:
        list_col.append(col)
df.columns = list_col

final_count = df.shape[0]

df.to_csv('data/full_EnfantAEEH.csv', encoding='utf-8', index=False)

## Features 
#u'NB_enfant_AEEH_2009',
#       u'NB_enfant_AEEH_2010', u'NB_enfant_AEEH_2011', u'AEEH_0A2_2011',
#       u'AEEH_3A5_2011', u'AEEH_6A11_2011', u'AEEH_12A15_2011',
#       u'AEEH_16A17_2011', u'AEEH_18A20_2011', u'NB_enfant_AEEH_2012',
#       u'AEEH_0A2_2012', u'AEEH_3A5_2012', u'AEEH_6A11_2012',
#       u'AEEH_12A15_2012', u'AEEH_16A17_2012', u'AEEH_18A20_2012',
#       u'NB_enfant_AEEH_2013', u'AEEH_0A2_2013', u'AEEH_3A5_2013',
#       u'AEEH_6A11_2013', u'AEEH_12A15_2013', u'AEEH_16A17_2013',
#       u'AEEH_18A20_2013', u'NB_enfant_AEEH_2014', u'AEEH_0A2_2014',
#       u'AEEH_3A5_2014', u'AEEH_6A11_2014', u'AEEH_12A15_2014',
#       u'AEEH_16A17_2014', u'AEEH_18A20_2014'

