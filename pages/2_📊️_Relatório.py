import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

st.set_page_config(layout="wide", page_title="Relatório", page_icon="📊")

# importando os dados e salvando em cache
@st.cache(allow_output_mutation=True)
def main1():
    data1 = pd.read_csv('abandono.csv')
    return data1

def main2():
    data2 = pd.read_csv('escolas.csv')
    return data2

abandono = main1()
escolas = main2()

st.sidebar.markdown("# Relatório 📊️")

st.write("# Relatório do abandono escolar em Bagé/RS")
st.markdown(""" ## Localização das escolas de ensino médio em Bagé
As escolas de ensino médio do município de Bagé ficam localizadas em geral 
na região central da cidade estando os bairros afastados sem oferta ocasionando, possivelmente,
abandono escolar""")

# Criando mapa e definindo o zoom
map = folium.Map(location=[abandono.Latitude.mean(), abandono.Longitude.mean()], zoom_start=13, control_scale=True,
                 attr='Mapbox')

escolas_filtrado1= escolas.query('Nivel == "Séries Finais e Médio" ') #filtra por tipo de escola
escolas_filtrado2= escolas.query('Nivel == "Médio" ') #filtra por tipo de escola
escolas_filtrado3= escolas.query('Nivel == "Fundamental e Médio" ') #filtra por tipo de escola

# Adicionando Escolas no Mapa
for index, location_info in escolas_filtrado1.iterrows():
    folium.Marker([location_info["Latitude"], location_info["Longitude"]],
                  icon=folium.Icon(color="red", icon="info-sign"),
                  popup=location_info["Escola"]).add_to(map)

for index, location_info in escolas_filtrado2.iterrows():
    folium.Marker([location_info["Latitude"], location_info["Longitude"]],
                  icon=folium.Icon(color="red", icon="info-sign"),
                  popup=location_info["Escola"]).add_to(map)

for index, location_info in escolas_filtrado3.iterrows():
    folium.Marker([location_info["Latitude"], location_info["Longitude"]],
                  icon=folium.Icon(color="red", icon="info-sign"),
                  popup=location_info["Escola"]).add_to(map)

folium_static(map, width=870, height=550)  # Printa o gráfico