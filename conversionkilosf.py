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

count = 0

increment = st.button('Increment')
if increment:
    count += 1

st.write('Count = ', count)



