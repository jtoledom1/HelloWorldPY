# *****************************
# FUNCIONES y PROCEDIMIENTOS
def encabezado():
	print(r"""

      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)  Felix Lee 
    """)
    print("Dados dos números enteros los voy a sumar\n\n")
    
	
def pedirNumero(arg):
	while True:
		try:
			num = int( input(arg) )
			break
		except:
			print("Dato incorrecto\n")
	return num
	
# *****************************
# PRINCIPAL
encabezado()
num1 = pedirNumero("Dame un número: ")
num2 = pedirNumero("Dame otro número: ")
print(f"\n{num1}+{num2}={num1+num2}")
