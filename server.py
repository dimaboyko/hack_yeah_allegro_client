from flask import Flask, request, jsonify, redirect, Response
app = Flask(__name__)

from suds.client import Client
import time
import json

url = 'https://webapi.allegro.pl/service.php?wsdl'

client = Client(url)

#Wpisz swoje webapi
webAPI = 'a36da5f5'
countryId = 1
chunk_size = 100

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


@app.route('/status')
def status():
    return 'Up !'


@app.route('/get_items')
def get_status():
    wynik = client.service.doGetItemsList(webAPI, countryId, filtr_query, resultScope = 3,resultSize = chunk_size)
    results = []
    for x in xrange(1,chunk_size):
      item = wynik.itemsList.item[x]
      results.append({
            # "itemTitle": item.itemTitle,
            "itemId": item.itemId,
            # "conditionInfo": item.conditionInfo,
            # "priceValue": item.priceInfo[0][0].priceValue,
            # # "pictureUrls": ["1","2"],# item.photosInfo.item[-1].photoUrl, # map !!!
            # "pictureUrls": map(lambda x: x.photoUrl, item.photosInfo.item),# item.photosInfo.item[-1].photoUrl, # map !!!
            # "parametersStan": item.parametersInfo.item[0].parameterValue.item[0],
            # "userLogin": item.sellerInfo.userLogin,
            "userId": item.sellerInfo.userId
          })
    return json.dumps(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
