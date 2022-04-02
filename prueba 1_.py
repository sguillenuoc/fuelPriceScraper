# Librerías
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import os
import pandas as pd

# Web a analizar, parametros formulario y fichero salida
url = 'https://www.dieselogasolina.com/'
pro = 'BARCELONA'
loc = 'SABADELL'
combustible = 'Gasolina sin plomo 95'
txt_name = 'dieselogasolina.txt'

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

###
# utilizamos Beautifulsoup para estructurar el contenido y así poder interacturar-encontrar los elementos.
content = driver.page_source
soup = BeautifulSoup(content, "html5lib")

# la tabla con el contenido que nos interesa tiene paginación. Obtenemos el elemento y navegaremos a través del botón next
navegacion = soup.find('div', id='rdos_gasolineras_paginate', class_='dataTables_paginate paging_full_numbers')
paginas = navegacion.find('span')

# la transformación utilizando pandas no es buena. Recorremos por la tabla para extraer su contenido.
tabla_datos = 'Localidad|Dirección|Margen|Horario|Empresa|Fecha|Precios'
i = 1  # índice
for child in paginas.children:
    # Actualizamos el contenido
    content = driver.page_source
    soup = BeautifulSoup(content, "html5lib")
    table = soup.find('table', id='rdos_gasolineras')
    # Recorremos las filas de la tabla y añadimos a la variable tabla_datos
    for tr in table.findAll('tr'):
        fila = str(i)
        for td in tr.findAll('td'):
            campo = str(td.text).strip()
            if (len(campo) > 0):
                fila = fila + '|' + campo
        if len(fila) > 2:
            tabla_datos = tabla_datos + '\n' + fila
            i = i + 1
    # Paginamos
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.ID, 'rdos_gasolineras_next'))) \
        .click()
    time.sleep(1)

# exportar los datos a un archivo txt
with open(txt_name, 'w', encoding='utf-8') as file:
    file.write(tabla_datos)

# cerramos el navegador
driver.quit()
