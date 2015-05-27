# -*- coding: utf-8 -*-

import pandas as pd

print "Initialisation..."

## Commerce
commerce = pd.read_excel('data/equip-serv-commerce-infra.xls', sheetname='IRIS')
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
sport = pd.read_excel('data/equip-sport-loisir-socio-infra-13.xls', sheetname='IRIS')
# creating header from file
header = sport.loc[4].tolist()
sport.columns = header
# to get real values
sport = sport[5:]
# creating new feature : sum all features non aggregated
features = [x for x in header if x not in ['CODGEO','LIBGEO','COM','LIBCOM','REG','DEP','ARR','CV','ZE2010','UU2010']]
sport['nb_sport'] =  sport[['NB_F101', 'NB_F102', 'NB_F103', 'NB_F104', 'NB_F105',
                            'NB_F106', 'NB_F107', 'NB_F108', 'NB_F109', 'NB_F110', 
                            'NB_F111', 'NB_F112', 'NB_F113', 'NB_F114', 'NB_F115',
                            'NB_F117', 'NB_F118']].applymap(lambda x: float(x)).sum(axis=1)
[features.append(i) for i in ['nb_sport', 'CODGEO']]
print "il y a  %d iris différentes pour le sport et %d features" % (len(sport.CODGEO.unique()), len(features) - 1)

data = pd.merge(data, sport[features], on='CODGEO', how='outer')


## Enseignement 1er degré 
enseignement_1 = pd.read_excel('data/equip-serv-ens-1er-degre-infra.xls', sheetname='IRIS')
# creating header from file
header = enseignement_1.loc[4].tolist()
enseignement_1.columns = header
# to get real values
enseignement_1 = enseignement_1[5:]
# creating new feature : sum all features non aggregated
features = [x for x in header if x not in ['CODGEO','LIBGEO','COM','LIBCOM','REG','DEP','ARR','CV','ZE2010','UU2010']]
enseignement_1['nb_enseignement_1'] =  enseignement_1[['NB_C101', 'NB_C102', 'NB_C104',
                                                        'NB_C105']].applymap(lambda x: float(x)).sum(axis=1)
[features.append(i) for i in ['nb_enseignement_1', 'CODGEO']]
print "il y a  %d iris différentes pour l'enseignement du 1er degré et %d features" % (len(enseignement_1.CODGEO.unique()), len(features) - 1)

data = pd.merge(data, enseignement_1[features], on='CODGEO', how='outer')


## Enseignement du second degré 
enseignement_2 = pd.read_excel('data/equip-serv-ens-2eme-degre-infra.xls', sheetname='IRIS')
# creating header from file
header = enseignement_2.loc[4].tolist()
enseignement_2.columns = header
# to get real values
enseignement_2 = enseignement_2[5:]
# creating new feature : sum all features non aggregated
features = [x for x in header if x not in ['CODGEO','LIBGEO','COM','LIBCOM','REG','DEP','ARR','CV','ZE2010','UU2010']]
enseignement_2['nb_enseignement_2'] =  enseignement_2[['NB_C201', 'NB_C301', 'NB_C302',
                                                        'NB_C303', 'NB_C304', 'NB_C305']].applymap(lambda x: float(x)).sum(axis=1)
[features.append(i) for i in ['nb_enseignement_2', 'CODGEO']]
print "il y a  %d iris différentes pour l'enseignement du second degré et %d features" % (len(enseignement_2.CODGEO.unique()), len(features) - 1)

data = pd.merge(data, enseignement_2[features], on='CODGEO', how='outer')


## Enseignement supérieur 
enseignement_sup = pd.read_excel('data/equip-serv-ens-sup-form-serv-infra.xls', sheetname='IRIS')
# creating header from file
header = enseignement_sup.loc[4].tolist()
enseignement_sup.columns = header
# to get real values
enseignement_sup = enseignement_sup[5:]
# creating new feature : sum all features non aggregated
features = [x for x in header if x not in ['CODGEO','LIBGEO','COM','LIBCOM','REG','DEP','ARR','CV','ZE2010','UU2010']]
enseignement_sup['nb_enseignement_sup'] =  enseignement_sup[['NB_C401', 'NB_C402', 'NB_C403',
                                                            'NB_C409', 'NB_C501', 'NB_C502', 
                                                            'NB_C503', 'NB_C504', 'NB_C509', 
                                                            'NB_C601', 'NB_C602', 'NB_C603', 
                                                            'NB_C604', 'NB_C605', 'NB_C609', 
                                                            'NB_C701', 'NB_C702']].applymap(lambda x: float(x)).sum(axis=1)
[features.append(i) for i in ['nb_enseignement_sup', 'CODGEO']]
print "il y a  %d iris différentes pour l'enseignement du supérieur et %d features" % (len(enseignement_sup.CODGEO.unique()), len(features) - 1)

data = pd.merge(data, enseignement_sup[features], on='CODGEO', how='outer')


### Revenu have 4 files [ménage, personne, unité de consomation, ensemble]
#-------------------------------------------------------------------------

## Revenu Ménage
revenu_menage = pd.read_excel('data/RFDM2011IRI.xls', sheetname=1) #using int cause name of sheetname have some "é"
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
revenu_personne = pd.read_excel('data/RFDP2011IRI.xls', sheetname=1) #using int cause name of sheetname have some "é"
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
revenu_uc = pd.read_excel('data/RFDU2011IRI.xls', sheetname=1) #using int cause name of sheetname have some "é"
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
revenu_impose = pd.read_excel('data/RFST2011IRI.xls', sheetname=1) #using int cause name of sheetname have some "é"
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

### Fin de revenu
#-------------------------------------------------------------------------


## Equipement social 
equipement_social = pd.read_excel('data/equip-serv-action-sociale-infra.xls', sheetname='IRIS')
# creating header from file
header = equipement_social.loc[4].tolist()
equipement_social.columns = header
# to get real values
equipement_social = equipement_social[5:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['CODGEO','LIBGEO','COM','LIBCOM','REG','DEP','ARR','CV','ZE2010','UU2010']]
equipement_social['nb_equipement_social'] =  equipement_social[features].applymap(lambda x: float(x)).sum(axis=1)
[features.append(i) for i in ['nb_equipement_social', 'CODGEO']]
print "il y a  %d iris différentes pour l'équipement social et %d features" % (len(equipement_social.CODGEO.unique()), len(features) - 1)

data = pd.merge(data, equipement_social[features], on='CODGEO', how='outer')


## Equipement santé
equipement_sante = pd.read_excel('data/equip-serv-sante-infra.xls', sheetname='IRIS')
# creating header from file
header = equipement_sante.loc[4].tolist()
equipement_sante.columns = header
# to get real values
equipement_sante = equipement_sante[5:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['CODGEO','LIBGEO','COM','LIBCOM','REG','DEP','ARR','CV','ZE2010','UU2010']]
equipement_sante['nb_equipement_sante'] =  equipement_sante[features].applymap(lambda x: float(x)).sum(axis=1)
[features.append(i) for i in ['nb_equipement_sante', 'CODGEO']]
print "il y a  %d iris différentes pour l'équipement de santé et %d features" % (len(equipement_sante.CODGEO.unique()), len(features) - 1)

data = pd.merge(data, equipement_sante[features], on='CODGEO', how='outer')


## Fonction médical
fonction_medical = pd.read_excel('data/equip-serv-medical-para-infra.xls', sheetname='IRIS')
# creating header from file
header = fonction_medical.loc[4].tolist()
fonction_medical.columns = header
# to get real values
fonction_medical = fonction_medical[5:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['CODGEO','LIBGEO','COM','LIBCOM','REG','DEP','ARR','CV','ZE2010','UU2010']]
fonction_medical['nb_fonction_medical'] =  fonction_medical[features].applymap(lambda x: float(x)).sum(axis=1)
[features.append(i) for i in ['nb_fonction_medical', 'CODGEO']]
print "il y a  %d iris différentes pour les fonctions médical et %d features" % (len(fonction_medical.CODGEO.unique()), len(features) - 1)

data = pd.merge(data, fonction_medical[features], on='CODGEO', how='outer')

## Service pour les particuliers
service_particulier = pd.read_excel('data/equip-serv-particuliers-infra.xls', sheetname='IRIS')
# creating header from file
header = service_particulier.loc[4].tolist()
service_particulier.columns = header
# to get real values
service_particulier = service_particulier[5:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['CODGEO','LIBGEO','COM','LIBCOM','REG','DEP','ARR','CV','ZE2010','UU2010']]
service_particulier['nb_service_particulier'] =  service_particulier[features].applymap(lambda x: float(x)).sum(axis=1)
[features.append(i) for i in ['nb_service_particulier', 'CODGEO']]
print "il y a  %d iris différentes pour les services aux particulier et %d features" % (len(service_particulier.CODGEO.unique()), len(features) - 1)

data = pd.merge(data, service_particulier[features], on='CODGEO', how='outer')


## Transport touristique
transport_tourisme = pd.read_excel('data/equip-tour-transp-infra.xls', sheetname='IRIS')
# creating header from file
header = transport_tourisme.loc[4].tolist()
transport_tourisme.columns = header
# to get real values
transport_tourisme = transport_tourisme[5:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['CODGEO','LIBGEO','COM','LIBCOM','REG','DEP','ARR','CV','ZE2010','UU2010']]
transport_tourisme['nb_transport_tourisme'] =  transport_tourisme[features].applymap(lambda x: float(x)).sum(axis=1)
[features.append(i) for i in ['nb_transport_tourisme', 'CODGEO']]
print "il y a  %d iris différentes pour le transport touristique et %d features" % (len(transport_tourisme.CODGEO.unique()), len(features) - 1)

data = pd.merge(data, transport_tourisme[features], on='CODGEO', how='outer')


## Logement
logement = pd.read_excel('data/base-ic-logement-2011.xls', sheetname='IRIS')
# creating header from file
header = logement.loc[4].tolist()
logement.columns = header
logement.rename(columns={'IRIS':'CODGEO'}, inplace=True)
# to get real values
logement = logement[5:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['IRIS','REG','DEP','UU2010','COM','LIBCOM','TRIRIS',
                                           'GRD_QUART','LIBIRIS','TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS']]
features.append('CODGEO')
print "il y a  %d iris différentes pour le logement et %d features" % (len(logement.CODGEO.unique()), len(features) - 1)

data = pd.merge(data, logement[features], on='CODGEO', how='outer')


## Diplome
diplome = pd.read_excel('data/base-ic-diplomes-formation-2011.xls', sheetname='IRIS')
# creating header from file
header = diplome.loc[4].tolist()
diplome.columns = header
diplome.rename(columns={'IRIS':'CODGEO'}, inplace=True)
# to get real values
diplome = diplome[5:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['IRIS','REG','DEP','UU2010','COM','LIBCOM','TRIRIS',
                                           'GRD_QUART','LIBIRIS','TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS']]
features.append('CODGEO')
print "il y a  %d iris différentes pour les diplomes et %d features" % (len(diplome.CODGEO.unique()), len(features) - 1)

data = pd.merge(data, diplome[features], on='CODGEO', how='outer')


## Famille
famille = pd.read_excel('data/base-ic-couples-familles-menages-2011.xls', sheetname='IRIS')
# creating header from file
header = famille.loc[4].tolist()
famille.columns = header
famille.rename(columns={'IRIS':'CODGEO'}, inplace=True)
# to get real values
famille = famille[5:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['IRIS','REG','DEP','UU2010','COM','LIBCOM','TRIRIS',
                                           'GRD_QUART','LIBIRIS','TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS']]
features.append('CODGEO')
print "il y a  %d iris différentes pour les familles et %d features" % (len(famille.CODGEO.unique()), len(features) - 1)

data = pd.merge(data, famille[features], on='CODGEO', how='outer')


## Population
population = pd.read_excel('data/base-ic-evol-struct-pop-2011.xls', sheetname='IRIS')
# creating header from file
header = population.loc[4].tolist()
population.columns = header
population.rename(columns={'IRIS':'CODGEO'}, inplace=True)
# to get real values
population = population[5:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['IRIS','REG','DEP','UU2010','COM','LIBCOM','TRIRIS',
                                           'GRD_QUART','LIBIRIS','TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS']]
features.append('CODGEO')
print "il y a  %d iris différentes pour le population et %d features" % (len(population.CODGEO.unique()), len(features) - 1)
data = pd.merge(data, population[features], on='CODGEO', how='outer')



## Activité
activite = pd.read_excel('data/base-ic-activite-residents-2011.xls', sheetname='IRIS')
# creating header from file
header = activite.loc[4].tolist()
activite.columns = header
activite.rename(columns={'IRIS':'CODGEO'}, inplace=True)
# to get real values
activite = activite[5:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['IRIS','REG','DEP','UU2010','COM','LIBCOM','TRIRIS',
                                           'GRD_QUART','LIBIRIS','TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS']]
features.append('CODGEO')
print "il y a  %d iris différentes pour l'activité et %d features" % (len(activite.CODGEO.unique()), len(features) - 1)
data = pd.merge(data, activite[features], on='CODGEO', how='outer')


# Extract 
print "Extracting file in /data/output.csv"
data.to_csv('data/output.csv', sep=';', index=False, encoding='utf-8')




