# -*- coding: utf-8 -*-


import urllib2
import json
import datetime
import pandas as pd
from nominatim import Nominatim
import argparse
import sys

################################################
#             ARGUMENTS PARSER
################################################

parser = argparse.ArgumentParser(description='To have weather forecast (4 days) on a city',
                                 epilog="Example of use : get_meteo.py -l 'Bordeaux 33000' -f 'csv' -p '../../meteo_bordeaux.csv'")
parser.add_argument('-l','--location', 
                    help='location of the weather. Example "Bordeaux 33000"',
                    type=str, required=True)
parser.add_argument('-f','--format', 
                    help="type of output you want. 'json' and 'csv' are alowed (default: 'csv')", 
                    type=str, default="csv")
parser.add_argument('-p', '--path', default="./",
                    help="You can indicate the path. Example : '../../my_meteo.json').(default: will be the localisation in the directory)",
                    type=str)
                    

args = vars(parser.parse_args())

output_type = ""

if args['format'] == "csv":
    output_type = "csv"
elif args['format'] == "json":
    output_type = "json"
else:
    print "Error on format. Only 'json' and 'csv' are alowed. Program stop"
    sys.exit()
    
output_path = ""

if args['path'] == "./":
    output_path = args['path'] + args['location'].lower().replace(" ", "_") + "." + args['format']
else:
    output_path = args['path']

################################################
#                   WEATHER
################################################

my_city = Nominatim()
city_detail = my_city.query(args['location'])[0] ## Take the best city match name

print "Weather forecast for : " + city_detail['display_name']

my_url = "http://www.prevision-meteo.ch/services/json/lat=" + city_detail['lat'] + "lng=" + city_detail['lon']

obj_string = urllib2.urlopen(my_url).read()
obj_json = json.loads(obj_string)

date =  obj_json['current_condition']['date']
year = int(obj_json['current_condition']['date'][6:])
month = int(obj_json['current_condition']['date'][3:5])
day = int(obj_json['current_condition']['date'][0:2])


time = obj_json['current_condition']['hour']
hour = int(obj_json['current_condition']['hour'][0:2])

datetime_start = datetime.datetime(year, month, day, hour)

calendar = {"fcst_day_0" : datetime_start,
            "fcst_day_1" : datetime_start + datetime.timedelta(days=1),
            "fcst_day_2" : datetime_start + datetime.timedelta(days=2),
            "fcst_day_3" : datetime_start + datetime.timedelta(days=3),
            "fcst_day_4" : datetime_start + datetime.timedelta(days=4)}

hour_list = []
for i in range(0, 24):
    hour_list.append(str(i) + "H00")
    
forcast_day = ["fcst_day_0",
               "fcst_day_1",
               "fcst_day_2",
               "fcst_day_3",
               "fcst_day_4"]

obj_df = []
# DOC
# http://www.prevision-meteo.ch/uploads/pdf/recuperation-donnees-meteo.pdf

for days in forcast_day:
    for hours in hour_list:
        try:
            obj_df.append({'date_day' : str(calendar.get(days).date()),
                           'hour' : str(hours.split("H")[0].zfill(2)),
                           'condition' : obj_json[days]['hourly_data'][hours]['CONDITION'],                  # Conditions (texte) *
                           'temperature' : obj_json[days]['hourly_data'][hours]['TMP2m'],                    # Température [°C] 
                           'dew_point' : obj_json[days]['hourly_data'][hours]['DPT2m'],                      # Point de rosée [°C] 
                           'eolien_cooling' : obj_json[days]['hourly_data'][hours]['WNDCHILL2m'],            # Refroidissement éolien [°C]  
                           'relative_humidity' : obj_json[days]['hourly_data'][hours]['RH2m'],               # Humidité relative [%]
                           'atmospheric_pressure' : obj_json[days]['hourly_data'][hours]['PRMSL'],           # Pression atmosphérique [Hpa]
                           'precipitation' : obj_json[days]['hourly_data'][hours]['APCPsfc'],                # Précipitations [mm]
                           'speed_wind' : obj_json[days]['hourly_data'][hours]['WNDSPD10m'],                 # Vitesse du vent à 10m [Km/h]
                           'squall' : obj_json[days]['hourly_data'][hours]['WNDGUST10m'],                    # Rafales à 10m [Km/h] 
                           'wind_direction_degree' : obj_json[days]['hourly_data'][hours]['WNDDIR10m'],      # Direction du vent [°] 
                           'wind_direction_cardinal' : obj_json[days]['hourly_data'][hours]['WNDDIRCARD10'], # Direction du vent
                           'precipitation_type' : obj_json[days]['hourly_data'][hours]['ISSNOW'],            # Type de précipitation [0 = pluie,1 = neige]
                           'high_altitude_cloud' : obj_json[days]['hourly_data'][hours]['HCDC'],             # Nuages haute altitude
                           'medium_altitude_cloud' : obj_json[days]['hourly_data'][hours]['MCDC'],           # Nuages moyenne altitude
                           'low_altitude_cloud' : obj_json[days]['hourly_data'][hours]['LCDC'],              # Nuages basse altitude
                           'isotherme_0_degre' : obj_json[days]['hourly_data'][hours]['HGT0C'],              # Isotherme zéro degré [°C] 
                           'k_index' : obj_json[days]['hourly_data'][hours]['KINDEX'],                       # K-index (potentiel orageux)
                           'cape_180_0' : float(obj_json[days]['hourly_data'][hours]['CAPE180_0']),          # CAPE 180-0
                           'cin_180_0' : obj_json[days]['hourly_data'][hours]['CIN180_0']                    # CIN 180-0
            })
        except Exception, e:
	    print "Error : " + str(e) 

df = pd.DataFrame(obj_df)
df['date'] = pd.to_datetime(df.date_day + " " + df.hour + ":"+"00",
                            format='%Y-%m-%d %H:%M')

df['year'] = df.date.dt.year
df['month'] = df.date.dt.month
df['day'] = df.date.dt.day
df['dayofweek'] = df.date.dt.dayofweek
df['hours'] = df.date.dt.hour

df['condition'] = df['condition'].str.encode('utf-8')

df = df[['date', 'date_day', 'year', 'month', 'day', 'dayofweek','hour',
           'condition', 'temperature', 'dew_point', 'eolien_cooling',
           'relative_humidity', 'atmospheric_pressure', 'precipitation', 
           'speed_wind', 'squall', 'wind_direction_degree', 'wind_direction_cardinal',
           'precipitation_type', 'high_altitude_cloud', 'medium_altitude_cloud',
           'low_altitude_cloud', 'isotherme_0_degre', 'k_index', 'cape_180_0',
           'cin_180_0']]


if output_type == "csv":
    df.to_csv(output_path, index=False)
elif output_type == "json":
    df.to_json(output_path, orient="records")