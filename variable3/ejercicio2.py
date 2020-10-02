# E2: Leer dos números enteros por teclado y mostrar el mayor de los dos por pantalla
num1 = float(input("Dame el primer numero: "))
num2 = float(input("Dame el segundo numero: "))
if num1 > num2:
    print(num1, "es mayor que: ", num2)
elif num1 < num2:
    print(num1, "es menor que: ", num2)
else:
    print(num1, "es igual que: ", num2)