def multiplicacion(numero1,numero2):
    return numero1*numero2
def division(numero1,numero2):
    if numero2 == 0:
       return "infinito"

    else:
        return numero1/numero2
def suma(numero1,numero2):
    return numero1+numero2
def resta(numero1,numero2):
    return numero1-numero2
ejecutar = True

while ejecutar :

    print("\n--- CALCULADORA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elige opción: ")

    if opcion == "5":
        ejecutar = False
        print("Saliendo...")
        break

    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        print("Resultado:", suma(numero1, numero2))
    elif opcion == "2":
        print("Resultado:", resta(numero1, numero2))
    elif opcion == "3":
        print("Resultado:", multiplicacion(numero1, numero2))
    elif opcion == "4":
        print("Resultado:", division(numero1, numero2))
    else:
        print("opcion invalida")
