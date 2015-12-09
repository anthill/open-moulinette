# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 13:47:48 2015

@author: GILLES Armand
"""

import pandas as pd
import glob

df = pd.read_csv('source/LOGPersPrestaCom2009.csv', sep=";")

df.columns = ['Communes', 'Codes_Insee', 'NB_Pers_Couv_Al_2009', 
              'Pers_Couv_Al_ALF_2009', 'Pers_Couv_Al_ALS_2009',
              'Pers_Couv_Al_APL_2009']

files = glob.glob('source/LOGPersPrestaCom*')

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
        list_col.append(col+"_LPPC") # LPPC = LOGPersPrestaCom
    else:
        list_col.append(col)
df.columns = list_col

df.to_csv('data/full_LogPersPrestaCom.csv', encoding='utf-8', index=False)

## Features 
#u'NB_Pers_Couv_Al_2009',
#       u'Pers_Couv_Al_ALF_2009', u'Pers_Couv_Al_ALS_2009',
#       u'Pers_Couv_Al_APL_2009', u'NB_Pers_Couv_Al_2010',
#       u'Pers_Couv_Al_ALF_2010', u'Pers_Couv_Al_ALS_2010',
#       u'Pers_Couv_Al_APL_2010', u'NB_Pers_Couv_Al_2011',
#       u'Pers_Couv_Al_ALF_2011', u'Pers_Couv_Al_ALS_2011',
#       u'Pers_Couv_Al_APL_2011', u'NB_Pers_Couv_Al_2012',
#       u'Pers_Couv_Al_ALF_2012', u'Pers_Couv_Al_ALS_2012',
#       u'Pers_Couv_Al_APL_2012', u'NB_Pers_Couv_Al_2013',
#       u'Pers_Couv_Al_ALF_2013', u'Pers_Couv_Al_ALS_2013',
#       u'Pers_Couv_Al_APL_2013', u'NB_Pers_Couv_Al_2014',
#       u'Pers_Couv_Al_ALF_2014', u'Pers_Couv_Al_ALS_2014',
#       u'Pers_Couv_Al_APL_2014'
