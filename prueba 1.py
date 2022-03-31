from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from time import sleep
import os


def get_robot_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'
    req = requests.get(path + "robots.txt", data=None)
    return req.text


# web a analizar

url = "https://geoportalgasolineras.es/#/Inicio"

# Setting options for the webdriver

option = webdriver.ChromeOptions()
option.add_argument("--incognito")  # open incognito mode
option.add_argument("user-agent=AcademicCrawler")

# set our UserAgent name, in this case AcademicCrawler

# Getting current folder path
My_path = os.path.dirname(os.path.abspath(__file__))

# mirar codigo html del formulario para encontrar campos minimos a rellenar
# parametros formulario

StationsMenu = "Estaciones servicio"
ccaa = "CATALUNYA"
combustible = "Gasolina 95 E5"

# inicio navegador

browser = webdriver.Chrome(executable_path=My_path + '/chromedriver.exe', chrome_options=option)
browser.get(url)

# introducir todos los campos mínimos
# introducir parametro station en formulario

stf = browser.find_element(By.NAME, "tipoBusqueda")
stf.send_keys(StationsMenu)
sleep(5)

# introducir parametro ccaa en formulario

caf = browser.find_element(By.NAME, "provincia")
caf.send_keys(ccaa)
sleep(5)

carf = browser.find_element(By.NAME, "tipoCarburante")
caf.send_keys(combustible)
sleep(5)

# pulsar boton buscar (mirar etiqueta de boton)

search = browser.find_element(By.ID, "botonBuscar")
search.click()

# inicio scraping

result = requests.get(url)
src = result.content
soup = BeautifulSoup(src, "xlml")
