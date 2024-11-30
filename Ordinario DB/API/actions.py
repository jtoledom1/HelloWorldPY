from conect import interacmongo
def menu(Resp):
    match Resp:
        case '1':
            interacmongo('insert_many',query=[
                {
                    "codigo": "016",
                    "nombre": "Sheldon",
                    "AP": "Cooper",
                    "AM": "Martínez",
                    "edad": 34,
                    "Telefono": ["+521234567890", "+529876543210"],
                    "Temas": ["viajes", "gastronomía", "futbol"]
                },
                {
                    "codigo": "017",
                    "nombre": "Missy",
                    "AP": "Sánchez",
                    "AM": "Ramírez",
                    "edad": 28,
                    "Telefono": ["+521111223344", "+529876512345"],
                    "Temas": ["moda", "literatura", "películas", "tecnología"]
                }
        ])
        case '2':
            interacmongo('insert_one',query=[
                {
                    "codigo": "015",
                    "nombre": "Sheldon",
                    "AP": "Cooper",
                    "AM": "Martínez",
                    "edad": 34,
                    "Telefono": ["+521234567890", "+529876543210"],
                    "Temas": ["viajes", "gastronomía", "futbol"]
                }
        ])
        case '3':
            interacmongo('insert_many',query=[
                {
                    "ident":"001",
                    "colores":["Azul","Rojo","Amarillo"],
                    "precio":23000,
                    "Existencia":12,
                    "nombre":"Cofre",
                    "Materiales":["Metal","Madera"]

                },
                {
                    "ident":"002",
                    "colores":["Azul","Rojo","Amarillo"],
                    "precio":12500,
                    "Existencia":12,
                    "nombre":"Pala",
                    "Materiales":["Hierro","Madera"]

                },
                {
                    "ident":"003",
                    "colores":["Reflejante","Polarizado","Transparente"],
                    "precio":1000,
                    "Existencia":12,
                    "nombre":"Ventana",
                    "Materiales":["Aluminio","Cristal"]
                }
                ])            
menu(input("\n\nOpción\n\n\n"))