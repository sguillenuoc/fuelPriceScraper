from fuelWebScraping import scrapfuel

print("\nBuscador estaciones de servicio ATiempo")
print("==========================================")

print("\nIntroduzca la Provincia")
provincia = input()

print('Introduzca la Localidad')
localidad = input()

print('Introduzca el tipo de combustible')
print("Opciones:\n Gasolina sin plomo 95 / Gasolina sin plomo 97 / Gasolina sin plomo 98/\n"
      "Gasóleo A habitual / Gasóleo A mejorado / Gasóleo b / Gasóleo C\n"
      "Biodiésel / Autogas GLP / Gas N.Compr / Gas N. Licuado ")

combustible = input()
scrapfuel(provincia, localidad, combustible)

print("=====================")
print("Extracción de información completada")
print("=====================")
