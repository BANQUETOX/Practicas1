# Encontrar la edad de Ana dentro de diez años, si la edad de Ana es dos veces la edad de Elena. El
# programa recibe como entrada la edad actual de Elena, y debe imprimir la edad de Ana dentro de
# diez años.
def find_ana_age_in_10_years(elenaAge):
    print("---------------------------------------------")
    print("Calculando la edad de Ana dentro de 10 años")
    anaAge = (elenaAge * 2) + 10
    print("Ana tendra %i años dentro de 10 años" % anaAge)
    print("---------------------------------------------")


elenaAge = int(input("Que edad tiene Elena ahora?"))

find_ana_age_in_10_years(elenaAge)
