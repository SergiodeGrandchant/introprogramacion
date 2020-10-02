# E4: Debido a la actual escasez de agua, la empresa COSAALT ha decidido penalizar el consumo excesivo de agua incrementando el precio según la cantidad consumida. Escribir un programa que calcule el monto a pagar considerando la siguiente escala de precios:
agua = float(input("Ingrese el consumo de agua en m**3 de la person: "))
if agua < 100:
    print("La persona debe pagar: ", (agua * 1), "Bs")
elif agua >= 100 and agua <= 499:
    print("La persona debe pagar: ", (agua * 1.20), "Bs")
elif agua >= 500 and agua <= 999:
    print("La persona debe pagar: ", (agua * 1.50), "Bs")
else:
    print("La persona debe pagar: ", (agua * 2), "Bs")
