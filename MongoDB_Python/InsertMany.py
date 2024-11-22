from pymongo import MongoClient
try:
    client = MongoClient('localhost', 27017)
    database = client['admin']
    collection = database['Empleados_Toledotte']
    documents = collection.find()

    collection.insert_many([
            {
                "codigo": "007",
                "nombre": "Luis",
                "AP": "González",
                "AM": "Martínez",
                "edad": 34,
                "Telefono": ["+521234567890", "+529876543210"],
                "Temas": ["viajes", "gastronomía", "futbol"]
            },
            {
                "codigo": "008",
                "nombre": "Sara",
                "AP": "Jiménez",
                "AM": "Ramírez",
                "edad": 28,
                "Telefono": ["+521111223344", "+529876512345"],
                "Temas": ["moda", "literatura", "películas", "tecnología"]
            },
            {
                "codigo": "009",
                "nombre": "Carlos",
                "AP": "Pérez",
                "AM": "López",
                "edad": 45,
                "Telefono": ["+521234555666", "+529876678910"],
                "Temas": ["tecnología", "deportes", "negocios", "economía", "videojuegos"]
            }
    ]

    )

    for document in documents:
        print(document)

except Exception as ex:
    print("Error durante la conexión: {}".format(ex))
finally:
    client.close()
    print("Éxito.")