# E6: Escribir un programa que determine si un año es bisiesto (tiene366 días). Para ser bisiesto debe ser divisible entre 4 no se ser divisible entre 100, excepto que también sea divisible entre 400
año = int(input("¿En que año estas? "))
if año%4 == 0:
    if año%100 == 0:
        if año%400 == 0:
            print("El año que elegiste es una año bisiesto")
        else:
            print("El año no es bisiesto")
    else:
        print("El año es bisiesto")
else:
    print("El año no es bisiesto")