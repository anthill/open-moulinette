# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 13:47:48 2015

@author: GILLES Armand
"""


import pandas as pd
import glob

df = pd.read_csv('source/BasrevenuCom2009.csv', sep=";")

df.columns = ['Communes', 'Codes_Insee', 'NB_Allocataires_2009', 
              'ALL_bas_revenu_2009', 'Pers_bas_revenu_2009']

files = glob.glob('source/BasrevenuCom*')

for path_file in files:
    year = str(path_file[-8:-4])
    if (year != '2009'):
        df_temp = pd.read_csv(path_file, sep=';')
        
        # Rename Col with year
        year_col = ['Communes', 'Codes_Insee']
        features_col = []
        for col in df_temp.columns[-3:]:
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
        list_col.append(col+"_BC") # BC = BasrevnuCOM
    else:
        list_col.append(col)
df.columns = list_col

df.to_csv('data/full_BasrevenuCom.csv', encoding='utf-8', index=False)

## Features 
#u'NB_Allocataires_2009_BC',
#       u'ALL_bas_revenu_2009', u'Pers_bas_revenu_2009',
#       u'NB_allocataires_2010_BC', u'ALL_bas_revenu_2010',
#       u'Pers_bas_revenu_2010', u'NB_allocataires_2011_BC',
#       u'ALL_bas_revenu_2011', u'Pers_bas_revenu_2011',
#       u'NB_allocataires_2012_BC', u'ALL_bas_revenu_2012',
#       u'Pers_bas_revenu_2012', u'NB_allocataires_2013_BC',
#       u'ALL_bas_revenu_2013', u'Pers_bas_revenu_2013',
#       u'NB_allocataires_2014_BC', u'ALL_bas_revenu_2014',
#       u'Pers_bas_revenu_2014'

