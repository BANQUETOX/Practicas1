# Calcular la cantidad de kilómetros de un viaje realizado en carro. El algoritmo debe recibir el
# kilometraje del vehículo antes de iniciar el viaje, y el kilometraje del vehículo al terminar el viaje. Se
# debe imprimir el total de kilómetros del viaje.

def calc_kilometers(initialKilometers, finalKilometers):
    print("------------------------------------------------------------")
    print("Calculando distancia del viaje ...")
    totalTraveled = finalKilometers - initialKilometers
    print("Usted viajo un total de: %f km" % totalTraveled)
    print("------------------------------------------------------------")


initialKilometers = float(
    input("Cuanto marcaba el kilometraje de su vehiculo antes de inicial el viaje?")
)
finalKilometers = float(
    input("Cuanto marcaba el kilometraje de su vehiculo al finalizar el viaje?")
)

calc_kilometers(initialKilometers, finalKilometers)
