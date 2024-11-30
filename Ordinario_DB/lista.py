import streamlit as st

# Título de la aplicación
st.title('Ejemplo de Lista Desplegable para Seleccionar Múltiples Opciones')

# Lista de opciones
opciones = ['Opción 1', 'Opción 2', 'Opción 3', 'Opción 4']

# Menú desplegable para seleccionar múltiples opciones
opciones_seleccionadas = st.multiselect('Selecciona una o más opciones', opciones)

# Botón para mostrar las opciones seleccionadas
if st.button('Mostrar opciones seleccionadas'):
    if opciones_seleccionadas:
        st.write(f'Has seleccionado: {", ".join(opciones_seleccionadas)}')
    else:
        st.write('No has seleccionado ninguna opción')
