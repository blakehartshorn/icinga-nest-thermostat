#!/usr/bin/python3
import requests

def weather(config,unit):

    station = config['wgov_station']

    r = requests.get(f'https://api.weather.gov/stations/{station}/observations/latest')

    w = r.json()

    humidity = w['properties']['relativeHumidity']['value']
    temperature = w['properties']['temperature']['value']

    if unit == 'F':
        temperature = (temperature * 1.8) + 32
    
    return(f'outside_humidity={humidity:.2f}%;;;0;100 outside_temp={temperature:.2f} ')
