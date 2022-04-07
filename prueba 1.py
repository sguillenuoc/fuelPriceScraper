from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import csv
import os

# Web a analizar, parametros formulario y fichero salida
url = 'https://www.dieselogasolina.com/'
pro = 'BARCELONA'
loc = 'SABADELL'
combustible = 'Gasolina sin plomo 95'
csv_name = 'dieselogasolina.csv'

# Opciones de navegación
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')  # ventana maximizada
options.add_argument('--disable-extensions')  # sin extensiones

# Path actual (donde está ubicado el driver chromedriver.exe)
My_path = os.path.dirname(os.path.abspath(__file__))

# Inicializamos el navegador
driver = webdriver.Chrome(executable_path=My_path + '/chromedriver.exe', options=options)
driver.get(url)

# Interactuamos con la web con Selenium
###

# Aceptamos el uso de cookies
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                       'button.btn.btn-blue'))) \
    .click()
time.sleep(2)

# Redirección a la pantalla de búsqueda
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[1]/div[2]/div[1]/div[2]/ul/li[1]/a'))) \
    .click()
time.sleep(2)

# Selector de la provincia
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.ID, 'provincia'))) \
    .send_keys(pro)

# Selector de la provincia
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.ID, 'localidad'))) \
    .send_keys(loc)

# Selector del tipo de combustible
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.ID, 'tipo_combustible'))) \
    .send_keys(combustible)

# Pulsamos el botón de buscar
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.XPATH,
                                       '/html/body/div[2]/div[2]/div[2]/div/div[3]/div[1]/div/div/div[2]/div/div/form/p[2]/input'))) \
    .click()
time.sleep(5)

contents = driver.find_elements(By.XPATH, """//table[@id="rdos_gasolineras"]/tbody/tr""")

info_stations = []

for content in contents:
    info_station = {
        "loc":  content.find_element(By.XPATH, """.//td[@class="localidad sorting_1"]""").text,
        "dir": content.find_element(By.XPATH, """.//td[@class="direccion"]""").text,
        "horario": content.find_element(By.XPATH, """.//td[@class="horario"]""").text,
        "empresa": content.find_element(By.XPATH, """.//td[@class="empresa"]""").text,
        "link": content.find_element(By.XPATH, """.//a""").get_attribute("href")
    }

    info_stations.append(info_station)
    print(info_stations)
WebDriverWait(driver, 5) \
    .until(EC.element_to_be_clickable((By.ID, 'rdos_gasolineras_next'))) \
    .click()
time.sleep(1)

filename = "/StationData.txt"
file = open(My_path + filename, "w+")

keys = []
for key in info_station:
    keys.append(key)
# Dump all the data with CSV format
for i in range(len(keys)):
    file.write(str(keys[i]) + ";")
file.write("\n")
for i in range(len(info_stations)):
    for j in range(len(keys)):
        file.writelines(str(info_stations[i][keys[j]]) + ";")
    file.write("\n")
file.close()
