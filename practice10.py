# Una línea aérea pone en promoción los viajes a África. La promoción indica que el costo del tiquete
# tendrá una rebaja del 15 %. Imprima el costo real del tiquete si el programa recibe el precio original
# del mismo.

def calc_ticket_price(ticketPrice):
    print("-----------------------------------------------------")
    print("Calculando el precio final del tiquete")
    discount = ticketPrice * (15 / 100)
    finalPrice = ticketPrice - discount
    print("El precio final del tickete es de %f" % finalPrice)
    print("-------------------------------------------------------")


calc_ticket_price(1000)
