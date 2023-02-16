# Gabriel es un trabajador independiente que cobra 50 dólares por cada página web. Calcule los
# ingresos del total del mes de Gabriel. El programa recibe la cantidad de páginas web que le
# contrataron a Gabriel.

def calc_monthly_gains(websCreated):
    print("---------------------------------------------------")
    print("Calculando las ganancias del mes...")
    totalGains = websCreated * 50
    print("Ha ganado %i colones creando paginas web " % totalGains)
    print("--------------------------------------------------")


calc_monthly_gains(int(input("Cuantas paginas ha creado?")))
