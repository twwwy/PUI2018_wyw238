#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 23:14:59 2018

@author: Wei-Yun Wang
"""
from __future__ import print_function
import sys
import json

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 3:
    print("Invalid number of arguments. Run as: python show_bus_location.py <MTA_KEY> <BUS_LINE>")
    sys.exit()

key = str(sys.argv[1])
bus_line = str(sys.argv[2])

def get_jsonparsed_data(url):
    """
    from http://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urllib.urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


bus_url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key='\
        + key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_line
        
busdata = get_jsonparsed_data(bus_url)

#with open('local_busdata.json') as data_file:
#    busdata = json.load(data_file)


print('Bus Line : ', bus_line)
print('Number of Active Buses : ', len(busdata['Siri']['ServiceDelivery']\
   ['VehicleMonitoringDelivery'][0]['VehicleActivity']))
for i in range(len(
        busdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]\
        ['VehicleActivity'])):
    print('Bus ' + str(i) + ' is at latitude ' + str(busdata['Siri']['ServiceDelivery']\
      ['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]\
      ['MonitoredVehicleJourney']['VehicleLocation']['Latitude']) + ' and longtitude '\
      + str(busdata['Siri']['ServiceDelivery']\
      ['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]\
      ['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))