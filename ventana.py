from tkinter import*
from pruebasMultiples import*
import threading as th
ventana = Tk()
ventana.geometry("400x400")
Label(text="Proyecto Redes PC", font=("Times", 20, "bold")).pack()
ip_sv = "8.8.8.8"
Button(text="Latencia", 
       command=lambda: th.Thread(target=lambda: pruebaLatencia(ip=ip_sv)).start()
       ).pack()

Button(text="Velocidad", 
       command=lambda: th.Thread(target=lambda: pruebaST(ip=ip_sv)).start()
       ).pack()
    
Button(text="Perdida paquetes", 
       command=lambda: th.Thread(target=lambda: pruebaPPaquetes(ip=ip_sv)).start()
       ).pack()

op = StringVar()
op.set("*")
region = op.get()
OptionMenu(ventana, op, *["*", "Norteamerica", "Sudamerica", "Europa", "Asia", "Oceania"]).pack()

Button(text="Exportar resultados", 
       command=lambda: print("TODO")
       ).pack()

ventana.mainloop()