#instalación de librerias
# la libreria requests nos sirve para mandar solicitudes a la página web
# la librería BeautifulSoup nos sirve
# la libreria lxml sirve para hacer el parse de la web

# Cargamos las librerías que vamos a utilizar
import json
import requests
from bs4 import BeautifulSoup
import Geolocalizacion

#variables
l_sCCAA = '13'
l_sPuntoReferencia = Geolocalizacion.PosicionGeografica("Calle de Atocha 125, Madrid")

#https://geoportalgasolineras.es/#/Inicio
l_sURL = f'https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/FiltroCCAA/{l_sCCAA}'
l_sTXT = f'DatosEstacionesServicio_{l_sCCAA}.csv'

#hacemos petición a la página
result = requests.get(l_sURL)

#obtenemos el contenido de la web en formato texto.
content = result.text

#utilizamos Beautifulsoup para estructurar el contenido recuperado (texto) y así poder interacturar-encontrar los elementos.
# como parámetros del función indicamos el contenido y el tipo de parser que utilizamos
soup = BeautifulSoup(content, 'lxml')

#imprimimos para ver qué es lo que tenemos hasta ahora.
#print(soup.prettify())

#prioridades para buscar elmentos: ID, class name, Tag name, CSS Selector, Xpath
contenido= soup.find('p').get_text()
contenido.replace('},', '}, \n')
# print(contenido)
data=json.loads(contenido)


# #exportar los datos a un archivo txt
with open(l_sTXT, 'w', encoding='utf-8') as file:
 file.write("Municipio|CP|Dirección|Gasolina95|Gasoleo|Distancia"+'\n')
 for gasolinera in data['ListaEESSPrecio']:
  distancia = Geolocalizacion.haversine(l_sPuntoReferencia[0], l_sPuntoReferencia[1], float((gasolinera['Longitud (WGS84)']).replace(',', '.')), float((gasolinera['Latitud']).replace(',', '.')))
  estacionServicio = gasolinera['Municipio']+'|'+gasolinera['C.P.']+'|'+gasolinera['Dirección']+'|'+gasolinera['Precio Gasolina 95 E5']+'|'+gasolinera['Precio Gasoleo A'] +'|'+ str(distancia) +'\n'
  # print(estacion)
  file.write(estacionServicio)
