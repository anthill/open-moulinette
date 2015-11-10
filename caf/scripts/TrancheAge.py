# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 13:47:48 2015

@author: GILLES Armand
"""

import pandas as pd
import glob

df = pd.read_csv('source/TrancheAge2009.csv', sep=";")

df.columns = ['Communes', 'Codes_Insee', 'NB_Allocataires_2009', 
              'ALL0A19_2009', 'ALL20A24_2009', 'ALL25A29_2009', 'ALL30A39_2009',
              'ALL40A49_2009', 'ALL50A59_2009', 'ALL60AX_2009', 'ALLAGEX_2009']

files = glob.glob('source/TrancheAge*')

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
        list_col.append(col+"_TA") # TA = TrancheAge
    else:
        list_col.append(col)
df.columns = list_col

df.to_csv('data/full_TrancheAge.csv', encoding='utf-8', index=False)

## Features 
#u'NB_Allocataires_2009_TA',
#       u'ALL0A19_2009', u'ALL20A24_2009', u'ALL25A29_2009', u'ALL30A39_2009',
#       u'ALL40A49_2009', u'ALL50A59_2009', u'ALL60AX_2009', u'ALLAGEX_2009',
#       u'NB_allocataires_2010_TA', u'ALL0A19_2010', u'ALL20A24_2010',
#       u'ALL25A29_2010', u'ALL30A39_2010', u'ALL40A49_2010', u'ALL50A59_2010',
#       u'ALL60AX_2010', u'ALLAGEX_2010', u'NB_allocataires_2011_TA',
#       u'ALL0A19_2011', u'ALL20A24_2011', u'ALL25A29_2011', u'ALL30A39_2011',
#       u'ALL40A49_2011', u'ALL50A54_2011', u'ALL55A59_2011', u'ALL60A64_2011',
#       u'ALL65A69_2011', u'ALL70AX_2011', u'ALLAGEX_2011',
#       u'NB_allocataires_2012_TA', u'ALL0A19_2012', u'ALL20A24_2012',
#       u'ALL25A29_2012', u'ALL30A39_2012', u'ALL40A49_2012', u'ALL50A54_2012',
#       u'ALL55A59_2012', u'ALL60A64_2012', u'ALL65A69_2012', u'ALL70AX_2012',
#       u'ALLAGEX_2012', u'NB_allocataires_2013_TA', u'ALL0A19_2013',
#       u'ALL20A24_2013', u'ALL25A29_2013', u'ALL30A39_2013', u'ALL40A49_2013',
#       u'ALL50A54_2013', u'ALL55A59_2013', u'ALL60A64_2013', u'ALL65A69_2013',
#       u'ALL70AX_2013', u'ALLAGEX_2013', u'NB_allocataires_2014_TA',
#       u'ALL0A19_2014', u'ALL20A24_2014', u'ALL25A29_2014', u'ALL30A39_2014',
#       u'ALL40A49_2014', u'ALL50A54_2014', u'ALL55A59_2014', u'ALL60A64_2014',
#       u'ALL65A69_2014', u'ALL70AX_2014', u'ALLAGEX_2014'
