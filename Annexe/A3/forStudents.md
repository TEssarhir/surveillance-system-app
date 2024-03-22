# Documentation for the examples
*V Chevrier Nov 22*

## What to know
In python, use of **requests** package that enables call to web service (as html addresses do) -->client side
and use of **flask** package for web services ---> server side


## Examples 

### File client1.py
Simple call to a distant web service : ask for weather in Nancy
see https://openweathermap.org/current#geo for more information



* Questions

	* Explain why we need to write ***print(answer.text)***
	* what means the string output format ?
* Exercises:

        1. Change response format to XML, the language as French
        2. learn how to ask for weather forecast (with free version)
        3. What happens if you type the following as address in your favorite web browser ?
            https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=a2cabf37326f4cf77d2948c17c62705a
        4. Explain how to pass parameters to a web service

**API reference**
[https://openweathermap.org/api](https://openweathermap.org/price#weather)
have a look on it to learn what is **possible** and how

1. all requests need an id
2. there is a limit on the number of requests each day

## Examples server and client : learn how to define services (and how to call them from python client)

### A) serviceT1 (clientT1)
***Lessons learned*** how to define a server and two services
definition of 2 services on the server
- one at root basic service (just returns a string)
- one called *bonjour* that takes a ***nom*** as param and say bonjour to nom if exists



### B) serviceT2 / serviceT2json (and cleinetT2/clientT2json)
***Lessons learned*** use of *external* code in services and the use of JSON format


T2 Simple service to show that returned value can change over time
The returned values are as **text** format.

T2j
Simple service to show that returned value can change over time.
The returned values are as **json** format.

In client
    - How is managed the json format?
    - Can you see an advantage to use it?

### B) serviceT3 (and clientT3)

***Lessons learned*** use of arguments in services

Services :
- service0
    Shows how to build a simple service that
    - gets the parameters and their values
    - returns them as a list of couple ou value

    The returned values are as text format.

- exemple3
    How to get  the value of a parameter ***valeur**

        Note that the parameter are in Json format but ....
        What is the type of the values we get ??

 - exemple 4 et exemple5 shows how to get typed values if params are in JSON

Exercices:  code the client for the services not treated in example file.



### serviceT4.py
Use of global variables
Exercice: code the client


##More interesting
### The shutdown problem (ServerShutDown.py)
When the server is running it uses a givent port on the machine and forbids another server to be run. If python ends improperly, the port can be "blocked".

According to your programmig environment, it can be very difficult to shutdown/kill the server.

The file ***servershutdown.py*** shows how to integrate a shutdown service in the server.

### Non local server

serverNonLocal.py illustates how to have a non local server

### Misc

app1 directory : 
# See how toreturn results as html/use html to ask for services (just core ideas )
