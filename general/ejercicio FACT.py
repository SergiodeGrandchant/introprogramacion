def factorial ():
    num = int(input("Dame el numero al que quieras sacar el factorial: "))
    factorial = []
    for i in range(1,20+1):
        numres = str(i) + "!"
        factorial.append(numres)
    print(factorial)

    mul = 1
    while num > 1:
        mul = num * mul
        num = num-1
        print("El FACT DE ", num, " es: ", mul)

factorial()
