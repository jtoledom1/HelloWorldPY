from func import interacmongo

interacmongo('insert_many',query=[
            {
                "codigo": "012",
                "nombre": "Luis",
                "AP": "González",
                "AM": "Martínez",
                "edad": 34,
                "Telefono": ["+521234567890", "+529876543210"],
                "Temas": ["viajes", "gastronomía", "futbol"]
            },
            {
                "codigo": "013",
                "nombre": "Sara",
                "AP": "Jiménez",
                "AM": "Ramírez",
                "edad": 28,
                "Telefono": ["+521111223344", "+529876512345"],
                "Temas": ["moda", "literatura", "películas", "tecnología"]
            },
            {
                "codigo": "014",
                "nombre": "Carlos",
                "AP": "Pérez",
                "AM": "López",
                "edad": 45,
                "Telefono": ["+521234555666", "+529876678910"],
                "Temas": ["tecnología", "deportes", "negocios", "economía", "videojuegos"]
            }
    ])
