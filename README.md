## Open-Moulinette

Open-data is often not in an appropriate format. When it is the case, hackers like ourselves need some efforts to clean it. Each folder contains:

- a README explaining waht dataset is being cleaned, what are the outputs etc
- a makefile to download the original data
- scripts to run the *moulinette*

Don't hesitate to contribute.

## Cleaned datasets

- **insee-iris** converts all the Insee IRIS shapefiles encoded in Lambert 93 into a single geojson file encoded with longitude/latitude.

- **insee** will download all the datasets of the INSEE at the iris level and cleanly aggregate them in on single csv file.

- **weather_forecast** to have four days of weather prediction (only for Switzerland, France and Belgium) asked for a city.

- **caf** will download all the datasets from caf open-data at the city level and cleanly aggregate them in on single csv file. 

## Dashboard

We made a workshop to show how we can visualize and query these datasets with elastic search and kibana.
