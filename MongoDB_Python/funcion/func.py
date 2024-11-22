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
        if TolAct == 'insert_one':
            collection.insert_one(query)
        if TolAct == 'insert_many':
            collection.insert_many(query)
    except Exception as ex:
        print("Error durante la conexión: {}".format(ex))
    finally:
        client.close()
        print("Éxito.")

