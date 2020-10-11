# https://bit.ly/36LtifW
eleccion = input("dime que operacion quieres ►SUMA◄ ►RESTA◄ ►MULTIPLICACION◄ ►DIVISION◄ ►POTENCIACION◄ ")
if eleccion == "suma":
    num1 = float(input("Dame el primer numero de la suma: "))
    num2 = float(input("Dame el segunda numero de la suma: "))
    res = num1 + num2
    print(num1, " + ", num2, "=", res)
elif eleccion == "resta":
    num1 = float(input("Dame el primer numero de la resta: "))
    num2 = float(input("Dame el segunda numero de la resta: "))
    res = num1 - num2
    print(num1, " - ", num2, "=", res)
elif eleccion == "multiplicacion":
    num1 = float(input("Dame el primer numero de la multiplicacion: "))
    num2 = float(input("Dame el segunda numero de la multiplicacion: "))
    res = num1 * num2
    print(num1, " * ", num2, "=", res)
elif eleccion == "division":
    num1 = float(input("Dame el primer numero de la division: "))
    num2 = float(input("Dame el segunda numero de la division: "))
    res = num1 / num2
    print(num1, "/", num2, "=", res)
elif eleccion == "potenciacion":
    num1 = float(input("Dame el numero de la potenciacion: "))
    num2 = float(input("Dame el  numero que elevara la potenciacion: "))
    res = num1 ** num2
    print(num1, "**", num2, "=", res)
else:
    print("Datos invalidos vuelva a ejecutar el programa si quiere realizar una operacion")