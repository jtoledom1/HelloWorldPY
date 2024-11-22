from pymongo import MongoClient
try:
    client = MongoClient('localhost', 27017)
    database = client['admin']
    collection = database['Empleados_Toledotte']
    documents = collection.find()
    for document in documents:
        print(document)

except Exception as ex:
    print("Error durante la conexión: {}".format(ex))
finally:
    client.close()
    print("Éxito.")