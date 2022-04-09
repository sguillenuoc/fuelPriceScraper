## Práctica 1: Web scraping
## Descripción

Esta práctica utiliza técnicas de web scraping para extraer los precios de diferentes tipos de combustible de la página web del (https://www.dieselogasolina.com/).

## Miembros del equipo

La práctica ha sido realizada por **Carlos Pérez Cebrián** y **Sandra Guillén Resina**.

## Ficheros del repositorio

* **README.md**: archivo con la información del repositirio, así como las instruciones para su ejecución.
* **requirements.txt** : arcvivo con la información de los paquetes Python necesarios para ejecutar el código.
* **__init__.py**: archibo que contiene el código que ejecuta el web scraping.
* **fuelWebScraping.csv**: archivo que contitne la funcion scrapfuel.
* **M2.851_sguillen1_cperezceb_PRA1_WebScraping.pdf** : archivo pdf con las respuestas de la práctica.

## Instrucciones para la ejecucion del script

Para ejecutar el script es necesario instalar la siguientes bibliotecas:

```
selenium
time
os
scrapfuel
```

Para instalar las bibliotecas necesarias para la ejeccución del script es necesario ejecutar el siguiente comando: 

```
python get-pip.py install -r requirements.txt
```

El script se debe ejecutar de la siguiente manera:

```
python _init_.py 
```

A continuación debe introducir la provincia, localidad y tipo de combustible que se desee y el script extraera los datos y los guardara en un archivo csv con la información.
