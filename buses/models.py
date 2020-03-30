from django.db import models
from django.utils import timezone
import json
import urllib3
import requests
import xmltodict
from django.http import JsonResponse
import datetime

# Create your models here.

victor_lat = "41.980262"
victor_long = "-87.668452"
api_key = "AmNgqJNq6l9j6cdJnGg1_JlKUQyZUYX7WMYTjE9MufgRbMri_3ecun7O66NmuaKk"
buses_url = "ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22"
prefix_distance_url = "https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?origins="

def get_buses():
    print("Getting buses...")
    http = urllib3.PoolManager()
    response = http.request('GET',buses_url)
    data = xmltodict.parse(response.data)
    essen={}
    buseslist=[]
    testlist=[]

    for x in range(0,len(data['buses']['bus'])):
        if data['buses']['bus'][x]['pd']=="Northbound":

            print(data['buses']['bus'][x]['id'],data['buses']['bus'][x]['pd'])


            ## to save lat and long for distance matrix
            lat = data['buses']['bus'][x]['lat']
            long = data['buses']['bus'][x]['lon']
            distance_url = prefix_distance_url + victor_lat + "," + victor_long +"&destinations="+str(lat)+","+str(long)+"&travelMode=driving&timeUnit=second&key="+api_key

            json_data = requests.get(distance_url)
            json_file = json_data.json()

            dist = json_file['resourceSets'][0]['resources'][0]['results'][0]['travelDistance']

            ### Place in a dictionary
            essen[data["buses"]["bus"][x]["id"]]=[{"direction":data["buses"]["bus"][x]["pd"],
            "latitude":data["buses"]["bus"][x]["lat"],
            "longitude":data["buses"]["bus"][x]["lon"],
            "distance":dist}]

            ### Place in a list
            buseslist.append({"idno":data['buses']['bus'][x]['id'],"direction":data['buses']['bus'][x]['pd'],
            "latitude":data['buses']['bus'][x]['lat'],"longitude":data['buses']['bus'][x]['lon'],
            "distance":dist})


        else:
            continue
    return buseslist



