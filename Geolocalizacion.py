from geopy.geocoders import Nominatim
from math import radians, cos, sin, asin, sqrt

#Fórmula de Haversine
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r


def PosicionGeografica(direccion):
    geolocator = Nominatim(user_agent="pra1")
    localizacion = geolocator.geocode(direccion)
    # print(localizacion)
    #print(localizacion.raw)
    return [localizacion.longitude, localizacion.latitude]



# puntoA = PosicionGeografica("Calle de Atocha 125, Madrid")
# puntoB = PosicionGeografica("Paseo de la Castellana 300, Madrid")
#
# print(puntoA)
# print(puntoB)
# distancia = haversine(puntoA[0], puntoA[1], puntoB[0], puntoB[1])
# print(distancia)



