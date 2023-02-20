def suma(a, b):
    return a + b
def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        print("Error: no se puede dividir por cero.")
        return
    return a / b
opcion = None
while opcion != 0:
    print("""
    0 Salir
    1 Sumar
    2 Restar
    3 Multiplicar
    4 Dividir
    """)
    opcion = input("Seleccione una opción: ")
    try:
        opcion = int(opcion)
        if opcion == 0:
            break
        elif opcion > 4 or opcion < 0:
            print("Opción inválida. Intente de nuevo.")
            continue
        else:
            if opcion == 1:
                print("Escogiste la opcion Suma")
                n1 = float(input("Ingrese el primer número: "))
                n2 = float(input("Ingrese el segundo número: "))
                print("El resultado es:", suma(n1, n2))

            elif opcion == 2:
                print("Escogiste la opcion Resta")
                n1 = float(input("Ingrese el primer número: "))
                n2 = float(input("Ingrese el segundo número: "))
                print("El resultado es:", resta(n1, n2))

            elif opcion == 3:
                print("Escogiste la opcion Multiplicacion")
                n1 = float(input("Ingrese el primer número: "))
                n2 = float(input("Ingrese el segundo número: "))
                print("El resultado es:", multiplicacion(n1, n2))

            elif opcion == 4:
                print("Escogiste la opcion Division")
                n1 = float(input("Ingrese el primer número: "))
                n2 = float(input("Ingrese el segundo número: "))
                print("El resultado es:", division(n1, n2))
    except ValueError:
        print("Entrada inválida. Intente de nuevo con un número.")
