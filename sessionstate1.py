
import streamlit as st

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

st.set_page_config(
    layout="wide", page_title="Ejemplo de uso de Session state", page_icon="🍪"
)
icon("🍪")
st.title('Ejemplos de Session state (Estado de las sesiones)')

st.markdown(''':orange[El botón solamente funciona una vez]''')

contador = 0
incremento = st.button('Incremento 🔼')
if incremento:
    contador += 1

st.write('Contador = ', contador)

st.markdown(''':green[El botón funciona todas las veces]''')

if "counter" not in st.session_state:
    st.session_state.counter = 0

def increment():
    st.session_state.counter += 1

st.write("Contador:", st.session_state.counter)
st.button("Más uno ➕", on_click=increment)

if st.session_state.counter <= 5:
    st.success("Sigue adelante con la cuenta 🎈")
elif st.session_state.counter > 5:
    st.success("¡Ya alcanzaste la cuenta necesaria para el 🏆 " + str(st.session_state.counter))
    st.balloons()

def limpiar_cache():
    #keys = list(st.session_state.keys())
    #for key in keys:
        #st.session_state.pop(key)

    for key in st.session_state.keys():
        del st.session_state[key]

st.button("Borrar 🧹", on_click= limpiar_cache)
