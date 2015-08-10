## Weather forecast

This script give you the weather forecast on a city (4 days forecast) using prevision-meteo.ch. Only for Switzerland, France and Belgium.

## Dependency

You just have to 

```
pip install -r requirements.txt
```

## Usage

There are some arguments:

- ```--location``` or ```-l``` : City where you want the weather [required]
- ```--format``` or ```-f```: JSON or CSV (default: csv)
- ```--path``` or ```-p```: output path (default: current directory)

Try to be explicit for the location, you can add Postal code or country.

Example :

```python get_weather.py -l "bordeaux 33000" -f "json" -p "../data/my_weather.csv"```

or 

```python get_weather.py -l "bordeaux 33000"```

will give you bordeaux_33000.csv.

## Property 

- date : 2015-08-12 09:00:00
- date_day : 2015-08-12
- year : 2015
- month : 8
- day : 12
- dayofweek : 2
- hour : 09
- condition : Eclaircies
- temperature : 22.5
- dew_point : 18.2
- eolien_cooling :  22.5
- relative_humidity : 77
- atmospheric_pressure : 1013.8
- precipitation : 0
- speed_wind : 15
- squall: 24
- wind_direction_degree : 132
- wind_direction_cardinal : SE
- precipitation_type : 0
- high_altitude_cloud : 0.00
- medium_altitude_cloud :  19.00
- low_altitude_cloud : 14.00
- isotherme_0_degre : 4100
- k_index : 32
- cape_180_0 : 770
- cin_180_0 : -196




