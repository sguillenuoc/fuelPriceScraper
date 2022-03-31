from selenium import webdriver
import requests
from bs4 import BeautifullSoup

# web a analizar

url = "https://geoportalgasolineras.es/#/Inicio"

# mirar codigo html del formulario para encontrar campos minimos a rellenar
# parametros formulario

StationsMenu = "Estaciones servicio"
ccaa = "BARCELONA"
combustible = "Gasolina 95 E5"

# inicio navegador

nav = werbdriver.Edge(executable_path='C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')
nav.get(url)

# introducir todos los campos mínimos
# introducir parametro station en formulario

stf = driver.find_element_by_name("tipoBusqueda")
stf.send_keys(StationsMenu)
sleep(5)

#introducir parametro ccaa en formulario

caf = driver.find_element_by_name ("provincia")
caf.send_keys (ccaa)
sleep(5)

carf = driver.find_element_by_name ("tipoCarburante")
caf.send_keys (combustible)
sleep(5)


# pulsar boton buscar (mirar etiqueta de boton)

search = driver.find_element_by_id("botonBuscar")
submit.click()

# inicio scraping

result = requests.get(url)
src = result.content
soup = BeautifulSoup(src, "xlml)
                     
fs = bs.find_all("fieldset")
for t in fs:
    print(t.get_text())

