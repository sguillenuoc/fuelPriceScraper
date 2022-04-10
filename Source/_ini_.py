from fuelWebScraping import scrapfuel

print("\nBuscador estaciones de servicio ATiempo")
print("==========================================")

print("\nIntroduzca la Provincia")
provincia = input()

print('Introduzca la Localidad')
localidad = input()

print('Introduzca el tipo de combustible')
print("Opciones:\n Gasolina sin plomo 95 / Gasolina sin plomo 97 / Gasolina sin plomo 98/\n"
      "Gasóleo A habitual / Gasóleo A mejorado / Gasóleo B / Gasóleo C\n"
      "Biodiésel / Autogas GLP / Gas N.Compr / Gas N. Licuado ")
combustible = input()

print('Dirección actual:')
print('(ejemplo: Calle de Atocha 125, Madrid)\n')
direccion = input()

scrapfuel(provincia, localidad, combustible, direccion)

print("=====================")
print("Extracción de información completada")
print("=====================")