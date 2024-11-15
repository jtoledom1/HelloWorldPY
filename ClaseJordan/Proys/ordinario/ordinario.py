import time
from os import system
def entrada ():
    CYAN = '\033[0;36m'
    print("")
    system("clear")
    print(f"""
    {CYAN}  
    :::::::::::       ::::::::       :::        ::::::::::       :::::::::       :::::::: 
        :+:          :+:    :+:      :+:        :+:              :+:    :+:     :+:    :+: 
        +:+          +:+    +:+      +:+        +:+              +:+    +:+     +:+    +:+  
        +#+          +#+    +:+      +#+        +#++:++#         +#+    +:+     +#+    +:+   
        +#+          +#+    +#+      +#+        +#+              +#+    +#+     +#+    +#+    
        #+#          #+#    #+#      #+#        #+#              #+#    #+#     #+#    #+#     
        ###           ########       ########## ##########       #########       ########       

        """)
    
entrada()

def mostrar_contador():
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

def hacer_pregunta(pregunta, opciones, respuesta_correcta, puntaje):
    print("\n" + pregunta)
    for idx, opcion in enumerate(opciones, 1):
        print(f"{idx}. {opcion}")
    
    respuesta = input("Respuesta: ")
    if respuesta.isdigit() and int(respuesta) == respuesta_correcta:
        puntaje += 10
        print(f"Puntaje agregado =  10\nTotal hasta ahora =  {puntaje}")
    else:
        print(f"Puntaje agregado =  0\nTotal hasta ahora =  {puntaje}")
    
    return puntaje

def main():
    puntaje = 0
    
    # Pregunta 1
    mostrar_contador()
    puntaje = hacer_pregunta(
        "¿Cuál es la capital de Rusia?", 
        ["Moscú", "Yugoslavia", "Medellín"], 
        1, 
        puntaje
    )

    # Pregunta 2
    mostrar_contador()
    puntaje = hacer_pregunta(
        "¿Qué es considerado Putón?", 
        ["Planeta", "Planeta enano", "Satélite de Neptuno"], 
        2, 
        puntaje
    )

    # Pregunta 3
    mostrar_contador()
    puntaje = hacer_pregunta(
        "¿Si 3=1, cuanto es 1*(6/2)+2?", 
        ["5", "1", "3"], 
        3, 
        puntaje
    )

    # Pregunta 4
    mostrar_contador()
    puntaje = hacer_pregunta(
        "En porcentaje, ¿Cuánta agua hay en el Planeta Tierra?", 
        ["2.5%", "70%", "60%"], 
        2, 
        puntaje
    )

    # Pregunta 5
    mostrar_contador()
    puntaje = hacer_pregunta(
        "¿Quiénes hicieron las pirámides de Egipto?", 
        ["Esclavos", "Aliens", "Trabajadores y esclavos"], 
        3, 
        puntaje
    )

    # Resultado final
    print("\n--------------------")
    mostrar_contador()
    print(f"Puntaje final =  {puntaje}")
    if puntaje < 30:
        print("Deberías estudiar un poco más")
    else:
        print("¡Buen trabajo!")
    
    print("¡Gracias por jugar!")

if __name__ == "__main__":
    main()

