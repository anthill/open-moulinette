# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 14:41:12 2015

@author: GILLES Armand
"""


import pandas as pd
import glob

df = pd.read_csv('source/NivComTotal2009.csv', sep=";")
origin_count = df.shape[0]
#df.shape() = (36729, 5)
df.columns = ['Communes', 'Codes_Insee', 'NB_Pers_par_Foyer_Alloc_2009', 
              'NB_Enfants_0_2_ans', 'NB_Enfants_3_5_ans', 'NB_Enfants']

files = glob.glob('source/NivComTotal*')

for path_file in files:
    year = str(path_file[-8:-4])
    if (year != '2009'):
        df_temp = pd.read_csv(path_file, sep=';')
        
        # Rename Col with year
        year_col = ['Communes', 'Codes_Insee']
        features_col = []
        for col in df_temp.columns[-4:]:
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
        list_col.append(col+"_NCT") # NCT = NivComTotal
    else:
        list_col.append(col)
df.columns = list_col

final_count = df.shape[0]

if (origin_count == final_count):
    print "File NivComTotal is OK"
else:
    print "Hey we lost some lines in NivComTotal"

df.to_csv('data/full_NivComTotal.csv', encoding='utf-8', index=False)

## Features 
#[u'NB_Pers_par_Foyer_Alloc_2009_NCT',
#   u'NB_Enfants_0_2_ans', u'NB_Enfants_3_5_ans', u'NB_Enfants',
#   u'NB_Pers_par_Foyer_Alloc_2010_NCT', u'NB_Enfants_0_2_ans_2010',
#   u'NB_Enfants_3_5_ans_2010', u'NB_Enfants_2010',
#   u'NB_Pers_par_Foyer_Alloc_2011_NCT', u'NB_Enfants_0_2_ans_2011',
#   u'NB_Enfants_3_5_ans_2011', u'NB_Enfants_2011',
#   u'NB_Pers_par_Foyer_Alloc_2012_NCT', u'NB_Enfants_0_2_ans_2012',
#   u'NB_Enfants_3_5_ans_2012', u'NB_Enfants_2012',
#   u'NB_Pers_par_Foyer_Alloc_2013_NCT', u'NB_Enfants_0_2_ans_2013',
#   u'NB_Enfants_3_5_ans_2013', u'NB_Enfants_2013',
#   u'NB_Pers_par_Foyer_Alloc_2014_NCT', u'NB_Enfants_0_2_ans_2014',
#   u'NB_Enfants_3_5_ans_2014', u'NB_Enfants_2014']

