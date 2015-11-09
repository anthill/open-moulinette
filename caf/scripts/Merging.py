# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 11:42:15 2015

@author: babou
"""

import pandas as pd
import glob
import pyprind

commune_insee = pd.read_csv("source/commune_insee.csv", sep=";")

commune_insee.columns = ['Codes_Insee', 'Code_Postal', 'Commune', 'Departement', 'Region',
                         'Statut', 'Altitude_Moyenne', 'Superficie', 'Population',
                         'geo_point_2d', 'geo_shape', 'ID_Geogla', 'Code_Commune',
                         'Code_Canton', 'Code_Arrondissement', 'Code_Département',
                         'Code_Région']


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

print "Extracting..."
commune_insee.to_csv('data/caf_data.csv', encoding='utf-8', index=False)

print "Extract in data/caf_data.csv. " + str(len(commune_insee)) + " cities."
    
