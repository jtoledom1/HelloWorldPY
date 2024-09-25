#esto es un comentario 
# Todo producto de la función input es una cadena

print("Ingresa la información...")
anything = input()
print("Tu información fué: ", anything, "¿verdad?")

# Para hacer operaciones con lo ingresado por el usuario se debe de modificar
#con la finalidad de ser entendido como un número P/E

an = float(input("Inserta un número: "))
Smt= an ** 2.0
print(anything, "al cuadrado es", Smt)

# La función type nos arroja el tipo de dato que se encuentra dentro de nuestra variable

x = input("Ingresa un número: ") # El usuario ingresa un 2 
# A pesar de haber introducido un número la respuesta será que es un string porque no se transformó a número
# Toda entrada de input sin transformar, es directamente un string
print(type(x))
