import streamlit as st
import os
from datetime import datetime
import pytz

st.set_page_config(page_title="App Azul", page_icon="🍣", layout="wide")
st.title(":blue[App Azul - ¡Bienvenido!]")
st.header("¡Bienvenido a su App Azul!", divider="rainbow")
st.write("Esta aplicación le será de ayuda para el monitoreo y control de su diabetes.")

st.subheader("Registro")
st.write("Cree el registro de glucosa.")

with st.container():
  zona_local = pytz.timezone("America/Mexico_City")
  hora_local = datetime.now(zona_local)

  fecha =st.date_input("Fecha:",hora_local)
  hora = st.time_input("Hora:",hora_local)
  
  tiempo_medicion = st.text_input("Tiempo de la medición:",
                                  placeholder="Ejemplo: 10 minutos antes de la comida.")
  
  lectura = st.number_input("Glucosa marcada:", placeholder="Ejemplo: 100 mg/dL")
