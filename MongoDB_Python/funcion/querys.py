from func import interacmongo
def menu(Resp):
    match Resp:
        case 'insert_many':
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
        case 'insertOne':
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
menu(input("\n\nOpción\n\n\n"))