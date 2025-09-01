import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

st.title("Visualización de Vehículos en EE. UU.")

# Botón para mostrar histograma de odómetro
if st.button("Mostrar histograma de odómetro"):
    fig_hist = px.histogram(car_data, x="odometer")
    st.write("Histograma de odómetro")
    st.plotly_chart(fig_hist)

# Botón para mostrar gráfico de dispersión odómetro vs precio
if st.button("Mostrar dispersión odómetro vs precio"):
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="model_year",             # ejemplo de columna existente para colorear
        # columnas existentes para mostrar al pasar el cursor
        hover_data=['model', 'model_year']
    )
    st.write("Gráfico de dispersión: odómetro vs precio")
    st.plotly_chart(fig_scatter)
