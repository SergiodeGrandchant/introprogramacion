# E5: Escribir un programa que lea un número por teclado y muestre una triángulo de altura equivalente al número leído.
num = int(input("Dame un numero: "))
for i in range(num):
    print("* " * (i+1))