## Caf


This script dowload (100 files) and concatenate all the features from [CAF open-data](http://data.caf.fr/site/) files in one clean csv (more than 80 multiply by 7 years actually) at city level. 

For a better reuse, we add geo spatial and city's features.

See [documentation](https://github.com/armgilles/open-moulinette/blob/master/caf/documentation.md) for details

## Edit :

- 29/03/2017 : There are now 2015 files

## Dependency

- Python
- Pandas
- glob
- pyprind


## Getting started

```
Make
```

- Install Dependency
- Download commune's files
- Run script
- Merging process

## Reuse

```
import pandas as pd
data = pd.read_csv('data/caf_data.csv')
data.iloc[5953][0:30] #Bordeaux

Codes_Insee                                                         33063
Code_Postal                                 33000/33100/33200/33300/33800
Commune                                                          BORDEAUX
Departement                                                       GIRONDE
Region                                                          AQUITAINE
Statut                                               Préfecture de région
Altitude_Moyenne                                                        9
Superficie                                                           4970
Population                                                          236.7
geo_shape               {"type": "Polygon", "coordinates": [[[-0.57387...
ID_Geogla                                                            5720
Code_Commune                                                           63
Code_Canton                                                            99
Code_Arrondissement                                                     2
Code_Departement                                                       33
Code_Region                                                            72
lat                                                               44.8572
lon                                                             -0.573697
NB_Allocataires_2009                                                69596
NB_Allocataires_2010                                                69959
NB_Allocataires_2011                                                71208
NB_Allocataires_2012                                                71416
NB_Allocataires_2013                                                73846
NB_Allocataires_2014                                                73622
ALL_AAH_2009                                                         5376
ALL_AAH_2010                                                         5491
ALL_AAH_2011                                                         5722
ALL_AAH_2012                                                         5839
ALL_AAH_2013                                                         5736
ALL_AAH_2014                                                         5566
```




