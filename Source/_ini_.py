# from fuelWebScraping import scrapfuel
# from fuelPriceScrapingMinisterio import scrapfuel
from fuelWebScrapingGeoPortal import scrapfuel

print("\nBuscador estaciones de servicio ATiempo")
print("==========================================")

print("\nIntroduzca la Provincia")
provincia = input()

print('Introduzca la Localidad')
localidad = input()

print('Introduzca el tipo de combustible')
print("Opciones:\n Gasolina 95 E5 / Gasóleo A habitual \n"
      "Biodiésel / Gas natural licuado ")
combustible = input()

print('Dirección actual:')
print('(ejemplo: Calle de Atocha 125, Madrid)')
direccion = input()

scrapfuel(provincia, localidad, combustible, direccion)

print("=====================")
print("Extracción de información completada")
print("=====================")