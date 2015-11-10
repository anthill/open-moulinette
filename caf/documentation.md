# Documentation

This script aggregates more than 80 indicators (on 6 years) available for each city in one single clean file.

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

Attention :

Certaines villes ont fusionné avec d'autres :

*Fort-Mardyck* (Codes_Insee == 59248) est maintenant rattaché à *Dunkerque* (59183) et est donc absent de notre référenciel.

A partir de 2014, le champ géographique d’observation du jeu de données correspond à la commune de résidence du foyer allocataire telle qu’elle est enregistrée dans le fichier statistique des allocataires extrait début d’année N+1 et ce quelle que soit la Caf de gestion.Les deux premières lignes du fichier recouvrent les allocataires résidents à l'étranger (code 99999) et les allocataires dont la commune de résidence est inconnue (code XXXXX). En 2012 et 2013 les résidents à l'étranger n'ont pas été comptabilisés. 

En 2009, 2010 et 2011, la première ligne (code 99999) recouvre, en plus des résidents à l'étranger, tous les allocataires vivant sur une commune en dehors du territoire de leur caf de gestion.

## Vocubulaire de la CAF :

**Le foyer allocataire** est l’entité administrative à laquelle les Caf versent au moins une prestation. Il est composé de l’allocataire (personne qui perçoit au moins une prestation au regard de sa situation familiale et/ou monétaire), de son conjoint/concubin/pacsé éventuel, des enfants à charge et autres personnes à charge au sens de la réglementation en vigueur. Un foyer allocataire peut donc comporter une ou plusieurs personnes.

**Le droit versable** signifie que le foyer allocataire remplit toutes les conditions pour être effectivement payé au titre du mois d’observation. En particulier ne sont pas inclus dans ce périmètre les bénéficiaires qui n’ont pas fourni l’intégralité de leurs pièces justificatives, ou ceux dont le montant de la prestation est inférieur au seuil de versement.

## Nombre d'allocataires total :

- **NB_Allocataires_yyyy** : nombre total de foyers allocataires de la branche famille.

*yyyy : de 2009 à 2014 inclus*

## Indicateur sur la part des prestations dans les ressources des foyers allocataires :

[source](http://data.caf.fr/dataset/indicateur-sur-la-part-des-prestations-dans-les-ressources-des-foyers-allocataires-par-commune)

## **BC** Foyers allocataires à "bas revenus" 

 - **ALL_bas_revenu_yyyy** : nombre total de foyers allocataires bas revenus.
 - **Pers_bas_revenu_yyyy** : nombre total de personnes couvertes par les foyers bas revenus.

[source](http://data.caf.fr/dataset/beneficiaire-bas-revenus)

## **NCT** Population couverte par au moins une prestation

- **NB_Pers_par_Foyer_Alloc_yyyy_NCT** : nombre de personnes couvertes par la branche famille
- **NB_Enfants_yyyy_NCT** : nombre d'enfants couverts

Pour  2009, il y a une plus grande granularité pour le nombre d'enfants :
- **NB_Enfants_0_2_ans_NCT_2009** : Nombre d'enfants de 0 à 2 ans couverts
- **NB_Enfants_3_5_ans_NCT_2009** : Nombre d'enfants de 3 à 5 ans couverts


[source](http://data.caf.fr/dataset/population-des-foyers-allocataires-par-commune)

## **CF** Répartition des foyers allocataires selon le type de famille






