from pymongo import MongoClient
import json

masopciones=False
masopciones1=False

def menuopciones(op1,op2,op3):
    print("Ingrsa el número de la opción que desees realizar")
    print(f"""
        1. {op1}
        2. {op2}
        3. {op3} 
        """)
    op=input(" ")
    return op
def interacmongo(collection_inter,TolAct,query={},query2={}):
    try:
        client = MongoClient('localhost', 27017)
        database = client['MedicalTumbete']
        collection = database[collection_inter]
        documents = collection.find()
        
        for document in documents:
            print(document)

        match TolAct:
            case 'find':
                collection.find(query)
            case 'remove':
                collection.delete_one(query)
            #Modificar
            case 'updateOne':
                collection.update_one(query,query2)
            case 'insertOne':
                collection.insert_one(query)
            #Sólo admin    
            case 'insertMany':
                collection.insert_many(query)

            case _:
                print("Acción no reconocida")

    except Exception as ex:
        print("Error durante la conexión: {}".format(ex))
    finally:
        client.close()
        print("Éxito.")

def queryaddusr():
    usrvar = input("Ingresa usuario: ")
    passvar = input("Ingresa password: ")
    rolvar = input("Ingresa rol: ")
    query = {
        "nom_user": usrvar,
        "password": passvar,
        "rol": rolvar
    }    
    
    y=json.dumps(query)
    print(y)
    
    return query

def querydelusr():
    usrvar = input("Ingresa usuario: ")
    query={
        "nom_user":usrvar
    }
    y=json.dumps(query)
    print(y)

    return query

def queryupdusr1():
    usrvar = input("Ingresa usuario: ")
    query={
        "nom_user":usrvar
    }
    y=json.dumps(query)
    print(y)

    return query

def queryupdusr2():
    
    opc=menuopciones("Nombre","Password","Rol")
    match opc:
        case'1':
            print("A continuación introduce el nuevo nombre")
            usrvar = input("Nuevo nombre de usuario: ")
            query2={'$set':{"nom_user":usrvar}}
        case'2':
            print("A continuación introduce la nueva contraseña")
            usrvar = input("Nueva pass: ")
            query2={'$set':{"password":usrvar}}
        case'3':
            print("A continuación introduce el nuevo Rol")
            usrvar = input("Nuevo rol: ")
            query2={'$set':{"rol":usrvar}}            
    return query2

def queryaddcit(idmed):
    idusr = input("Ingresa el nombre del paciente")
    fech = input("Ingresa la fecha con el tipo yyyy-mm-dd/hh:mm:ss")
    query={
        "nom_user":idusr,
        "id_medico": idmed,
        "fecha_hora": fech
    }
    y=json.dumps(query)
    print(y)
    
    return query

def querydelcit(idmed):
    opc=input("Quieres ver las citas de un paciente y/n ")
    if opc=='y':
        idusr = input("Ingresa el nombre del paciente ")
        interacmongo("Citas","find",{'nom_user':idusr})
    fech = input("Ingresa la fecha con el tipo yyyy-mm-dd/hh:mm:ss")
    query={
        '_id':''
    }
    y=json.dumps(query)
    print(y)
    
    return query

def filtroupdcit():
    print("Qué quieres modificar?")
    filtnom=input(menuopciones("Usuario","Medico","fecha"))
    match filtnom:
        case'1':
            upd=input("Nuevo valor para usuario: ")
            query={'$set':{'nom_user':upd}}
        case'2':
            upd=input("Nuevo valor para médico (id): ")
            query={'$set':{'id_medico':upd}}
        case'3':
            upd=input("Nuevo valor para fecha y hora: ")
            query={'$set':{'fecha_hora':upd}}
    return query

def query2updcit():
    print("Estás en la opción modificar")
    print("ingresa el id de la cita que deseas")



################################################
#               PARTE OPERATIVA                #
################################################

opsel=menuopciones("Médico","Usuario","Admin")
match opsel:
    case'1':
        opsmed=menuopciones("Citas","Recetas","Diagnóstico")
        match opsmed:
            case'1':
                opsmedcit=menuopciones("Crear","Borrar","Modificar")
                match opsmedcit:
                    case'1':
                        addcit = queryaddcit('674d667692be37f7692bb3ae')
                        interacmongo("Citas","InsertOne",addcit)
                    case'2':
                        addcit = queryaddcit('674d667692be37f7692bb3ae')
                        interacmongo("Citas","remove",addcit)
                    case'3':
                        filtroupd=filtroupdcit()
                        
            case'3':
                opsmeddia=menuopciones("Crear","Cancelar","Modificar")

    case'2':
        opsusr=menuopciones("Citas", "Recetas", "Diagnóstico")
        match opsusr:
            case '1':
                print("")
                
    case'3':
        opsadm=menuopciones("Cear usuario","Borrar usuario","Modificar usuario")    
        match opsadm:
            case'1':
                Insrt=queryaddusr()
                interacmongo("Usuario","insertOne",Insrt)
            case'2':
                filtro=querydelusr()
                interacmongo("Usuario","remove",filtro)

            case'3':
                filtro=queryupdusr1()
                nuevodato=queryupdusr2()
                interacmongo("Usuario","updateOne",filtro,nuevodato)

