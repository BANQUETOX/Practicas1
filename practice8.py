# El costo de un automóvil nuevo viene dado por la suma total del costo del vehículo, el porcentaje de
# ganancia del vendedor y de los impuestos. Si el porcentaje del vendedor es de un 10 % y el impuesto
# del 30%, diseñe un algoritmo que permita leer el costo del automóvil e imprimir el costo final para el
# consumidor.

def get_car_price(carPrice):
    print("------------------------------------")
    print("Calculando el precio final del auto...")
    vendorGains = carPrice * (10 / 100)
    taxes = carPrice * (30 / 100)
    finalcarCost = carPrice + taxes + vendorGains
    print("El precio final es de %f colones" % finalcarCost)
    print("------------------------------------")


get_car_price(10000000)
