import tkinter
from tkinter import ttk
from tkinter import messagebox
from time import sleep
from pruebasMultiples import*

window = tkinter.Tk()
window.title("PROYECTO FINAL: REDES DE COMPUTADORAS")


frame = tkinter.Frame(window, bg="#FFFFFF")
frame.pack()


title_frame = tkinter.LabelFrame(frame, bg="#FFFFFF")
title_frame.grid(row = 0, column = 0, sticky="news", padx= 12, pady=(12,2))


title_label = tkinter.Label(title_frame, text = "  Analisis de la calidad \n de internet", font=("Courier New", 20, "bold"), bg="#FFFFFF", fg="#333333")
title_label.grid(row = 0, column = 0 , padx = 21, pady= (10,2))


img = tkinter.PhotoImage(file=r"ulimalogo.gif")

from PIL import Image, ImageTk
imagen_gif_1 = Image.open("ulimalogo.gif")
frames1 = []
try:
    while True:
        frames1.append(imagen_gif_1.copy())
        imagen_gif_1.seek(len(frames1))
except EOFError:
    pass

imagen = tkinter.Label(title_frame, image = img, bd=0)
imagen.grid(row=1, column=0, pady= 15)

def mostrar_siguiente_frame_GIF1(frame_index):
    frame_actual = frames1[frame_index]
    imagen1 = ImageTk.PhotoImage(frame_actual)
    imagen.config(image=imagen1)
    imagen.grid(row=3, column=0, sticky="WE")
    imagen.image = imagen1  # Evitar que la imagen sea eliminada por el recolector de basura
    window.after(50, mostrar_siguiente_frame_GIF1, (frame_index + 1) % len(frames1)) # 
mostrar_siguiente_frame_GIF1(0)


input_frame = tkinter.LabelFrame(frame, text = "  Ingreso de datos  ", bg="#FFFFFF")
input_frame.grid(row = 1, column = 0, sticky="news", padx= 12, pady=2)


ip_label = tkinter.Label(input_frame, text="IP:", bg="#FFFFFF")
ip_label.grid(row=0,column=0)

ip = tkinter.StringVar()
ip_textbox = tkinter.Entry(input_frame, width=18, bg="#FFFFFF", textvariable=ip)
ip_textbox.grid(row=0, column=1)


relleno = tkinter.Label(input_frame, text="             ", bg="#FFFFFF")
relleno.grid(row=0, column=2)


region_label = tkinter.Label(input_frame, text="Region:", bg="#FFFFFF")
region_label.grid(row=0, column=3)


region_opciones = ttk.Combobox(input_frame, values=["","Asia","America","Africa","Europa","Oceanía"], width=10, state='readonly')
region_opciones.grid(row=0, column=4)
def llenarIP(event):
    region = region_opciones.get()
    ip_var:str
    if region == "America":
        ip_var = "18.220.109.253" # Instancia EC2 en NA (Ohio)
    elif region == "Europa":
        ip_var = "52.16.98.249" # Instancia EC2 en EU (Irlanda)
    elif region == "Asia":
        ip_var = "117.102.109.186" # CAMBIAR POR INSTANCIA EC2
    elif region == "Oceania":
        ip_var = "117.102.109.186" # CAMBIAR POR INSTANCIA EC2
    else:
        ip_var = "127.0.0.1"
    ip.set(ip_var)    
    
region_opciones.bind('<<ComboboxSelected>>', llenarIP)

def testAnchoBanda(ip):
    try:
        rAnchoB = pruebaSubidaDescarga(ip)
        AnchoB_result.config(text=f"Descarga: {rAnchoB[0]}\nSubida: {rAnchoB[1]}")
    except Exception as Err:
        messagebox.showwarning("Error | Prueba de ancho de banda", f"Algo salió mal.\n{Err}")
        AnchoB_result.config(text="Error")

def testLatencia(ip):
    try:
        Latencia_result.config(text=f"{str(round(pruebaLatencia(ip), 4))} msec")
    except Exception as Err:
        messagebox.showwarning("Error | Prueba de latencia", f"Algo salio mal.\n{Err}")
        Latencia_result.config(text="Error")

def testPPaquetes(ip):
    try:
        loss = pruebaPPaquetes(ip)
        PerdidaP_result.config(text=f"{loss} paquetes perdidos")
    except Exception as Err:
        messagebox.showwarning("Error | Prueba de pérdida de paquetes", f"Algo salio mal.\n{Err}")
        PerdidaP_result.config(text="Error")

def capturarDatos():
    sleep(1)
    ip = ip_textbox.get()
    region = region_opciones.get()
    
    # Si no hay IP
    if ip == "":
        tkinter.messagebox.showwarning("Error", "Complete la dirección IP")
        return

    for i in [AnchoB_result, Latencia_result, PerdidaP_result]:
            i.config(text="Cargando...")
    
    import threading as t
    t.Thread(target=lambda: testAnchoBanda(ip)).start()
    t.Thread(target=lambda: testLatencia(ip)).start()
    t.Thread(target=lambda: testPPaquetes(ip)).start()

boton_enviar = tkinter.Button(input_frame, text="          Enviar          ", command=capturarDatos)
boton_enviar.grid(row=2, column=2)


for widget in input_frame.winfo_children():
    widget.grid_configure(padx = 10, pady= 7.5)
                         
output_frame = tkinter.LabelFrame(frame, text = "  Resultados  ", bg="#FFFFFF")
output_frame.grid(row = 2, column = 0, sticky="news", padx= 12, pady=(2,12))


AnchoB_label = tkinter.Label(output_frame, text="Ancho de banda:", bg="#FFFFFF")
AnchoB_label.grid(row=0,column=0)


Latencia_label = tkinter.Label(output_frame, text="Latencia:", bg="#FFFFFF")
Latencia_label.grid(row=0,column=1)


PerdidaP_label = tkinter.Label(output_frame, text="Perdida de paquetes:", bg="#FFFFFF")
PerdidaP_label.grid(row=0,column=2)


for widget in output_frame.winfo_children():
    widget.grid_configure(padx = 32.5, pady= 5)


AnchoB_result = tkinter.Label(output_frame, text=" ", bg="#FFFFFF")
AnchoB_result.grid(row=1,column=0, pady= (0,10))
Latencia_result = tkinter.Label(output_frame, text=" ", bg="#FFFFFF")
Latencia_result.grid(row=1,column=1, pady= (0,10))
PerdidaP_result = tkinter.Label(output_frame, text=" ", bg="#FFFFFF")
PerdidaP_result.grid(row=1, column=2, pady= (0,10))

window.mainloop()