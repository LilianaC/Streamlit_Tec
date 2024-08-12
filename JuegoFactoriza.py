import streamlit as st


st.sidebar.title("¿Cuáles números multiplicados dan...y sumados dan...")
st.sidebar.caption("Para practicar la factorización hecho por @LilianaMx")
st.sidebar.caption("Visita nuestro canal para mayor información")

with st.expander("Instrucciones:", expanded=True):
    st.markdown("""
    1. Selecciona el nivel
    2. Busca los números que sumados dan..y multiplicados dan 
    3. Presiona 'enviar' para revisar si los datos son correctos.
    
    --- 
    
    ⚙️ Use the 👈 sidebar to change the settings.
    🎈 Share this app with your friends! 
    """)

st.sidebar.header("Ajustes")

metric = st.sidebar.selectbox("Nivel:", ["Sencillo", "Fácil", "Experto"])
metric2 = st.sidebar.checkbox("Nivel:", ["Sencillo", "Fácil", "Experto"])
