# Calcular el precio final de cualquier producto, si se sabe que la tasa de impuesto al valor agregado es
# de un 13 %. El algoritmo debe recibir el nombre del producto y el precio, y debe imprimir el nombre
# del producto y el precio final. Para los efectos del ejercicio, TODOS los productos pagan impuesto.


def calc_final_price(productName, productPrice):
    print("Calculando precio final de acuerdo al IVA ...")
    print("IVA actual: 13%")
    iva = productPrice * 0.13
    finalPrice = productPrice + iva
    print("Su producto: %s" % productName)
    print("Tiene un valor final de: %f" % finalPrice)
    print("Que hecho mierda ah?")


productName = input("Como se llama su producto?")
productPrice = float(input("Cual es el valor del producto?"))

calc_final_price(productName, productPrice)
