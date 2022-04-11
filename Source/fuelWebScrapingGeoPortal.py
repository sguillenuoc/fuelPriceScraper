from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
import requests
from random import randint
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from bs4 import BeautifulSoup


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
    driver.get(url)
    time.sleep(1)

    # # Selector del tipo de
    # driver.find_element(By.CSS_SELECTOR, "#tipoBusqueda_chosen span").click()
    # # 4 | click | css=.result-selected |
    # driver.find_element(By.CSS_SELECTOR, ".result-selected").click()

    # Selector de la provincia. Buscamos nuestra provincia y pulsamos a enter. Esperamos que se cargue el combo de localidad
    driver.find_element(By.CSS_SELECTOR, "#provincias_select_id_chosen span").click()
    driver.find_element(By.CSS_SELECTOR, "#provincias_select_id_chosen input").send_keys(pro)
    driver.find_element(By.CSS_SELECTOR, "#provincias_select_id_chosen input").send_keys(Keys.ENTER)
    time.sleep(5)

    # Selector de la localidad. Buscamos y pulsamos a enter
    driver.find_element(By.CSS_SELECTOR, "#municipios_select_id_chosen span").click()
    driver.find_element(By.CSS_SELECTOR, "#municipios_select_id_chosen input").send_keys(loc)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#municipios_select_id_chosen input").send_keys(Keys.ENTER)

    # Selector del tipo de combustible
    driver.find_element(By.CSS_SELECTOR, "#tiposcombustible_select_id_chosen span").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#tiposcombustible_select_id_chosen input").send_keys(combustible)
    driver.find_element(By.CSS_SELECTOR, "#tiposcombustible_select_id_chosen input").send_keys(Keys.ENTER)
    time.sleep(2)

    # Pulsamos el botón de buscar
    driver.find_element(By.ID, "botonBuscar").click()
    time.sleep(2)

    # Obtenemos nuestra página para recuperar los datos
    content = driver.page_source
    soup = BeautifulSoup(content, "html5lib")

    i = 1
    tabla_datos = 'Cod|Provincia|Localidad|Dirección|Fecha|Precio|Venta|Remisión|Empresa|Horario'
    table = soup.find('table', attrs={'class': 'display tablaResultadoBusqueda ng-scope'})
    for rows in table.findAll('tr'):
        fila = str(i)
        for cols in rows.findAll('td', {'class': 'ng-binding'}):
            campo = str(cols.text).strip()
            if (len(campo) > 0):
                fila = fila + '|' + campo.replace('\n','')
        if len(fila) > 2:
            tabla_datos = tabla_datos + '\n' + fila
            i = i + 1
    # exportar los datos a un archivo txt
    filename = "StationData.csv"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(tabla_datos)

    # subimos el fichero al repositorio (no publicamos)
    # zenodo_upload(My_path + filename, filename)

    # cerramos el navegador
    driver.quit()


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
