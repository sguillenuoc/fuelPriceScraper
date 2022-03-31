from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from time import sleep
import os
import urlopen


# web a analizar

url = "https://www.dieselogasolina.com/buscador-gasolineras.html"

# Setting options for the webdriver

option = webdriver.ChromeOptions()
option.add_argument("--incognito")  # open incognito mode
option.add_argument("user-agent=AcademicCrawler")

# set our UserAgent name, in this case AcademicCrawler

# Getting current folder path
My_path = os.path.dirname(os.path.abspath(__file__))

TimeOut = 5

# mirar codigo html del formulario para encontrar campos minimos a rellenar
# parametros formulario

pro = "BARCELONA"
loc = "SABADELL"
combustible = "Ninguno en concreto"
marca = "Cualquiera"

# inicio navegador

browser = webdriver.Chrome(executable_path=My_path + '/chromedriver.exe', chrome_options=option)
browser.get(url)

# introducir todos los campos mínimos
# introducir parametro station en formulario

stf = browser.find_element(By.NAME, "provincia")
stf.send_keys(pro)
sleep(5)

# introducir parametro ccaa en formulario

caf = browser.find_element(By.NAME, "localidad")
caf.send_keys(loc)
sleep(5)

carf = browser.find_element(By.NAME, "tipo_combustible")
caf.send_keys(combustible)
sleep(5)

marf = browser.find_element(By.NAME, "empresa")
caf.send_keys(marca)
sleep(5)


# pulsar boton buscar (mirar etiqueta de boton)

search = browser.find_element(By.CLASS_NAME, "btn.btn-red.shadowover")
search.click()




# inicio scraping

result = requests.get(url)
src = result.content
soup = BeautifulSoup(src, "html.parser")

print(soup.prettify())
"""
elements = browser.find_elements(By.ID, "rdos_gasolineras_wrapper")
links = []
for element in elements:
    links.append(element.get_attribute("href"))

# Navigate through the links
dictlist = []

for link in links:
    browser.get(link)
    browser.implicitly_wait(TimeOut)
    userStatsDict = {}

# crear archivo

filename = "/FuelData.csv"
file = open(My_path + filename, "w+")


for i in range(len(links)):
    file.write(str(links[i]) + ";")
file.write(\n)


file.close()
browser.quit()"""
