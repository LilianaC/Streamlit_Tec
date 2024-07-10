import streamlit as st
import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQy_3VusOhQHehdbyBITYO3YkIeZ9agx3SDvkcCk0s02Yo9jqB_2c5wS2O7x5cdo1KXavy_tlqbNvHy/pub?gid=65918408&single=true&output=csv'
df = pd.read_csv(url)
urlc = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQy_3VusOhQHehdbyBITYO3YkIeZ9agx3SDvkcCk0s02Yo9jqB_2c5wS2O7x5cdo1KXavy_tlqbNvHy/pub?gid=1699633182&single=true&output=csv'
dfc = pd.read_csv(urlc)

st.title('🍬 La dulcería: Editable ✍🏻')
edited_df = st.data_editor(df)
edited_dfc = st.data_editor(dfc)
