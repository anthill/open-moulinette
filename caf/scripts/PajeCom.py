# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 13:47:48 2015

@author: GILLES Armand
"""

import pandas as pd
import glob

df = pd.read_csv('source/PajeCom2009.csv', sep=";")

df.columns = ['Communes', 'Codes_Insee', 'NB_Allocataires_2009', 
              'ALL_PAJE_2009', 'ALL_PRIM_2009', 'ALL_BASEP_2009',
              'ALL_ASMA_2009','ALL_Clca_Colca_2009']

files = glob.glob('source/PajeCom*')

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
        list_col.append(col+"_PC") # PC = PageCom
    else:
        list_col.append(col)
df.columns = list_col

df.to_csv('data/full_PageCom.csv', encoding='utf-8', index=False)

## Features 
#u'NB_Allocataires_2009_PC',
#       u'ALL_PAJE_2009', u'ALL_PRIM_2009', u'ALL_BASEP_2009', u'ALL_ASMA_2009',
#       u'ALL_Clca_Colca_2009', u'NB_Allocataires_2010_PC', u'ALL_PAJE_2010',
#       u'ALL_PRIM_2010', u'ALL_BASEP_2010', u'ALL_ASMA_2010',
#       u'ALL_Clca_Colca_2010', u'NB_Allocataires_2011_PC', u'ALL_PAJE_2011',
#       u'ALL_PRIM_2011', u'ALL_BASEP_2011', u'ALL_ASMA_2011',
#       u'ALL_Clca_Colca_2011', u'NB_Allocataires_2012_PC', u'ALL_PAJE_2012',
#       u'ALL_PRIM_2012', u'ALL_BASEP_2012', u'ALL_ASMA_2012',
#       u'ALL_Clca_Colca_2012', u'NB_Allocataires_2013_PgC', u'ALL_PAJE_2013',
#       u'ALL_PRIM_2013', u'ALL_BASEP_2013', u'ALL_ASMA_2013',
#       u'ALL_Clca_Colca_2013', u'NB_Allocataires_2014_PC', u'ALL_PAJE_2014',
#       u'ALL_PRIM_2014', u'ALL_BASEP_2014', u'ALL_CMG_2014',
#       u'ALL_CMG_ASMA_2014', u'ALL_CMG_DOM_2014', u'ALL_CMG_A_2014',
#       u'ALL_Clca_Colca_2014'
