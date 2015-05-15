## Data for IRIS

This script will dowload and concatenate all the features from many Insee's files in one clean csv.

For some files, we add a feature "nb_name_of_feature" witch is an aggregate all feature in file (example : sum all médical fonction).

## Dependency

- Python
- Pandas

## Usage

- `make` : to automatically download files and process to the output csv
- `make download` : download all files
- `make convert` : process to the concatenation and extract csv

## Format

CODGEO;LIBGEO;COM;LIBCOM;REG;DEP;ARR;CV;ZE2010;UU2010;NB_B101
010040101;Les Perouses-Triangle d'Activite;01004;Ambérieu-en-Bugey;82;01;011;0101;8201;01302;0;2;
010040102;Longeray-Gare;01004;Ambérieu-en-Bugey;82;01;011;0101;8201;01302;0;2;
010040201;Centre-St Germain-Vareilles;01004;Ambérieu-en-Bugey;82;01;011;0101;8201;01302;0;0;


## Reuse

import pandas as pd

data = pd.read_csv('data/output.csv', sep=";")



