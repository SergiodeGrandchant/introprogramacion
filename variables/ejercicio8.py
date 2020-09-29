# E8: Escribir un programa que lea del teclado un monto a invertir, el interés anual y el número de años a invertir. Mostar en pantalla la ganancia neta generada por la inversión. Utilizar la formula para calcular el interés compuesto.
# mi = monto inicial
mi = float(input("¿Con cuanta plata estas invirtiendo? "))
# ts = tasa de interes
ts = float(input("¿Cual es la tasa de interes en donde vas a invertir? "))
# pa = periodo de ahorro
pa = float(input("¿Cuantos años vas a invertir? "))
# mf = monto final (ganacia neta)
mf = mi*(1+ts)**pa
print("la ganacia neta es de: ", mf)