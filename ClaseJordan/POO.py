# ********************************
# CLASES
class Perro:
    # Atributos
    raza = "eléctrico"
    color = "marrón"
    trompa = "chata"
    cola = "larga"

    # Constructor
    def __init__(self,raza,color,trompa,cola):
        self.raza = raza
        self.color = color
        self.trompa = trompa
        self.cola = cola

# ********************************
# PROCEDIMIENTOS y FUNCIONES
def mostrar(cual,nombre):
    # cual es el objeto, ¿cuál perrito?
    # nommbre real del perrito
    print(f"""
    {nombre}
    raza = {cual.raza}
    color = {cual.color}
    trompa = {cual.trompa}
    cola = {cual.cola}
    """)
    
# ********************************
# PRINCIPAL
solovino = Perro("Doberman","Negro","Alargada","Corta")
el_dogo  = Perro
la_cuquis = Perro

# Mostramos las instancias
mostrar(solovino, "Solovino")
mostrar(el_dogo, "El Dogo")
mostrar(la_cuquis, "La Cuquis")
