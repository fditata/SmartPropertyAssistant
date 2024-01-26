import streamlit as st

# Simula la generación de una lista de equipamiento basada en los inputs del usuario
def generar_lista_equipamiento(tipo_propiedad, cant_habitaciones, cant_banos, patio, pileta):
    # Base de equipamiento esencial para todas las propiedades
    equipamiento_base = [
        'Wi-Fi', 'TV', 'Calefacción', 'Aire acondicionado', 'Detector de humo', 'Extintor de incendios',
        'Juego de sábanas', 'Almohadas', 'Toallones', 'Jabón', 'Shampoo', 'Utensilios de cocina básicos',
        'Platos y cubiertos', 'Cafetera', 'Tostadora'
    ]
    
    # Agrega elementos específicos según el tipo de propiedad
    if tipo_propiedad == 'Departamento':
        equipamiento_base += ['Plancha', 'Secador de pelo']
    elif tipo_propiedad == 'Casa':
        equipamiento_base += ['Lavadora', 'Secadora']
    
    # Considera características específicas de la propiedad
    if cant_banos > 1:
        equipamiento_base += ['Juego adicional de toallones por baño']
    
    if patio:
        equipamiento_base += ['Muebles de patio']
    
    if pileta:
        equipamiento_base += ['Toallas para la pileta', 'Reposeras']
    
    return equipamiento_base

# Título de la aplicación
st.title('SmartProperty Assistant')

# Descripción de la aplicación
st.write("""
Esta aplicación te ayuda a equipar tu departamento para Airbnb, asegurando que tengas todo lo necesario para una estancia confortable y satisfactoria para tus huéspedes.
""")

# Entradas del usuario
st.header('Configura tu propiedad')
tipo_propiedad = st.selectbox('Tipo de Propiedad', ['Departamento', 'Casa', 'Estudio'])
cant_habitaciones = st.number_input('Cantidad de Habitaciones', min_value=1, max_value=10, step=1)
cant_banos = st.number_input('Cantidad de Baños', min_value=1, max_value=5, step=1)
patio = st.checkbox('¿Tiene Patio?')
pileta = st.checkbox('¿Tiene Pileta?')

# Botón de acción y generación de lista de equipamiento
if st.button('Generar Lista de Equipamiento'):
    lista_equipamiento = generar_lista_equipamiento(tipo_propiedad, cant_habitaciones, cant_banos, patio, pileta)
    st.success('Lista de equipamiento generada con éxito!')
    st.write('Aquí tienes una lista personalizada de equipamiento para tu propiedad:')
    for item in lista_equipamiento:
        st.write(f"- {item}")

# Sección "Cómo funciona"
st.header('¿Cómo funciona SmartProperty Assistant?')
st.write("""
Basado en el tipo de propiedad, la cantidad de habitaciones, baños y características especiales como patio o pileta, SmartProperty Assistant genera una lista detallada de equipamiento esencial. Esta lista está diseñada para cubrir todas las necesidades básicas de tus huéspedes, mejorando su experiencia y tus calificaciones en Airbnb.
""")

# Notas adicionales
st.sidebar.header('Notas Adicionales')
st.sidebar.write("""
- Considera las preferencias y necesidades de tus huéspedes al seleccionar los ítems de esta lista.
- Revisa y actualiza regularmente el equipamiento de tu propiedad para mantener la satisfacción de los huéspedes.
""")
