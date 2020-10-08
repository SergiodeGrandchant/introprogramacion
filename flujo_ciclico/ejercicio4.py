# E4: Escribir un programa que calcule la suma de todos los números entre 1 y un número ingresado por teclado.
num = int(input("Dame un numero entero "))
suma = 0
for i in range(1,num+1):
    suma = suma+ num
    print(i)
print(suma)