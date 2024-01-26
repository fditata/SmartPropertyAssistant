import streamlit as st

# Simula la generación de una lista de equipamiento basada en los inputs del usuario
def generar_lista_equipamiento(tipo_hospedaje, cant_habitaciones):
    # Base de equipamiento común para todos los tipos de hospedaje
    equipamiento_base = ['Wi-Fi', 'Detector de humo', 'Botiquín de primeros auxilios', 'Extintor de incendios']
    
    # Agrega equipamiento específico según el tipo de hospedaje
    if tipo_hospedaje == 'Casa completa':
        equipamiento_base += ['Cocina equipada', 'Lavadora', 'Patio o balcón']
    elif tipo_hospedaje == 'Apartamento':
        equipamiento_base += ['Cocina equipada', 'Lavavajillas']
    elif tipo_hospedaje == 'Habitación privada':
        equipamiento_base += ['Cerradura en la puerta de la habitación']
    
    # Ajusta la lista basándose en la cantidad de habitaciones
    if cant_habitaciones > 1:
        equipamiento_base += ['Baño adicional', f'{cant_habitaciones} juegos de llaves']
    
    return equipamiento_base

# Título de la aplicación
st.title('SmartProperty Assistant')

# Descripción de la aplicación
st.write("""
SmartProperty Assistant es una aplicación innovadora diseñada para optimizar la gestión de propiedades en plataformas de alquiler vacacional. Utilizando inteligencia artificial, facilita el equipamiento inicial y el mantenimiento continuo de las propiedades, mejorando la experiencia de los huéspedes y la rentabilidad de las mismas.
""")

# Entradas del usuario
st.header('Configura tu propiedad')
tipo_hospedaje = st.selectbox('Tipo de Hospedaje', ['Casa completa', 'Apartamento', 'Habitación privada'])
cant_habitaciones = st.number_input('Cantidad de Habitaciones', min_value=1, max_value=10, step=1)

# Botón de acción y generación de lista de equipamiento
if st.button('Generar Lista de Equipamiento'):
    lista_equipamiento = generar_lista_equipamiento(tipo_hospedaje, cant_habitaciones)
    st.success('Lista de equipamiento generada con éxito!')
    st.write('Aquí tienes una lista personalizada de equipamiento para tu propiedad:')
    for item in lista_equipamiento:
        st.write(f"- {item}")

# Sección "Cómo funciona"
st.header('¿Cómo funciona SmartProperty Assistant?')
st.write("""
SmartProperty Assistant utiliza algoritmos de inteligencia artificial para ofrecer recomendaciones personalizadas de equipamiento basadas en el tipo de hospedaje, la cantidad de habitaciones y otros factores. Estas recomendaciones están diseñadas para satisfacer las expectativas de los huéspedes y mejorar la rentabilidad de tu propiedad.
""")

# Notas adicionales
st.sidebar.header('Notas Adicionales')
st.sidebar.write("""
- Las recomendaciones se personalizan según las características de cada propiedad.
- Regularmente actualizamos nuestra base de datos con las últimas tendencias del mercado y expectativas de los huéspedes.
""")
