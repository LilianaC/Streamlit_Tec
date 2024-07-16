import streamlit as st
import pandas as pd
from datetime import date



data = {
    "id": ["P-1001", "P-1002", "P-1003", "P-1004", "P-1005"],
    "name": [
        "Teclado Gaming",
        "Mouse Inalámbrico",
        "Monitor",
        "Funda para Laptop",
        "USB Hub",
    ],
    "image": [
        "https://m.media-amazon.com/images/I/81P5HmwEW9L._AC_UY436_FMwebp_QL65_.jpg",
        "https://m.media-amazon.com/images/I/61d0uTjKbkL._AC_UY436_FMwebp_QL65_.jpg",
        "https://m.media-amazon.com/images/I/71s74LCUyCL._AC_UY436_FMwebp_QL65_.jpg",
        "https://m.media-amazon.com/images/I/61lGRfaagdL._AC_UY436_FMwebp_QL65_.jpg",
        "https://m.media-amazon.com/images/I/512Vua1otlL.__AC_SX300_SY300_QL70_ML2_.jpg",
    ],
    "stock": [50, 120, 30, 80, 150],
    "reorder": [20, 50, 10, 30, 60],
    "history": [
        [60, 70, 55, 50, 40],
        [100, 130, 150, 110, 120],
        [40, 35, 30, 25, 20],
        [90, 80, 85, 70, 80],
        [160, 170, 155, 150, 140],
    ],
    "last_updated": [
        "2023-03-25",
        "2023-03-28",
        "2023-04-01",
        "2023-04-05",
        "2023-04-10",
    ],
     "Links": ["http://www.rivera.com/",
              "http://hill.com/",
              "http://green.info/",
              "https://www.rose-freeman.net/",
              "https://thompson.com/"],

     "Avance": [0.97, 0.71, 0.89, 0.34, 0.79],

     "Actividad": [
     [75, 15, 24, 74, 10, 36, 56, 84, 15, 20, 87, 21, 14, 89, 88, 10, 42, 27, 32, 37, 10, 27, 27, 9, 16],
     [76, 73, 13, 37, 3, 29, 84, 53, 5, 47, 33, 34, 6, 31, 14, 79, 2, 73, 10, 10, 84, 67, 45, 14, 46],
     [76, 16, 64, 40, 13, 31, 36, 46, 17, 11, 82, 4, 54, 73, 32, 60, 50, 35, 83, 36, 60, 34, 10, 62, 63],
     [55, 34, 27, 9, 52, 38, 19, 83, 64, 61, 37, 88, 35, 35, 11, 85, 4, 70, 76, 84, 49, 46, 16, 45, 13],
     [38, 30, 5, 43, 18, 46, 31, 11, 23, 60, 67, 81, 32, 28, 15, 31, 9, 76, 31, 8, 38, 22, 16, 86, 82]
     ]


    
}


df = pd.DataFrame(data)


def icon(emoji: str):
    """Shows an emoji as a Notion-style page icon."""
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

st.set_page_config(
    layout="wide", page_title="Column config demo app", page_icon="🧮"
)
icon("🧮")
st.title('El inventario ✍🏻')


st.data_editor(
        data,
        width=1700, height=250,
        
        column_config={
            "id": "Product ID",
            "name": "Product Name",
            "image": st.column_config.ImageColumn("Image"),
            "stock": st.column_config.NumberColumn("Stock quantity", min_value=0),
            "reorder": st.column_config.NumberColumn("Reorder level", min_value=0),
           # "history": st.column_config.LineChartColumn("Stock history"),
            "history": st.column_config.AreaChartColumn("Stock history",width="medium"),
            "last_updated": "Actualización",
            "Links": st.column_config.LinkColumn(
            "Páginas", help="Una página random"
            ),
            "Actividad": st.column_config.BarChartColumn(
            "Actividad diaria",
            help="Actividad de los últimos 20 días",
            width="medium",
            y_min=0,
            y_max=1,
            ),
            "Avance": st.column_config.ProgressColumn(
            "Status", min_value=0, max_value=1, format="%.2f"),
                       
        },
        column_order=["name","image","history","Avance","Actividad","Links","id","stock","reorder","last_updated"],
        disabled=("id", "image", "name"),
        hide_index=True)

