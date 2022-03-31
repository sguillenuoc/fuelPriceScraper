## Práctica 1: Web scraping
## Descripción

Esta práctica utiliza técnicas de web scraping para extraer los precios de diferentes tipos de combustible de la página web del (https://geoportalgasolineras.es/#/Inicio) del Ministerio para la transición ecológica y el reto demográfico.

## Miembros del equipo

La práctica ha sido realizada por **Carlos Pérez Cebrián** y **Sandra Guillén Resina**.

## Ficheros del repositorio

* **README.md**: archivo con la información del repositirio, así como las instruciones para su ejecución.
* **PRA1.pdf** : archivo pdf con las respuestas de la práctica.
* **fuelPriceScraper.py**: contiene el script para la extración de información.
* **fuelPriceScraper.csv**: contiene la tabla con la información extraida.

## Instrucciones para la ejecucion del script

Para ejecutar el script es necesario instalar la siguientes bibliotecas:

```
pip install pandas
pip install selenium
pip install requests
pip install lxml
pip install beautifulsoup4
```

El script se debe ejecutar de la siguiente manera:

```
python fuelPriceScraper.py 
```


Actualmente extrae el precio actual de los siguientes combustibles:

- Gasolina 95 E5
- Gasolina 95 E10
- Gasolina 95 E5 Premium
- Gasolina 98 E5
- Gasolina 98 E10
- Gasóleo A habitual
- Gasóleo Premium
- Gasóleo B
- Gasóleo C
- Bioetanol
- Biodiésel
- Gases licuados del pretróleo
- Gas natural comprimido
- Gas natural licuado
- Hidrógeno
