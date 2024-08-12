

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
metric_in_use = st.sidebar.empty()


st.sidebar.markdown("---")

st.sidebar.markdown("---")

st.sidebar.info("""
Note on metrics:\n
Words with more frequent letters have a higher '**letter score**' (suggested for 1st or 2nd guesses).\n

More frequent words have a higher '**wiki score**' (suggested for later guesses). 

The metric '**auto**' will automatically use '**letter score**' for the first and second suggestions, and then '**wiki score**' for the rest.
The idea here is to maximize the chances of discovering all the letters in the first two guesses, and then aiming to find the target through the most common words.

""")
