import streamlit as st
import random

# Simula la generación de una lista de equipamiento
def generar_lista_equipamiento():
    # Lista de ejemplo de posibles equipamientos
    equipamientos = ['TV Smart', 'Wi-Fi', 'Cafetera', 'Aire acondicionado', 'Calefacción', 'Juego de toallas', 'Ropa de cama', 'Secador de pelo', 'Cocina equipada', 'Detector de humo']
    # Selecciona una cantidad aleatoria de equipamientos para simular la lista
    lista_seleccionada = random.sample(equipamientos, k=random.randint(5, len(equipamientos)))
    return lista_seleccionada

# Título de la aplicación
st.title('SmartProperty Assistant')

# Descripción de la aplicación
st.write("""
SmartProperty Assistant es una aplicación innovadora diseñada para optimizar la gestión de propiedades en plataformas de alquiler vacacional como Airbnb. Utilizando tecnologías avanzadas de inteligencia artificial, esta aplicación asiste a los administradores de propiedades en el equipamiento inicial y el mantenimiento continuo, asegurando una experiencia de alta calidad para los huéspedes y maximizando la rentabilidad de las propiedades.
""")

# Botón de acción y generación de lista de equipamiento
if st.button('Generar Lista de Equipamiento'):
    lista_equipamiento = generar_lista_equipamiento()
    st.success('Lista de equipamiento generada con éxito!')
    st.write('Aquí tienes una lista personalizada de equipamiento para tu propiedad:')
    for item in lista_equipamiento:
        st.write(f"- {item}")

# Sección "Cómo funciona"
st.header('¿Cómo funciona SmartProperty Assistant?')

st.write("""
SmartProperty Assistant utiliza algoritmos de inteligencia artificial para analizar datos de mercado y tendencias de huéspedes, ofreciendo recomendaciones personalizadas para cada propiedad. Las características clave incluyen:

- **Análisis de Tendencias:** La aplicación evalúa las tendencias actuales de los huéspedes y las expectativas del mercado para sugerir el equipamiento más relevante.
- **Mantenimiento Predictivo:** Utiliza aprendizaje automático para predecir cuándo los artículos necesitan ser reemplazados o reparados, asegurando que todo esté siempre en perfecto estado.
- **Personalización:** Se adapta a las necesidades específicas de cada propiedad, considerando su ubicación, tamaño y tipo.

Para comenzar, simplemente haz clic en el botón 'Generar Lista de Equipamiento' y la aplicación procesará los datos disponibles para proporcionarte una lista de equipamiento esencial personalizado para tu propiedad.
""")

# Instrucciones adicionales o notas si son necesarias
st.sidebar.header('Notas Adicionales')
st.sidebar.write("""
- La efectividad de las recomendaciones mejora con el uso, a medida que la aplicación aprende de las interacciones y feedback.
- Considera revisar regularmente las sugerencias de mantenimiento para mantener tus propiedades en óptimas condiciones.
""")
