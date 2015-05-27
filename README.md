## Open-Moulinette

Open-data is often not in an appropriate format. When it is the case, hackers like ourselves need some efforts to clean it. Each folder contains:

- a README explaining waht dataset is being cleaned, what are the outputs etc
- a makefile to download the original data
- scripts to run the *moulinette*

Don't hesitate to contribute.

## Cleaned datasets

- **insee-iris** is a script to convert all the Insee IRIS shapefiles encoded in Lambert 93 into a single geojson file encoded with Longitude/latitudes.
- **insee** is script to dowload and concatenate all the features from many Insee's files in one clean csv. 

