# Estetica
# from pprint import pprint

# Modulos de red
from ping3 import ping
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
# import subprocess

def pruebaLatencia(ip:str):
    latencia = ping(dest_addr=ip, unit="ms")
    if latencia: return latencia
    else: raise Exception("La IP no estableció conexión.")

# Requiere verificaion de Ookla Speedtest (resolvable DNS y otras specs mas)
# def pruebaST(ip:str):
#     sp_test = Speedtest(source_address=ip)
#     # sp_test = Speedtest()
#     velDescarga = sp_test.download(threads=None)/(1024*1024) # Obtener velocidad de descarga
#     velSubida = sp_test.upload(threads=None)/(1024*1024) # Obtener velocidad de subida
#     # print("Velocidad de descarga: %.2lf MBps\nVelocidad de subida: %.2lf MBps" % (velDescarga, velSubida))
#     # pprint(sp_test.results.dict())
#     return (velDescarga,velSubida)

# Obtenido de https://github.com/arnavchachra/openspeedtest/blob/main/speedtest.py
def pruebaSubidaDescarga(ip:str):
    import time
    from bs4 import BeautifulSoup

    # Preparar clase de driver y ejecutar chrome
    options = Options()
    options.headless = True
    navegador = webdriver.Chrome()

    # Verificar e Ir a la página de la IP en puerto 3000
    try: navegador.get(f'http://{ip}:3000/?R')
    except WebDriverException: raise Exception("La IP vinculada rechazó la conexión.") 
    
    # Verificar previo si la pagina contiene los elementos
    navegador.find_element(value="upResultC2")
    
    time.sleep(60)
    # Extraer contenido pasado la prueba
    contenido = navegador.page_source

    # Cerrar chrome
    navegador.quit()

    # Castear HTML mediante bs4
    pagina = BeautifulSoup(contenido, 'html.parser')

    # Obtener velocidad de subido y descarga
    velDescarga = pagina.find(id='downResultC1').get_text().replace('\n', ' ')
    velSubida = pagina.find(id='upResultC2').get_text().replace('\n', ' ')

    return (velDescarga,velSubida)

# El cmd de ping varía con el idioma y resultado de windows
# def pruebaPPaquetes(ip:str):
#     cmd_ping = subprocess.run(["ping", "-n", "5", ip], stdout=subprocess.PIPE, text=True)
    # pprint(cmd_ping.stdout)
    # cmd_stdout = cmd_ping.stdout.splitlines()[-4].split(",")[-1].strip()
    # loss = [int(i) for i in cmd_stdout.split() if i.isdigit()]
    # return loss
    # print(f"Loss: {paq_loss}")

def pruebaPPaquetes(ip:str):
    # List comprehension de pings
    pruebaPing = [ping(dest_addr=ip) for pong in range(5)]
    # Filtrar los que fallaron
    pruebaPing = list(filter(lambda pong: pong == None or pong == False , pruebaPing))
    # Retornar numero de fallos (paquetes perdidos)
    return len(pruebaPing)

    