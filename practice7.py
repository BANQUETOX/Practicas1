# . Johns Hopkins University Center for Systems Science and Engineering lleva un recuento de la
# cantidad de casos y la cantidad de muertes a nivel mundial por el Covid-19. Haga un programa que
# reciba el nombre del país, la cantidad de enfermos, la cantidad de muertos e imprima la tasa de
# mortalidad para dicho país.
def mortality_rate(countryName, sicks, deaths):
    print(
        "--------------------------------------------------------------------------------------------------"
    )
    print(
        "Calculando la taza de mortalidad entre pacientes enfermos de covid-19 en %s"
        % countryName
    )
    mortalityRate = deaths / sicks
    print(
        "La taza de mortalidad entre los enfermos es del %f porciento en %s"
        % (mortalityRate, countryName)
    )
    print(
        "--------------------------------------------------------------------------------------------------"
    )


mortality_rate(
    input("Cual es el nombre del pais de analizis?"),
    int(input("Cuantos enfermos hay en el pais?")),
    int(input("Cuantos de los enfermos han fallecido?")),
)
