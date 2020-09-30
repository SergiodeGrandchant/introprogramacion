# E9: Leer el día, mes y año de nacimiento del usuario de la entrada y mostrar un mensaje indicando si el usuario es mayor de 18 años o no
cumple = input("¿cuando es tu cumpleaños? ")
# a = años cuando nacio
a = int(input("¿En que año naciaste? "))
# aa = año actual
aa = int(input("¿En que año estas? "))
edad = (aa-a)

if edad >= 18:
    print("El usuario en mayor de edad con ", edad, "años")
else:
    print("el usuario es menor de e edad con ", edad, "años")