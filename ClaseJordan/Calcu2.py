from os import system
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[0;33m'
BLUE = '\033[0;34m'
MAGENTA = '\033[0;35m'
CYAN = '\033[0;36m'
WHITE = '\033[0;37m'
NC = '\033[0m' 

print(f"""
{CYAN}  :::::::::::       ::::::::       :::        ::::::::::       :::::::::       :::::::: 
     :+:          :+:    :+:      :+:        :+:              :+:    :+:     :+:    :+: 
    +:+          +:+    +:+      +:+        +:+              +:+    +:+     +:+    +:+  
   +#+          +#+    +:+      +#+        +#++:++#         +#+    +:+     +#+    +:+   
  +#+          +#+    +#+      +#+        +#+              +#+    +#+     +#+    +#+    
 #+#          #+#    #+#      #+#        #+#              #+#    #+#     #+#    #+#     
###           ########       ########## ##########       #########       ########       

      """)


num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
system("clear")  # Clear para mac/linux cls para Windows
print(f"EL Resultado de tu operación es: \n\n")
print(f"{YELLOW}{num1} {RED}+ {MAGENTA}{num2} {RED}= {BLUE}{num1 + num2}")
print(f"{YELLOW}{num1} {RED}- {MAGENTA}{num2} {RED}= {BLUE}{num1 - num2}")
print(f"{YELLOW}{num1} {RED}/ {MAGENTA}{num2} {RED}= {BLUE}{num1 / num2}")
print(f"{YELLOW}{num1} {RED}* {MAGENTA}{num2} {RED}= {BLUE}{num1 * num2}")
print(f"{YELLOW}{num1} {RED}^ {MAGENTA}{num2} {RED}= {BLUE}{num1 ** num2}")

