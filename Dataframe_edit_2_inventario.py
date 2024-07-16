import streamlit as st
import pandas as pd


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
}

df = pd.DataFrame(data)

st.title('🧮 El inventario ✍🏻')

st.data_editor(
        data,
        width=1700, height=200,
        column_config={
            "id": "Product ID",
            "name": "Product Name",
            "image": st.column_config.ImageColumn("Image"),
            "stock": st.column_config.NumberColumn("Stock quantity", min_value=0),
            "reorder": st.column_config.NumberColumn("Reorder level", min_value=0),
            "history": st.column_config.LineChartColumn("Stock history"),
            "last_updated": "Last updated",
        },
        disabled=("id", "name", "image", "last_updated"),
        hide_index=True)

