# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 13:47:48 2015

@author: GILLES Armand
"""

import pandas as pd
import glob

df = pd.read_csv('source/EnfantAgeCom2009.csv', sep=";")

df.columns = ['Communes', 'Codes_Insee', 'NB_Enfants_0_2_ans_2009', 
              'NB_Enfants_3_5_ans_2009', 'NB_Enfants_6_11_ans_2009',
              'NB_Enfants_12_15_ans_2009', 'NB_Enfants_16_17_ans_2009',
              'NB_Enfants_18_19_ans_2009', 'NB_Enfants_20_24_ans_2009',
              'NB_Enfants_2009']

files = glob.glob('source/EnfantAgeCom*')

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
    # We have to add indicator to create unique feature name before merging
    if col not in ['Communes', 'Codes_Insee']:
        list_col.append(col+"_EAC") # EAC = EnfantAgeCom
    else:
        list_col.append(col)
df.columns = list_col

final_count = df.shape[0]

df.to_csv('data/full_EnfantAgeCom.csv', encoding='utf-8', index=False)

## Features 
#u'NB_Enfants_0_2_ans_2009_EAC',
#       u'NB_Enfants_3_5_ans_2009_EAC', u'NB_Enfants_6_11_ans_2009_EAC',
#       u'NB_Enfants_12_15_ans_2009_EAC', u'NB_Enfants_16_17_ans_2009_EAC',
#       u'NB_Enfants_18_19_ans_2009_EAC', u'NB_Enfants_20_24_ans_2009_EAC',
#       u'NB_Enfants_2009_EAC', u'NB_Enfants_0_2_ans_2011_EAC',
#       u'NB_Enfants_3_5_ans_2011_EAC', u'NB_Enfants_6_11_ans_2011_EAC',
#       u'NB_Enfants_12_15_ans_2011_EAC', u'NB_Enfants_16_17_ans_2011_EAC',
#       u'NB_Enfants_18_19_ans_2011_EAC', u'NB_Enfants_20_24_ans_2011_EAC',
#       u'NB_Enfants_2011_EAC', u'NB_Enfants_0_2_ans_2012_EAC',
#       u'NB_Enfants_3_5_ans_2012_EAC', u'NB_Enfants_6_11_ans_2012_EAC',
#       u'NB_Enfants_12_15_ans_2012_EAC', u'NB_Enfants_16_17_ans_2012_EAC',
#       u'NB_Enfants_18_19_ans_2012_EAC', u'NB_Enfants_20_24_ans_2012_EAC',
#       u'NB_Enfants_2012_EAC', u'NB_Enfants_0_2_ans_2013_EAC',
#       u'NB_Enfants_3_5_ans_2013_EAC', u'NB_Enfants_6_11_ans_2013_EAC',
#       u'NB_Enfants_12_15_ans_2013_EAC', u'NB_Enfants_16_17_ans_2013_EAC',
#       u'NB_Enfants_18_19_ans_2013_EAC', u'NB_Enfants_20_24_ans_2013_EAC',
#       u'NB_Enfants_2013_EAC', u'NB_Enfants_0_2_ans_2014_EAC',
#       u'NB_Enfants_3_5_ans_2014_EAC', u'NB_Enfants_6_11_ans_2014_EAC',
#       u'NB_Enfants_12_15_ans_2014_EAC', u'NB_Enfants_16_17_ans_2014_EAC',
#       u'NB_Enfants_18_19_ans_2014_EAC', u'NB_Enfants_20_24_ans_2014_EAC',
#       u'NB_Enfants_2014_EAC'

