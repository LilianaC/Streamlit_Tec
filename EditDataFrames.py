import pandas as pd
import streamlit as st
from PIL import Image


url='https://docs.google.com/spreadsheets/d/e/2PACX-1vSp88guAuK5q0hg3cp6clhOQwtQPYXrY-FvbcTmcBIJH8zCw4RDuGcRBbKHq9x0wpEaN9bonn-aW_f2/pub?gid=1562725821&single=true&output=csv'
df=pd.read_csv(url,encoding='ISO-8859-1')

st.title('🎙️ Dataframe de Spotify 🎼')
st.dataframe(df, use_container_width=True)

