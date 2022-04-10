## Práctica 1: Web scraping
## Descripción

Esta práctica utiliza técnicas de web scraping para extraer los precios de diferentes tipos de combustible de la página web del (https://www.dieselogasolina.com/).

## Miembros del equipo

La práctica ha sido realizada por **Carlos Pérez Cebrián** y **Sandra Guillén Resina**.

## Ficheros del repositorio

* **README.md**: archivo con la información del repositorio, así como las instrucciones para su ejecución.
* **requirements.txt** : archivo con la información de los paquetes Python necesarios para ejecutar el código.
* **__init__.py**: archivo que contiene el código que ejecuta el web scraping.
* **fuelWebScraping.py**: archivo que contiene la funcion scrapfuel.
* **robots.py** : archivo que contiene la función para examinar las restricciones de la página. 
* **M2.851_sguillen1_cperezceb_PRA1_WebScraping.pdf** : archivo pdf con las respuestas de la práctica.
* **StationData.csv** : archivo csv con la información extraída.

## Instrucciones para la ejecución del script

Para ejecutar el script es necesario instalar las siguientes bibliotecas:

```
selenium      #Interactuar con la web
time          #Establecer tiempos de espera 
os            #Funcionalidad con el sistema (path actual)
scrapfuel     #Fichero con las funcionalidades de webscraping, localización y zenodo
requests      #Interactuar con el api de zenodo
random        #Utilizado para modular las solicitudes en la obtención de coordenadas geografica.
geopy         #Cliente que da acceso a varios servicios geocodificación, como Nominatim que es el servicio utilizado.

```

Para instalar las bibliotecas necesarias del script es necesario ejecutar el siguiente comando: 

```
python get-pip.py install -r requirements.txt
```

El script se debe ejecutar de la siguiente manera:

```
python _init_.py 
```

A continuación debe introducir la provincia, localidad y tipo de combustible que se desee. El script extraerá los datos y los guardara en un archivo csv con la información.
