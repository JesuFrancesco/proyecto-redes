# Estetica
from pprint import pprint
# Modulos de red
from speedtest import Speedtest
from ping3 import ping
import subprocess

def pruebaLatencia(ip:str):
    latencia = ping(dest_addr=ip, unit="ms")
    print(f"Latencia: {latencia} ms")
    # return latencia

def pruebaST(ip:str):
    # sp_test = Speedtest(source_address=ip)
    sp_test = Speedtest()
    velDescarga = sp_test.download(threads=None)/(1024*1024) # Obtener velocidad de descarga
    velSubida = sp_test.upload(threads=None)/(1024*1024) # Obtener velocidad de subida
    print("Velocidad de descarga: %.2lf MBps\nVelocidad de subida: %.2lf MBps" % (velDescarga, velSubida))
    # pprint(sp_test.results.dict())
    # return (velDescarga,velSubida)

def pruebaPPaquetes(ip:str):
    cmd_ping = subprocess.run(["ping", "-n", "5", ip], stdout=subprocess.PIPE, text=True)
    # pprint(cmd_ping.stdout)
    paq_loss = cmd_ping.stdout.splitlines()[-3].split(",")[2].strip()
    print(f"Loss: {paq_loss}")