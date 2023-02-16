# Felipe es un programador que debe marcar todos lo días la hora de entrada y la hora de salida. Haga
# un programa que, recibiendo la tarifa por hora, imprima el total de dinero que Felipe recibió en ese día
# y la cantidad de horas que trabajó.
def calc_hours_worked_and_gains(entryHour, exitHour, moneyRate):
    print("-------------------------------------------")
    if entryHour > 24:
        print("Hora invalida")
    if exitHour > 24:
        print("Hora invalida")

    print("Calculando las ganacias de hoy...")
    totalHoursWorked = exitHour - entryHour
    totalGains = moneyRate * totalHoursWorked
    print("Usted ha ganado %i colones hoy" % totalGains)
    print("-------------------------------------------")


calc_hours_worked_and_gains(
    int(input("A que hora entro al trabajo? (formato 24horas)")),
    int(input("A que hora salio del trabajo? (formato 24horas)")),
    int(input("Cuanto le pagan por hora?")),
)
