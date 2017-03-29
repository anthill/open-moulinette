# Documentation

This script aggregates more than 80 indicators (on 6 years) available for each city in one single clean file. 90 different files will be load to do the job.

In the `caf_data.csv` column's names are like `xxxxx_2009`, which xxxx is the feature's name. So you can compare feature from 2009 to 2014. 

**this document enumerates each column and explains it**. Decription is in French as all the data concerne French's city.


## List of file :

- Indicateur sur la part des prestations dans les ressources des foyers allocataires
- Foyers allocataires à "bas revenus"
- Population couverte par au moins une prestation
- Répartition des foyers allocataires selon le type de famille
- Dénombrement et répartition des foyers allocataires selon l’âge du responsable de dossier
- Foyers allocataires percevant une aide au logement en décembre
- Foyers allocataires percevant la prestation d'accueil du jeune enfant (Paje)
- Population couverte par le revenu de solidarité active (RSA) en décembre
- Bénéficiaires de l’allocation aux adultes handicapés au cours du mois de décembre
- Répartition des enfants couverts par au moins une prestations Caf - par tranche d'âge
- Nombre d'enfants couverts par l'allocation d'éducation de l'enfant handicapé (AEEH)
- Foyers allocataires percevant le revenu de solidarité active (RSA)
- Foyers allocataires percevant une prestation enfance et jeunesse (AF, CF, ASF, AEEH et ARS)
- Population couverte par une aide personnelle au logement en décembre
- Nombre d'enfants couverts par l'allocation de rentrée scolaire (ARS)


## Description géographique

- Codes_Insee : Code insee de la commune
- Code_Postal : Code postal
- Commune : Libellé de commune
- Departement : Libellé de département
- Region : Libellé de région
- Statut : Statut de la commune
- Altitude_Moyenne : Altitude moyenne de la commune
- Superficie : Superficie de la commune (en hectare)
- Population : Population de la commune (en millier d'habitants)
- geo_point_2d : Latitude, longitude de la commune (point)
- geo_shape : Polygone de la commune (geojson)
- ID_Geogla : id geogla
- Code_Commune : Code de la commune
- Code_Canton : Code du canton
- Code_Arrondissement : Code de l'arrondissement
- Code_Departement : Code du département
- Code_Region : Code de la région

*Attention :*

Certaines villes ont fusionné avec d'autres :

*Fort-Mardyck* (Codes_Insee == 59248) est maintenant rattaché à *Dunkerque* (59183) et est donc absent de notre référenciel.

A partir de 2014, le champ géographique d’observation du jeu de données correspond à la commune de résidence du foyer allocataire telle qu’elle est enregistrée dans le fichier statistique des allocataires extrait début d’année N+1 et ce quelle que soit la Caf de gestion.Les deux premières lignes du fichier recouvrent les allocataires résidents à l'étranger (code 99999) et les allocataires dont la commune de résidence est inconnue (code XXXXX). En 2012 et 2013 les résidents à l'étranger n'ont pas été comptabilisés. 

En 2009, 2010 et 2011, la première ligne (code 99999) recouvre, en plus des résidents à l'étranger, tous les allocataires vivant sur une commune en dehors du territoire de leur caf de gestion.

## Vocubulaire de la CAF :

**Le foyer allocataire** est l’entité administrative à laquelle les Caf versent au moins une prestation. Il est composé de l’allocataire (personne qui perçoit au moins une prestation au regard de sa situation familiale et/ou monétaire), de son conjoint/concubin/pacsé éventuel, des enfants à charge et autres personnes à charge au sens de la réglementation en vigueur. Un foyer allocataire peut donc comporter une ou plusieurs personnes.

**Le droit versable** signifie que le foyer allocataire remplit toutes les conditions pour être effectivement payé au titre du mois d’observation. En particulier ne sont pas inclus dans ce périmètre les bénéficiaires qui n’ont pas fourni l’intégralité de leurs pièces justificatives, ou ceux dont le montant de la prestation est inférieur au seuil de versement.

**L’âge retenu** est l’âge atteint dans l’année (ou âge  par génération). Il correspond à la différence entre l'année d’observation et l'année de naissance de l'individu. Les intervalles des tranches d'âges sont des intervalles fermés.

**L'âge inconnu** correspond à des problèmes techniques ou des valeurs aberrantes saisies dans la base de données. A titre d'exemple les âges inférieurs à 15 ans et supérieur à 120 ans sont considérés aberrants.

## Nombre d'allocataires total :

- **NB_Allocataires_2009** : nombre total de foyers allocataires de la branche famille en 2009.
- **NB_Allocataires_2010** : nombre total de foyers allocataires de la branche famille en 2010.
- **NB_Allocataires_2011** : nombre total de foyers allocataires de la branche famille en 2011.
- **NB_Allocataires_2012** : nombre total de foyers allocataires de la branche famille en 2012.
- **NB_Allocataires_2013** : nombre total de foyers allocataires de la branche famille en 2013.
- **NB_Allocataires_2014** : nombre total de foyers allocataires de la branche famille en 2014.

*Les années seront représentées par "yyyy" par la suite (allant de 2009 à 2014 inclus)*

## Indicateur sur la part des prestations dans les ressources des foyers allocataires *(DPC)*

- **TR50PFRB_yyyy** : 
- **TR100PFRB_yyyy** : 

*Absence de documentation sur le portail...*

[source](http://data.caf.fr/dataset/indicateur-sur-la-part-des-prestations-dans-les-ressources-des-foyers-allocataires-par-commune)

## Foyers allocataires à "bas revenus" *(BC)* 

 - **ALL_bas_revenu_yyyy** : nombre total de foyers allocataires bas revenus.
 - **Pers_bas_revenu_yyyy** : nombre total de personnes couvertes par les foyers bas revenus.
 - **NB_allocataires_ress_yyyy** : nombre de foyers allocataires de référence pour le calcul des "bas revenus"
 - **NB_pers_couv_ress_yyyy** : nombre de personnes couvertes de référence pour le calcul des "bas revenus"

[source](http://data.caf.fr/dataset/beneficiaire-bas-revenus)

## Population couverte par au moins une prestation *(NCT)*

- **NB_Pers_par_Foyer_Alloc_yyyy_NCT** : nombre de personnes couvertes par la branche famille
- **NB_Enfants_yyyy_NCT** : nombre d'enfants couverts

Pour  2009, il y a une plus grande granularité pour le nombre d'enfants :
- **NB_Enfants_0_2_ans_NCT_2009** : Nombre d'enfants de 0 à 2 ans couverts
- **NB_Enfants_3_5_ans_NCT_2009** : Nombre d'enfants de 3 à 5 ans couverts


[source](http://data.caf.fr/dataset/population-des-foyers-allocataires-par-commune)

## Répartition des foyers allocataires selon le type de famille *(CF)*

- **COUP_0_ENF_yyyy** : nombre de foyers allocataires couples sans enfant
- **COUP_1_ENF_yyyy** : nombre de foyers allocataires couples avec 1 enfant
- **COUP_2_ENF_yyyy** : nombre de foyers allocataires couples avec 2 enfants
- **COUP_3_ENF_yyyy** : nombre de foyers allocataires couples avec 3 enfants
- **COUP_4plus_ENF_yyyy** : nombre de foyers allocataires couples avec 4 ou x enfants
- **Homme_Isole_yyyy** : nombre de foyers allocataires messieurs isoles
- **Femme_Isolee_yyyy** : nombre de foyers allocataires mesdames isolees
- **MONO_1_ENF_yyyy** : nombre de foyers allocataires monoparents avec 1 enfant
- **MONO_2_ENF_yyyy** : nombre de foyers allocataires monoparents avec 2 enfants
- **MONO_3_ENF_yyyy** : nombre de foyers allocataires monoparents avec 3 enfants
- **MONO_4plus_ENF_yyyy** : nombre de foyers allocataires monoparents avec 4 ou x enfants

Les notions de couples, de familles monoparentales et de personnes isolées sont établies au sens de la législation familiale.

La notion d'enfant dans ce jeu de données renvoit à la notion d'enfant à charge au sens de la législation familiale.
Pour avoir la charge d’un enfant, l’allocataire doit assurer financièrement son entretien de manière effective et permanente et assumer à son égard la responsabilité affective et éducative, sans obligation de lien de parenté avec l’enfant. On distingue deux notions d’enfant à charge dans la législation :

- Enfant à charge au sens des prestations familiales (Pf) : 
un enfant est reconnu à charge s’il est âgé d’un mois à moins
de 20 ans quelle que soit sa situation, dès lors que son salaire
net mensuel ne dépasse pas 55 % du Smic brut.

- Enfant à charge au sens de la législation familiale: 
en plus des enfants à charge au sens des Pf, sont également considérés à charge
pour les aides au logement, les enfants âgés de moins de 21 ans en Métropole (22 ans dans les Dom), les enfants âgés de 20 à 25 ans pour le calcul du Rmi/Rsa, et dès le mois de leur naissance, les enfants bénéficiaires de l’allocation de base de la Paje.

[source](http://data.caf.fr/dataset/repartition-des-foyers-allocataires-selon-le-type-de-famille-par-commune)


## Dénombrement et répartition des foyers allocataires selon l’âge du responsable de dossier *(TA)*

- **ALL0A19_yyyy** : nombre de foyers allocataires dont le titutailre du dossier est age de moins de 20 ans
- **ALL20A24_yyyy** : nombre de foyers allocataires dont le titutailre du dossier est age de 20 a 24 ans
- **ALL25A29_yyyy** : nombre de foyers allocataires dont le titutailre du dossier est age de 25 a 29 ans
- **ALL30A39_yyyy** : nombre de foyers allocataires dont le titutailre du dossier est age de 30 a 39 ans
- **ALL40A49_yyyy** : nombre de foyers allocataires dont le titutailre du dossier est age de 40 a 49 ans
- **ALL50A54_yyyy** : nombre de foyers allocataires dont le titutailre du dossier est age de 50 a 54 ans
- **ALL55A59_yyyy** : nombre de foyers allocataires dont le titutailre du dossier est age de 55 a 59 ans
- **ALL60A64_yyyy** : nombre de foyers allocataires dont le titutailre du dossier est age de 60 a 64 ans
- **ALL65A69_yyyy** : nombre de foyers allocataires dont le titutailre du dossier est age de 65 a 69 ans
- **ALL70AX_yyyy** : nombre de foyers allocataires dont le titutailre du dossier est age de 70 ans ou plus
- **ALLAGEX_yyyy** : nombre de foyers allocataires dont le titutailre du dossier est d'age inconnu

*Attention* avant 2011 les tranches de plus de 50 ans étaient réparties comme suit "ALL50A59_yyyy" et "ALL60AX_yyyy"

[source](http://data.caf.fr/dataset/denombrement-et-repartition-des-foyers-allocataires-selon-l-age-du-responsable)

## Foyers allocataires percevant une aide au logement en décembre *(LC)*

- **total_allocataires_logement_yyyy** : nombre total de foyers allocataires beneficiaire d'une aide au logement
- **total_ALF_yyyy** : nombre total de foyers allocataires beneficiaire de l'ALF
- **total_ALS_yyyy** : nombre total de foyers allocataires beneficiaire de l'ALS
- **total_APL_yyyy** : nombre total de foyers allocataires beneficiaire de l'APL
- **locataire_ALF_yyyy** : nombre de foyers allocataires, en location ou en foyer beneficiaire de l'ALF
- **locataire_ALS_yyyy** : nombre de foyers allocataires, en location ou en foyer beneficiaire de l'ALS
- **locataire_APL_yyyy** : nombre de foyers allocataires, en location ou en foyer beneficiaire de l'APL
- **proprietaire_ALF_yyyy** : nombre de foyers allocataires, proprietaire beneficiaire de l'ALF
- **proprietaire_ALS_yyyy** : nombre de foyers allocataires, proprietaire beneficiaire de l'ALS
- **proprietaire_APL_yyyy** : nombre de foyers allocataires, proprietaire beneficiaire de l'APL
- **total_locataire_yyyy* : nombre total de foyers allocataires, en location ou en foyer beneficiaire d'une aide au logement
- **total_proprietaire_yyyy** : nombre total de foyers allocataires, proprietaire beneficiaire d'une aide au logement

AFL : Allocation de Logement Familiale
ALS : Allocation de Logement Social
APL : Aide Personnalisée au Logement

Ces trois aides ne sont pas cumulables. L’ordre de priorité d’attribution est le suivant : APL, ALF, ALS.

[source](http://data.caf.fr/dataset/population-des-foyers-allocataires-percevant-une-aide-personnelle-au-logement)

## Foyers allocataires percevant la prestation d'accueil du jeune enfant (Paje) *(PC)*

- **ALL_PAJE_yyyy** : nombre de foyers allocataires PAJE versable
- **ALL_PRIM_yyyy** : nombre de foyers allocataires PRIME naissance ou adoption versees
- **ALL_BASEP_yyyy** : nombre de foyers allocataires avec droit base PAJE versable
- **ALL_CMG_yyyy_yyyy** : nombre de foyers allocataires CMG versable
- **ALL_CMG_ASMA_yyyy** : nombre de foyers allocataires CMG assistante maternelle versable
- **ALL_CMG_DOM_yyyy** : nombre de foyers allocataires cmg garde a domicile versable
- **ALL_CMG_A_yyyy** : nombre de foyers allocataires cmg structure (entreprise ou association) versable
- **ALL_Clca_yyyy** : nombre de foyers allocataires clca versable

La prestation d'accueil du jeune enfant (PAJE) est versée pour un enfant né ou adopté, elle comprend quatre composantes :
 - la prime à la naissance et/ou à l’adoption (sous conditions de ressources)
 - l’allocation de base (sous conditions de ressources) pour les enfants de moins de 3 ans (ou moins de 20 ans pour des enfants adoptés) 
 - le complément de libre choix d’activité (CLCA) pour toute naissance ou adoption avant le 1er janvier 2015 (si vous avez cessé ou réduit votre activité professionnelle pour élever votre ou vos enfant(s)) de moins de 3 ans( ou moins de 20 ans dans le cas d’adoption), puis la prestation partagée d’accueil d’éducation de l’enfant (PreParE) pour toute naissance ou adoption après le 31 décembre 2014 ) 
 - le complément de libre choix de mode de garde (CMG), lorsque le(s) enfant(s) de moins de 6 ans sont gardés par une assistante maternelle agréée, par une garde à domicile, par une association ou entreprise habilitée ou par une micro-crèche

Les colonnes "ALL_CMG_ASMA", "ALL_CMG_A", "ALL_CMG_DOM" et "ALL_CMG" sont extraites au titre du mois novembre. C'est une exception dû à des contraintes techniques.

[source](http://data.caf.fr/dataset/foyers-allocataires-percevant-la-prestation-d-accueil-du-jeune-enfant-paje-par-commune)

## Population couverte par le revenu de solidarité active (RSA) en décembre *(RPC)*

- **NB_Pers_par_Foyer_Alloc_yyyy_RPC** : nombre de personnes couvertes par une prestation de la branche famille
- **NB_Pers_couv_RSA_yyyy** : nombre de personnes couvertes par le rsa
- **RSA_SOCLE_non_Majore_Pers_couv_yyyy** : nombre de personnes couvertes par le rsa socle sans majoration versable
- **RSA_SOCLE_Majore_Pers_couv_yyyy** : nombre de personnes couvertes par le rsa socle avec majoration versable
- **RSA_activite_Pers_couv_yyyy** : nombre de personnes couvertes par le rsa activite versable

Le RSA est une prestation sous conditions de ressources versée mensuellement sur la base des ressources du trimestre précédent. Entré en vigueur le 1er juin 2009 en France métropolitaine et le 1er janvier 2011 dans les départements d’Outre-mer, cette prestation remplace le revenu minimum d'insertion (RMI) et l'allocation de parent isolé (API) pour les personnes privées d'emploi. Il apporte une incitation 
financière aux personnes sans ressource qui reprennent un emploi (le RSA garantit à quelqu'un qui reprend un travail que ses revenus augmentent). Enfin il complète les ressources des personnes dont l'activité professionnelle ne leur apporte que des revenus limités.

Le RSA est versé sans limitation de durée, tant que les revenus du bénéficiaire sont inférieurs au montant maximal du RSA. Le montant versé peut varier si la situation familiale, professionnelle et les ressources du foyer évoluent. Le RSA est constitué de trois composantes : le "RSA socle", le "RSA socle et activité" et le "RSA activité". Ainsi, le RSA couvre une population large, puisqu’il concerne aussi bien des foyers n’ayant aucune ressource, que des personnes percevant des revenus d’activité proches du Smic. Un foyer allocataire du "RSA socle seul" n’a pas de revenus d’activité (toutefois, en cas de reprise d’activité, le bénéficiaire peut cumuler salaires et allocation pendant trois mois). 

Les bénéficiaires du "RSA socle et activité" ont de faibles revenus d’activité et l’ensemble de leurs ressources est inférieur au montant forfaitaire. Ceux du "RSA activité seul" ont de faibles revenus d’activité et l’ensemble de leurs ressources est supérieur au montant forfaitaire. 

Deux types de publics peuvent se combiner aux composantes de RSA :

-les personnes en état de grossesse ou assumant seules la charge d’au moins un enfant bénéficient du "RSA majoré" (on parle alors de "socle majoré" ou "socle et activité majoré" ou "activité majoré")
-les bénéficiaires du RSA ne faisant partie du public "RSA majoré" correspondent au RSA "non majoré". Au sein du public "non majoré" on peut distinguer le public "RSA jeune". Le public RSA jeune concerne les jeunes de moins de 25 ans isolés et sans enfant à charge et versé sous condition d’activité antérieure (deux ans au cours des trois dernières années).

[source](http://data.caf.fr/dataset/population-des-foyers-allocataires-percevant-le-revenu-de-solidarite)

## Bénéficiaires de l’allocation aux adultes handicapés au cours du mois de décembre *(AAHC)*

- **ALL_AAH_yyyy** : nombre d'allocataires avec AAH versable

L’AAH est une prestation versée sous conditions de ressources et résulte de la loi d’orientation du 30 juin 1975 relative aux personnes handicapées. L’AAH permet de garantir un revenu minimal à un adulte handicapé Depuis 2011, le montant de l’allocation aux adultes handicapés (AAH) est calculé par trimestre lorsque la personne exerce une activité en milieu ordinaire. Dans les autres cas la déclaration des ressources 
est annuelle. Les modalités de cumul de la prestation avec les revenus d’activité ont également évolué. Ainsi, une personne seule peut désormais percevoir de l’AAH si ses revenus d’activité sont inférieurs à 1,4 fois le montant du Smic.

Pour bénéficier l’AAH la personne doit avoir au moins 20 ans et un taux de handicap d’au moins 80%. Cependant, les personnes ayant un taux de handicap compris entre 50% et 80% peuvent y avoir droit si elles sont âgées de moins de 60 ans, n’ont pas travaillé depuis au moins un an et si leur handicap constitue un frein à l’accès à l’emploi. Dans tous les cas, l’éventuel bénéficiaire de l’Aah ne doit pas recevoir de pension ou de rente d’accident du travail supérieure à un certain montant.

[source](http://data.caf.fr/dataset/personnes-ayant-un-droit-versable-a-l-allocation-aux-adultes-handicapes)

## Répartition des enfants couverts par au moins une prestations Caf *(EAC)*

- **NB_enfants_yyyy_EAC** : nombre d'enfants beneficiaires d'au moins une prestation CAF versable
- **NB_Enfants_0_2_ans_yyyy_EAC** : nombre d'enfants de 0 a 2 ans, beneficiaires d'au moins une prestation CAF versable
- **NB_Enfants_3_5_ans_yyyy_EAC** : nombre d'enfants de 3 a 5 ans, beneficiaires d'au moins une prestation CAF versable
- **NB_Enfants_6_11_ans_yyyy_EAC** : nombre d'enfants de 6 a 11 ans, beneficiaires d'au moins une prestation CAF versable
- **NB_Enfants_12_15_ans_yyyy_EAC** : nombre d'enfants de 12 a 15 ans, beneficiaires d'au moins une prestation CAF versable
- **NB_Enfants_16_17_ans_yyyy_EAC** : nombre d'enfants de 16 a 17 ans, beneficiaires d'au moins une prestation CAF versable
- **NB_Enfants_18_19_ans_yyyy_EAC** : nombre d'enfants de 18 a 19 ans, beneficiaires d'au moins une prestation CAF versable
- **NB_Enfants_20_24_ans_yyyy_EAC** : nombre d'enfants de 20 a 24 ans, beneficiaires d'au moins une prestation CAF versable

[source](http://data.caf.fr/dataset/repartition-par-tranche-d-age-des-enfants-couverts-par-des-prestations-caf)

## Nombre d'enfants couverts par l'allocation d'éducation de l'enfant handicapé *(AEEH)*

- **NB_enfant_AEEH_yyyy** : nombre d'enfants beneficiaires de l'aeeh versable
- **AEEH_0A2_yyyy** : nombre d'enfants de 0 a 2 ans, beneficiaires de l'aeeh versable
- **AEEH_3A5_yyyy** : nombre d'enfants de 3 a 5 ans, beneficiaires de l'aeeh versable
- **AEEH_6A11_yyyy** : nombre d'enfants de 6 a 11 ans, beneficiaires de l'aeeh versable
- **AEEH_12A15_yyyy** : nombre d'enfants de 12 a 15 ans, beneficiaires de l'aeeh versable
- **AEEH_16A17_yyyy** : nombre d'enfants de 16 a 17 ans, beneficiaires de l'aeeh versable
- **AEEH_18A20_yyyy** : nombre d'enfants de 18 a 20 ans, beneficiaires de l'aeeh versable

L’AEEH s’adresse aux familles ayant à leur charge des enfants handicapés. Elle remplace, depuis le 1er janvier 2006, l’allocation d’éducation spéciale (AES) créée en 1975. Pour en bénéficier, l’enfant doit remplir plusieurs conditions:

- être âgé de moins de 20 ans
- avoir une incapacité permanente d’au moins 80 %. Celle-ci peut aussi être comprise entre 50 % et 80 % si l’enfant fréquente un établissement spécialisé ou si son état exige le recours à un service d’éducation spécialisée ou de soins à domicile
- ne pas résider en internat avec prise en charge intégrale des frais de séjours par l’Assurance maladie, l’État ou l’Aide sociale

C’est la Commission des droits et de l’autonomie des personnes handicapées (CDAPH) qui apprécie l’état de santé de l’enfant et propose l’attribution de l’AEEH, pour une durée comprise entre 1 et 5 ans, sauf aggravation du taux d’incapacité.

[source](http://data.caf.fr/dataset/nombre-d-enfants-couverts-par-l-allocation-d-education-de-l-enfant-handicape-aeeh-par-commune)

## Foyers allocataires percevant le revenu de solidarité active RSA *(RSAC)*  

- **NB_allocataire_RSA_yyyy** : nombre total de foyers allocataires RSA
- **Dont_RSA_jeune_yyyy** : nombre de foyers allocataires RSA jeune
- **RSA_SOCLE_non_Majore_yyyy** : nombre de foyers allocataires rsa socle sans majoration versable
- **RSA_SOCLE_Majore_yyyy** : nombre de foyers allocataires rsa socle avec majoration versable
- **RSA_activite_yyyy** : nombre de foyers allocataires rsa activite versable

Le RSA est une prestation sous conditions de ressources versée mensuellement sur la base des ressources du trimestre précédent. Entré en vigueur le 1er juin 2009 en France métropolitaine et le 1er janvier 2011 dans les départements d’Outre-mer, cette prestation remplace le revenu minimum d'insertion (RMI) et l'allocation de parent isolé (API) pour les personnes privées d'emploi. Il apporte une incitation financière aux personnes sans ressource qui reprennent un emploi (le RSA garantit à quelqu'un qui reprend un travail que ses revenus augmentent). Enfin il complète les ressources des personnes dont l'activité professionnelle ne leur apporte que des revenus limités.

Le RSA est versé sans limitation de durée, tant que les revenus du bénéficiaire sont inférieurs au montant maximal du RSA. Le montant versé peut varier si la situation familiale, professionnelle et les ressources du foyer évoluent. Le RSA est constitué de trois composantes : le "RSA socle", le "RSA socle et activité" et le "RSA activité". Ainsi, le RSA couvre une population large, puisqu’il concerne aussi bien des foyers n’ayant aucune ressource, que des personnes percevant des revenus d’activité proches du Smic. Un foyer allocataire du "RSA socle seul" n’a pas de revenus d’activité (toutefois, en cas de reprise d’activité, le bénéficiaire peut cumuler salaires et allocation pendant trois mois). Les bénéficiaires du "RSA socle et activité" ont de faibles revenus d’activité et l’ensemble de leurs ressources est inférieur au montant forfaitaire. Ceux du "RSA activité seul" ont de faibles revenus d’activité et l’ensemble de leurs ressources est supérieur au montant forfaitaire. Deux types de publics peuvent se combiner aux composantes de RSA :

- les personnes en état de grossesse ou assumant seules la charge d’au moins un enfant bénéficient du "RSA majoré" (on parle alors de "socle majoré" ou "socle et activité majoré" ou "activité majoré")
- les bénéficiaires du RSA ne faisant partie du public "RSA majoré" correspondent au RSA "non majoré". Au sein du public "non majoré" on peut distinguer le public "RSA jeune". Le public RSA jeune concerne les jeunes de moins de 25 ans isolés et sans enfant à charge et versé sous condition d’activité antérieure (deux ans au cours des trois dernières années).

[source](http://data.caf.fr/dataset/foyers-allocataires-percevant-le-revenu-de-solidarite-active-rsa-par-commune)

## Foyers allocataires percevant une prestation enfance et jeunesse (AF, CF, ASF, AEEH et ARS) *(EJC)*

- **ALL_AF_yyyy** : nombre de foyers allocataires avec AF versable
- **ALL_CF_yyyy** : nombre de foyers allocataires avec CF versable
- **ALL_ARS_yyyy** : nombre de foyers allocataires avec ARS versable
- **ALL_ASF_yyyy** : nombre de foyers allocataires avec ASF versable
- **ALL_AEEH_yyyy** : nombre de foyers allocataires avec AEEH versable

Créées dans leur forme actuelle en 1946, les allocations familiales (AF) sont versées aux familles d’au moins 2 enfants en Métropole et dès le premier enfant dans les Dom. Elles sont destinées aux enfants de moins de 20 ans à charge.

Le complément familial (CF) est attribué en Métropole, aux familles d’au moins 3 enfants, âgés de 3 ans à moins de 21 ans. Dans les Dom, pour y avoir droit, la famille doit assumer la charge d’au moins un enfant de plus de 3 ans et de moins de 5 ans et ne pas avoir d’enfant de 0 à 3 ans. En Métropole comme dans les Dom, le Cf est soumis à condition de ressources. Il est non cumulable avec l’allocation de base de la Paje.

L’allocation de soutien familial (ASF) est versée sans condition de ressources pour élever un enfant de moins de 20 ans privé de l’aide de l’un ou de ses deux parents, ou pour aider les personnes qui ont la charge de l’éduquer. Sous une même appellation, elle concerne tout à la fois des enfants orphelins et ceux pour lesquels une pension alimentaire n’est pas versé.

L’allocation d’éducation de l’enfant handicapé (AEEH) s’adresse aux familles ayant à leur charge des enfants handicapés. Pour en bénéficier, l’enfant doit remplir plusieurs conditions :

- être âgé de moins de 20 ans
- avoir une incapacité permanente d’au moins 80 %. Celle-ci peut aussi être comprise entre 50 % et 80 % si l’enfant fréquente un établissement spécialisé ou si son état exige le recours à un service d’éducation spécialisée ou de soins à domicile 
- ne pas résider en internat avec prise en charge intégrale des frais de séjours par l’Assurance maladie, l’État ou l’Aide sociale

C’est la Commission des droits et de l’autonomie des personnes handicapées (Cdaph) qui apprécie l’état de santé de l’enfant et propose l’attribution de l’AEEH, pour une durée comprise entre 1 et 5 ans, sauf aggravation du taux d’incapacité.

L’allocation de rentrée scolaire (ARS) aide les familles à assumer le coût de la rentrée scolaire de leurs enfants de 6 à 18 ans.

[source](http://data.caf.fr/dataset/foyers-allocataires-percevant-une-prestation-enfance-et-jeunesse-af-cf-asf-aeeh-et-ars-par-comm)

## Population couverte par une aide personnelle au logement en décembre *(LPPC)*

- **NB_Pers_Couv_Al_yyyy** : nombre de personnes couvertes par une aide au logement versable
- **Pers_Couv_Al_ALF_yyyy** : nombre de personnes couvertes par ALF versable
- **Pers_Couv_Al_ALS_yyyy** : nombre de personnes couvertes par ALS versable
- **Pers_Couv_Al_APL_yyyy** : nombre de personnes couvertes par APL versable


AFL : Allocation de Logement Familiale
ALS : Allocation de Logement Social
APL : Aide Personnalisée au Logement

Ces trois aides ne sont pas cumulables. L’ordre de priorité d’attribution est le suivant : APL, ALF, ALS.

[source](http://data.caf.fr/dataset/population-des-foyers-allocatair)

## Nombre d'enfants couverts par l'allocation de rentrée scolaire (ARS) *(ARS)*

- **NB_enfant_ARS_yyyy** : nombre d'enfants ouvrant droit a l'ARS versable
- **ARS_5A10_yyyy** : nombre d'enfants de 5 a 10 ans, ouvrant droit a l'ARS versable
- **ARS_11A14_yyyy** : nombre d'enfants de 11 a 14 ans, ouvrant droit a l'ARS versable
- **ARS_15A17_yyyy** : nombre d'enfants de 15 a 17 ans, ouvrant droit a l'ARS versable

L'ARS est une prestation versée sous conditions de ressources en une seule fois (généralement en septembre) et les enfants ouvrant droit à l'ARS doivent être scolarisés et agés de 6 à 18 ans.

[source](http://data.caf.fr/dataset/nombre-denfants-couverts-par-l-allocation-de-rentree-scolaire-ars-par-commune)
