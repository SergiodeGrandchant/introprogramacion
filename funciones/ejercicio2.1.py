#Tabla del 1 - 10
def tablaM():
    for j in range(1, 11):
        print("Tabla del numero: ", j)
        for i in range(1, 11):
            print(j, " X ", i, " = ", i * j)

tablaM()