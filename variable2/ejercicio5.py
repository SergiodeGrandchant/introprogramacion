# E5: Leer un número entero por teclado y mostrar en pantalla, para cada enunciado, si es verdadero o falso:
num = float(input("Dame un numero entero: "))

print("¿El número es igual a 5? ", num == 5)

print("¿El número es igual que 5.0?", num == 0.5)

print("¿El número es mayor que 0 y menor que 10?", num > 0 and num < 10)

if num < 0:
    print("¿El número es menor que 0? True")
elif num > 10:

    print("¿mayor que 10? True")
if num == 5:
    print("¿El número es igual a 5,? True")
elif num > 10 and num < 20:
    print("¿es mayor que 10 y menor que 20? True")
else:
    print("¿El número es igual a 5, o en caso de no serlo, si es mayor que 10 y menor que 20? False")