# ********************************
# CLASES
class Perro:
    # Constructor
    def __init__(self, raza="electrico", color="marrón", trompa="chata", cola="larga"):
        self.raza = raza
        self.color = color
        self.trompa = trompa
        self.cola = cola

    # Métodos
    def mostrar(self, nombre):
        print(f"""
        {nombre}
        raza = {self.raza}
        color = {self.color}
        trompa = {self.trompa}
        cola = {self.cola}
        """)
    
# ********************************
# PRINCIPAL
solovino = Perro("Doberman","negro","alargada","corta")
el_dogo  = Perro(color="verde", cola="corta")
la_cuquis = Perro(raza="Coquer", color="blanco con café")

# Mostramos las instancias
solovino.mostrar("Solovino")
el_dogo.mostrar("El Dogo")
la_cuquis.mostrar("La Cuquis")

