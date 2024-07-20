#Referencia para código de contadores https://docs.streamlit.io/develop/concepts/architecture/session-state?ref=blog.streamlit.io
#Ejemplos de session state como aplicaciones https://streamlit-release-demos-0-84streamlit-app-0-84-2ec1k9.streamlit.app/?page=headliner

import streamlit as st

def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

st.set_page_config(
    layout="wide", page_title="Column config demo app", page_icon="🧮"
)
icon("🖩")
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
    keys = list(st.session_state.keys())
    for key in keys:
        st.session_state.pop(key)

st.button("Borrar 🧹", on_click= limpiar_cache)

st.markdown(''':blue[Ahora una prueba para enviar información fuera de un formulario]''')



import datetime

if 'count' not in st.session_state:
    st.session_state.count = 0
    st.session_state.last_updated = datetime.time(0,0)

def update_counter():
    st.session_state.count += st.session_state.increment_value
    st.session_state.last_updated = st.session_state.update_time

with st.form(key='my_form'):
    st.time_input(label='Enter the time', value=datetime.datetime.now().time(), key='update_time')
    st.number_input('Enter a value', value=0, step=1, key='increment_value')
    submit = st.form_submit_button(label='Update', on_click=update_counter)

st.write('Current Count = ', st.session_state.count)
st.write('Last Updated = ', st.session_state.last_updated)
