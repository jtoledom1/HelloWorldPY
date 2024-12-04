from pymongo import MongoClient
import json
from datetime import date

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
    return query

def querydelcit(idmed):
    opc=input("Quieres ver las citas de un paciente y/n ")
    if opc=='y':
        idusr = input("Ingresa el nombre del paciente: ")
        interacmongo("Citas","find",{'nom_user':idusr})
    fech = input("Ingresa la fecha con el tipo yyyy-mm-dd/hh:mm:ss")
    query={
        '_id':''
    }
    y=json.dumps(query)
    print(y)
    
    return query

def query2updcit():
    print("Estás en la opción modificar\n")
    opc=input("Quieres ver las citas de un paciente y/n ")
    if opc=='y':
        idusr = input("Ingresa el nombre del paciente: ")
        interacmongo("Citas","find",{'nom_user':idusr})

    print("ingresa el id de la cita que deseas modificar")
    id=input("_id: ")
    query2upd={
        "_id":id
    }
    return query2upd

def filtroupdcit():
    print("Qué quieres modificar de la cita?")
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

def crear_registro():
    print("Estás en la opción de crear un nuevo registro.")
    
    id_paciente = input("Ingresa el ID del paciente: ")
    id_medico = input("Ingresa el ID del médico: ")
    
    # Medicamentos (puede haber más de uno)
    medicamentos = []
    while True:
        medicamento = {}
        medicamento["nombre"] = input("Nombre del medicamento: ")
        medicamento["dosis"] = input("Dosis del medicamento: ")
        medicamento["frecuencia"] = input("Frecuencia del medicamento: ")
        medicamentos.append(medicamento)
        
        otra = input("¿Deseas ingresar otro medicamento? (s/n): ")
        if otra.lower() != 's':
            break
    
    # Tratamiento (con diagnóstico y pruebas)
    tipo_diagnostico = input("Tipo de diagnóstico: ")
    descripcion = input("Descripción del diagnóstico: ")
    pruebas_realizadas = input("Pruebas realizadas (separadas por coma): ").split(",")
    fecha_diagnostico = input("Fecha del diagnóstico (AAAA-MM-DD): ")

    # Crear el objeto completo con la estructura dada
    nuevo_registro = {
        "id_Paciente": id_paciente,
        "id_Medico": id_medico,
        "medicamentos": medicamentos,
        "fecha_emision": str(date.today()),  # Fecha actual
        "diagnostico_asociado": descripcion,
        "Tratamiento": {
            "tipo_diagnostico": tipo_diagnostico,
            "descripcion": descripcion,
            "pruebas_realizadas": pruebas_realizadas,
            "fecha_diagnostico": fecha_diagnostico
        }
    }
    
    # Inserción en la base de datos
    interacmongo("Registros", "insertOne", nuevo_registro)
    
def leer_registro():
    print("Estás en la opción de leer registros.")
    paciente_id = input("Ingresa el ID del paciente para ver sus registros: ")
    interacmongo("Registros", "find", {'id_Paciente': paciente_id})

def actualizar_registro():
    print("Estás en la opción de modificar un registro.")
    
    # Primero, obtener el ID del registro (paciente) para actualizar
    id_paciente = input("Ingresa el ID del paciente para modificar el registro: ")
    query = {"id_Paciente": id_paciente}
    
    print("¿Qué campo deseas modificar?")
    print("1. Medicamentos")
    print("2. Diagnóstico")
    print("3. Tratamiento")
    opcion = input("Selecciona una opción (1-3): ")
    
    if opcion == '1':
        medicamentos = []
        while True:
            medicamento = {}
            medicamento["nombre"] = input("Nuevo nombre del medicamento: ")
            medicamento["dosis"] = input("Nueva dosis del medicamento: ")
            medicamento["frecuencia"] = input("Nueva frecuencia del medicamento: ")
            medicamentos.append(medicamento)

            otra = input("¿Deseas ingresar otro medicamento? (s/n): ")
            if otra.lower() != 's':
                break

        # Actualizar medicamentos
        query2 = {'$set': {'medicamentos': medicamentos}}

    elif opcion == '2':
        nuevo_diagnostico = input("Nuevo diagnóstico asociado: ")
        query2 = {'$set': {'diagnostico_asociado': nuevo_diagnostico}}

    elif opcion == '3':
        nuevo_tipo_diagnostico = input("Nuevo tipo de diagnóstico: ")
        nueva_descripcion = input("Nueva descripción del diagnóstico: ")
        nuevas_pruebas = input("Nuevas pruebas realizadas (separadas por coma): ").split(",")
        nueva_fecha_diagnostico = input("Nueva fecha de diagnóstico (AAAA-MM-DD): ")

        query2 = {'$set': {
            'Tratamiento.tipo_diagnostico': nuevo_tipo_diagnostico,
            'Tratamiento.descripcion': nueva_descripcion,
            'Tratamiento.pruebas_realizadas': nuevas_pruebas,
            'Tratamiento.fecha_diagnostico': nueva_fecha_diagnostico
        }}

    # Realizar la actualización
    interacmongo("Registros", "updateOne", query, query2)
    
def eliminar_registro():
    print("Estás en la opción de eliminar un registro.")
    
    # Seleccionamos el ID del paciente para eliminar el registro
    id_paciente = input("Ingresa el ID del paciente para eliminar el registro: ")
    query = {"id_Paciente": id_paciente}
    
    # Eliminar el registro
    interacmongo("Registros", "remove", query)

def menu_Rec_Tra():
    while True:
        print("\nSelecciona una opción:")
        print("1. Crear nuevo registro (Paciente, Médico, Tratamiento)")
        print("2. Leer registros")
        print("3. Actualizar registro")
        print("4. Eliminar registro")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == '1':
            crear_registro()
        elif opcion == '2':
            leer_registro()
        elif opcion == '3':
            actualizar_registro()
        elif opcion == '4':
            eliminar_registro()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 5.")

def queryfindcit():
    idusr = input("Ingresa el nombre del paciente")
    query={"nom_user":idusr}
    return query


opsel=menuopciones("Médico","Usuario","Admin")
match opsel:
##MEDICO    
    case'1':
        opsmed=menuopciones("Citas","Recetas","Salir")
        match opsmed:
    #CITAS            
            case'1':
                opsmedcit=menuopciones("Crear","Borrar","Modificar")
                match opsmedcit:
                    case'1':
                        addcit = queryaddcit('674d667692be37f7692bb3ae')
                        interacmongo("Citas","insertOne",addcit)
                    case'2':
                        addcit = queryaddcit('674d667692be37f7692bb3ae')
                        interacmongo("Citas","remove",addcit)
                    case'3':
                        slct=query2updcit()
                        fltro=filtroupdcit()
                        interacmongo("Citas","updateOne",slct,fltro)
    #RECETAS
            case'2':
                menu_Rec_Tra()
    #SALIR               
            case'3':
                print("Saliendo")
##USUSARIO
    case'2':
        opsusr=menuopciones("Citas", "Recetas", "Salir")
        match opsusr:
            case '1':
                
                crefinusrcit=menuopciones("Crear", "Consultar", "Salir")
                match crefinusrcit:
                    case'1':
                        interacmongo("Citas","find",queryfindcit)
                    case '2':
                        addcit = queryaddcit('674d667692be37f7692bb3ae')
                        interacmongo("Citas","insertOne",addcit)
                    case'3':
                        print("Saliendo ...")
            case'2':
                interacmongo("Registros","find",queryfindcit)
            case'3':
                print("Saliendo")
##Admin    
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
                

