
def cantidadBM(mont,billete):
    cantB = mont//billete
    if billete >= 10:
        print("Billete de ", billete, " = ", cantB)
    else:
        print("Moneda de   ", billete, " = ", cantB)
    mont = mont % billete
    return mont


monto = int(input(" Dame el monto a fraccionar: "))
monto = cantidadBM(monto,100)
monto = cantidadBM(monto,50)
monto = cantidadBM(monto,20)
monto = cantidadBM(monto,10)
monto = cantidadBM(monto,5)
monto = cantidadBM(monto,2)
monto = cantidadBM(monto,1)

