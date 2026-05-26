import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles_us.csv")

st.header("Dashboard de Anúncios de Venda de Carros")

st.write("Este dashboard apresenta uma análise exploratória básica de anúncios de venda de carros usados.")

hist_button = st.button("Criar histograma")

if hist_button:
    st.write("Histograma da quilometragem dos veículos")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button("Criar gráfico de dispersão")

if scatter_button:
    st.write("Gráfico de dispersão entre preço e quilometragem")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)