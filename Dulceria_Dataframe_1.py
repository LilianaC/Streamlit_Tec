#https://colab.research.google.com/drive/1kAb5pKs0oky0rdayDNTvdnKrWwCQnglQ#scrollTo=qPS4YA7XOTes

import streamlit as st
import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQy_3VusOhQHehdbyBITYO3YkIeZ9agx3SDvkcCk0s02Yo9jqB_2c5wS2O7x5cdo1KXavy_tlqbNvHy/pub?gid=504292800&single=true&output=csv'
df = pd.read_csv(url)


st.title('🍬 La dulcería: El dataframe ✍🏻')


#Utilizar las configuración de las columnas:
#Cambiar el título de las columnas
#Mostrar las imágenes
#Valor entero %d
#Agregar el símbolo de pesos y dos valores decimales

st.dataframe(df,

             width=150, height=420,
             hide_index=True,use_container_width=True,

             column_order=['producto','Fotografía','precio','categoría','cantidad'],
             column_config={
                      "cantidad": "Inventario",
                      "producto": "Nuestros productos",
                      "Fotografía": st.column_config.ImageColumn("Imagen"),
                      "precio": st.column_config.NumberColumn("Precio",format= "$%.2f")
                    }

            )



