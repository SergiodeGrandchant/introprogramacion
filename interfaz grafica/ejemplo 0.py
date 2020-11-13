import tkinter as tk
from tkinter import ttk

def transportar():
    numeroA = entradaNA.get()
    salidaRES.set(numeroA)

#Creación de ventana
#Utilzamos el "tk" porque en la parte superior de la importación de la
#librería indicamos que en vez de utilizar la palabra "tkinter" utilizaremos
#tk es por eso el uso del "as"
ventana=tk.Tk()

#Configurar el tamaño de la ventana
ventana.config(width=300,height=200)


etiquetaNA=ttk.Label(ventana,text="Número A:")
etiquetaNA.place(x=0,y=0)



#Creación de una entrada "caja de texto" con la palabra "ttk" que proviene
#de la libreria tkinter
#Le indicamos también que esta entrada estara dentro de nuestra ventana
entradaNA=ttk.Entry(ventana)
#Posteriormente le damos una posición a esta entrada o caja de texto
entradaNA.place(x=70,y=0)




etiquetaNB=ttk.Label(ventana,text="Número B:")
etiquetaNB.place(x=0,y=30)
entradaNB=ttk.Entry(ventana)
entradaNB.place(x=70,y=30)

etiquetaRES=ttk.Label(ventana,text="Resultado:")
etiquetaRES.place(x=0,y=60)
entradaRES=ttk.Entry(ventana)
entradaRES.place(x=70,y=60)




botontransportar = tkk.Button(ventana, text = "Transportar -->", command=funtransport)

ventana.mainloop()