def Pedir():
    global fun  # Declara que 'fun' es una variable global
    fun = "eee"  # Asigna el valor a la variable global

def dar():
    print(fun)  # Imprime la variable global 'fun'

Pedir()
dar()
