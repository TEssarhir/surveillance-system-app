""" how to ask in python a web service """

# see https://openweathermap.org/api
# what is possible : https://openweathermap.org/price#weather

import requests


# some simple manipulations

# 1 get info on current weather
# test code : print("Teste1",requests.get("https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=a2cabf37326f4cf77d2948c17c62705a").text)


## some parameters
id = "6c7536caec8cea574d9b049fde683a35" # Api id Chevrier Thanks to use your own id ... :-)
idSEG="a2cabf37326f4cf77d2948c17c62705a"
lat = "48.650002" # latitude
lon="6.18333" # longitude



# websevice parameters
wslon="lon="+lon
wslat="lat="+lat
wsappid="appid="+id

# first request
#--------------------------------
requestTxt="https://api.openweathermap.org/data/2.5/weather?"+wslat+"&"+wslon+"&"+wsappid
print("essai2", requestTxt)
answer=requests.get(requestTxt)
print(answer.text)


# other example



# solution to exo 1
requestSol=requestTxt+"&lang=fr"+"&mode=xml"
answer=requests.get(requestSol)
print("sol",answer.text)

