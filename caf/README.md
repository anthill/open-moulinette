## Caf


This script dowload (90 files) and concatenate all the features from [CAF open-data](http://data.caf.fr/site/) files in one clean csv (more than 80 multiply by 6 years actually) at city level. 

For a better reuse, we add geo spatial and city's features. See [documentation](https://github.com/armgilles/open-moulinette/blob/master/caf/documentation.md) for details

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
```




