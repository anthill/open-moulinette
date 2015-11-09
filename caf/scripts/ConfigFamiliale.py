# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:08:22 2015

@author: GILLES Armand
"""


import pandas as pd
import glob

df = pd.read_csv('source/ConfigFamiliale2009.csv', sep=";")
origin_count = df.shape[0]

df.columns = ['Communes', 'Codes_Insee', 'NB_Allocataires_2009', 
              'COUP_0_ENF', 'COUP_1_ENF', 'COUP_2_ENF', 'COUP_3_ENF', 'COUP_4plus_ENF',
              'Homme_Isole', 'Femme_Isolee', 'MONO_1_ENF', 'MONO_2_ENF',
              'MONO_3_ENF', 'MONO_4plus_ENF']

files = glob.glob('source/ConfigFamiliale*')

for path_file in files:
    year = str(path_file[-8:-4])
    if (year != '2009'):
        df_temp = pd.read_csv(path_file, sep=';')
        
        # Rename Col with year
        year_col = ['Communes', 'Codes_Insee']
        features_col = []
        for col in df_temp.columns[-12:]:
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
        list_col.append(col+"_CF") # CF = ConfigFamiliale
    else:
        list_col.append(col)
df.columns = list_col

final_count = df.shape[0]

if (origin_count == final_count):
    print "File ConfigFamiliale is OK"
else:
    print "Hey we lost some lines in ConfigFamiliale"

df.to_csv('data/full_ConfigFamiliale.csv', encoding='utf-8', index=False)

## Features 
#[ 'NB_Allocataires_2009_CF', u'COUP_0_ENF',
#   u'COUP_1_ENF', u'COUP_2_ENF', u'COUP_3_ENF', u'COUP_4plus_ENF',
#   u'Homme_Isole', u'Femme_Isolee', u'MONO_1_ENF', u'MONO_2_ENF',
#   u'MONO_3_ENF', u'MONO_4plus_ENF', u'NB_allocataires_2010',
#   u'COUP_0_ENF_2010', u'COUP_1_ENF_2010', u'COUP_2_ENF_2010',
#   u'COUP_3_ENF_2010', u'COUP_4plus_ENF_2010', u'Homme_Isole_2010',
#   u'Femme_Isolee_2010', u'MONO_1_ENF_2010', u'MONO_2_ENF_2010',
#   u'MONO_3_ENF_2010', u'MONO_4plus_ENF_2010', u'NB_allocataires_2011',
#   u'COUP_0_ENF_2011', u'COUP_1_ENF_2011', u'COUP_2_ENF_2011',
#   u'COUP_3_ENF_2011', u'COUP_4plus_ENF_2011', u'Homme_Isole_2011',
#   u'Femme_Isolee_2011', u'MONO_1_ENF_2011', u'MONO_2_ENF_2011',
#   u'MONO_3_ENF_2011', u'MONO_4plus_ENF_2011', u'NB_allocataires_2012',
#   u'COUP_0_ENF_2012', u'COUP_1_ENF_2012', u'COUP_2_ENF_2012',
#   u'COUP_3_ENF_2012', u'COUP_4plus_ENF_2012', u'Homme_Isole_2012',
#   u'Femme_Isolee_2012', u'MONO_1_ENF_2012', u'MONO_2_ENF_2012',
#   u'MONO_3_ENF_2012', u'MONO_4plus_ENF_2012', u'NB_allocataires_2013',
#   u'COUP_0_ENF_2013', u'COUP_1_ENF_2013', u'COUP_2_ENF_2013',
#   u'COUP_3_ENF_2013', u'COUP_4plus_ENF_2013', u'Homme_Isole_2013',
#   u'Femme_Isolee_2013', u'MONO_1_ENF_2013', u'MONO_2_ENF_2013',
#   u'MONO_3_ENF_2013', u'MONO_4plus_ENF_2013', u'NB_allocataires_2014',
#   u'COUP_0_ENF_2014', u'COUP_1_ENF_2014', u'COUP_2_ENF_2014',
#   u'COUP_3_ENF_2014', u'COUP_4plus_ENF_2014', u'Homme_Isole_2014',
#   u'Femme_Isolee_2014', u'MONO_1_ENF_2014', u'MONO_2_ENF_2014',
#   u'MONO_3_ENF_2014', u'MONO_4plus_ENF_2014']

