#pip install pymongo
from pymongo import MongoClient

# Conectar a la base de datos de MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['gestion_salud']

# Acceder a las colecciones
pacientes = db['pacientes']
medicos = db['medicos']
diagnosticos = db['diagnosticos']
tratamientos = db['tratamientos']
recetas = db['recetas']
citas = db['citas']

def agregar_paciente(paciente):
    result = pacientes.insert_one(paciente)
    return result.inserted_id

def obtener_paciente(id_paciente):
    paciente = pacientes.find_one({"_id": id_paciente})
    return paciente

def actualizar_tratamiento(id_tratamiento, tratamiento):
    result = tratamientos.update_one(
        {"_id": id_tratamiento},
        {"$set": tratamiento}
    )
    return result.modified_count

def eliminar_cita(id_cita):
    result = citas.delete_one({"_id": id_cita})
    return result.deleted_count
