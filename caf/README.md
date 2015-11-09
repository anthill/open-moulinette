## Caf


This script dowload and concatenate all the features from [CAF open-data](http://data.caf.fr/site/) files in one clean csv (more than 550 actually) at city level.

For a better reuse, we had geo-shape (Polygon of all city).

Documentation are coming...

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




