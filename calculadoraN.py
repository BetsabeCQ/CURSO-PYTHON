def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    return a / b
def validaCero(divisor):
    if (divisor == 0):
        print("Error: El divisor no puede ser cero.")
        return leerEntero("  Nuevo divisor (0 para salir):")
    else:
        return divisor

def leerEntero(mensaje):
    contador = 0
    while contador < 3:
        try:
            return int(input(mensaje))
            # break;
        except:
            print(":El numero entero no es valido. ")
            contador = contador + 1
    print("Usted excedió los intentos validos, regresará al menu")
    print("")
    return None

def menu():
    print("0- Salir")
    print("1- Suma")
    print("2- Resta")
    print("3- Multiplicacion")
    print("4- Division")
    return leerEntero("  >> Por favor ingrese una opcion:")

def main():
    while True:
        opcion = menu()
        if (opcion == 0):
            break
        else:
            match(opcion):
                case 1:
                    print("Escogiste la opcion Suma")
                    num1 = leerEntero("Ingresar Numero 1: ")
                    if num1 is None:
                        print("Valor ingresado no válido")
                        continue
                    num2 = leerEntero("Ingresar Numero 2: ")
                    if num2 is None:
                        print("Valor ingresado no válido")
                        continue
                    print("El resultado de Numero 1 y Numero 2 es de:",suma(num1,num2))
                case 2:
                    print("Escogiste la opcion Resta")
                    num1 = leerEntero("Ingrese Numero 1: ")
                    if num1 is None:
                        print("Valor ingresado no válido")
                        continue
                    num2 = leerEntero("Ingrese Numero 2: ")
                    if num2 is None:
                        print("Valor ingresado no válido")
                        continue
                    print("El resultado de Numero 1 y Numero 2 es de:", resta(num1, num2))
                case 3:
                    print("Escogiste la opcion Multiplicacion")
                    num1 = leerEntero("Ingrese Numero 1: ")
                    if num1 is None:
                        print("Valor ingresado no válido")
                        continue
                    num2 = leerEntero("Ingrese Numero 2: ")
                    if num2 is None:
                        print("Valor ingresado no válido")
                        continue
                    print("El resultado de Numero 1 y Numero 2 es de:", multiplicacion(num1, num2))
                case 4:
                    print("Escogiste la opcion Division")
                    num1 = leerEntero("Ingrese Numero 1: ")
                    if num1 is None:
                        print("Valor ingresado no Válido")
                        continue
                    num2 = validaCero(leerEntero("Ingrese numero 2: "))
                    if num2 is None:
                        print("Valor ingresado no Válido")
                        continue
                    if (num2 != 0):
                        print(division(num1, num2))
                    else:
                        print("El divisor sigue siendo cero. Regresando al menu.")


main()