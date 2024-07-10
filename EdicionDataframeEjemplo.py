import streamlit as st
import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQy_3VusOhQHehdbyBITYO3YkIeZ9agx3SDvkcCk0s02Yo9jqB_2c5wS2O7x5cdo1KXavy_tlqbNvHy/pub?gid=2084252518&single=true&output=csv'
df = pd.read_csv(url)


st.title('🍬 La dulcería: Editable ✍🏻')
edf = st.data_editor(df)
edf['Total a pagar']=edf['¿Cuántos compras?']*['Precio']
