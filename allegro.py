# -*- coding: utf8 -*-
from suds.client import Client
import time
import json


url = 'https://webapi.allegro.pl/service.php?wsdl'

client = Client(url)

#Wpisz swoje webapi
webAPI = 'a36da5f5'
countryId = 1
chunk_size = 500
filtr_query=client.factory.create('ArrayOfFilteroptionstype')

tablica = {'category':'165',
           'condition':'',
           }
rangeUp = len(tablica)-1

for i in range(0,rangeUp):
    filtr = client.factory.create('FilterOptionsType')
    filtr.filterId = tablica.keys()[i]
    filtrAOS = client.factory.create('ArrayOfString')
    filtrAOS.item = tablica.values()[i]
    filtr.filterValueId = filtrAOS
    filtr_query.item.append(filtr)


wynik = client.service.doGetItemsList(webAPI, countryId, filtr_query, resultScope = 3,resultSize = chunk_size)

print type(wynik.itemsList.item[226].item)

# results = []
# for x in xrange(1,chunk_size):
#   item = wynik.itemsList.item[x]
#   print x
#   results.append({
#         "itemTitle": item.itemTitle,
#         "itemId": item.itemId,
#         "conditionInfo": item.conditionInfo,
#         "priceValue": item.priceInfo[0][0].priceValue,
#         "pictureUrls": map(lambda x: x.photoUrl, item.photosInfo.item),
#         "parametersStan": item.parametersInfo.item[0].parameterValue.item[0],
#         "userLogin": item.sellerInfo.userLogin,
#         "userId": item.sellerInfo.userId
#       })

# print json.dumps(results[0])


# print "Otrzymano %d wynikow." % wynik.itemsCount , "Sukces! %s " % time.strftime("%A, %H:%M:%S")


