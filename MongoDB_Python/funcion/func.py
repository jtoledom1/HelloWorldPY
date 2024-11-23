from pymongo import MongoClient
def interacmongo(TolAct,query={}):
    try:
        client = MongoClient('localhost', 27017)
        database = client['admin']
        collection = database['Empleados_Toledotte']
        documents = collection.find()
        for document in documents:
            print(document)

        match TolAct:
            case 'find':
                collection.find(query)
            case 'remove':
                collection.remove(query, True)
            case 'updateOne':
                collection.updateOne(query)
            case 'insert_many':
                collection.insert_many(query)
            case 'insertOne':
                collection.insert_one(query)
            case _:
                print("Acción no reconocida")

    except Exception as ex:
        print("Error durante la conexión: {}".format(ex))
    finally:
        client.close()
        print("Éxito.")

