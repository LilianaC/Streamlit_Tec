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

st.write(
        """
        ## :purple[💯 El contador que sí funciona]

        """
    )

if "counter" not in st.session_state:
    st.session_state.counter = 0

def increment():
    st.session_state.counter += 1

st.write("Counter:", st.session_state.counter)
st.button("Más uno ➕", on_click=increment)

if st.session_state.counter >= 5:
    st.success("King of counting there! Your trophy for reaching 50: 🏆")
elif st.session_state.counter >= 7:
    st.warning("You made it to 10! Keep going to win a prize 🎈")
