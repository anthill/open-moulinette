# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 13:47:48 2015

@author: GILLES Armand
"""

import pandas as pd
import glob

df = pd.read_csv('source/LOGCom2009.csv', sep=";")

df.columns = ['Communes', 'Codes_Insee', 'NB_Allocataires_2009', 
              'total_ALF_2009', 'total_ALS_2009', 'total_APL_2009', 'locataire_ALF_2009',
              'locataire_ALS_2009', 'locataire_APL_2009', 'proprietaire_ALF_2009', 'proprietaire_ALS_2009',
              'proprietaire_APL_2009', 'total_locataire_2009', 'total_proprietaire_2009',
              'total_allocataires_logement_2009']

files = glob.glob('source/LOGCom*')

for path_file in files:
    year = str(path_file[-8:-4])
    if (year != '2009'):
        df_temp = pd.read_csv(path_file, sep=';')
        df_temp.rename(columns={'total_allocataires':'NB_Allocataires'}, inplace=True)
        
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
        list_col.append(col+"_LC") # LC = LogCom
    else:
        list_col.append(col)
df.columns = list_col

df.to_csv('data/full_LogCom.csv', encoding='utf-8', index=False)

## Features 
#u'NB_Allocataires_2009_LC',
#       u'total_ALF_2009', u'total_ALS_2009', u'total_APL_2009',
#       u'locataire_ALF_2009', u'locataire_ALS_2009', u'locataire_APL_2009',
#       u'proprietaire_ALF_2009', u'proprietaire_ALS_2009',
#       u'proprietaire_APL_2009', u'total_locataire_2009',
#       u'total_proprietaire_2009', u'total_allocataires_logement_2009',
#       u'NB_Allocataires_2010_LC', u'total_ALF_2010', u'total_ALS_2010',
#       u'total_APL_2010', u'locataire_ALF_2010', u'locataire_ALS_2010',
#       u'locataire_APL_2010', u'proprietaire_ALF_2010',
#       u'proprietaire_ALS_2010', u'proprietaire_APL_2010',
#       u'total_locataire_2010', u'total_proprietaire_2010',
#       u'total_allocataires_logement_2010', u'NB_Allocataires_2011_LC',
#       u'total_ALF_2011', u'total_ALS_2011', u'total_APL_2011',
#       u'locataire_ALF_2011', u'locataire_ALS_2011', u'locataire_APL_2011',
#       u'proprietaire_ALF_2011', u'proprietaire_ALS_2011',
#       u'proprietaire_APL_2011', u'total_locataire_2011',
#       u'total_proprietaire_2011', u'total_allocataires_logement_2011',
#       u'NB_Allocataires_2012_LC', u'total_ALF_2012', u'total_ALS_2012',
#       u'total_APL_2012', u'locataire_ALF_2012', u'locataire_ALS_2012',
#       u'locataire_APL_2012', u'proprietaire_ALF_2012',
#       u'proprietaire_ALS_2012', u'proprietaire_APL_2012',
#       u'total_locataire_2012', u'total_proprietaire_2012',
#       u'total_allocataires_logement_2012', u'NB_Allocataires_2013_LC',
#       u'total_ALF_2013', u'total_ALS_2013', u'total_APL_2013',
#       u'locataire_ALF_2013', u'locataire_ALS_2013', u'locataire_APL_2013',
#       u'proprietaire_ALF_2013', u'proprietaire_ALS_2013',
#       u'proprietaire_APL_2013', u'total_locataire_2013',
#       u'total_proprietaire_2013', u'total_allocataires_logement_2013',
#       u'NB_Allocataires_2014_LC', u'total_ALF_2014', u'total_ALS_2014',
#       u'total_APL_2014', u'locataire_ALF_2014', u'locataire_ALS_2014',
#       u'locataire_APL_2014', u'proprietaire_ALF_2014',
#       u'proprietaire_ALS_2014', u'proprietaire_APL_2014',
#       u'total_locataire_2014', u'total_proprietaire_2014',
#       u'total_allocataires_logement_2014'

