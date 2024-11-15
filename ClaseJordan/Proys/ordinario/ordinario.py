import time
from os import system

RED = '\033[0;31m'
CYAN = '\033[0;36m'
GREEN = '\033[0;32m'
BLUE = '\033[0;34m'
def ray():
    print(f"{CYAN}----------------------------------------")

def clar():
        system("clear")

def entrada ():
    print("")
    clar()
    print(f"""
    {CYAN}  
        :::::::::::       ::::::::       :::            ::::::::::       :::::::::       :::::::: 
            :+:          :+:    :+:      :+:            :+:              :+:    :+:     :+:    :+: 
            +:+          +:+    +:+      +:+            +:+              +:+    +:+     +:+    +:+  
            +#+          +#+    +:+      +#+            +#++:++#         +#+    +:+     +#+    +:+   
            +#+          +#+    +#+      +#+            +#+              +#+    +#+     +#+    +#+    
            #+#          #+#    #+#      #+#            #+#              #+#    #+#     #+#    #+#     
            ###           ########       ##########     ##########       #########       ########       

        """)
    
    print("Bienvenido a esta trivia, espero te diviertas y pongas a prueba tus conocimientos, esta es una breve\npero interesante serie de preguntas, tus errores se mostrarán en rojo y es muy importante que uses\nun sist operativo tipo unix, ya que de lo contrario no funcionará el programa como es debido.")
    time.sleep(3)
def mostrar_contador(frase_opner):
    time.sleep(1)
    clar()
    ray()
    print(f"{GREEN}\n" + frase_opner + "\n")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    ray()
    time.sleep(1)
    clar()

def hacer_pregunta(pregunta, opciones, respuesta_correcta, puntaje):
    ray()
    print(f"{BLUE}\n" + pregunta)
    # Este bucle for recorre la lista opciones, y para cada elemento, 
    # idx tendrá el número de índice (empezando desde 1) 
    # y opcion tendrá el valor de ese elemento.
    # de tal forma que idx es el numerito en las opciones de salida :)
    for idx, opcion in enumerate(opciones, 1):
        print(f"{CYAN}{idx}. {opcion}{BLUE}")
    
    while True:
        respuesta = input(f"{BLUE}Respuesta:{RED} ")
        
        # Validamos que la respuesta sea un número entero entre 1 y 3
        if respuesta.isdigit():
            respuesta_numero = int(respuesta)
            if 1 <= respuesta_numero <= 3:
                break
            else:
                print("Por favor, elige un número entre 1 y 3.")
        else:
            print("Por favor, ingresa un número válido entre 1 y 3.")
    
    # Comprobamos si la respuesta es correcta
    if respuesta_numero == respuesta_correcta:
        puntaje += 10
        print(f"{BLUE}Puntaje agregado =  {RED}10\n{BLUE}Total hasta ahora = {RED}{puntaje}{BLUE}")
    else:
        print(f"{BLUE}Puntaje agregado =  {RED}0\n{BLUE}Total hasta ahora = {RED}{puntaje}{BLUE}")
    ray()
    return puntaje
def main():
    puntaje = 0
    
    # Pregunta 1
    mostrar_contador("Espero hayas estudiado Geografía...")
    puntaje = hacer_pregunta(
        "¿Cuál es la capital de Rusia?", 
        ["Moscú", "Yugoslavia", "Medellín"], 
        1, 
        puntaje
    )

    # Pregunta 2
    mostrar_contador("Ahora pasemos de la Tierra al Espacio, ¿Quieres?")
    puntaje = hacer_pregunta(
        "¿Qué es considerado Plutón?", 
        ["Planeta", "Planeta enano", "Satélite de Neptuno"], 
        2, 
        puntaje
    )

    # Pregunta 3
    mostrar_contador("¡¡Bienvenido a Juegos Mentales!!")
    puntaje = hacer_pregunta(
        "¿Si 3=1, cuanto es 1*(6/2)+2?", 
        ["5", "1", "3"], 
        3, 
        puntaje
    )

    # Pregunta 4
    mostrar_contador("Hablemos de algo importante...")
    puntaje = hacer_pregunta(
        "En porcentaje, ¿Cuánta agua hay en el Planeta Tierra?", 
        ["2.5%", "70%", "60%"], 
        2, 
        puntaje
    )

    # Pregunta 5
    mostrar_contador("Demos un viaje al pasado")
    puntaje = hacer_pregunta(
        "¿Quiénes hicieron las pirámides de Egipto?", 
        ["Esclavos", "Aliens", "Trabajadores y esclavos"], 
        3, 
        puntaje
    )

    # Resultado final
    print("\n--------------------")
    mostrar_contador("Eso es to, eso es to, eso es todo amigos!!")
    print(f"Puntaje final =  {puntaje}")
    if puntaje < 30:
        print("Deberías estudiar un poco más")
    else:
        print("¡Buen trabajo!")
    
    print("¡Gracias por jugar!")

if __name__ == "__main__":
    entrada()
    main()

