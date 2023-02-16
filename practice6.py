# Con la situación del Covid-19, el Gobierno decidió poner un impuesto al salario bruto de todos los
# trabajadores. Haga un programa que reciba el porcentaje de impuesto y el salario bruto de un
# trabajador, e imprima lo que le queda luego de rebajar el impuesto.
def calc_taxes(salary, taxPercentaje):
    print("--------------------------------------------------------------")
    print("Calculando el salario despues de pagar el impuesto...")
    decimalTax = taxPercentaje / 100
    finalTax = salary * decimalTax
    finalSalary = salary - finalTax
    print("Usted debe pagar %f colones de impuestos" % finalTax)
    print("Despues de pagar el impuesto le quedan %f de su salario" % finalSalary)
    print("--------------------------------------------------------------")


calc_taxes(
    float(input("Cual es su salario?")),
    int(input("Cual es el porcentaje del impuesto?")),
)
