import streamlit as st
import Pacientes as pac

exglb = False
rol_usuario = None

usuarios_validos = {
    "admin": {"password": "admin1234", "rol": "Admin"},
    "usuario1": {"password": "password1", "rol": "Médico"},
    "usuario2": {"password": "mypassword", "rol": "Paciente"},
}

def menu(op1, op2, op3, op4):
    opt = st.selectbox(
        "Selecciona qué acción quieres ejecutar",
        (op1, op2, op3, op4),
    )
    return opt

def login(opcmenu): 
    global exglb 
    st.title(f"Inicio de sesión como: {opcmenu}")

    username = st.text_input("Usuario", max_chars=50)
    password = st.text_input("Contraseña", type="password", max_chars=50)

    if st.button(f"Iniciar sesión"):
        if username in usuarios_validos and usuarios_validos[username]["password"] == password:
            rol_usuario = usuarios_validos[username]["rol"]  # Guardamos el rol del usuario
            
            if rol_usuario == opcmenu:
                exglb = True
                st.success("Acceso exitoso.")
            else:
                st.error("Usuario o contraseña incorrectos. Intenta de nuevo.")
        else:
            st.error("Usuario o contraseña incorrectos. Intenta de nuevo.")

def crear_cuenta(usuario, password, rol):
    if usuario in usuarios_validos:
        st.error("El nombre de usuario ya existe.")
    else:
        usuarios_validos[usuario] = {"password": password, "rol": rol}
        st.success(f"Cuenta para {usuario} creada con éxito.")

def signup():
    st.title('Creación de Cuenta')

    
    usuario = st.text_input("Nombre de usuario")
    password = st.text_input("Contraseña", type="password")
    rol = st.selectbox("Selecciona el rol", ["Admin", "Médico", "Paciente"])

    if st.button('Crear Cuenta'):
        if usuario and password and rol:
            crear_cuenta(usuario, password, rol)
        else:
            st.error("Por favor, completa todos los campos.")

    st.subheader("Usuarios existentes:")
    for user, data in usuarios_validos.items():
        st.write(f"Usuario: {user}, Rol: {data['rol']}")    

def new_func():
    paciente_json = pac.mostrar_formulario()


st.title("Bienvenido al sistema para gestión de salud")
opcmenu = menu("Selecciona una opción", "Médico", "Paciente", "Admin")


if opcmenu != "Selecciona una opción":
    if opcmenu == 'Médico':
        login(opcmenu)  
        if exglb: 
            new_func()

    elif opcmenu == 'Paciente':
        login(opcmenu)  
        if exglb:
            pacmenu = menu("Selecciona una opción", "Citas", "Historia clínica", "Mis datos")

    elif opcmenu == 'Admin':
        login(opcmenu)  
        if exglb:
            signup()