import streamlit as st
import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQy_3VusOhQHehdbyBITYO3YkIeZ9agx3SDvkcCk0s02Yo9jqB_2c5wS2O7x5cdo1KXavy_tlqbNvHy/pub?gid=504292800&single=true&output=csv'
df = pd.read_csv(url)


st.title('🍬 La dulcería: El dataframe ✍🏻')
#st.dataframe(df, use_container_width=True)

#Modificar el ancho y alto del dataframe
#Esconder el índice del dataframe

st.dataframe(df, 
             width=100, height=350, use_container_width=True,
             hide_index=True,
             column_order=['producto','precio','categoría']
            )

#Utilizar  column_config={
                   #   "Producto": "Nuestros productos",
                   #   "Fotografía": st.column_config.ImageColumn("Imagen")   
                   # }
