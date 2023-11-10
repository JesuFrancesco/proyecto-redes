# Estetica
# from pprint import pprint
# Modulos de red
from speedtest import Speedtest
from ping3 import ping
import subprocess

def pruebaLatencia(ip:str):
    latencia = ping(dest_addr=ip, unit="ms")
    # print(f"Latencia: {latencia} ms")
    return latencia

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
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from bs4 import BeautifulSoup

    # Configure Chrome browser and initialize a WebDriver instance
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    # Navigate to the OpenSpeedTest website
    driver.get(f'http://{ip}:3000/?R')
    time.sleep(40) # Originalmente 60 (1 minuto)
    # Extract the fully rendered HTML content of the page
    html_content = driver.page_source

    # Quit the WebDriver instance
    driver.quit()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract download, upload, and ping speeds from the page
    velDescarga = soup.find(id='downResultC1').get_text().replace('\n', ' ')
    velSubida = soup.find(id='upResultC2').get_text().replace('\n', ' ')

    return (velDescarga,velSubida)


def pruebaPPaquetes(ip:str):
    cmd_ping = subprocess.run(["ping", "-n", "5", ip], stdout=subprocess.PIPE, text=True)
    # pprint(cmd_ping.stdout)
    cmd_stdout = cmd_ping.stdout.splitlines()[-4].split(",")[-1].strip()
    loss = [int(i) for i in cmd_stdout.split() if i.isdigit()]
    return loss
    # print(f"Loss: {paq_loss}")
    