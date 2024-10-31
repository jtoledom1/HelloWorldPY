from os import system 
system("clear")

def mostrar_menu():
    print("\t\t\nSeleccione una opción\n")
    print("1. Multiplicar")
    print("2. Dividir")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()  
        
        opcion = input("Ingrese su opción (1/2/3): ")

        if opcion == '3':
            print("Saliendo del programa. ¡Adiós!")
            break

        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            system("clear")

        except ValueError:
            print("Por favor, ingrese números válidos.")
            continue

        if opcion == '1':
            resultado = num1 * num2
            print(f"El resultado de {num1} multiplicado por {num2} es: {resultado}")

        elif opcion == '2':
            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
            else:
                resultado = num1 / num2
                print(f"El resultado de {num1} dividido por {num2} es: {resultado}")

        else:
            print("Seleccione 1, 2 o 3.")

if __name__ == "__main__":
    main()
