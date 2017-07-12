## Description (FR)

Impôts locaux : fichier de recensement des éléments d'imposition à la fiscalité directe locale (REI)

Le fichier de recensement des éléments d’imposition à la fiscalité directe locale (REI) est un fichier agrégé au niveau communal. Il détaille l'ensemble des données de fiscalité directe locale par taxe et par collectivité bénéficiaire (commune, syndicats et assimilés, intercommunalité, département, région). Ces données concernent exclusivement les impositions primitives, c’est-à-dire ne tiennent pas compte des impositions supplémentaires consécutives à des omissions ou insuffisances de l'imposition initiale. Ce fichier contient notamment les informations relatives aux principaux impôts locaux suivants :

- la taxe foncière sur les propriétés non bâties (TFPNB)
- la taxe foncière sur les propriétés bâties (TFPB)
- la taxe d'habitation (TH)
- la cotisation foncière des entreprises (CFE)
- la cotisation sur la valeur ajoutée des entreprises (CVAE)
- la taxe spéciale d'équipement au profit de la région d'Île-de-France et d'établissements publics (TSE)
- la taxe d'enlèvement des ordures ménagères (TEOM)
- les impositions forfaitaires sur les entreprises de réseaux (IFER)
- la taxe sur les surfaces commerciales (TASCOM)
- Il comprend aussi les informations concernant les taxes annexes au profit des chambres d'agriculture, de la caisse d'assurance des accidents agricoles, des chambres de commerce et d'industrie et des chambres des métiers
- La taxe pour la gestion des milieux aquatiques et la prévention des inondations (GEMAPI) - uniquement 2016
- la taxe additionnelle spéciale annuelle instituée au profit de la région Île-de-France
(TASARIF) - uniquement 2016

Il y a plus de 900 variables sur les années 2013, 2014, 2015 et 2016. Une [documentation](https://github.com/anthill/open-moulinette/blob/master/impot_locaux/documentation.md)  est à votre disposition pour mieux comprendre les noms des variables.


[Source data.gouv.fr](https://www.data.gouv.fr/fr/datasets/impots-locaux-fichier-de-recensement-des-elements-dimposition-a-la-fiscalite-directe-locale-rei-3/) et [impot.gouv.fr](https://www.impots.gouv.fr/portail/statistiques/recensement-des-elements-dimposition-la-fiscalite-directe-locale-rei)

The size of the output is 400 Mo. It take about 25 minutes to run. 

## Dependency

- Python
- Pandas
- glob

You can install the dependencies with `pip install pandas glob`.

## Usage

- `make` : to automatically download files and process to the output csv
- `make download` : download all files
- `make process` : process to the concatenation and extract csv

## Format

The generated `impot_output.csv` file will look like this:


```csv
DEP  DIR  COM  REC    Q02      SIREPCI                          Q03 OPTEPCI  \
0   1  0.0    1  NaN  10141  200035210.0         CC Chalaronne Centre     FPZ   
1   1  0.0    2  NaN  10135  240100883.0     CC de la Plaine de l'Ain     FPU   
2   1  0.0    4    R  10135  240100883.0     CC de la Plaine de l'Ain     FPU   
3   1  0.0    5  NaN  10120  240100735.0  CC Porte Ouest de la Dombes     FPU   
4   1  0.0    6  NaN  10124  240100354.0       CC de Belley-Bas Bugey     FPA   

  FORJEPCI LIBDEP       LIBREG IDCOM                 LIBCOM B00_13 B11_13  
0       CC    AIN  RHONE-ALPES  1001  ABERGEMENT CLEMENCIAT   1532  60732  
1       CC    AIN  RHONE-ALPES  1002    ABERGEMENT DE VAREY     90   7545  
2       CC    AIN  RHONE-ALPES  1004      AMBERIEU EN BUGEY   1252  45318  
3       CC    AIN  RHONE-ALPES  1005    AMBERIEUX EN DOMBES   1714  75217  
4       CC    AIN  RHONE-ALPES  1006                AMBLEON    164   6367  
```

## Reuse

```
import pandas as pd
data = pd.read_csv('data/impot_output.csv')
```
