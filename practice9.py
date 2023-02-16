# Vilma Picapiedra envía a Pedro a comprar el pan, le jamón, el queso, el tomate y la lechuga para
# hacer el almuerzo del domingo. Vilma le entregó a Pedro 10 mil colones, y regresó con 2700. Cuando
# Vilma le preguntó cuánto le costó cada cosa, Pedro le contesta que el pan le costó un 15 %, el tomate
# un 35 %, el queso y el jamón ambos un 20 % y la lechuga un 10%. Haga un programa que calcule el
# costo en colones de cada ingrediente.

def calc_proucts_price(initialMoney, finalMoney):
    print("---------------------------------------")
    print("Calculando el precio de los productos?")
    usedMoney = initialMoney - finalMoney
    bread = usedMoney * (15 / 100)
    tomatoes = usedMoney * (35 / 100)
    chesse = usedMoney * (20 / 100)
    jam = usedMoney * (20 / 100)
    lettuce = usedMoney * (10 / 100)
    print("Los precios de cada producto son los siguientes")
    print(bread)
    print(tomatoes)
    print(chesse)
    print(jam)
    print(lettuce)
    print("---------------------------------------")


calc_proucts_price(
    float(input("Con cuanta plata salio?")), float(
        input("Con cuanta plata termino?"))
)
