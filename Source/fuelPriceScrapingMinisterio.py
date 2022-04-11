from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import os
import requests
import pandas as pd
from random import randint
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


# Genera un fichero con los precios del carburates dada una ubicación
def scrapfuel(pro, loc, combustible, direccion):
    # Web a analizar, parametros formulario y fichero salida
    url = 'https://geoportalgasolineras.es/'

    # Opciones de navegación
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')  # ventana maximizada
    options.add_argument('--disable-extensions')  # sin extensiones

    # Path actual (donde está ubicado el driver chromedriver.exe)
    My_path = os.path.dirname(os.path.abspath(__file__))

    # Inicializamos el navegador
    driver = webdriver.Chrome(executable_path=My_path + '/chromedriver.exe', options=options)

    # Interactuamos con la web con Selenium
    # 1 | open | / |
    driver.get(url)
    time.sleep(1)
    # 2 | setWindowSize | 968x1020 |
    driver.set_window_size(1024, 900)
    time.sleep(2)
    # 3 | click | css=#tipoBusqueda_chosen span |
    driver.find_element(By.CSS_SELECTOR, "#tipoBusqueda_chosen span").click()
    # 4 | click | css=.result-selected |
    driver.find_element(By.CSS_SELECTOR, ".result-selected").click()
    # 5 | click | css=#provincias_select_id_chosen span |
    driver.find_element(By.CSS_SELECTOR, "#provincias_select_id_chosen span").click()
    # 6 | type | css=#provincias_select_id_chosen input | barcelona
    driver.find_element(By.CSS_SELECTOR, "#provincias_select_id_chosen input").send_keys("Alicante")
    # 7 | sendKeys | css=#provincias_select_id_chosen input | ${KEY_ENTER}
    driver.find_element(By.CSS_SELECTOR, "#provincias_select_id_chosen input").send_keys(Keys.ENTER)
    time.sleep(5)
    # 8 | click | css=#municipios_select_id_chosen span |
    driver.find_element(By.CSS_SELECTOR, "#municipios_select_id_chosen span").click()
    # 9 | type | css=#municipios_select_id_chosen input | badalona
    driver.find_element(By.CSS_SELECTOR, "#municipios_select_id_chosen input").send_keys("Denia")
    time.sleep(2)
    # 10 | sendKeys | css=#municipios_select_id_chosen input | ${KEY_ENTER}
    driver.find_element(By.CSS_SELECTOR, "#municipios_select_id_chosen input").send_keys(Keys.ENTER)
    # 11 | click | css=#tiposcombustible_select_id_chosen span |
    driver.find_element(By.CSS_SELECTOR, "#tiposcombustible_select_id_chosen span").click()
    time.sleep(2)
    # 12 | type | css=#tiposcombustible_select_id_chosen input | gasolina 95 e5
    driver.find_element(By.CSS_SELECTOR, "#tiposcombustible_select_id_chosen input").send_keys(
        "gasolina 95 e5")
    # 13 | sendKeys | css=#tiposcombustible_select_id_chosen input | ${KEY_ENTER}
    driver.find_element(By.CSS_SELECTOR, "#tiposcombustible_select_id_chosen input").send_keys(Keys.ENTER)
    time.sleep(2)
    # 14 | click | id=botonBuscar |
    driver.find_element(By.ID, "botonBuscar").click()
    time.sleep(2)
    #15 | click | css=tbody > .ng-scope:nth-child(1) > .ng-binding:nth-child(1) |
    col0101 = driver.find_element(By.CSS_SELECTOR, "tbody > .ng-scope:nth-child(1) > .ng-binding:nth-child(1)").text
    print(col0101)
    col0102 = driver.find_element(By.CSS_SELECTOR, "tbody > .ng-scope:nth-child(1) > .ng-binding:nth-child(2)").text
    print(col0102)
    col0103 = driver.find_element(By.CSS_SELECTOR, "tbody > .ng-scope:nth-child(1) > .ng-binding:nth-child(3)").text
    print(col0103)

    info_stations = []
    col0101 = driver.find_element(By.XPATH, "//table[@id=\'datatableResultadoBusqueda\']/tbody/tr[5]/td").text
    print(col0101)
    col0102 = driver.find_element(By.XPATH, "//table[@id=\'datatableResultadoBusqueda\']/tbody/tr[5]/td[2]").text
    print(col0102)
    col0103 = driver.find_element(By.XPATH, "//table[@id=\'datatableResultadoBusqueda\']/tbody/tr[5]/td[3]").text
    print(col0103)
    col0103 = driver.find_element(By.XPATH, "//table[@id=\'datatableResultadoBusqueda\']/tbody/tr[9]/td").text
    print(col0103)

    info_stations=[]
    pags = 2
    for i in range(pags):
        i = i+1
        print(f"//table[@id=\'datatableResultadoBusqueda\']/tbody/tr[{i}]/td[2]")
        print(driver.find_element(By.XPATH, f"//table[@id=\'datatableResultadoBusqueda\']/tbody/tr[{i}]/td[2]").text)
        # info_station = dict(loc=driver.find_element(By.XPATH, f"//table[@id=\'datatableResultadoBusqueda\']/tbody/tr[{i}]/td[2]").text,
        #                     dir=driver.find_element(By.XPATH, f"//table[@id=\'datatableResultadoBusqueda\']/tbody/tr[{i}]/td[3]").text)
        # info_stations.append(info_station)

    # for content in contents:
    #     col0101 = content.find_element(By.XPATH, "//td[3]").text
    #     print(col0101)
    #     col0101 = content.find_element(By.XPATH, "//td[4]").text
    #     print(col0101)
    #     col0101 = content.find_element(By.XPATH, "//td[5]").text
    #     print(col0101)
    #     col0101 = content.find_element(By.XPATH, "//td[6]").text
    #     print(col0101)
    #     col0101 = content.find_element(By.XPATH, "//td[7]").text
    #     print(col0101)
    #     col0101 = content.find_element(By.XPATH, "//td[8]").text
    #     print(col0101)


    time.sleep(20)




#Calcula la distancia entre dos puntos
def Distancia(ptoRef, ptoB):
    puntoB = PosicionGeografica(ptoB)
    distancia = geodesic(ptoRef, puntoB).kilometers
    return distancia


#Obtener coordenadas de una dirección dada
def PosicionGeografica(direccion):
    # Limpiamos la dirección (aumenta el % de aciertos de obtener las coordenadas)
    direccion = LimpiarDireccion(direccion)

    # https://nominatim.org. Nominatim usa OpenStreetMap. Gratuito pero con limitaciones en el número de solicitudes
    # Vamos actualizando el agente y el tiempo entre solicitudes.
    user_agent = 'fuelWebScraping_{}'.format(randint(10000, 99999))
    time.sleep(randint(1 * 100, 1 * 100) / 100)
    geolocator = Nominatim(user_agent=user_agent)
    localizacion = geolocator.geocode(direccion)
    #Evaluamos sí ha sido capaz de obtener las coordenadas de la dirección
    if localizacion is None:
        return [-6.066313011301985, 76.60688866999108]
    else:
        return [localizacion.longitude, localizacion.latitude]

def LimpiarDireccion(direccion):
    direccion = direccion.upper()
    direccion = direccion.replace('CALLE', '')
    direccion = direccion.replace('CARRER', '')
    direccion = direccion.replace('AVENIDA', '')
    direccion = direccion.replace('AVINGUDA', '')
    direccion = direccion.replace('PLAZA', '')
    direccion = direccion.replace('S/N', '1')
    direccion = direccion.replace('C.', '')
    direccion = direccion.replace('AV.', '')
    direccion = direccion.replace('CR', '')
    direccion = direccion.replace('CARRETERA', '')
    direccion = direccion.replace('AUTOVIA', '')
    direccion = direccion.replace('KM.', '')
    direccion = direccion.replace('.', '')
    return direccion

def zenodo_upload(path, filename):
    # Accedemos al repositorio haciendo uso de nuestro token
    # el token lo creamos desde la página de Zenodo
    token = '6Yx0eQpSrtfxUXW0qmSgeKFwkg7jqnydb5xSPk2J9seuHpQzt6RxKUqEXQFz'
    cabecera = {'Content-Type': 'application/json'}
    parametros = params = {'access_token': token}
    descripcion = {
        'metadata': {
            'title': 'fuelPriceScraper',
            'upload_type': 'Dataset',
            'description': 'El dataset contiene la información de estaciones de servicio. \n Los datos proceden de la información publicada por el Ministerio para la transición ecológica y el reto demográfico. \n Generado con fines educativos.',
            'creators': [{'name': 'sguillen1'}, {'name': 'cperezceb'}]
        }
    }

    #Creamos una nueva descarga
    r = requests.post('https://zenodo.org/api/deposit/depositions'
                      , params=parametros
                      , json={}
                      , headers=cabecera)

    #Subimos nuestro documento (no publica)
    bucket_url = r.json()["links"]["bucket"]
    with open(path, "rb") as fp:
        r = requests.put(
            "%s/%s" % (bucket_url, filename),
            data=fp,
            params=params
        )
    r.json()
    print(r.status_code)
    print(r.json())
