print("Dados dos números enteros los voy a sumar\n\n")
while True:
	try:
		num1 = int( input("Dame un número: ") )
		break
	except:
		print("Dato incorrecto\n")
		
num2 = float( input("Dame otro número: ") )

num1 = int(num1)
num2 = int(num2)

print(f"\n{num1}+{num2}={num1+num2}")
