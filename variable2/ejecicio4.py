# E4: Leer dos números por teclado y mostrar en pantalla, para cada enunciado, si es verdadero o falso: • Los dos números son iguales • Los dos números son diferentes • El primer número es mayor al segundo • El primer número es menor o igual al segundo
num1 = int(input("dame el primer numero: "))
num2 = int(input("Dame el segundo numero: "))
print("¿Los dos números son iguales? ", num1 == num2)
print("¿Los dos números son diferentes?", num1 != num2)
print("¿El primer número es mayor al segundo?", num1 > num2)
print("¿El primer número es menor o igual al segundo?", num1 < num2)
