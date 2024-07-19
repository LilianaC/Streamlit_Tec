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
st.title('Convertidor de kg a kg-fuerza 🖩')


def kgs_kgf():
  st.session_state.kgsf = st.session_state.kgs * 9.80665

  
def kgf_kg():
  st.session_state.kgs = st.session_state.kgsf / 9.80665
  

"st.session_state object:",st.session_state

col1, buff, col2 = st.columns([2,1,2])

with col1:
  kilos = st.number_input("kilos:",key="kgs",
                          on_change = kgs_kgf)

with col2:
  fuerza = st.number_input("kilos fuerza:",key="kgsf",
                           on_change = kgf_kg)
