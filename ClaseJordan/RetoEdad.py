# Código unificado por José Diego Toledo Muñoz
# En el código tenemos 2 funciones principales calcular_edad & main
# En la función calcular edad hacemos el cálculo, dadas las especificaciones 
# Decidí leer el formato completo dd/mm/yyyy esto lo defino desde la linea 38 
# Se declara la fecha actual en la siguiente linea para poder hacer el cálculo 
# La linea 42 está dividida en 2 partes: diferencia entre años, y la verificación del mes y día ente la actual y la de nacimiento
# En main vamos a recibir los datos de la fecha y validar el formato, por parte de la verificación, tenemos ifs anidados, 
# En estos validamos la longitud, que los días estén máximo entre 1 y 31, que los meses sean 1-12
# Cabe mencionar que se hizo uso de colores para embellecer la salida del código
# Incluí una excepción en el Try pero creo que está lo suficientemente protegido para no necesitarlo, el último if simplemente manda a llamar al método main. 

from os import system
from datetime import datetime

RED = '\033[0;31m'
YELLOW = '\033[0;33m'
CYAN = '\033[0;36m'

print(" ")#Este print junto con el system clear inicializa la consola en 0.
system("cls")
print(f"""
{CYAN}  :::::::::::       ::::::::       :::        ::::::::::       :::::::::       :::::::: 
     :+:          :+:    :+:      :+:        :+:              :+:    :+:     :+:    :+: 
    +:+          +:+    +:+      +:+        +:+              +:+    +:+     +:+    +:+  
   +#+          +#+    +:+      +#+        +#++:++#         +#+    +:+     +#+    +:+   
  +#+          +#+    +#+      +#+        +#+              +#+    +#+     +#+    +#+    
 #+#          #+#    #+#      #+#        #+#              #+#    #+#     #+#    #+#     
###           ########       ########## ##########       #########       ########       

      """)
print(f"\n\n\t\t{YELLOW} Calculadora-Edad\n\n")

def calcular_edad(fecha_nacimiento):
    # Convertir la cadena de fecha en un objeto datetime
    nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
    hoy = datetime.now()
    
    # Calcular la edad
    edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
    return edad

def main():
    fecha_nacimiento = input("Por favor, ingresa tu fecha de nacimiento (dd/mm/yyyy): ")

# Validar que tenga 10 caracteres
    if len(fecha_nacimiento) != 10:
        system("cls")
        print(f"{RED}La fecha debe tener 10 caracteres en el formato dd/mm/yyyy.")
    else:
        # Verificar el formato dd/mm/yyyy
        if fecha_nacimiento[2] == '/' and fecha_nacimiento[5] == '/':
            dia = int(fecha_nacimiento[:2])
            mes = int(fecha_nacimiento[3:5])
            
            # Verificar que el día esté entre 1 y 31
            if 1 <= dia <= 31:
                # Verificar que el mes esté entre 1 y 12
                if 1 <= mes <= 12:
                    print("")
                else:
                    print(f"{RED}El mes no es válido. Debe estar entre 1 y 12.")
            else:
                print(f"{RED}El día no es válido. Debe estar entre 1 y 31.")
        else:
            print(f"{RED}El formato de la fecha es incorrecto. Debe ser dd/mm/yyyy.")


    # Intentar calcular la edad
    try:
        edad = calcular_edad(fecha_nacimiento)
        print(f"Tienes {edad} años.")
    except ValueError:
        print("La fecha ingresada no es válida. Asegúrate de usar el formato dd/mm/yyyy.")

if __name__ == "__main__":
    main()