# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 11:42:15 2015

@author: babou
"""

import pandas as pd
import glob
import pyprind
import json

def CustomParser(data):
    """
    To load column geo_shape in "commune_insee.csv" like dict
    """
    j1 = json.loads(data)
    return j1


def reduce_shape(shapes):
    """
    Reduce size of lat/lon in geo_shape
    """
    new_shapes = []
    if shapes['type'] == "Polygon":
        for shape in shapes['coordinates'][0]:
            new_shapes.append([round(x, 7) for x in shape])
        shapes['coordinates'] = [new_shapes]
        return shapes
    else:
        for i in range(0, len(shapes['coordinates'])):
            multi_shape = []
            for shape in shapes['coordinates'][i][0]:
                multi_shape.append([round(x, 7) for x in shape])
            new_shapes.append([multi_shape])
        shapes['coordinates'] = new_shapes
        return shapes


pd.options.mode.chained_assignment = None # No warning on SettingWithCopyWarning

commune_insee = pd.read_csv("source/commune_insee.csv", sep=";", converters={'geo_shape':CustomParser})

commune_insee.columns = ['Codes_Insee', 'Code_Postal', 'Commune', 'Departement', 'Region',
                         'Statut', 'Altitude_Moyenne', 'Superficie', 'Population',
                         'geo_point_2d', 'geo_shape', 'ID_Geogla', 'Code_Commune',
                         'Code_Canton', 'Code_Arrondissement', 'Code_Departement',
                         'Code_Region']

# To reduce size cf https://github.com/anthill/open-moulinette/issues/32
commune_insee['lat'] = commune_insee.geo_point_2d.apply(lambda x: round(float(x.split(",")[0]), 7))
commune_insee['lon'] = commune_insee.geo_point_2d.apply(lambda x: round(float(x.split(",")[1]), 7))
commune_insee = commune_insee.drop('geo_point_2d', axis=1) 

commune_insee['geo_shape'] = commune_insee.geo_shape.apply(lambda x: reduce_shape(x))                         


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

list_col = commune_insee.columns[0:18].tolist() # all cities's features

# Juste to had "NB_Allocataires" feature in the list. Rename later
list_col.append("NB_Allocataires_2009_AAHC")
list_col.append("NB_Allocataires_2010_AAHC")
list_col.append("NB_Allocataires_2011_AAHC")
list_col.append("NB_allocataires_2012_AAHC")
list_col.append("NB_allocataires_2013_AAHC")
list_col.append("NB_Allocataires_2014_AAHC")

# We don't all "NB_Allocataires" redundancy features
for col in commune_insee.columns[18:]:
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
    
