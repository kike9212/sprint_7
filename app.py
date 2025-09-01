import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

st.title("Visualización de vehículos")

# Botón para gráfico de dispersión
if st.button("Mostrar dispersión odómetro vs precio"):
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="model_year",  # puedes usar otra columna existente
        hover_data=['model', 'model_year']  # columnas que sí existen
    )
    st.write("Gráfico de dispersión: odómetro vs precio")
    st.plotly_chart(fig_scatter)
