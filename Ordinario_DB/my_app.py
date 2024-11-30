import streamlit as st
import json

# Función para mostrar la página de registro de pacientes
def mostrar_formulario():
    # Título de la aplicación
    st.title('Formulario de Registro de Pacientes')

    # Subtítulo
    st.subheader('Por favor, complete la siguiente información del paciente')

    # Campo para el identificador único
    identificador = st.text_input("Identificador único del paciente")

    # Campo para el nombre
    nombre = st.text_input("Nombre del paciente")

    # Campo para la fecha de nacimiento
    fecha_nacimiento = st.date_input("Fecha de nacimiento")

    # Campo para el sexo
    sexo = st.radio("Sexo", ('Masculino', 'Femenino', 'Otro'))

    # Campo para la dirección
    direccion = st.text_input("Dirección")

    # Campo para el número de teléfono
    telefono = st.text_input("Número de teléfono")

    # Campo para el correo electrónico
    correo = st.text_input("Correo electrónico")

    # Campo para el historial médico
    historial_medico = st.text_area("Historial médico")

    # Campo para las condiciones preexistentes
    condiciones = st.text_area("Condiciones preexistentes")

    # Campo para el número de seguro médico
    seguro_medico = st.text_input("Número de seguro médico")

    # Campo para el contacto de emergencia
    contacto_nombre = st.text_input("Nombre del contacto de emergencia")
    contacto_telefono = st.text_input("Número de teléfono del contacto de emergencia")

    # Campo para las alergias
    alergias = st.text_area("Alergias (si las hay)")

    # Botón para enviar los datos
    if st.button("Guardar Información"):
        # Crear un diccionario con los datos introducidos
        paciente = {
            "identificador": identificador,
            "nombre": nombre,
            "fecha_nacimiento": str(fecha_nacimiento),  # Convertir la fecha a string
            "sexo": sexo,
            "direccion": direccion,
            "telefono": telefono,
            "correo": correo,
            "historial_medico": historial_medico,
            "condiciones_preexistentes": condiciones,
            "seguro_medico": seguro_medico,
            "contacto_emergencia": {
                "nombre": contacto_nombre,
                "telefono": contacto_telefono
            },
            "alergias": alergias
        }

        # Convertir el diccionario a un JSON
        paciente_json = json.dumps(paciente, indent=4)

        # Mostrar mensaje de éxito y los datos en formato JSON
        st.success("¡Información del paciente guardada con éxito!")
        st.write("Datos del paciente en formato JSON:")
        st.json(paciente_json)

# Función principal para la home page
def home_page():
    st.title('Página Principal')

    # Un botón en la home page para acceder al formulario
    if st.button("Ir al Formulario de Registro"):
        mostrar_formulario()  # Llamar a la función que muestra el formulario

# Llamar a la función principal (home page)
home_page()
