# Encontrar la edad de la abuela de Ana a hoy, si es 7 años menor que el abuelo de Ana, y en el año
# del matrimonio, el abuelo tenía 25 años. El programa recibe como entrada el año del matrimonio.

def find_gandma_years_today(marriageYear, presentYear):
    print("-------------------------------------------------------")
    print("Calculando la edad de la abuela de Ana ...")
    grandpaAge = (presentYear - marriageYear) + 25
    grandmaAge = grandpaAge - 7
    print("La abuela de Ana tiene %i años" % grandmaAge)
    print("-------------------------------------------------------")


marriageYear = int(input("Que año se casaron los abuelos de Ana?"))
presentYear = int(input("En que años estamos"))
find_gandma_years_today(marriageYear, presentYear)
