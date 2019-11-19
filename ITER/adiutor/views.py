
from django.shortcuts import render
import json
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import requests
from math import *
import math
from collections import Counter,OrderedDict
from django.http import JsonResponse


dir_dict={'North':[],'South':[],'West':[],'East':[],'NE':[],'SE':[],'SW':[],'NW':[]}
map_info={'North':[],'South':[],'West':[],'East':[],'NE':[],'SE':[],'SW':[],'NW':[]}
result=[]
nameindex=[]
loc1={'lat':11.0176,'lng':76.9674}
last=[]
place='coimbatore'

#Enter YOUR_API  in the urls to use the api

def weather(para):
    url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&APPID=YOUR_API&units=metric'.format(para['lat'],para['lng'])
    req=requests.get(url)
    data=req.json()
    temp=data['main']['temp']
    data=data['weather']
    data=data[0]
    return data['description'],temp

def dup(duplicates):
    final=[]
    for i in duplicates:
        if i not in final:
            final.append(i)
    return final

def compass(pointA, pointB):
    if (type(pointA) != tuple) or (type(pointB) != tuple):
        raise TypeError("Only tuples are supported as arguments")

    lat1 = math.radians(pointA[0])
    lat2 = math.radians(pointB[0])

    diffLong = math.radians(pointB[1] - pointA[1])

    x = math.sin(diffLong) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
            * math.cos(lat2) * math.cos(diffLong))

    initial_bearing = math.atan2(x, y)
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360

    return compass_bearing
def distance(loc1,loc2):
    R = 6373.0

    lat1 = radians(11.0176)
    lon1 = radians(76.9674)
    lat2 = radians(loc2['lat'])
    lon2 = radians(loc2['lng'])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance


def direction(index,response,degree):
     if((degree>=350 and degree<=360) or (degree>=0 and degree<=10)):
        dir_dict['North'].append([(distance(loc1,response[index]['geometry']['location']),index)])

     if((degree>=11 and degree<=79)):
        dir_dict['NE'].append([(distance(loc1,response[index]['geometry']['location']),index)])

     if((degree>=80 and degree<=100)):
        dir_dict['East'].append([(distance(loc1,response[index]['geometry']['location']),index)])

     if((degree>=101 and degree<=169)):
        dir_dict['SE'].append([(distance(loc1,response[index]['geometry']['location']),index)])

     if((degree>=170 and degree<=190)):
        dir_dict['South'].append([(distance(loc1,response[index]['geometry']['location']),index)])

     if((degree>=191 and degree<=259)):
        dir_dict['SW'].append([(distance(loc1,response[index]['geometry']['location']),index)])

     if((degree>=260 and degree<=280)):
        dir_dict['West'].append([(distance(loc1,response[index]['geometry']['location']),index)])

     if((degree>=281 and degree<=349)):
        dir_dict['NW'].append([(distance(loc1,response[index]['geometry']['location']),index)])

def set_max():
  if dir_dict['North']!=[]:
    map_info['North'].append(max(dir_dict['North'])[0][1])
  if dir_dict['NE']!=[]:
    map_info['NE'].append(max(dir_dict['NE'])[0][1])
  if dir_dict['NW']!=[]:
    map_info['NW'].append(max(dir_dict['NW'])[0][1])
  if dir_dict['East']!=[]:
    map_info['East'].append(max(dir_dict['East'])[0][1])
  if dir_dict['West']!=[]:
    map_info['West'].append(max(dir_dict['West'])[0][1])
  if dir_dict['South']!=[]:
    map_info['South'].append(max(dir_dict['South'])[0][1])
  if dir_dict['SE']!=[]:
    map_info['SE'].append(max(dir_dict['SE'])[0][1])
  if dir_dict['SW']!=[]:
    map_info['SW'].append(max(dir_dict['SW'])[0][1])






def start(place):
 url_poitoursit='https://maps.googleapis.com/maps/api/place/textsearch/json?query={}+tourist+attraction+point+of+interest&language=en&radius=50000&key=YOUR_API'.format(place)
 url_malls='https://maps.googleapis.com/maps/api/place/textsearch/json?query={}+shopping_malls&radius=50000&language=en&key=YOUR_API'.format(place)
 url_hills='https://maps.googleapis.com/maps/api/place/textsearch/json?query={}+hills&radius=50000&language=en&key=YOUR_API'.format(place)
 url_falls='https://maps.googleapis.com/maps/api/place/textsearch/json?query={}+waterfalls&radius=50000&language=en&key=YOUR_API'.format(place)
 response=requests.get(url_poitoursit).json()
 response1=requests.get(url_malls).json()
 response2=requests.get(url_hills).json()
 response3=requests.get(url_falls).json()
 response=response['results']
 response1=response1['results']
 response2=response2['results']
 response3=response3['results']
 response.extend(response1)
 response.extend(response2)
 response.extend(response3)
 result.extend(response)
 index=[]
 tup1=(loc1['lat']),loc1['lng']
 tup2=[]
 for k in range(len(response)):
  for j in response[k]['types']:
     if j=="place_of_worship":
           index.append(k)

 for q in range(len(index)):
     response.pop(index[q]-q)
 for i in range(len(response)):

  tup2=[response[i]['geometry']['location']['lat'],response[i]['geometry']['location']['lng']]
  direction(i,response,int(compass(tup1,tuple(tup2))))

def main():
    list1=[]

    start(place)
    set_max()

    choice='y'
    if choice=='y' or choice=='Y':
            if dir_dict['North']!=[]:
              str1=result[map_info['North'][0]]['formatted_address']
              list1=str1.split(",")

              if any(i.isdigit() for i in list1[0]):
                 if list1[1]!='Unnamed Road':
                     start(list1[1])
                 else:
                     start(list1[2])
              elif list1[0]!='Unnamed Road':
                  start(list1[0])
              else:
                  start(list1[1])

            if dir_dict['NE']!=[]:

              str1=result[map_info['NE'][0]]['formatted_address']
              list1=str1.split(",")

              if any(i.isdigit() for i in list1[0]):
                 if list1[1]!='Unnamed Road':
                    start(list1[1])
                 else:
                     start(list1[2])
              elif list1[0]!='Unnamed Road':
                 start(list1[0])
              else:
                  start(list1[1])

            if dir_dict['NW']!=[]:
              # ("searching from NW")
              str1=result[map_info['NW'][0]]['formatted_address']
              list1=str1.split(",")
              if any(i.isdigit() for i in list1[0]):
                 if list1[1]!='Unnamed Road':
                     start(list1[1])
                 else:
                     start(list1[2])
              elif list1[0]!='Unnamed Road':
                  start(list1[0])
              else:
                 start(list1[1])
            if dir_dict['East']!=[]:
              str1=result[map_info['East'][0]]['formatted_address']
              list1=str1.split(",")
              if any(i.isdigit() for i in list1[0]):
                 if list1[1]!='Unnamed Road':
                     start(list1[1])
                 else:
                     start(list1[2])
              elif list1[0]!='Unnamed Road':
                 start(list1[0])
              else:
                 start(list1[1])
            if dir_dict['West']!=[]:
              str1=result[map_info['West'][0]]['formatted_address']
              list1=str1.split(",")
              if any(i.isdigit() for i in list1[0]):
                 if list1[1]!='Unnamed Road':
                     start(list1[1])
                 else:
                     start(list1[2])
              elif list1[0]!='Unnamed Road':
                 start(list1[0])
              else:
                 start(list1[1])
            if dir_dict['South']!=[]:
              str1=result[map_info['South'][0]]['formatted_address']
              list1=str1.split(",")
              if any(i.isdigit() for i in list1[0]):
                 if list1[1]!='Unnamed Road':
                     start(list1[1])
                 else:
                     start(list1[2])
              elif list1[0]!='Unnamed Road':
                 start(list1[0])
              else:
                 start(list1[1])
            if dir_dict['SE']!=[]:
              str1=result[map_info['SE'][0]]['formatted_address']
              list1=str1.split(",")
              if any(i.isdigit() for i in list1[0]):
                 if list1[1]!='Unnamed Road':
                     start(list1[1])
                 else:
                     start(list1[2])
              elif list1[0]!='Unnamed Road':
                 start(list1[0])
              else:
                 start(list1[1])
            if dir_dict['SW']!=[]:
              str1=result[map_info['SW'][0]]['formatted_address']
              list1=str1.split(",")
              if any(i.isdigit() for i in list1[0]):
                 if list1[1]!='Unnamed Road':
                     start(list1[1])
                 else:
                     start(list1[2])
              elif list1[0]!='Unnamed Road':
                 start(list1[0])
              else:
                 start(list1[1])

    lname=[]
    for i in range(len(result)):
        nameindex.append((result[i]['name'],i))
        lname.append(result[i]['name'])
    lname=dup(lname)

    for index in  lname:
        for i in nameindex:
            if index==i[0]:
             last.append((i[1],result[i[1]]['name'],result[i[1]]['geometry']['location'],distance(loc1,result[i[1]]['geometry']['location']),weather(result[i[1]]['geometry']['location'])))
             break


def Begin(request):
    return render(request,'index.html')



@csrf_exempt
def handle(request):
   global place
   if request.method=="POST":
       rp=json.loads(request.body.decode('utf-8'))
       url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&APPID=YOUR_API&units=metric'.format(rp['lat'],rp['lon'])
       req=requests.get(url)
       data=req.json()
       data=data['name']
       place=data
       main()
       global last
       return JsonResponse(last,safe=False)
