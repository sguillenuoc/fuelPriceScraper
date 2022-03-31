from selenium import webdriver
import requests
from bs4 import BeautifullSoup

# web a analizar

url = 

# mirar codigo html del formulario para encontrar campos minimos a rellenar
# parametros formulario

StationsMenu = "Estaciones servicio"
ccaa = "Cataluña"
combustible = ""

# inicio navegador

nav = werbdriver.chrome
nav.get(url)

# introducir parametro station en formulario

stf = driver.find_element_by_name("widthStationsMenu")
stf.send_keys(StationsMenu)
sleep(5)

#introducir parametro ccaa en formulario

caf = driver.find_element_by_name ("CCAA")
caf.send_keys (ccaa)
sleep(5)

# introducir todos los campos minimos
...


# pulsar boton buscar (mirar etiqueta de boton)

search = driver.find_element_by_id("boton search")
submit.click()

# inicio scraping

result = requests.get(url)
src = result.content
soup = BeautifulSoup(src, "xlml)


