from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
from geopy.geocoders import Nominatim
from math import radians, cos, sin, asin, sqrt
from random import randint

# Genera un fichero con los precios del carburates dada una ubicación
def scrapfuel(pro, loc, combustible, direccion):
    # Web a analizar, parametros formulario y fichero salida
    url = 'https://www.dieselogasolina.com/'

    # Opciones de navegación
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')  # ventana maximizada
    options.add_argument('--disable-extensions')  # sin extensiones

    # Path actual (donde está ubicado el driver chromedriver.exe)
    My_path = os.path.dirname(os.path.abspath(__file__))

    # Inicializamos el navegador
    driver = webdriver.Chrome(executable_path=My_path + '/chromedriver.exe', options=options)
    driver.get(url)
    time.sleep(1)

    # Interactuamos con la web con Selenium

    # Aceptamos el uso de cookies
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-blue'))) \
        .click()
    time.sleep(2)

    # Redirección a la pantalla de búsqueda
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/ul/li[1]/a'))) \
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
    time.sleep(2)

    # Pulsamos el botón de buscar
    WebDriverWait(driver, 5) \
        .until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[2]/div[2]/div/div[3]/div[1]/div/div/div[2]/div/div/form/p[2]/input'))) \
        .click()
    time.sleep(2)

    info_stations = []
    num_pag = driver.find_element(By.XPATH, """.//span/a[last()]""").text
    pags = int(num_pag)
    puntoRef = PosicionGeografica(direccion)

    for i in range(pags):
        contents = driver.find_elements(By.XPATH, """//table[@id="rdos_gasolineras"]/tbody/tr""")
        for content in contents:
            info_station = dict(loc=content.find_element(By.XPATH, """.//td[@class="localidad sorting_1"]""").text,
                                dir=content.find_element(By.XPATH, """.//td[@class="direccion"]""").text,
                                horario=content.find_element(By.XPATH, """.//td[@class="horario"]""").text,
                                empresa=content.find_element(By.XPATH, """.//td[@class="empresa"]""").text,
                                precio=content.find_element(By.XPATH, """.//td[@class="precio"]""").text,
                                fecha=content.find_element(By.XPATH,""".//td[@class="fecha_actualizacion"]""").text,
                                link=content.find_element(By.XPATH, """.//a""").get_attribute("href"),
                                distancia=Distancia(puntoRef, f'{content.find_element(By.XPATH, """.//td[@class="direccion"]""").text},{content.find_element(By.XPATH, """.//td[@class="localidad sorting_1"]""").text}')
                                )

            info_stations.append(info_station)

        if i < pags-1:
            # print(f'Click:{i}')
            WebDriverWait(driver, 5) \
                .until(EC.element_to_be_clickable((By.XPATH, """.//a[@class="paginate_button next"]"""))) \
                .click()
            time.sleep(2)

    filename = "/StationData.csv"
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

    driver.quit()

def Distancia(ptoRef, ptoB):
    # return 10
    # time.sleep(1)
    puntoB = PosicionGeografica(ptoB)
    distancia = haversine(ptoRef[0], ptoRef[1], puntoB[0], puntoB[1])
    return distancia


#Fórmula de Haversine: Calcular la distancia en Km entre dos coordenadas
def haversine(lon1, lat1, lon2, lat2):

    # Conversión a radianes
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Fórmula haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radio de la Tierra en Km.
    return c * r

#Obtener coordenadas de una dirección dada
def PosicionGeografica(direccion):
    user_agent = 'fuelWebScraping_{}'.format(randint(10000, 99999))
    time.sleep(randint(1 * 100, 1 * 100) / 100)
    geolocator = Nominatim(user_agent=user_agent)
    localizacion = geolocator.geocode(direccion)
    #Evaluamos sí ha sido capaz de obtener las coordenadas de la dirección
    if localizacion is None:
        return [-6.066313011301985, 76.60688866999108]
    else:
        return [localizacion.longitude, localizacion.latitude]
