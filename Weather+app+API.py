##Aplicativo de previsão do tempo usando API

import requests
import json
accuweatherAPIKey = "jIyUms2HGeT2JgHXAAdQOvsWEypzcGeR"

req = requests.get("http://www.geoplugin.net/json.gp")

if(req.status_code != 200):
  print("Não foi possível obter a localização.")
else:
  location = json.loads(req.text)
  lat = location["geoplugin_latitude"]
  long = location["geoplugin_longitude"]

  locationAPIUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/" \
                   + "search?apikey=" + accuweatherAPIKey + "&q=" + lat + "%2C%20" + long + "&language=pt-br"

  req2 = requests.get(locationAPIUrl)
  if(req2.status_code != 200):
    print("Não foi possível obter o código da localização.")
  else:
    locationResponse = json.loads(req2.text)
    localName = locationResponse["LocalizedName"] + ", " \
                + locationResponse["AdministrativeArea"]["LocalizedName"] + ". " \
                + locationResponse["Country"]["LocalizedName"]
    localCode = locationResponse["Key"]
    print("Local: ", localName)

    currentConditionsAPIUrl = "http://dataservice.accuweather.com/currentconditions/v1/" \
                             + localCode + "?apikey=" + accuweatherAPIKey + "&language=pt-br"

    req3 = requests.get(currentConditionsAPIUrl)
    if (req3.status_code != 200):
      print("Não foi possível obter a condição climática.")
    else:
      currentConditionsResponse = json.loads(req3.text)
      climeText = currentConditionsResponse[0]["WeatherText"]
      temperature = currentConditionsResponse[0]["Temperature"]["Metric"]["Value"]
      print("Condição atual: " + climeText)
      print("Temperatura: " + str(temperature))
