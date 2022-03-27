# fuelPriceScraper
## Español

Extrae los precios de diferentes tipos de combustible de la página web del (https://geoportalgasolineras.es/#/Inicio) del Ministerio para la transición ecológica y el reto demagráfico.

Para ejecutar el script es necesario instalar la siguientes bibliotecas:
```
pip install pandas
```

El script se debe ejecutar de la siguiente manera:
```
python fuelPriceScraper.py --startDate 01/01/2020 --endDate 27/03/2022
```

Donde **startDate** es la fecha de inicio y **endDate** es la fecha de fin del intervalo de tiempo que se deseea extraer. Los registros se almacenan en un archivo de tipo CSV.

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


## English

Extract prices of different types of fuels from the website (https://geoportalgasolineras.es/#/Inicio) of the Ministerio para la transición ecológica y el reto demagráfico.

To run is necessary install the following libraries:
```
pip install pandas

```

To run the script:
```
python fuelPriceScraper.py --startDate 01/01/2020 --endDate 27/03/2022
```

Where **startDate** is the start date and **endDate** is the end date of interval of time to query. All data between this interval is extracted into csv file.


It currently extracts the current price of the following fuels:

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
