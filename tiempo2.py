
import json
import requests
import webbrowser
from jinja2 import Template

#Funcion que devuelve la cardinalidad del viento:

def direcc_viento (cadena):
		if cadena >= 337.5 and cadena >=0 or cadena < 22.5:
				return "N"
		if cadena >= 22.5 and cadena <= 67.5:
				return "N.E"
		if cadena >= 67.5 and cadena < 112.5:
				return "E"
		if cadena >= 112.5 and cadena < 157.5:
				return "S.E"
		if cadena >= 157.5 and cadena < 202.5:
				return "S"
		if cadena >= 202.5 and cadena < 247.5:
				return "S.O"
		if cadena >= 247.5 and cadena < 292.5:
				return "O"
		if cadena >= 292.5 and cadena < 337.5:
				return "NO"

#Creamos una lista de ciudades:

nombre_ciudades = {'Almeria','Cadiz','Cordoba','Huelva','Jaen','Malaga','Sevilla'}


f_tiempo = open('weather1.html','w')
temp_min = []
temp_max = []
velocidad_viento = []
direccion = []
capital = []

for ciudad in nombre_ciudades:
	capital.append(ciudad)
	respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather?',params={'q':'%s,spain' %ciudad})
	#print respuesta.url
#Buscamos en el diccionario la ciudad evaluada
	diccionario_json = json.loads(respuesta.text)
#Velocidad viento	
	velocidad_viento.append(int(diccionario_json["wind"]["speed"]*1.61))
	direccion.append(direcc_viento(diccionario_json["wind"]["deg"]))
	print velocidad_viento
	#print direccion
#Temperatura se muestra en grados celcius:	
	temp_min.append(int(diccionario_json["main"]["temp_min"]-273))
	temp_max.append(int(diccionario_json["main"]["temp_max"]-273))
	#print temp_min
print ciudad

f = open('plantilla.html','r')
html= ''

for linea in f:
	html += linea

print html

mi_template = Template(html)
salida = mi_template.render(nombre_ciudades=capital, temperatura_min=temp_min, temperatura_max=temp_max, viento_velocidad=velocidad_viento, viento_direccion= direccion)

f_tiempo.write(salida)
webbrowser.open("weather1.html")	
