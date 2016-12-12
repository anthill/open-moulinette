# -*- coding: utf-8 -*-

import pandas as pd
from comparison import compare_geo, fillna_with_other_table

print "Initialisation..."

def _correct_LIBGEO(data):
    #spécifique 2012
    data['LIB_IRIS'] = data['LIB_IRIS'].str.replace(u' \(commune non irisée\)', '')
    # on le met avant le title()
    data['LIB_IRIS'] = data['LIB_IRIS'].str.title()
    #des fautes d'accent ou de virgule mineures
    data['LIB_IRIS'] = data['LIB_IRIS'].str.replace(u"Jean Bart Guynemer", u"Jean Bart,Guynemer")
    data['LIB_IRIS'] = data['LIB_IRIS'].str.replace(u"Nouveau Siècle", u"Nouveau Siecle")
    data['LIB_IRIS'] = data['LIB_IRIS'].str.replace(u"Labuissière", u"Labuissiere")
    return data


## Commerce
commerce = pd.read_excel('data/equip-serv-commerce-infra-2015.xls', sheetname='IRIS')
# creating header from file
header = commerce.loc[4].tolist()
commerce.columns = header
# to get real values
commerce = commerce[5:]
# clean Nan Columns
commerce.dropna(how='any', axis=(1), inplace=True)
header = [x for x in header if str(x) !='nan'] # remove NaN to header to create new sum feature
# creating new feature : sum of all feature
features = [x for x in header if x not in ['IRIS','LIB_IRIS','COM','LIB_COM','REG','REG2016','DEP']]
commerce['nb_commerce'] =  commerce[features].applymap(lambda x: float(x)).sum(axis=1)

data = commerce
print "il y a  %d iris différentes pour le commerce et %d features" % (len(commerce.IRIS.unique()), len(features))


## Sport
sport = pd.read_excel('data/equip-sport-loisir-socio-infra-2015.xls', sheetname='IRIS')
# creating header from file
header = sport.loc[4].tolist()
sport.columns = header
# to get real values
sport = sport[5:]
# creating new feature : sum all features non aggregated
features = [x for x in header if x not in ['IRIS','LIB_IRIS','COM','LIB_COM','REG','REG2016','DEP']]
# Sum NB_F101 to NB_F118
sport['nb_sport'] = sport[[x for x in sport.columns if x[:5] == 'NB_F1' and len(x) == 7]]\
                    .applymap(lambda x: float(x)).sum(axis=1)
# Sum NB_F101_NB_AIREJEU to NB_F118_NB_AIREJEU
sport['nb_airjeu_sport'] =  sport[[x for x in sport.columns if x[:5] == 'NB_F1' and x[-10:] == 'NB_AIREJEU']]\
                                .applymap(lambda x: float(x)).sum(axis=1)
[features.append(i) for i in ['nb_sport', 'IRIS']]
print "il y a  %d iris différentes pour le sport et %d features" % (len(sport.IRIS.unique()), len(features) - 1)

compare_geo(data, sport)
data = pd.merge(data, sport[features], on='IRIS', how='outer')


## Enseignement 1er degré
enseignement_1 = pd.read_excel('data/equip-serv-ens-1er-degre-infra-2015.xls', sheetname='IRIS')
# creating header from file
header = enseignement_1.loc[4].tolist()
enseignement_1.columns = header
# to get real values
enseignement_1 = enseignement_1[5:]
# creating new feature : sum all features non aggregated
features = [x for x in header if x not in ['IRIS','LIB_IRIS','COM','LIB_COM','REG','REG2016','DEP']]
# Sum NB_C101 to NB_C105
enseignement_1['nb_enseignement_1'] = enseignement_1[[x for x in enseignement_1.columns if x[:2] == 'C1' and len(x) == 4]]\
                                        .applymap(lambda x: float(x)).sum(axis=1)
[features.append(i) for i in ['nb_enseignement_1', 'IRIS']]
print "il y a  %d iris différentes pour l'enseignement du 1er degré et %d features" % (len(enseignement_1.IRIS.unique()), len(features) - 1)

compare_geo(data, enseignement_1)
data = pd.merge(data, enseignement_1[features], on='IRIS', how='outer')


## Enseignement du second degré
enseignement_2 = pd.read_excel('data/equip-serv-ens-2eme-degre-infra-2015.xls', sheetname='IRIS')
# creating header from file
header = enseignement_2.loc[4].tolist()
enseignement_2.columns = header
# to get real values
enseignement_2 = enseignement_2[5:]
# creating new feature : sum all features non aggregated
features = [x for x in header if x not in ['IRIS','LIB_IRIS','COM','LIB_COM','REG','REG2016','DEP']]
# Sum NB_C201 to NB_C305
enseignement_2['nb_enseignement_2'] = enseignement_2[[x for x in enseignement_2.columns if x[0] == 'C' and len(x) == 4]]\
                                        .applymap(lambda x: float(x)).sum(axis=1)
[features.append(i) for i in ['nb_enseignement_2', 'IRIS']]
print "il y a  %d iris différentes pour l'enseignement du second degré et %d features" % (len(enseignement_2.IRIS.unique()), len(features) - 1)

compare_geo(data, enseignement_2)
data = pd.merge(data, enseignement_2[features], on='IRIS', how='outer')


## Enseignement supérieur
enseignement_sup = pd.read_excel('data/equip-serv-ens-sup-form-serv-infra-2015.xls', sheetname='IRIS')
# creating header from file
header = enseignement_sup.loc[4].tolist()
enseignement_sup.columns = header
# to get real values
enseignement_sup = enseignement_sup[5:]
# creating new feature : sum all features non aggregated
features = [x for x in header if x not in ['IRIS','LIB_IRIS','COM','LIB_COM','REG','REG2016','DEP']]
# Sum special columns
enseignement_sup['nb_enseignement_sup'] =  enseignement_sup[['C401', 'C402', 'C403',
                                                             'C409', 'C501', 'C502',
                                                             'C503', 'C504', 'C509',
                                                             'C601', 'C602', 'C603',
                                                             'C604', 'C605', 'C609']].applymap(lambda x: float(x)).sum(axis=1)
[features.append(i) for i in ['nb_enseignement_sup', 'IRIS']]
print "il y a  %d iris différentes pour l'enseignement du supérieur et %d features" % (len(enseignement_sup.IRIS.unique()), len(features) - 1)

compare_geo(data, enseignement_sup)
data = pd.merge(data, enseignement_sup[features], on='IRIS', how='outer')


### Revenu have 4 files [ménage, personne, unité de consomation, ensemble]
#-------------------------------------------------------------------------

## Revenu Ménage
revenu_menage = pd.read_excel('data/RFDM2011IRI.xls', sheetname=1) #using int cause name of sheetname have some "é"
# creating header from file
header = revenu_menage.loc[5].tolist()
revenu_menage.columns = header
# to get real values
revenu_menage = revenu_menage[6:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['IRIS','LIBIRIS','COM','LIBCOM','REG','DEP','ARR','CV','ZE2010']] # special list for this file
# No need to sum features here (% and quantile)
features.append('IRIS')
print "il y a  %d iris différentes pour le revenu par ménage et %d features" % (len(revenu_menage.IRIS.unique()), len(features) - 1)

revenu_menage['LIBCOM'] = revenu_menage['LIBCOM'].str.replace(' - ', '-')
compare_geo(data, revenu_menage)
data = pd.merge(data, revenu_menage[features], on='IRIS', how='outer')

## Revenu par personne
revenu_personne = pd.read_excel('data/RFDP2011IRI.xls', sheetname=1) #using int cause name of sheetname have some "é"
# creating header from file
header = revenu_personne.loc[5].tolist()
revenu_personne.columns = header
# to get real values
revenu_personne = revenu_personne[6:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['IRIS','LIBIRIS','COM','LIBCOM','REG','DEP','ARR','CV','ZE2010']] # special list for this file
# No need to sum features here (% and quantile)
features.append('IRIS')
print "il y a  %d iris différentes pour le revenu par personne et %d features" % (len(revenu_personne.IRIS.unique()), len(features) - 1)

revenu_personne['LIBCOM'] = revenu_personne['LIBCOM'].str.replace(u' - ', u'-')
data = fillna_with_other_table(data, revenu_personne, 'IRIS')
compare_geo(data, revenu_personne)
data = pd.merge(data, revenu_personne[features], on='IRIS', how='outer')


## Revenu par unité de consomation
revenu_uc = pd.read_excel('data/RFDU2011IRI.xls', sheetname=1) #using int cause name of sheetname have some "é"
# creating header from file
header = revenu_uc.loc[5].tolist()
revenu_uc.columns = header
# to get real values
revenu_uc = revenu_uc[6:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['IRIS','LIBIRIS','COM','LIBCOM','REG','DEP','ARR','CV','ZE2010']] # special list for this file
# No need to sum features here (% and quantile)
features.append('IRIS')
print "il y a  %d iris différentes pour le revenu par unité de consomation et %d features" % (len(revenu_uc.IRIS.unique()), len(features) - 1)

revenu_uc['LIBCOM'] = revenu_uc['LIBCOM'].str.replace(u' - ', u'-')
compare_geo(data, revenu_uc, debug=True)
data = pd.merge(data, revenu_uc[features], on='IRIS', how='outer')

## Revenu % imposé + détails (% ménage imposé, dont traitement salaire etc..)
revenu_impose = pd.read_excel('data/RFST2011IRI.xls', sheetname=1) #using int cause name of sheetname have some "é"
# creating header from file
header = revenu_impose.loc[5].tolist()
revenu_impose.columns = header
# to get real values
revenu_impose = revenu_impose[6:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['IRIS','LIBIRIS','COM','LIBCOM','REG','DEP','ARR','CV','ZE2010']] # special list for this file
# No need to sum features here (% and quantile)
features.append('IRIS')
print "il y a  %d iris différentes pour le revenu par ménage imposé et %d features" % (len(revenu_impose.IRIS.unique()), len(features) - 1)

revenu_impose['LIBCOM'] = revenu_impose['LIBCOM'].str.replace(u' - ', u'-')
compare_geo(data, revenu_impose)
data = pd.merge(data, revenu_impose[features], on='IRIS', how='outer')

### Fin de revenu
#-------------------------------------------------------------------------


## Equipement social
equipement_social = pd.read_excel('data/equip-serv-action-sociale-infra-2015.xls', sheetname='IRIS')
# creating header from file
header = equipement_social.loc[4].tolist()
equipement_social.columns = header
# to get real values
equipement_social = equipement_social[5:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['IRIS','LIB_IRIS','COM','LIB_COM','REG','REG2016','DEP','ARR']]
equipement_social['nb_equipement_social'] =  equipement_social[features].applymap(lambda x: float(x)).sum(axis=1)
[features.append(i) for i in ['nb_equipement_social', 'IRIS']]
print "il y a  %d iris différentes pour l'équipement social et %d features" % (len(equipement_social.IRIS.unique()), len(features) - 1)

compare_geo(data, equipement_social)
data = pd.merge(data, equipement_social[features], on='IRIS', how='outer')


## Equipement santé
equipement_sante = pd.read_excel('data/equip-serv-sante-infra-2015.xls', sheetname='IRIS')
# creating header from file
header = equipement_sante.loc[4].tolist()
equipement_sante.columns = header
# to get real values
equipement_sante = equipement_sante[5:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['IRIS','LIB_IRIS','COM','LIB_COM','REG','REG2016','DEP','ARR']]
equipement_sante['nb_equipement_sante'] =  equipement_sante[features].applymap(lambda x: float(x)).sum(axis=1)
[features.append(i) for i in ['nb_equipement_sante', 'IRIS']]
print "il y a  %d iris différentes pour l'équipement de santé et %d features" % (len(equipement_sante.IRIS.unique()), len(features) - 1)

compare_geo(data, equipement_sante)
data = pd.merge(data, equipement_sante[features], on='IRIS', how='outer')


## Fonction médical
fonction_medical = pd.read_excel('data/equip-serv-medical-para-infra-2015.xls', sheetname='IRIS')
# creating header from file
header = fonction_medical.loc[4].tolist()
fonction_medical.columns = header
# to get real values
fonction_medical = fonction_medical[5:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['IRIS','LIB_IRIS','COM','LIB_COM','REG','REG2016','DEP','ARR']]
fonction_medical['nb_fonction_medical'] =  fonction_medical[features].applymap(lambda x: float(x)).sum(axis=1)
[features.append(i) for i in ['nb_fonction_medical', 'IRIS']]
print "il y a  %d iris différentes pour les fonctions médical et %d features" % (len(fonction_medical.IRIS.unique()), len(features) - 1)

compare_geo(data, fonction_medical)
data = pd.merge(data, fonction_medical[features], on='IRIS', how='outer')

## Service pour les particuliers
service_particulier = pd.read_excel('data/equip-serv-particuliers-infra-2015.xls', sheetname='IRIS')
# creating header from file
header = service_particulier.loc[4].tolist()
service_particulier.columns = header
# to get real values
service_particulier = service_particulier[5:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['IRIS','LIB_IRIS','COM','LIB_COM','REG','REG2016','DEP','ARR']]
service_particulier['nb_service_particulier'] =  service_particulier[features].applymap(lambda x: float(x)).sum(axis=1)
[features.append(i) for i in ['nb_service_particulier', 'IRIS']]
print "il y a  %d iris différentes pour les services aux particulier et %d features" % (len(service_particulier.IRIS.unique()), len(features) - 1)

compare_geo(data, service_particulier)
data = pd.merge(data, service_particulier[features], on='IRIS', how='outer')


## Transport touristique
transport_tourisme = pd.read_excel('data/equip-tour-transp-infra-2015.xls', sheetname='IRIS')
# creating header from file
header = transport_tourisme.loc[4].tolist()
transport_tourisme.columns = header
# to get real values
transport_tourisme = transport_tourisme[5:]
# creating new feature : sum of all feature
features = [x for x in header if x not in ['IRIS','LIB_IRIS','COM','LIB_COM','REG','REG2016','DEP','ARR']]
transport_tourisme['nb_transport_tourisme'] =  transport_tourisme[features].applymap(lambda x: float(x)).sum(axis=1)
[features.append(i) for i in ['nb_transport_tourisme', 'IRIS']]
print "il y a  %d iris différentes pour le transport touristique et %d features" % (len(transport_tourisme.IRIS.unique()), len(features) - 1)

compare_geo(data, transport_tourisme)
data = pd.merge(data, transport_tourisme[features], on='IRIS', how='outer')

############################################################
####                CENSUS FILES 2011
############################################################

## Logement 2011
logement11 = pd.read_excel('data/base-ic-logement-2011.xls', sheetname='IRIS')
# creating header from file
header = logement11.loc[4].tolist()
logement11.columns = header
logement11.rename(columns={'LIBIRIS': 'LIB_IRIS', 'LIBCOM': 'LIB_COM'}, inplace=True)
# to get real values
logement11 = logement11[5:]

# Adding IRIS (iris ID) and other geo features witch are not in data
features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM']]
features.remove('P11_PMEN') # P11_PMEN is already in Population file (https://github.com/anthill/open-moulinette/issues/18)
[features.append(i) for i in ['LIB_IRIS', 'LIB_COM']]

key = ['IRIS', 'LIB_IRIS', 'COM', 'LIB_COM', 'REG', 'DEP']
print "il y a  %d iris différentes pour le logement 2011 et %d features" % (len(logement11.IRIS.unique()), len(features) - 1)

logement11 = _correct_LIBGEO(logement11)

data = fillna_with_other_table(data, logement11, 'IRIS')
data = _correct_LIBGEO(data)
compare_geo(data, logement11)
data = pd.merge(data, logement11[features], on=key, how='outer')
data.drop_duplicates(subset='IRIS', keep='first', inplace=True)


## Diplome 2011
diplome11 = pd.read_excel('data/base-ic-diplomes-formation-2011.xls', sheetname='IRIS')
# creating header from file
header = diplome11.loc[4].tolist()
diplome11.columns = header
diplome11.rename(columns={'LIBIRIS': 'LIB_IRIS', 'LIBCOM': 'LIB_COM'}, inplace=True)
# to get real values
diplome11 = diplome11[5:]

# Adding IRIS (iris ID) and other geo features witch are not in data
features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM']]
features.remove('P11_POP0610') # P11_POP0610 is already in Population file (https://github.com/anthill/open-moulinette/issues/18)
features.remove('P11_POP1824') # P11_POP1824 is already in Population file (https://github.com/anthill/open-moulinette/issues/18)
[features.append(i) for i in ['LIB_IRIS', 'LIB_COM']]

key = ['IRIS', 'LIB_IRIS', 'COM', 'LIB_COM', 'REG', 'DEP', 'UU2010',
       'TRIRIS', 'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS'] # This line has been load with Logement file
print "il y a  %d iris différentes pour les diplomes 2011 et %d features" % (len(diplome11.IRIS.unique()), len(features) - 1)

diplome11 = _correct_LIBGEO(diplome11)
compare_geo(data, diplome11)
data = pd.merge(data, diplome11[features], on=key, how='outer')
data.drop_duplicates(subset='IRIS', keep='first', inplace=True)


## Famille 2011
famille11 = pd.read_excel('data/base-ic-couples-familles-menages-2011.xls', sheetname='IRIS')
# creating header from file
header = famille11.loc[4].tolist()
famille11.columns = header
famille11.rename(columns={'LIBIRIS': 'LIB_IRIS', 'LIBCOM': 'LIB_COM'}, inplace=True)
# to get real values
famille11 = famille11[5:]

# Adding CODGEO (iris ID) and other geo features witch are not in data
features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM']]
features.remove('P11_POP1524') # P11_POP1524 is already in Activité file (https://github.com/anthill/open-moulinette/issues/18)
features.remove('P11_POP2554') # P11_POP2554 is already in Activité file (https://github.com/anthill/open-moulinette/issues/18)
features.remove('P11_POP80P') # P11_POP80P is already in Population file (https://github.com/anthill/open-moulinette/issues/18))))
[features.append(i) for i in ['LIB_IRIS', 'LIB_COM']]

key = ['IRIS', 'LIB_IRIS', 'COM', 'LIB_COM', 'REG', 'DEP', 'UU2010',
       'TRIRIS', 'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS'] # This line has been load with Logement file

print "il y a  %d iris différentes pour les familles 2011 et %d features" % (len(famille11.IRIS.unique()), len(features) - 1)

famille11 = _correct_LIBGEO(famille11)
compare_geo(data, famille11)
data = pd.merge(data, famille11[features], on=key, how='outer')
data.drop_duplicates(subset='IRIS', keep='first', inplace=True)


## Population 2011
population11 = pd.read_excel('data/base-ic-evol-struct-pop-2011.xls', sheetname='IRIS')
# creating header from file
header = population11.loc[4].tolist()
population11.columns = header
population11.rename(columns={'LIBIRIS': 'LIB_IRIS', 'LIBCOM': 'LIB_COM'}, inplace=True)
# to get real values
population11 = population11[5:]

# Adding CODGEO (iris ID) and other geo features witch are not in data
features = [x for x in header if x not in ['LIBCOM', 'LIBIRIS']]
[features.append(i) for i in ['LIB_IRIS', 'LIB_COM']]

key = ['IRIS', 'LIB_IRIS', 'COM', 'LIB_COM', 'REG', 'DEP', 'UU2010',
       'TRIRIS', 'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS'] # This line has been load with Logement file

print "il y a  %d iris différentes pour le population 2011 et %d features" % (len(population11.IRIS.unique()), len(features) - 1)
population11 = _correct_LIBGEO(population11)
compare_geo(data, population11)
data = pd.merge(data, population11[features], on=key, how='outer')
data.drop_duplicates(subset='IRIS', keep='first', inplace=True)


## Activité 2011
activite11 = pd.read_excel('data/base-ic-activite-residents-2011.xls', sheetname='IRIS')
# creating header from file
header = activite11.loc[4].tolist()
activite11.columns = header
activite11.rename(columns={'LIBIRIS': 'LIB_IRIS', 'LIBCOM': 'LIB_COM'}, inplace=True)
# to get real values
activite11 = activite11[5:]

# Adding CODGEO (iris ID) and other geo features witch are not in data
features = [x for x in header if x not in ['LIBCOM', 'LIBIRIS']]
features.remove('P11_POP5564') # P11_POP5564 is already in Population file (https://github.com/anthill/open-moulinette/issues/18)
[features.append(i) for i in ['LIB_IRIS', 'LIB_COM']]

key = ['IRIS', 'LIB_IRIS', 'COM', 'LIB_COM', 'REG', 'DEP', 'UU2010',
       'TRIRIS', 'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS'] # This line has been load with Logement file

print "il y a  %d iris différentes pour l'activité 2011 et %d features" % (len(activite11.IRIS.unique()), len(features) - 1)
activite11 = _correct_LIBGEO(activite11)
compare_geo(data, activite11)
data = pd.merge(data, activite11[features], on=key, how='outer')
data.drop_duplicates(subset='IRIS', keep='first', inplace=True)


# 110 rows are NaN for this label #corrected with fillna_with_other_table
#data.dropna(subset=[u'LIBGEO',
#                     u'COM',
#                     u'LIBCOM',
#                     u'REG',
#                     u'DEP',
#                     u'UU2010'], how='all', inplace=True)

############################################################
####                CENSUS FILES 2012
############################################################

# New Region Code (REG2016)

new_reg_dict = {'01' : '01',
                '02' : '02',
                '03' : '03',
                '04' : '04',
                '11' : '11',
                '21' : '44',
                '22' : '32',
                '23' : '28',
                '24' : '24',
                '25' : '28',
                '26' : '27',
                '31' : '32',
                '41' : '44',
                '42' : '44',
                '43' : '27',
                '52' : '52',
                '53' : '53',
                '54' : '75',
                '72' : '75',
                '73' : '76',
                '74' : '75',
                '82' : '84',
                '83' : '84',
                '91' : '76',
                '93' : '93',
                '94' : '94'}
data['REG2016'] = data.REG.map(new_reg_dict)


# Logement 2012
logement12 = pd.read_excel('data/base-ic-logement-2012.xls', sheetname='IRIS')
# creating header from file
header = logement12.loc[4].tolist()
logement12.columns = header
logement12.rename(columns={'LIBIRIS': 'LIB_IRIS', 'LIBCOM': 'LIB_COM'}, inplace=True)
# to get real values
logement12 = logement12[5:]

# Adding CODGEO (iris ID) and other geo features witch are not in data
features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM']]
features.remove('P12_PMEN') # P12_PMEN is already in Population file
[features.append(i) for i in ['LIB_IRIS', 'LIB_COM']]

key = ['IRIS', 'LIB_IRIS', 'COM', 'LIB_COM', 'REG', 'REG2016', 'LAB_IRIS',
       'DEP', 'UU2010', 'TRIRIS', 'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS']
print "il y a  %d iris différentes pour le logement 2012 et %d features" % (len(logement12.IRIS.unique()), len(features) - 1)

logement12 = _correct_LIBGEO(logement12)
compare_geo(data, logement12)
# recommandation: merge on CODGEO only and take 2012 LIBGEO.
# LIBGEO12 seems an update of LIBGEO11
# examples : Mendela => Mandela; Anne Franck => Anne Frank,...
# pareil pour LIBCOM ?
data = pd.merge(data, logement12[features], on=key, how='outer')
data.drop_duplicates(subset='IRIS', keep='first', inplace=True)


## Diplome 2012
diplome12 = pd.read_excel('data/base-ic-diplomes-formation-2012.xls', sheetname='IRIS')
# creating header from file
header = diplome12.loc[4].tolist()
diplome12.columns = header
diplome12.rename(columns={'LIBIRIS': 'LIB_IRIS', 'LIBCOM': 'LIB_COM'}, inplace=True)
# to get real values
diplome12 = diplome12[5:]

# Adding CODGEO (iris ID) and other geo features witch are not in data
features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM']]
features.remove('P12_POP0610') # P12_POP0610 is already in PopPulation file
features.remove('P12_POP1824') # P12_POP1824 is already in Population file
[features.append(i) for i in ['LIB_IRIS', 'LIB_COM']]

key = ['IRIS', 'LIB_IRIS', 'COM', 'LIB_COM', 'REG', 'DEP', 'UU2010', 'REG2016',
       'TRIRIS', 'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS']

print "il y a  %d iris différentes pour le diplome 2012 et %d features" % (len(diplome12.IRIS.unique()), len(features) - 1)

diplome12 = _correct_LIBGEO(diplome12)
#compare_geo(data, diplome12)
data = pd.merge(data, diplome12[features], on=key, how='outer')
data.drop_duplicates(subset='IRIS', keep='first', inplace=True)


## Famille 2012
famille12 = pd.read_excel('data/base-ic-couples-familles-menages-2012.xls', sheetname='IRIS')
# creating header from file
header = famille12.loc[4].tolist()
famille12.columns = header
famille12.rename(columns={'LIBIRIS': 'LIB_IRIS', 'LIBCOM': 'LIB_COM'}, inplace=True)
# to get real values
famille12 = famille12[5:]

# Adding CODGEO (iris ID) and other geo features witch are not in data
features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM']]
features.remove('P12_POP1524') # P12_POP1524 is already in Activité file
features.remove('P12_POP2554') # P12_POP2554 is already in Activité file
features.remove('P12_POP80P') # P12_POP80P is already in Population file
[features.append(i) for i in ['LIB_IRIS', 'LIB_COM']]

key = ['IRIS', 'LIB_IRIS', 'COM', 'LIB_COM', 'REG', 'DEP', 'UU2010', 'REG2016',
       'TRIRIS', 'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS']

print "il y a  %d iris différentes pour les familles 2012 et %d features" % (len(famille12.IRIS.unique()), len(features) - 1)

famille12 = _correct_LIBGEO(famille12)
#compare_geo(data, famille12)
# recommandation: merge on CODGEO only and take 2012 LIBGEO.
# LIBGEO12 seems an update of LIBGEO11
# examples : Mendela => Mandela; Anne Franck => Anne Frank,...
# pareil pour LIBCOM ?
data = pd.merge(data, famille12[features], on=key, how='outer')
data.drop_duplicates(subset='IRIS', keep='first', inplace=True)


## Population 2012
population12 = pd.read_excel('data/base-ic-evol-struct-pop-2012.xls', sheetname='IRIS')
# creating header from file
header = population12.loc[4].tolist()
population12.columns = header
population12.rename(columns={'LIBIRIS': 'LIB_IRIS', 'LIBCOM': 'LIB_COM'}, inplace=True)
# to get real values
population12 = population12[5:]

# Adding CODGEO (iris ID) and other geo features witch are not in data
features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM']]
[features.append(i) for i in ['LIB_IRIS', 'LIB_COM']]

key = ['IRIS', 'LIB_IRIS', 'COM', 'LIB_COM', 'REG', 'DEP', 'UU2010', 'REG2016',
       'TRIRIS', 'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS'] # This line has been load with Logement file

print "il y a  %d iris différentes pour le population 2012 et %d features" % (len(population12.IRIS.unique()), len(features) - 1)

population12 = _correct_LIBGEO(population12)
#compare_geo(data, population12)
# recommandation: merge on CODGEO only and take 2012 LIBGEO.
# LIBGEO12 seems an update of LIBGEO11
# examples : Mendela => Mandela; Anne Franck => Anne Frank,...
# pareil pour LIBCOM ?
data = pd.merge(data, population12[features], on=key, how='outer')
data.drop_duplicates(subset='IRIS', keep='first', inplace=True)


## Activité 2012
activite12 = pd.read_excel('data/base-ic-activite-residents-2012.xls', sheetname='IRIS')
# creating header from file
header = activite12.loc[4].tolist()
activite12.columns = header
activite12.rename(columns={'LIBIRIS': 'LIB_IRIS', 'LIBCOM': 'LIB_COM'}, inplace=True)
# to get real values
activite12 = activite12[5:]

# Adding CODGEO (iris ID) and other geo features witch are not in data
features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM']]
features.remove('P12_POP5564') # P12_POP5564 is already in Population file
[features.append(i) for i in ['LIB_IRIS', 'LIB_COM']]

key = ['IRIS', 'LIB_IRIS', 'COM', 'LIB_COM', 'REG', 'DEP', 'UU2010', 'REG2016',
       'TRIRIS', 'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS'] # This line has been load with Logement file

print "il y a  %d iris différentes pour l'activité 2012 et %d features" % (len(activite12.IRIS.unique()), len(features) - 1)

activite12 = _correct_LIBGEO(activite12)
#compare_geo(data, activite12)
# recommandation: merge on CODGEO only and take 2012 LIBGEO.
# LIBGEO12 seems an update of LIBGEO11
# examples : Mendela => Mandela; Anne Franck => Anne Frank,...
# pareil pour LIBCOM ?
data = pd.merge(data, activite12[features], on=key, how='outer')
data.drop_duplicates(subset='IRIS', keep='first', inplace=True)


############################################################
####                CENSUS FILES 2013
############################################################

# Logement 2013
logement13 = pd.read_excel('data/base-ic-logement-2013.xls', sheetname='IRIS')
# creating header from file
header = logement13.loc[4].tolist()
logement13.columns = header
logement13.rename(columns={'LIBIRIS': 'LIB_IRIS', 'LIBCOM': 'LIB_COM'}, inplace=True)
# to get real values
logement13 = logement13[5:]

# Adding CODGEO (iris ID) and other geo features witch are not in data
features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM']]
features.remove('P13_PMEN') # P13_PMEN is already in Population file
[features.append(i) for i in ['LIB_IRIS', 'LIB_COM']]

key = ['IRIS', 'LIB_IRIS', 'COM', 'LIB_COM', 'REG', 'REG2016', 'LAB_IRIS',
       'DEP', 'UU2010', 'TRIRIS', 'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS']
print "il y a  %d iris différentes pour le logement 2013 et %d features" % (len(logement13.IRIS.unique()), len(features) - 1)

logement13 = _correct_LIBGEO(logement13)
compare_geo(data, logement13)
data = pd.merge(data, logement13[features], on=key, how='outer')
data.drop_duplicates(subset='IRIS', keep='first', inplace=True)


## Diplome 2013
diplome13 = pd.read_excel('data/base-ic-diplomes-formation-2013.xls', sheetname='IRIS')
# creating header from file
header = diplome13.loc[4].tolist()
diplome13.columns = header
diplome13.rename(columns={'LIBIRIS': 'LIB_IRIS', 'LIBCOM': 'LIB_COM'}, inplace=True)
# to get real values
diplome13 = diplome13[5:]

# Adding CODGEO (iris ID) and other geo features witch are not in data
features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM']]
features.remove('P13_POP0610') # P13_POP0610 is already in Population file (https://github.com/anthill/open-moulinette/issues/18)
features.remove('P13_POP1824') # P13_POP1824 is already in Population file (https://github.com/anthill/open-moulinette/issues/18)
[features.append(i) for i in ['LIB_IRIS', 'LIB_COM']]

key = ['IRIS', 'LIB_IRIS', 'COM', 'LIB_COM', 'REG', 'DEP', 'UU2010', 'REG2016',
       'TRIRIS', 'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS']

print "il y a  %d iris différentes pour le diplome 2013 et %d features" % (len(diplome13.IRIS.unique()), len(features) - 1)

diplome13 = _correct_LIBGEO(diplome13)
#compare_geo(data, diplome13)
data = pd.merge(data, diplome13[features], on=key, how='outer')
data.drop_duplicates(subset='IRIS', keep='first', inplace=True)


## Famille 2013
famille13 = pd.read_excel('data/base-ic-couples-familles-menages-2013.xls', sheetname='IRIS')
# creating header from file
header = famille13.loc[4].tolist()
famille13.columns = header
famille13.rename(columns={'LIBIRIS': 'LIB_IRIS', 'LIBCOM': 'LIB_COM'}, inplace=True)
# to get real values
famille13 = famille13[5:]

# Adding CODGEO (iris ID) and other geo features witch are not in data
features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM']]
features.remove('P13_POP1524') # P13_POP1524 is already in Activité file
features.remove('P13_POP2554') # P13_POP2554 is already in Activité file
features.remove('P13_POP80P') # P13_POP80P is already in Population file
[features.append(i) for i in ['LIB_IRIS', 'LIB_COM']]

key = ['IRIS', 'LIB_IRIS', 'COM', 'LIB_COM', 'REG', 'DEP', 'UU2010', 'REG2016',
       'TRIRIS', 'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS']

print "il y a  %d iris différentes pour les familles 2013 et %d features" % (len(famille13.IRIS.unique()), len(features) - 1)

famille13 = _correct_LIBGEO(famille13)
data = pd.merge(data, famille13[features], on=key, how='outer')
data.drop_duplicates(subset='IRIS', keep='first', inplace=True)


## Population 2013
population13 = pd.read_excel('data/base-ic-evol-struct-pop-2013.xls', sheetname='IRIS')
# creating header from file
header = population13.loc[4].tolist()
population13.columns = header
population13.rename(columns={'LIBIRIS': 'LIB_IRIS', 'LIBCOM': 'LIB_COM'}, inplace=True)
# to get real values
population13 = population13[5:]

# Adding CODGEO (iris ID) and other geo features witch are not in data
features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM']]
[features.append(i) for i in ['LIB_IRIS', 'LIB_COM']]

key = ['IRIS', 'LIB_IRIS', 'COM', 'LIB_COM', 'REG', 'DEP', 'UU2010', 'REG2016',
       'TRIRIS', 'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS'] # This line has been load with Logement file

print "il y a  %d iris différentes pour le population 2013 et %d features" % (len(population13.IRIS.unique()), len(features) - 1)

population13 = _correct_LIBGEO(population13)
data = pd.merge(data, population13[features], on=key, how='outer')
data.drop_duplicates(subset='IRIS', keep='first', inplace=True)


## Activité 2013
activite13 = pd.read_excel('data/base-ic-activite-residents-2013.xls', sheetname='IRIS')
# creating header from file
header = activite13.loc[4].tolist()
activite13.columns = header
activite13.rename(columns={'LIBIRIS': 'LIB_IRIS', 'LIBCOM': 'LIB_COM'}, inplace=True)
# to get real values
activite13 = activite13[5:]

# Adding CODGEO (iris ID) and other geo features witch are not in data
features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM']]
features.remove('P13_POP5564') # P13_POP5564 is already in Population file
[features.append(i) for i in ['LIB_IRIS', 'LIB_COM']]

key = ['IRIS', 'LIB_IRIS', 'COM', 'LIB_COM', 'REG', 'DEP', 'UU2010', 'REG2016',
       'TRIRIS', 'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS'] # This line has been load with Logement file

print "il y a  %d iris différentes pour l'activité 2013 et %d features" % (len(activite13.IRIS.unique()), len(features) - 1)

activite13 = _correct_LIBGEO(activite13)
data = pd.merge(data, activite13[features], on=key, how='outer')
data.drop_duplicates(subset='IRIS', keep='first', inplace=True)


############################################################
####                CENSUS FILES 2010
############################################################

# Logement 2010
logement10 = pd.read_excel('data/base-ic-logement-2010.xls', sheetname='IRIS')
# creating header from file
header = logement10.loc[4].tolist()
logement10.columns = header
logement10.rename(columns={'LIBIRIS': 'LIB_IRIS', 'LIBCOM': 'LIB_COM'}, inplace=True)
# to get real values
logement10 = logement10[5:]

# Adding CODGEO (iris ID) and other geo features witch are not in data
features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'REG2016']]
features.remove('P10_PMEN') # P10_PMEN is already in Population file
[features.append(i) for i in ['LIB_IRIS', 'LIB_COM']]

key = ['IRIS', 'LIB_IRIS', 'COM', 'LIB_COM', 'REG', 'LAB_IRIS',
       'DEP', 'UU2010', 'TRIRIS', 'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS']
print "il y a  %d iris différentes pour le logement 2010 et %d features" % (len(logement10.IRIS.unique()), len(features) - 1)

logement10 = _correct_LIBGEO(logement10)
compare_geo(data, logement10)
data = pd.merge(data, logement10[features], on=key, how='outer')
data.drop_duplicates(subset='IRIS', keep='first', inplace=True)


## Diplome 2010
diplome10 = pd.read_excel('data/base-ic-diplomes-formation-2010.xls', sheetname='IRIS')
# creating header from file
header = diplome10.loc[4].tolist()
diplome10.columns = header
diplome10.rename(columns={'LIBIRIS': 'LIB_IRIS', 'LIBCOM': 'LIB_COM'}, inplace=True)
# to get real values
diplome10 = diplome10[5:]

# Adding CODGEO (iris ID) and other geo features witch are not in data
features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'REG2016']]
features.remove('P10_POP0610') # P10_POP0610 is already in Population file (https://github.com/anthill/open-moulinette/issues/18)
features.remove('P10_POP1824') # P10_POP1824 is already in Population file (https://github.com/anthill/open-moulinette/issues/18)
[features.append(i) for i in ['LIB_IRIS', 'LIB_COM']]

key = ['IRIS', 'LIB_IRIS', 'COM', 'LIB_COM', 'REG', 'DEP', 'UU2010',
       'TRIRIS', 'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS']

print "il y a  %d iris différentes pour le diplome 2010 et %d features" % (len(diplome10.IRIS.unique()), len(features) - 1)

diplome10 = _correct_LIBGEO(diplome10)
#compare_geo(data, diplome10)
data = pd.merge(data, diplome10[features], on=key, how='outer')
data.drop_duplicates(subset='IRIS', keep='first', inplace=True)


## Famille 2010
famille10 = pd.read_excel('data/base-ic-couples-familles-menages-2010.xls', sheetname='IRIS')
# creating header from file
header = famille10.loc[4].tolist()
famille10.columns = header
famille10.rename(columns={'LIBIRIS': 'LIB_IRIS', 'LIBCOM': 'LIB_COM'}, inplace=True)
# to get real values
famille10 = famille10[5:]

# Adding CODGEO (iris ID) and other geo features witch are not in data
features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'REG2016']]
features.remove('P10_POP1524') # P10_POP1524 is already in Activité file
features.remove('P10_POP2554') # P10_POP2554 is already in Activité file
features.remove('P10_POP80P') # P10_POP80P is already in Population file
[features.append(i) for i in ['LIB_IRIS', 'LIB_COM']]

key = ['IRIS', 'LIB_IRIS', 'COM', 'LIB_COM', 'REG', 'DEP', 'UU2010',
       'TRIRIS', 'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS']

print "il y a  %d iris différentes pour les familles 2010 et %d features" % (len(famille10.IRIS.unique()), len(features) - 1)

famille10 = _correct_LIBGEO(famille10)
data = pd.merge(data, famille10[features], on=key, how='outer')
data.drop_duplicates(subset='IRIS', keep='first', inplace=True)


## Population 2010
population10 = pd.read_excel('data/base-ic-evol-struct-pop-2010.xls', sheetname='IRIS')
# creating header from file
header = population10.loc[4].tolist()
population10.columns = header
population10.rename(columns={'LIBIRIS': 'LIB_IRIS', 'LIBCOM': 'LIB_COM'}, inplace=True)
# to get real values
population10 = population10[5:]

# Adding CODGEO (iris ID) and other geo features witch are not in data
features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'REG2016']]
[features.append(i) for i in ['LIB_IRIS', 'LIB_COM']]

key = ['IRIS', 'LIB_IRIS', 'COM', 'LIB_COM', 'REG', 'DEP', 'UU2010',
       'TRIRIS', 'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS'] # This line has been load with Logement file

print "il y a  %d iris différentes pour le population 2010 et %d features" % (len(population10.IRIS.unique()), len(features) - 1)

population10 = _correct_LIBGEO(population10)
data = pd.merge(data, population10[features], on=key, how='outer')
data.drop_duplicates(subset='IRIS', keep='first', inplace=True)


## Activité 2010
activite10 = pd.read_excel('data/base-ic-caract-emploi-2010.xls', sheetname='IRIS')
# creating header from file
header = activite10.loc[4].tolist()
activite10.columns = header
activite10.rename(columns={'LIBIRIS': 'LIB_IRIS', 'LIBCOM': 'LIB_COM'}, inplace=True)
# to get real values
activite10 = activite10[5:]

# Adding CODGEO (iris ID) and other geo features witch are not in data
features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'REG2016']]
features.remove('P10_POP5564') # P10_POP5564 is already in Population file
[features.append(i) for i in ['LIB_IRIS', 'LIB_COM']]

key = ['IRIS', 'LIB_IRIS', 'COM', 'LIB_COM', 'REG', 'DEP', 'UU2010',
       'TRIRIS', 'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS'] # This line has been load with Logement file

print "il y a  %d iris différentes pour l'activité 2010 et %d features" % (len(activite10.IRIS.unique()), len(features) - 1)

activite10 = _correct_LIBGEO(activite10)
data = pd.merge(data, activite10[features], on=key, how='outer')
data.drop_duplicates(subset='IRIS', keep='first', inplace=True)


# Extract
print "Extracting file in /data/output.csv"
data.to_csv('data/output.csv', sep=';', index=False, encoding='utf-8')




