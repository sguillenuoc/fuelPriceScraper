# Analizamos el archivo robots.txt de la web de estudio
# Creamos una función para analizar la web
def robot_txt(url):
    if url.endswith('/'):
        path = url
    else:
        path = url + '/'

    req = requests.get(path + "robots.txt",data =None)
    return req.text
