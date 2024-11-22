from pymongo import MongoClient
def interacmongo(TolAct,query={}):
    try:
        client = MongoClient('localhost', 27017)
        database = client['admin']
        collection = database['Empleados_Toledotte']
        documents = collection.find()
        for document in documents:
            print(document)
        if TolAct == 'find':
            collection.find(query)
        if TolAct == 'remove':
            collection.remove(query,true)
        if TolAct == 'updateOne':
            collection.updateOne(query)
        if TolAct == 'insert_many':
            collection.insert_many(query)
    except Exception as ex:
        print("Error durante la conexión: {}".format(ex))
    finally:
        client.close()
        print("Éxito.")

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
