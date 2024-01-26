import os
import openai
import streamlit as st
from dotenv import load_dotenv

# Carga las variables de entorno desde .env
load_dotenv()

# Configura tu clave de API de OpenAI usando una variable de entorno
openai.api_key = os.getenv('OPENAI_API_KEY')

def obtener_recomendaciones(tipo_propiedad, cant_habitaciones, cant_banos, patio, pileta):
    # Construye el prompt para la API de OpenAI
    prompt = f"Generar una lista de recomendaciones de equipamiento para un {tipo_propiedad} con {cant_habitaciones} habitaciones, {cant_banos} baños, {'con' if patio else 'sin'} patio, y {'con' if pileta else 'sin'} pileta, destinado a Airbnb."

    # Llama a la API de OpenAI y obtiene la respuesta
    response = openai.Completion.create(
        engine="text-davinci-003",  # O el modelo más adecuado para tus necesidades
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )

    # Asegúrate de acceder correctamente al texto de la respuesta
    return response['choices'][0]['text'].strip()

# Configuración de Streamlit
st.title("SmartProperty Assistant")

# Recolección de inputs del usuario
tipo_propiedad = st.selectbox("Tipo de Propiedad", ["Departamento", "Casa", "Estudio"])
cant_habitaciones = st.number_input("Cantidad de Habitaciones", min_value=1, step=1)
cant_banos = st.number_input("Cantidad de Baños", min_value=1, step=1)
patio = st.checkbox("¿Tiene Patio?")
pileta = st.checkbox("¿Tiene Pileta?")

if st.button("Generar Recomendaciones de Equipamiento"):
    recomendaciones = obtener_recomendaciones(tipo_propiedad, cant_habitaciones, cant_banos, patio, pileta)
    st.write(recomendaciones)
