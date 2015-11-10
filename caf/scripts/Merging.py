# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 11:42:15 2015

@author: babou
"""

import pandas as pd
import glob
import pyprind

pd.options.mode.chained_assignment = None # No warning on SettingWithCopyWarning

commune_insee = pd.read_csv("source/commune_insee.csv", sep=";")

commune_insee.columns = ['Codes_Insee', 'Code_Postal', 'Commune', 'Departement', 'Region',
                         'Statut', 'Altitude_Moyenne', 'Superficie', 'Population',
                         'geo_point_2d', 'geo_shape', 'ID_Geogla', 'Code_Commune',
                         'Code_Canton', 'Code_Arrondissement', 'Code_Departement',
                         'Code_Region']

files = glob.glob("data/full*")

bar = pyprind.ProgBar(len(files), title='Merging Process', width=150)
for path_file in files:
    df_temp = pd.read_csv(path_file, low_memory=False)
    
    # Drop Commune, doublon with commune_insee
    df_temp = df_temp.drop('Communes', axis=1)
        
    # Fill nan value to 0
    df_temp.fillna(0, inplace=True)
    
    # merging
    commune_insee = pd.merge(commune_insee, df_temp, how='left', on='Codes_Insee')
    bar.update()

print "\n"
print "cleaning features..."

list_col = commune_insee.columns[0:17].tolist() # all cities's features

# Juste to had "NB_Allocataires" feature in the list. Rename later
list_col.append("NB_Allocataires_2009_AAHC")
list_col.append("NB_Allocataires_2010_AAHC")
list_col.append("NB_Allocataires_2011_AAHC")
list_col.append("NB_allocataires_2012_AAHC")
list_col.append("NB_allocataires_2013_AAHC")
list_col.append("NB_Allocataires_2014_AAHC")

# We don't all "NB_Allocataires" redundancy features
for col in commune_insee.columns[17:]:
    if "nb_allocataires" not in col.lower():
        list_col.append(col)

# Dataframe with selected column
result = commune_insee[list_col]

result.rename(columns={'NB_Allocataires_2009_AAHC':'NB_Allocataires_2009'}, inplace=True)
result.rename(columns={'NB_Allocataires_2010_AAHC':'NB_Allocataires_2010'}, inplace=True)
result.rename(columns={'NB_Allocataires_2011_AAHC':'NB_Allocataires_2011'}, inplace=True)
result.rename(columns={'NB_allocataires_2012_AAHC':'NB_Allocataires_2012'}, inplace=True)
result.rename(columns={'NB_allocataires_2013_AAHC':'NB_Allocataires_2013'}, inplace=True)
result.rename(columns={'NB_Allocataires_2014_AAHC':'NB_Allocataires_2014'}, inplace=True)


print "Extracting..."
result.to_csv('data/caf_data.csv', encoding='utf-8', index=False)

print "Extract in data/caf_data.csv. " + str(len(commune_insee)) + " cities."
    
