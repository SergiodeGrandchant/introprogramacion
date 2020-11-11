import tkinter as tk
from tkinter import *

def limpiarCampos():
    NA.set(0)
    NB.set(0)

def sumar():
    numeroA=NA.get()
    numeroB=NB.get()
    numeroR=numeroA+numeroB
    NR.set(numeroR)
    limpiarCampos()

def resta():
    numeroA=NA.get()
    numeroB=NB.get()
    numeroR=numeroA-numeroB
    NR.set(numeroR)
    limpiarCampos()

def mul():
    numeroA=NA.get()
    numeroB=NB.get()
    numeroR=numeroA*numeroB
    NR.set(numeroR)
    limpiarCampos()

def div():
    numeroA=NA.get()
    numeroB=NB.get()
    numeroR=numeroA/numeroB
    NR.set(numeroR)
    limpiarCampos()

ventana = tk.Tk()
ventana.config(width=250,height=180)

etiquetaNA=Label(ventana,text="Número A:")
etiquetaNA.place(x=0,y=0)

NA=IntVar()
entradaNA=Entry(ventana,textvariable=NA)
entradaNA.place(x=70,y=0)


etiquetaNB=Label(ventana,text="Número B:")
etiquetaNB.place(x=0,y=30)

NB=IntVar()
entradaNB=Entry(ventana,textvariable=NB)
entradaNB.place(x=70,y=30)


etiquetaRES=Label(ventana,text="Resultado:")
etiquetaRES.place(x=90,y=90)

NR=IntVar()
salidaRES=Entry(ventana,textvariable=NR)
salidaRES.place(x=60,y=110)

botonTransportar=Button(ventana,text="SUMA", command=sumar)
botonTransportar.place(x=0,y=60)

botonTransportar=Button(ventana,text="RESTA", command=resta)
botonTransportar.place(x=50,y=60)

botonTransportar=Button(ventana,text="MULTIPLICAR", command=mul)
botonTransportar.place(x=100,y=60)

botonTransportar=Button(ventana,text="DIVIDIR", command=div)
botonTransportar.place(x=190,y=60)

ventana.mainloop()