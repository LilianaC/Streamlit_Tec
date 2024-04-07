import pandas as pd
import streamlit as st

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQy_3VusOhQHehdbyBITYO3YkIeZ9agx3SDvkcCk0s02Yo9jqB_2c5wS2O7x5cdo1KXavy_tlqbNvHy/pub?gid=65918408&single=true&output=csv'
df = pd.read_csv(url)

listadulces = df['categoría'].unique().tolist()

selecc = st.selectbox('Selecciona la lista', listadulces, ['Tamarindo'],help='Selecciona la categoría de dulces. Presiona Enviar 📤')

st.dataframe(df[df['categoría'] == selecc])
