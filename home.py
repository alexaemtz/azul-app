import streamlit as st

with open("style/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    
st.title(":blue[App Azul - ¡Bienvenido!]")
st.header("¡Bienvenido a su App Azul!", divider="rainbow")
st.write("Esta aplicación le será de ayuda para el monitoreo y control de su diabetes.")

# --- PAGE SETUP ---
main_page = st.Page("home.py",
                    title="Inicio",
                    icon=":material/home:"),

register_page = st.Page("views/register.py", 
                        title="Registro", 
                        icon=":material/description:"),

counter_page = st.Page("views/detection.py", 
                       title="Calculo de calorias", 
                       icon=":material/favorite:"),

# --- NAVIGATION SETUP [WITH SECTIONS] ----
pg = st.navigation({
    "Inicio" : main_page,
    "Registro" : register_page,
    "Monitoreo" : counter_page
})

pg.run()
