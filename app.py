import os
import openai
import streamlit as st
#from dotenv import load_dotenv

# Carga las variables de entorno desde .env
# load_dotenv()

# Configura tu clave de API de OpenAI usando una variable de entorno
openai.api_key = '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'



def obtener_recomendaciones(tipo_propiedad, cant_habitaciones, cant_banos, patio, pileta):
    # Construye el prompt para la API de OpenAI
    prompt = f"Generar una lista de recomendaciones de equipamiento para un {tipo_propiedad} con {cant_habitaciones} habitaciones, {cant_banos} baños, {'con' if patio else 'sin'} patio, y {'con' if pileta else 'sin'} pileta, destinado a Airbnb."

    # Llama a la API de OpenAI y obtiene la respuesta usando el endpoint de chat
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",  # Usando el modelo de chat
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}]
    )

    # Asegúrate de acceder correctamente al texto de la respuesta
    return response['choices'][0]['message']['content']

# Configuración de Streamlit
st.title("SmartProperty Assistant")

# Sección "Cómo funciona"
st.header("Cómo funciona")
st.write("""
- **Características clave**: `SmartProperty Assistant` utiliza la inteligencia artificial avanzada de OpenAI para generar recomendaciones personalizadas de equipamiento para propiedades destinadas a alquileres vacacionales como Airbnb. Analiza las características específicas de cada propiedad para ofrecer una lista detallada de elementos necesarios.
- **Cómo realizar solicitudes**: Simplemente selecciona las características de tu propiedad en el formulario de la aplicación, como el tipo de propiedad, la cantidad de habitaciones y baños, y si cuenta con patio o pileta.
- **Qué esperar como resultado**: Después de enviar tus preferencias haciendo clic en "Generar Recomendaciones de Equipamiento", recibirás una lista personalizada de recomendaciones para equipar tu propiedad, mejorando así la experiencia de los huéspedes y potencialmente aumentando la rentabilidad de tus alquileres.
- **Información adicional**: La precisión de las recomendaciones puede variar según la complejidad de la solicitud y las tendencias actuales del mercado. Se recomienda utilizar estas recomendaciones como una guía inicial y ajustar según sea necesario.
""")

# Recolección de inputs del usuario
st.subheader("Configura tu propiedad")
tipo_propiedad = st.selectbox("Tipo de Propiedad", ["Departamento", "Casa", "Estudio"])
cant_habitaciones = st.number_input("Cantidad de Habitaciones", min_value=1, step=1)
cant_banos = st.number_input("Cantidad de Baños", min_value=1, step=1)
patio = st.checkbox("¿Tiene Patio?")
pileta = st.checkbox("¿Tiene Pileta?")

if st.button("Generar Recomendaciones de Equipamiento"):
    recomendaciones = obtener_recomendaciones(tipo_propiedad, cant_habitaciones, cant_banos, patio, pileta)
    st.write(recomendaciones)
