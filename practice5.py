# Hugo, Paco y Luis decidieron vender limonada en el barrio. Decidieron cobrar por cada limonada 10
# colones debido a que fabricar cada limonada les cuesta 5.50 colones. Como no todos trabajaron por
# igual, decidieron que las ganancias se iban a repartir de la siguiente forma 30 % para Paco, 30 %
# para Luis y 40 % para Hugo. Haga un programa que reciba la cantidad total de limonadas que
# vendieron, e imprima cuánto ganó Hugo, cuánto ganó Paco y cuánto ganó Luis.

def limonade_gains(sells):
    print("-------------------------------")
    print("Calculando las ganacias de cada vendedor")
    totalGains = sells * 10
    hugoGains = totalGains * 0.4
    pacoGains = totalGains * 0.3
    luisGains = totalGains * 0.3
    print("Total de ganacias: %i" % totalGains)
    print("Hugo debe recibir %i del total de ganancias" % hugoGains)
    print("Paco debe recibir %i del total de ganancias" % pacoGains)
    print("Luis debe recibir %i del total de ganancias" % luisGains)
    print("--------------------------------")


limonade_gains(int(input("Cuantas ventas de realizaron?")))
