# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

## Commerce
commerce = pd.read_excel('../data/equip-serv-commerce-infra.xls', sheetname='IRIS')
# creating header from file
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
print "il y a  %d iris différentes pour le commerce et %d features" % (len(commerce.CODGEO.unique()), len(features))


## Sport
sport = pd.read_excel('../data/equip-sport-loisir-socio-infra-13.xls', sheetname='IRIS')
# creating header from file
header = sport.loc[4].tolist()
sport.columns = header
# to get real values
sport = sport[5:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['CODGEO','LIBGEO','COM','LIBCOM','REG','DEP','ARR','CV','ZE2010','UU2010']]
sport['nb_sport'] =  sport[features].applymap(lambda x: float(x)).sum(axis=1)
[features.append(i) for i in ['nb_sport', 'CODGEO']]
print "il y a  %d iris différentes pour le sport et %d features" % (len(sport.CODGEO.unique()), len(features) - 1)

data = pd.merge(data, sport[features], on='CODGEO', how='outer')


## Enseignement 1er degré 
enseignement_1 = pd.read_excel('../data/equip-serv-ens-1er-degre-infra.xls', sheetname='IRIS')
# creating header from file
header = enseignement_1.loc[4].tolist()
enseignement_1.columns = header
# to get real values
enseignement_1 = enseignement_1[5:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['CODGEO','LIBGEO','COM','LIBCOM','REG','DEP','ARR','CV','ZE2010','UU2010']]
enseignement_1['nb_enseignement_1'] =  enseignement_1[features].applymap(lambda x: float(x)).sum(axis=1)
[features.append(i) for i in ['nb_enseignement_1', 'CODGEO']]
print "il y a  %d iris différentes pour l'enseignement du 1er degré et %d features" % (len(enseignement_1.CODGEO.unique()), len(features) - 1)

data = pd.merge(data, enseignement_1[features], on='CODGEO', how='outer')


## Enseignement du second degré 
enseignement_2 = pd.read_excel('../data/equip-serv-ens-2eme-degre-infra.xls', sheetname='IRIS')
# creating header from file
header = enseignement_2.loc[4].tolist()
enseignement_2.columns = header
# to get real values
enseignement_2 = enseignement_2[5:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['CODGEO','LIBGEO','COM','LIBCOM','REG','DEP','ARR','CV','ZE2010','UU2010']]
enseignement_2['nb_enseignement_2'] =  enseignement_2[features].applymap(lambda x: float(x)).sum(axis=1)
[features.append(i) for i in ['nb_enseignement_2', 'CODGEO']]
print "il y a  %d iris différentes pour l'enseignement du second degré et %d features" % (len(enseignement_2.CODGEO.unique()), len(features) - 1)

data = pd.merge(data, enseignement_2[features], on='CODGEO', how='outer')


## Enseignement supérieur 
enseignement_sup = pd.read_excel('../data/equip-serv-ens-sup-form-serv-infra.xls', sheetname='IRIS')
# creating header from file
header = enseignement_sup.loc[4].tolist()
enseignement_sup.columns = header
# to get real values
enseignement_sup = enseignement_sup[5:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['CODGEO','LIBGEO','COM','LIBCOM','REG','DEP','ARR','CV','ZE2010','UU2010']]
enseignement_sup['nb_enseignement_sup'] =  enseignement_sup[features].applymap(lambda x: float(x)).sum(axis=1)
[features.append(i) for i in ['nb_enseignement_sup', 'CODGEO']]
print "il y a  %d iris différentes pour l'enseignement du supérieur et %d features" % (len(enseignement_sup.CODGEO.unique()), len(features) - 1)

data = pd.merge(data, enseignement_sup[features], on='CODGEO', how='outer')


### Revenu have 4 files [ménage, personne, unité de consomation, ensemble]

## Revenu Ménage
revenu_menage = pd.read_excel('../data/RFDM2011IRI.xls', sheetname=1) #using int cause name of sheetname have some "é"
# creating header from file
header = revenu_menage.loc[5].tolist()
revenu_menage.columns = header
revenu_menage.rename(columns={'IRIS':'CODGEO'}, inplace=True)
# to get real values
revenu_menage = revenu_menage[6:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['IRIS','LIBIRIS','COM','LIBCOM','REG','DEP','ARR','CV','ZE2010']] # special list for this file
# No need to sum features here (% and quantile)
features.append('CODGEO')
print "il y a  %d iris différentes pour le revenu par ménage et %d features" % (len(revenu_menage.CODGEO.unique()), len(features) - 1)

data = pd.merge(data, revenu_menage[features], on='CODGEO', how='outer')

## Revenu par personne
revenu_personne = pd.read_excel('../data/RFDP2011IRI.xls', sheetname=1) #using int cause name of sheetname have some "é"
# creating header from file
header = revenu_personne.loc[5].tolist()
revenu_personne.columns = header
revenu_personne.rename(columns={'IRIS':'CODGEO'}, inplace=True)
# to get real values
revenu_personne = revenu_personne[6:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['IRIS','LIBIRIS','COM','LIBCOM','REG','DEP','ARR','CV','ZE2010']] # special list for this file
# No need to sum features here (% and quantile)
features.append('CODGEO')
print "il y a  %d iris différentes pour le revenu par personne et %d features" % (len(revenu_personne.CODGEO.unique()), len(features) - 1)

data = pd.merge(data, revenu_personne[features], on='CODGEO', how='outer')


## Revenu par unité de consomation
revenu_uc = pd.read_excel('../data/RFDU2011IRI.xls', sheetname=1) #using int cause name of sheetname have some "é"
# creating header from file
header = revenu_uc.loc[5].tolist()
revenu_uc.columns = header
revenu_uc.rename(columns={'IRIS':'CODGEO'}, inplace=True)
# to get real values
revenu_uc = revenu_uc[6:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['IRIS','LIBIRIS','COM','LIBCOM','REG','DEP','ARR','CV','ZE2010']] # special list for this file
# No need to sum features here (% and quantile)
features.append('CODGEO')
print "il y a  %d iris différentes pour le revenu par unité de consomation et %d features" % (len(revenu_uc.CODGEO.unique()), len(features) - 1)

data = pd.merge(data, revenu_uc[features], on='CODGEO', how='outer')

## Revenu % imposé + détails (% ménage imposé, dont traitement salaire etc..)
revenu_impose = pd.read_excel('../data/RFST2011IRI.xls', sheetname=1) #using int cause name of sheetname have some "é"
# creating header from file
header = revenu_impose.loc[5].tolist()
revenu_impose.columns = header
revenu_impose.rename(columns={'IRIS':'CODGEO'}, inplace=True)
# to get real values
revenu_impose = revenu_impose[6:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['IRIS','LIBIRIS','COM','LIBCOM','REG','DEP','ARR','CV','ZE2010']] # special list for this file
# No need to sum features here (% and quantile)
features.append('CODGEO')
print "il y a  %d iris différentes pour le revenu par ménage imposé et %d features" % (len(revenu_impose.CODGEO.unique()), len(features) - 1)

data = pd.merge(data, revenu_impose[features], on='CODGEO', how='outer')



