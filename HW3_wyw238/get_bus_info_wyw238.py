#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 01:51:26 2018

@author: Wei-Yun Wang
"""

from __future__ import print_function
import sys
import json

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 4:
    print("Invalid number of arguments. Run as: python show_bus_location.py <MTA_KEY> <BUS_LINE> <BUS_LINE.csv>")
    sys.exit()

key = str(sys.argv[1])
bus_line = str(sys.argv[2])
output = open(sys.argv[3], 'w')

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

###############################
#with open('local_busdata.json') as data_file:
#    busdata = json.load(data_file)
#output = open('B57.csv', 'w')
###############################

bus_url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key='\
        + key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_line
        
busdata = get_jsonparsed_data(bus_url)

output.write("Latitude,Longitude,Stop Name,Stop Status\n")
for i in range(len(
        busdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]\
        ['VehicleActivity'])):
    line = ''
    line += str(busdata['Siri']['ServiceDelivery']\
      ['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]\
      ['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    line += ',' + str(busdata['Siri']['ServiceDelivery']\
      ['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]\
      ['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    if busdata['Siri']['ServiceDelivery']\
      ['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]\
      ['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'] == None:
          line += ',' + 'N/A'
    else:
        line += ',' + busdata['Siri']['ServiceDelivery']\
      ['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]\
      ['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    if busdata['Siri']['ServiceDelivery']\
      ['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]\
      ['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']\
      ['Distances']['PresentableDistance'] == None:
          line += ',' + 'N/A\n'
    else:
        line += ',' + busdata['Siri']['ServiceDelivery']\
      ['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]\
      ['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']\
      ['Distances']['PresentableDistance'] + '\n'
    output.write(line)
    
    
    
output.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    