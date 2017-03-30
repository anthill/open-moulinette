# -*- coding: utf-8 -*-

import pandas as pd
from comparison import compare_geo, fillna_with_other_table

print "Initialisation..."

def _check_data(data, file_name):
    """
    Call _check_iris_doublon & _check_bad_merge_feature
    """
    _check_iris_doublon(data, file_name)
    _check_bad_merge_feature(data, file_name)
    

def _check_iris_doublon(data, file_name):
    """
    To monitor doublon in iris:
    - Input : data -> DataFrame (who is merged)
              file_name -> [string] Name of file merge with data
              
    - Exemple : _check_iris_doublon(data, "Logement 11")
    """
    iris_double = pd.DataFrame(data.IRIS.value_counts().reset_index(drop=False))
    iris_double.columns = ['IRIS', 'nb']
    iris_double_list = iris_double[iris_double.nb >=2].IRIS.unique()
    
    if len(iris_double_list) > 0:
        print "--[KO]-- Warning there is doublon (" +str(len(iris_double_list))+") with file " + file_name
        print iris_double_list
    else:
        print "[OK] No Iris's doublon with " + file_name
        
        
def _check_bad_merge_feature(data, file_name):
    """
    Check if there are some suffix after merge and print it if there is
    """
    
    if len([col for col in data.columns if '_x' in col[-2:]]) > 0:
        print "--[KO]]-- Warning Problem in merge with " + file_name + " : doublon features --> '.._x' / '.._y'"
        for col in data.columns:
            if '_x' in col[-2:]:
                print " -- " +col
    else:
        print "[OK] No doublon features in " + file_name

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
del commerce


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
[features.append(i) for i in ['nb_sport', 'IRIS', 'nb_airjeu_sport']]
print "il y a  %d iris différentes pour le sport et %d features" % (len(sport.IRIS.unique()), len(features) - 1)

compare_geo(data, sport)
data = pd.merge(data, sport[features], on='IRIS', how='outer')
_check_data(data, "Sport 15")
del sport


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
_check_data(data, "Enseignement 1er degré 15")
del enseignement_1


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
_check_data(data, "Enseignement 2nd degré 15")
del enseignement_2


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
_check_data(data, "Enseignement supérieur 15")
del enseignement_sup


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
_check_data(data, "Revenu Ménage 11")
del revenu_menage

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
_check_data(data, "Revenu par personne 11")
del revenu_personne


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
_check_data(data, "Revenu par unité de consomation 11")
del revenu_uc

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
_check_data(data, "Revenu impsé et détails 11")
del revenu_impose

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
_check_data(data, "Equipement social 15")
del equipement_social


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
_check_data(data, "Equipement santé 15")
del equipement_sante


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
_check_data(data, "Fonction médical 15")
del fonction_medical

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
_check_data(data, "Service pour les particuliers 15")
del service_particulier


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
_check_data(data, "Transport touristique 15")
del transport_tourisme

############################################################
####                CENSUS FILES 2011
############################################################

### Logement 2011
logement11 = pd.read_excel('data/base-ic-logement-2011.xls', sheetname='IRIS')
# creating header from file
header = logement11.loc[4].tolist()
logement11.columns = header
logement11.rename(columns={'LIBIRIS': 'LIB_IRIS', 'LIBCOM': 'LIB_COM'}, inplace=True)
# to get real values
logement11 = logement11[5:]

# Adding IRIS (iris ID) and other geo features witch are not in data
features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'COM', 'LIB_IRIS']]
features.remove('P11_PMEN') # P11_PMEN is already in Population file (https://github.com/anthill/open-moulinette/issues/18)

key = ['IRIS', 'REG', 'DEP']
print "il y a  %d iris différentes pour le logement 2011 et %d features" % (len(logement11.IRIS.unique()), len(features) - 1)

logement11 = _correct_LIBGEO(logement11)

data = fillna_with_other_table(data, logement11, 'IRIS')
data = _correct_LIBGEO(data)
compare_geo(data, logement11)
data = pd.merge(data, logement11[features], on=key, how='outer')
_check_data(data, "Logement 2011")
del logement11


## Diplome 2011
diplome11 = pd.read_excel('data/base-ic-diplomes-formation-2011.xls', sheetname='IRIS')
# creating header from file
header = diplome11.loc[4].tolist()
diplome11.columns = header
# to get real values
diplome11 = diplome11[5:]

# Adding IRIS (iris ID) and other geo features witch are not in data
features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'COM', 'UU2010', 'TRIRIS',
                                           'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS']] # This line has been load with Logement file
features.remove('P11_POP0610') # P11_POP0610 is already in Population file (https://github.com/anthill/open-moulinette/issues/18)
features.remove('P11_POP1824') # P11_POP1824 is already in Population file (https://github.com/anthill/open-moulinette/issues/18)
       
key = ['IRIS', 'REG', 'DEP']
print "il y a  %d iris différentes pour les diplomes 2011 et %d features" % (len(diplome11.IRIS.unique()), len(features) - 1)
compare_geo(data, diplome11)
data = pd.merge(data, diplome11[features], on=key, how='outer')
_check_data(data, "Diplome 2011")
del diplome11

## Famille 2011
famille11 = pd.read_excel('data/base-ic-couples-familles-menages-2011.xls', sheetname='IRIS')
# creating header from file
header = famille11.loc[4].tolist()
famille11.columns = header
# to get real values
famille11 = famille11[5:]

features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'COM', 'UU2010', 'TRIRIS',
                                           'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS']] # This line has been load with Logement file
features.remove('P11_POP1524') # P11_POP1524 is already in Activité file (https://github.com/anthill/open-moulinette/issues/18)
features.remove('P11_POP2554') # P11_POP2554 is already in Activité file (https://github.com/anthill/open-moulinette/issues/18)
features.remove('P11_POP80P') # P11_POP80P is already in Population file (https://github.com/anthill/open-moulinette/issues/18))))

key = ['IRIS', 'REG', 'DEP']

print "il y a  %d iris différentes pour les familles 2011 et %d features" % (len(famille11.IRIS.unique()), len(features) - 1)

compare_geo(data, famille11)
data = pd.merge(data, famille11[features], on=key, how='outer')
_check_data(data, "Famille 2011")
del famille11


## Population 2011
population11 = pd.read_excel('data/base-ic-evol-struct-pop-2011.xls', sheetname='IRIS')
# creating header from file
header = population11.loc[4].tolist()
population11.columns = header
# to get real values
population11 = population11[5:]

features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'COM', 'UU2010', 'TRIRIS',
                                           'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS']] # This line has been load with Logement file

key = ['IRIS', 'REG', 'DEP']

print "il y a  %d iris différentes pour le population 2011 et %d features" % (len(population11.IRIS.unique()), len(features) - 1)

compare_geo(data, population11)
data = pd.merge(data, population11[features], on=key, how='outer')
_check_data(data, "Population 2011")
del population11


## Activité 2011
activite11 = pd.read_excel('data/base-ic-activite-residents-2011.xls', sheetname='IRIS')
# creating header from file
header = activite11.loc[4].tolist()
activite11.columns = header
# to get real values
activite11 = activite11[5:]

features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'COM', 'UU2010', 'TRIRIS',
                                           'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS']] # This line has been load with Logement file
features.remove('P11_POP5564') # P11_POP5564 is already in Population file (https://github.com/anthill/open-moulinette/issues/18)

key = ['IRIS', 'REG', 'DEP']

print "il y a  %d iris différentes pour l'activité 2011 et %d features" % (len(activite11.IRIS.unique()), len(features) - 1)

compare_geo(data, activite11)
data = pd.merge(data, activite11[features], on=key, how='outer')
_check_data(data, "Activité 2011")
del activite11


#############################################################
#####                CENSUS FILES 2012
#############################################################

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
# to get real values
logement12 = logement12[5:]

features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'COM', 'UU2010', 'TRIRIS',
                                           'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS', # This line has been load with Logement file
                                           'REG2016']]
key = ['IRIS', 'REG', 'DEP']

print "il y a  %d iris différentes pour le logement 2012 et %d features" % (len(logement12.IRIS.unique()), len(features) - 1)

compare_geo(data, logement12)

data = pd.merge(data, logement12[features], on=key, how='outer')
_check_data(data, "Logement 2012")
del logement12


## Diplome 2012
diplome12 = pd.read_excel('data/base-ic-diplomes-formation-2012.xls', sheetname='IRIS')
# creating header from file
header = diplome12.loc[4].tolist()
diplome12.columns = header
# to get real values
diplome12 = diplome12[5:]

features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'COM', 'UU2010', 'TRIRIS',
                                           'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS', # This line has been load with Logement file
                                           'REG2016']]
features.remove('P12_POP0610') # P12_POP0610 is already in PopPulation file
features.remove('P12_POP1824') # P12_POP1824 is already in Population file

key = ['IRIS', 'REG', 'DEP']

print "il y a  %d iris différentes pour le diplome 2012 et %d features" % (len(diplome12.IRIS.unique()), len(features) - 1)

compare_geo(data, diplome12)
data = pd.merge(data, diplome12[features], on=key, how='outer')
_check_data(data, "Diplome 2012")
del diplome12


## Famille 2012
famille12 = pd.read_excel('data/base-ic-couples-familles-menages-2012.xls', sheetname='IRIS')
# creating header from file
header = famille12.loc[4].tolist()
famille12.columns = header
# to get real values
famille12 = famille12[5:]

features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'COM', 'UU2010', 'TRIRIS',
                                           'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS', # This line has been load with Logement file
                                           'REG2016']]
features.remove('P12_POP1524') # P12_POP1524 is already in Activité file
features.remove('P12_POP2554') # P12_POP2554 is already in Activité file
features.remove('P12_POP80P') # P12_POP80P is already in Population file


key = ['IRIS', 'REG', 'DEP']

print "il y a  %d iris différentes pour les familles 2012 et %d features" % (len(famille12.IRIS.unique()), len(features) - 1)

compare_geo(data, famille12)
data = pd.merge(data, famille12[features], on=key, how='outer')
_check_data(data, "Famille 2012")
del famille12


## Population 2012
population12 = pd.read_excel('data/base-ic-evol-struct-pop-2012.xls', sheetname='IRIS')
# creating header from file
header = population12.loc[4].tolist()
population12.columns = header
# to get real values
population12 = population12[5:]

features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'COM', 'UU2010', 'TRIRIS',
                                           'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS', # This line has been load with Logement file
                                           'REG2016']]
features.remove('P12_PMEN')  # Already in data

key = ['IRIS', 'REG', 'DEP']

print "il y a  %d iris différentes pour le population 2012 et %d features" % (len(population12.IRIS.unique()), len(features) - 1)

compare_geo(data, population12)
data = pd.merge(data, population12[features], on=key, how='outer')
_check_data(data, "Population 2012")
del population12


## Activité 2012
activite12 = pd.read_excel('data/base-ic-activite-residents-2012.xls', sheetname='IRIS')
# creating header from file
header = activite12.loc[4].tolist()
activite12.columns = header
# to get real values
activite12 = activite12[5:]

features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'COM', 'UU2010', 'TRIRIS',
                                           'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS', # This line has been load with Logement file
                                           'REG2016']]
features.remove('P12_POP5564')  # Already in data

key = ['IRIS', 'REG', 'DEP']

print "il y a  %d iris différentes pour l'activité 2012 et %d features" % (len(activite12.IRIS.unique()), len(features) - 1)

compare_geo(data, activite12)
data = pd.merge(data, activite12[features], on=key, how='outer')
_check_data(data, "Activité 2012")
del activite12


#############################################################
#####                CENSUS FILES 2013
#############################################################

# Logement 2013
logement13 = pd.read_excel('data/base-ic-logement-2013.xls', sheetname='IRIS')
# creating header from file
header = logement13.loc[4].tolist()
logement13.columns = header
# to get real values
logement13 = logement13[5:]

features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'COM', 'UU2010', 'TRIRIS',
                                           'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS', # This line has been load with Logement file
                                           'REG2016']]

key = ['IRIS', 'REG', 'DEP']

print "il y a  %d iris différentes pour le logement 2013 et %d features" % (len(logement13.IRIS.unique()), len(features) - 1)

compare_geo(data, logement13)
data = pd.merge(data, logement13[features], on=key, how='outer')
_check_data(data, "Logement 2013")
del logement13


## Diplome 2013
diplome13 = pd.read_excel('data/base-ic-diplomes-formation-2013.xls', sheetname='IRIS')
# creating header from file
header = diplome13.loc[4].tolist()
diplome13.columns = header
# to get real values
diplome13 = diplome13[5:]

features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'COM', 'UU2010', 'TRIRIS',
                                           'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS', # This line has been load with Logement file
                                           'REG2016']]

features.remove('P13_POP0610') # P13_POP0610 is already in Population file (https://github.com/anthill/open-moulinette/issues/18)
features.remove('P13_POP1824') # P13_POP1824 is already in Population file (https://github.com/anthill/open-moulinette/issues/18)

key = ['IRIS', 'REG', 'DEP']

print "il y a  %d iris différentes pour le diplome 2013 et %d features" % (len(diplome13.IRIS.unique()), len(features) - 1)

compare_geo(data, diplome13)
data = pd.merge(data, diplome13[features], on=key, how='outer')
_check_data(data, "Diplome 2013")
del diplome13


## Famille 2013
famille13 = pd.read_excel('data/base-ic-couples-familles-menages-2013.xls', sheetname='IRIS')
# creating header from file
header = famille13.loc[4].tolist()
famille13.columns = header
# to get real values
famille13 = famille13[5:]

features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'COM', 'UU2010', 'TRIRIS',
                                           'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS', # This line has been load with Logement file
                                           'REG2016']]
features.remove('P13_POP1524') # P13_POP1524 is already in Activité file
features.remove('P13_POP2554') # P13_POP2554 is already in Activité file
features.remove('P13_POP80P') # P13_POP80P is already in Population file


key = ['IRIS', 'REG', 'DEP']

print "il y a  %d iris différentes pour les familles 2013 et %d features" % (len(famille13.IRIS.unique()), len(features) - 1)

compare_geo(data, famille13)
data = pd.merge(data, famille13[features], on=key, how='outer')
_check_data(data, "Famille 2013")
del famille13


## Population 2013
population13 = pd.read_excel('data/base-ic-evol-struct-pop-2013.xls', sheetname='IRIS')
# creating header from file
header = population13.loc[4].tolist()
population13.columns = header
# to get real values
population13 = population13[5:]

features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'COM', 'UU2010', 'TRIRIS',
                                           'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS', # This line has been load with Logement file
                                           'REG2016']]
features.remove('P13_PMEN') # P13_POP1524 is already in Activité file


key = ['IRIS', 'REG', 'DEP']

print "il y a  %d iris différentes pour le population 2013 et %d features" % (len(population13.IRIS.unique()), len(features) - 1)


compare_geo(data, population13)
data = pd.merge(data, population13[features], on=key, how='outer')
data.drop_duplicates(subset='IRIS', keep='first', inplace=True)
_check_data(data, "Population 2013")
del population13


## Activité 2013
activite13 = pd.read_excel('data/base-ic-activite-residents-2013.xls', sheetname='IRIS')
# creating header from file
header = activite13.loc[4].tolist()
activite13.columns = header
# to get real values
activite13 = activite13[5:]

features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'COM', 'UU2010', 'TRIRIS',
                                           'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS', # This line has been load with Logement file
                                           'REG2016']]
features.remove('P13_POP5564') # P13_POP5564 is already in Population file

key = ['IRIS', 'REG', 'DEP']

print "il y a  %d iris différentes pour l'activité 2013 et %d features" % (len(activite13.IRIS.unique()), len(features) - 1)

compare_geo(data, activite13)
data = pd.merge(data, activite13[features], on=key, how='outer')
_check_data(data, "Activité 2013")
del activite13


############################################################
####                CENSUS FILES 2010
############################################################

# Logement 2010
logement10 = pd.read_excel('data/base-ic-logement-2010.xls', sheetname='IRIS')
# creating header from file
header = logement10.loc[4].tolist()
logement10.columns = header
# to get real values
logement10 = logement10[5:]


features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'COM', 'UU2010', 'TRIRIS',
                                           'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS', # This line has been load with Logement file
                                           'REG2016']]
features.remove('P10_PMEN') # P10_PMEN is already in Population file


key = ['IRIS', 'REG', 'DEP']       
       
print "il y a  %d iris différentes pour le logement 2010 et %d features" % (len(logement10.IRIS.unique()), len(features) - 1)

compare_geo(data, logement10)
data = pd.merge(data, logement10[features], on=key, how='outer')
_check_data(data, "Logement 2010")
del logement10

## Diplome 2010
diplome10 = pd.read_excel('data/base-ic-diplomes-formation-2010.xls', sheetname='IRIS')
# creating header from file
header = diplome10.loc[4].tolist()
diplome10.columns = header
# to get real values
diplome10 = diplome10[5:]

features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'COM', 'UU2010', 'TRIRIS',
                                           'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS', # This line has been load with Logement file
                                           'REG2016']]
features.remove('P10_POP0610') # P10_POP0610 is already in Population file (https://github.com/anthill/open-moulinette/issues/18)
features.remove('P10_POP1824') # P10_POP1824 is already in Population file (https://github.com/anthill/open-moulinette/issues/18)

key = ['IRIS', 'REG', 'DEP']

print "il y a  %d iris différentes pour le diplome 2010 et %d features" % (len(diplome10.IRIS.unique()), len(features) - 1)

compare_geo(data, diplome10)
data = pd.merge(data, diplome10[features], on=key, how='outer')
_check_data(data, "Diplome 2010")
del diplome10


## Famille 2010
famille10 = pd.read_excel('data/base-ic-couples-familles-menages-2010.xls', sheetname='IRIS')
# creating header from file
header = famille10.loc[4].tolist()
famille10.columns = header
# to get real values
famille10 = famille10[5:]

features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'COM', 'UU2010', 'TRIRIS',
                                           'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS', # This line has been load with Logement file
                                           'REG2016']]
features.remove('P10_POP1524') # P10_POP1524 is already in Activité file
features.remove('P10_POP2554') # P10_POP2554 is already in Activité file
features.remove('P10_POP80P') # P10_POP80P is already in Population file

key = ['IRIS', 'REG', 'DEP']

print "il y a  %d iris différentes pour les familles 2010 et %d features" % (len(famille10.IRIS.unique()), len(features) - 1)

compare_geo(data, famille10)
data = pd.merge(data, famille10[features], on=key, how='outer')
_check_data(data, "Famille 2010")
del famille10


## Population 2010
population10 = pd.read_excel('data/base-ic-evol-struct-pop-2010.xls', sheetname='IRIS')
# creating header from file
header = population10.loc[4].tolist()
population10.columns = header
# to get real values
population10 = population10[5:]

features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'COM', 'UU2010', 'TRIRIS',
                                           'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS', # This line has been load with Logement file
                                           'REG2016']]

key = ['IRIS', 'REG', 'DEP']

print "il y a  %d iris différentes pour le population 2010 et %d features" % (len(population10.IRIS.unique()), len(features) - 1)

compare_geo(data, population10)
data = pd.merge(data, population10[features], on=key, how='outer')
_check_data(data, "Population 2010")
del population10


## Activité 2010
activite10 = pd.read_excel('data/base-ic-caract-emploi-2010.xls', sheetname='IRIS')
# creating header from file
header = activite10.loc[4].tolist()
activite10.columns = header
# to get real values
activite10 = activite10[5:]

# Adding CODGEO (iris ID) and other geo features witch are not in data
features = [x for x in header if x not in ['LIBIRIS', 'LIBCOM', 'COM', 'UU2010', 'TRIRIS',
                                           'GRD_QUART', 'TYP_IRIS', 'MODIF_IRIS', 'LAB_IRIS', # This line has been load with Logement file
                                           'REG2016']]
features.remove('P10_POP5564') # P10_POP5564 is already in Population file


key = ['IRIS', 'REG', 'DEP']

print "il y a  %d iris différentes pour l'activité 2010 et %d features" % (len(activite10.IRIS.unique()), len(features) - 1)

compare_geo(data, activite10)
data = pd.merge(data, activite10[features], on=key, how='outer')
_check_data(data, "Activité 2010")
del activite10


# Extract
print "Extracting file in /data/output.csv"
data.to_csv('data/output.csv', sep=';', index=False, encoding='utf-8')
