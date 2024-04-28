import pandas as pd
import plotly.express as px
import streamlit as st


car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Histograma y gráfica de dispersión') #Encabezado

hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_disp = st.checkbox('Construir un gráfico de dispersión')

if build_disp: # si la casilla de verificación está seleccionada
    st.write('Construir un gráfico de dispersión para la columna odómetro')
    
    #crear gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
    
    #mostrar gráfico
    st.plotly_chart(fig, use_container_width=True)

