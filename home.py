import streamlit as st

register_page = st.Page("pages/Registro.py", title="Registrar de datos", icon=":material/add_circle:")
calorie_page = st.Page("pages/Calculo.py", title="Calculo de calorias", icon=":material/add_circle:")
pg = st.navigation([register_page, calorie_page])

st.set_page_config(page_title="App Azul", page_icon="🍣", layout="wide")

with open("style/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    
st.title(":blue[App Azul - ¡Bienvenido!]")
st.header("¡Bienvenido a su App Azul!", divider="rainbow")
st.write("Esta aplicación le será de ayuda para el monitoreo y control de su diabetes.")
