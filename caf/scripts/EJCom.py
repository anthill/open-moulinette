# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 09:57:03 2015

@author: babou
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 13:47:48 2015

@author: GILLES Armand
"""

import pandas as pd
import glob

df = pd.read_csv('source/EJCom2009.csv', sep=";")

df.columns = ['Communes', 'Codes_Insee', 'NB_allocataires_2009', 
              'ALL_AF_2009', 'ALL_CF_2009',
              'ALL_ARS_2009', 'ALL_ASF_2009',
              'ALL_AEEH_2009']

files = glob.glob('source/EJCom*')

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
        list_col.append(col+"_EJC") # EJC = EJCom
    else:
        list_col.append(col)
df.columns = list_col

final_count = df.shape[0]

df.to_csv('data/full_EJCom.csv', encoding='utf-8', index=False)

## Features 
#uNB_allocataires_2009_EJC',
#       u'ALL_AF_2009', u'ALL_CF_2009', u'ALL_ARS_2009', u'ALL_ASF_2009',
#       u'ALL_AEEH_2009', u'NB_Allocataires_2010_EJC', u'ALL_AF_2010',
#       u'ALL_CF_2010', u'ALL_ARS_2010', u'ALL_ASF_2010', u'ALL_AEEH_2010',
#       u'NB_Allocataires_2011_EJC', u'ALL_AF_2011', u'ALL_CF_2011',
#       u'ALL_ARS_2011', u'ALL_ASF_2011', u'ALL_AEEH_2011',
#       u'NB_Allocataires_2012_EJC', u'ALL_AF_2012', u'ALL_CF_2012',
#       u'ALL_ARS_2012', u'ALL_ASF_2012', u'ALL_AEEH_2012',
#       u'NB_Allocataires_2013_EJC', u'ALL_AF_2013', u'ALL_CF_2013',
#       u'ALL_ARS_2013', u'ALL_ASF_2013', u'ALL_AEEH_2013',
#       u'NB_Allocataires_2014_EJC', u'ALL_AF_2014', u'ALL_CF_2014',
#       u'ALL_ARS_2014', u'ALL_ASF_2014', u'ALL_AEEH_2014

