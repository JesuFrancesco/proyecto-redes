# Estetica
# from pprint import pprint

# Modulos de red
from ping3 import ping
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

def pruebaLatencia(ip:str):
    latencia = ping(dest_addr=ip, unit="ms", ttl=128)
    if not latencia: raise Exception("No se estableció conexión con la dirección.")

    n = 4
    tiempo = 0
    for i in range(n):
        rtt = ping(dest_addr=ip, unit="ms") # rtt = tiempo de ida y vuelta
        if rtt is not False:
            tiempo += rtt

    return tiempo / n

# Adaptado de https://github.com/arnavchachra/openspeedtest/blob/main/speedtest.py
def pruebaSubidaDescarga(ip:str):
    import time
    from bs4 import BeautifulSoup

    # Preparar clase de driver y ejecutar chrome
    options = Options()
    options.headless = True
    navegador = webdriver.Chrome()
    navegador.set_page_load_timeout(10)

    # Verificar e Ir a la página de la IP en puerto 3000
    try: navegador.get(f'http://{ip}:3000/?R')
    except WebDriverException: raise Exception("La IP no corresponde a un servicio de OpenSpeedTest o el puerto rechazó la conexión.") 
    time.sleep(3)

    # Verificar previo si la pagina contiene los elementos
    navegador.find_element(value="upResultC2")

    tmp = BeautifulSoup(navegador.page_source, 'html.parser').find(id="upResultC2").get_text().split()[0]
    while tmp == "---":
        time.sleep(5)
        tmp = BeautifulSoup(navegador.page_source, 'html.parser').find(id="upResultC2").get_text().split()[0]
    
    # Extraer contenido pasado la prueba
    contenido = navegador.page_source

    # Cerrar chrome
    navegador.quit()
    
    # Castear HTML mediante bs4
    pagina = BeautifulSoup(contenido, 'html.parser')

    # Obtener velocidad de subido y descarga
    velDescarga = float(pagina.find(id='downResultC1').get_text().split()[0])
    velSubida = float(pagina.find(id='upResultC2').get_text().split()[0])

    return (velDescarga,velSubida)

def pruebaPPaquetes(ip:str):
    # List comprehension de pings
    pruebaPing = [ping(dest_addr=ip) for pong in range(10)]
    # Filtrar los que fallaron
    pruebaPing = list(filter(lambda pong: pong == None or pong == False , pruebaPing))
    # Retornar numero de fallos (paquetes perdidos)
    return len(pruebaPing)

    