
def vocal(letra):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        print(letra, " = es una vocal")
    else:
        print(letra, " = es una consonante")

letra = input("Dame una letra: ")
vocal(letra)