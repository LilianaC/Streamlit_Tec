import streamlit as st
import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQy_3VusOhQHehdbyBITYO3YkIeZ9agx3SDvkcCk0s02Yo9jqB_2c5wS2O7x5cdo1KXavy_tlqbNvHy/pub?gid=504292800&single=true&output=csv'
df = pd.read_csv(url)


st.title('🍬 La dulcería: El dataframe ✍🏻')

st.dataframe(df.style.highlight_max(df['precio']), 
             width=150, height=420, use_container_width=True,
             hide_index=True,
             column_order=['producto','Fotografía','precio','categoría'],
             column_config={
                      "Producto": "Nuestros productos",
                      "Fotografía": st.column_config.ImageColumn("Imagen"),
                      "precio": st.column_config.NumberColumn("Costo", format="$ %.2f")
                    }
             
            )




