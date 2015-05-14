# -*- coding: utf-8 -*-
"""
Created on Thu May 14 17:01:11 2015

@author: babou
"""

import pandas as pd

## Commerce
commerce = pd.read_excel('../data/equip-serv-commerce-infra.xls', sheetname='IRIS')
# crating header form file
header = commerce.loc[4].tolist()
commerce.columns = header
# to get real values
commerce = commerce[5:]
# clean Nan Columns
commerce.dropna(how='any', axis=(1), inplace=True)
header = [x for x in header if str(x) !='nan'] # remove NaN to header to create new sum feature
# creating new feature : sum of all feature
features = [x for x in header if x not in ['CODGEO','LIBGEO','COM','LIBCOM','REG','DEP','ARR','CV','ZE2010','UU2010']]
commerce['nb_commerce'] =  commerce[features].applymap(lambda x: float(x)).sum(axis=1)

data = commerce
print "il y a  %d iris différentes pour le commerce" % len(commerce.CODGEO.unique())


## Sport
sport = pd.read_excel('../data/equip-sport-loisir-socio-infra-13.xls', sheetname='IRIS')
# crating header form file
header = sport.loc[4].tolist()
sport.columns = header
# to get real values
sport = sport[5:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['CODGEO','LIBGEO','COM','LIBCOM','REG','DEP','ARR','CV','ZE2010','UU2010']]
sport['nb_sport'] =  sport[features].applymap(lambda x: float(x)).sum(axis=1)
[features.append(i) for i in ['nb_sport', 'CODGEO']]
print "il y a  %d iris différentes pour le commerce" % len(commerce.CODGEO.unique())

data = pd.merge(data, sport[features], on='CODGEO', how='outer')


## 

