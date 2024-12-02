from pymongo import MongoClient
try:
    client = MongoClient('localhost', 27017)
    database = client['admin']
    collection = database['toleletee']
    documents = collection.find()
        
    for document in documents:
        print(document)
    Ins3rt = [
    {
        "ident":"006",
        "colores":["Azul","Rojo","Amarillo"],
        "precio":23000,
        "Existencia":12,
        "nombre":"Azada",
        "Materiales":["Metal","Madera"]

    },
    {
        "ident":"007",
        "colores":["Azul","Rojo","Amarillo"],
        "precio":12500,
        "Existencia":12,
        "nombre":"Pico",
        "Materiales":["Hierro","Madera"]

    }
]
    
    
    def insertmani():
        resultado=collection.insert_many(Ins3rt)
    
    def updatmany():
        filtro={'nombre':'Ventana'}
        nuevo_valor={'$set':{'Existencia':6}}
        resultado=collection.update_many(filtro, nuevo_valor)
        print(f'Documentos actualizados: {resultado.modified_count}')
    
    def addupmany():
        filtro={'nombre':'Cofre'}
        nuevo_dato={'$set':{'precioventa':74500}}    
        resultado=collection.update_one(filtro, nuevo_dato)
        print(f'Documentos actualizados: {resultado.modified_count}')

    #addupmany()
    def delet3():
        filtro={'ident':"002"}
        resultado=collection.delete_many(filtro) 
        print(f'Documentos eliminados: {resultado.deleted_count}')
    #delet3()

except Exception as ex:
    print("Error durante la conexión: {}".format(ex))
finally:
    client.close()
    print("Éxito.")


