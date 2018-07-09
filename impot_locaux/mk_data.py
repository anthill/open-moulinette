# -*- coding: utf-8 -*-
"""
Created on Mon Jui 10 09:09:54 2017

@author: GILLES Armand
"""

import pandas as pd
import glob


import_files = glob.glob('data/*.xlsx')

geo_features = ['DEP', 'DIR', 'COM', 'REC', 'Q02','SIREPCI','Q03', 'OPTEPCI',
                'FORJEPCI', 'LIBDEP', 'LIBREG', 'IDCOM', 'LIBCOM']

# Loop on impot's file
for file_path in import_files:
    # Check file's year
    file_year = file_path.split('_')[1][0:4]    # 2013
    small_year = file_year[2:]                  # 13
    
    # Loading file in DataFrame
    print("Loading " + file_year + " REI's file (takes some time +/- 6 min)")
    df_temp = pd.read_excel(file_path, sheetname='REI_'+file_year)
    # For merging after
    df_temp['IDCOM'] = df_temp['IDCOM'].astype('str') 
    
    # Select features
    all_columns = df_temp.columns
    
    REI_features = [col for col in all_columns if col not in geo_features]
    print("REI " + file_year + " have " + str(len(REI_features)) + " features and "\
    + str(len(df_temp)) + " lines") # 0.002 s / 0.0014
    
    # Transform features name
    # B11 -> B11_13   
    REI_features_year = []
    for col in df_temp.columns:
        #df_temp.rename(columns={col:col+"_"+small_year}, inplace=True)
        if col not in geo_features:
            REI_features_year.append(col+"_"+small_year)
        else:
            REI_features_year.append(col)
    
    df_temp.columns = REI_features_year
    
    # We take all features from df_temp not in geo_features
    merge_feature = [col for col in REI_features_year if col not in geo_features]
    # Adding IDCOM for merging.
    merge_feature = merge_feature + ['IDCOM']
    
    # If first file (2013)
    if file_year == '2013':
        df = df_temp
        del df_temp
    # Not the first file, we merge DataFrame
    else:
        # Merging process
        # IDCOM change with year so we have to left-join to keep histo
        df = df.merge(df_temp[merge_feature], on="IDCOM", how='left')
    
print("Export result in : data/impot_ouput.csv")
df.to_csv('data/impot_ouput.csv', index=False, encoding='utf-8')
