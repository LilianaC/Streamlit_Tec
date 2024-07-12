#https://colab.research.google.com/drive/1kAb5pKs0oky0rdayDNTvdnKrWwCQnglQ#scrollTo=qPS4YA7XOTes

import streamlit as st
import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQy_3VusOhQHehdbyBITYO3YkIeZ9agx3SDvkcCk0s02Yo9jqB_2c5wS2O7x5cdo1KXavy_tlqbNvHy/pub?gid=504292800&single=true&output=csv'
df = pd.read_csv(url)


st.title('🍬 La dulcería: El dataframe ✍🏻')


#Modificar el ancho y alto del dataframe
#Esconder el índice del dataframe
#Modificar el orden de las columnas


st.dataframe(df,
             width=100, height=350, use_container_width=True,
             hide_index=True,
             column_order=['producto','precio','categoría']
            )



