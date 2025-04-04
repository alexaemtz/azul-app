import streamlit as st

# --- PAGE SETUP ---
project_1_page = st.Page(
  page = "pages/regisro.py",
  title = "Registro",
  icon = ":material/description:",
  default = True,
)

project_2_page = st.Page(
  page = "pages/regisro.py",
  title = "Detección de calorías",
  icon = ":material/photo_camera:",
  default = True,
)

st.set_page_config(page_title="App Azul", page_icon="🍣", layout="wide")
st.title(":blue[App Azul - ¡Bienvenido!]")
st.header("¡Bienvenido a su App Azul!", divider="rainbow")
st.write("Esta aplicación le será de ayuda para el monitoreo y control de su diabetes.")
