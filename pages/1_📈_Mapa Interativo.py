import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

st.set_page_config(layout="wide", page_title="Mapa Interativo", page_icon="📈")
st.sidebar.markdown("# Mapa Interativo 📈")
st.sidebar.header("Escolha como deseja filtrar os dados")


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

# Começa a tela
# Titulo
st.title('Abandono Escolar em Bagé/RS\n')
st.write(
    'Para analisar os dados de abandono escolar no município de Bagé com mais detalhes você pode usar os filtros no'
    ' menu a sua esquerda')

genre = st.sidebar.radio(
    "### Escolha como deseja filtrar os dados",
    ('Mantenedora',
     'Escola',
     'Ano escolar',
     'Nível de Ensino'))

if genre == 'Mantenedora':
    # Filtro Para o mapa
    rtype_label = escolas.Tipo.unique().tolist()
    room_type_filter = st.multiselect(label="Escolha a escola por mantenedor",
                                      options=rtype_label,
                                      default=rtype_label)
    escolas_filtrado = escolas.query('Tipo == @room_type_filter')  # filtra por tipo de escola
    abandono_filtrado = abandono.query('Tipo ==@room_type_filter')  # filtra por tipo de escola
    # Criando mapa e definindo o zoom
    map = folium.Map(location=[abandono.Latitude.mean(), abandono.Longitude.mean()],
                     zoom_start=13,
                     control_scale=True,
                     attr='Mapbox')
    # Adicionando alunos no mapa
    col1, col2 = st.columns(2)

    with col1:
        aluno_invisivel = st.checkbox("Mostrar alunos",
                                      True,
                                      help="Desmarque essa opção para ocultar os alunos no mapa")
    if aluno_invisivel:
        map_cluster = MarkerCluster().add_to(map)
        for index, location_info in abandono_filtrado.iterrows():
            folium.Marker([location_info["Latitude"], location_info["Longitude"]],
                          popup=location_info["Aluno"]).add_to(map_cluster)
    # Adicionando escolas no mapa
    with col2:
        escola_invisivel = st.checkbox("Mostrar escolas",
                                       True,
                                       help="Desmarque essa opção para ocultar os alunos no mapa")
    if escola_invisivel:
        for index, location_info in escolas_filtrado.iterrows():
            folium.Marker([location_info["Latitude"], location_info["Longitude"]],
                          icon=folium.Icon(color="red", icon="info-sign"),
                          popup=location_info["Escola"]).add_to(map)
    # Printa o gráfico
    folium_static(map, width=870, height=550)
    st.write(abandono_filtrado)

elif genre == 'Escola':
    # filtros individual por escola
    st.markdown('## Selecionar escola para visualização tabela de dados')
    categorias = list(abandono['Escola'].unique())  # lista as escolas para escolher
    categorias.append('Todas')  # agrega todas as escolas
    categoria = st.selectbox('Clique na lista para escolher', options=categorias)

    # Criando mapa e definindo o zoom
    map1 = folium.Map(location=[abandono.Latitude.mean(), abandono.Longitude.mean()], zoom_start=13, control_scale=True,
                      attr='Mapbox')

    if categoria != 'Todas':
        df_categoria = abandono.query('Escola == @categoria')  # filtra por nome da escola
        df_categoria2 = escolas.query('Escola == @categoria')  # filtra por nome da escola
        # Adicionando alunos no mapa
        map_cluster1 = MarkerCluster().add_to(map1)
        for index, location_info in df_categoria.iterrows():
            folium.Marker([location_info["Latitude"], location_info["Longitude"]],
                          popup=location_info["Aluno"]).add_to(map_cluster1)

        # Adicionando Escolas no Mapa
        for index, location_info in df_categoria2.iterrows():
            folium.Marker([location_info["Latitude"], location_info["Longitude"]],
                          icon=folium.Icon(color="red", icon="info-sign"),
                          popup=location_info["Escola"]).add_to(map1)
        # Cria mapa
        folium_static(map1, width=870, height=550)  # Printa o gráfico
        # Cria tabela
        st.write(df_categoria)  # imprime a tabela de abandonos para escola selecionada
        # Cria gráfico
        fig, ax = plt.subplots(figsize=(6, 2))
        fruits = ['Abandono', 'Remoto']
        bar_labels = ['red', 'blue']
        bar_colors = ['tab:red', 'tab:blue']
        x = [df_categoria2.Abandono.iloc[0], df_categoria2.Remoto.iloc[0]]
        ax.bar(fruits, x, label=bar_labels, color=bar_colors)
        ax.set_ylabel('Quantidades')
        ax.set_title('Estatísticas da escola {}'.format(df_categoria2.Escola.iloc[0]))
        st.pyplot(fig)

    else:
        # Adicionando alunos no mapa
        map_cluster1 = MarkerCluster().add_to(map1)
        for index, location_info in abandono.iterrows():
            folium.Marker([location_info["Latitude"], location_info["Longitude"]],
                          popup=location_info["Aluno"]).add_to(map_cluster1)
        # cria mapa
        folium_static(map1, width=870, height=550)  # Printa o gráfico
        # Cria planilha
        st.write(abandono)  # imprime a tabela de abandonos para todas escolas
        # Cria gráfico
        fig, ax = plt.subplots(figsize=(6, 2))
        fruits = ['Abandono', 'Remoto']
        bar_labels = ['red', 'blue']
        bar_colors = ['tab:red', 'tab:blue']
        x = [escolas.Abandono.sum(), escolas.Remoto.sum()]
        ax.bar(fruits, x, label=bar_labels, color=bar_colors)
        ax.set_ylabel('Quantidades')
        ax.set_title('Estatísticas de todas as escolas públicas de Bagé')
        st.pyplot(fig)

elif genre == 'Ano escolar':
    # filtros individual por ano escolar
    st.markdown('## Selecionar o ano escolar para visualizar os abandonos')
    categorias = list(abandono['Serie'].unique())  # lista as escolas para escolher
    categorias.append('Todas')  # agrega todas as escolas
    categoria = st.selectbox('Clique na lista para escolher', options=categorias)

    # Criando mapa e definindo o zoom
    map1 = folium.Map(location=[abandono.Latitude.mean(), abandono.Longitude.mean()], zoom_start=13, control_scale=True,
                      attr='Mapbox')

    if categoria != 'Todas':
        df_categoria = abandono.query('Serie == @categoria')  # filtra por nome da escola
        # Adicionando alunos no mapa
        map_cluster1 = MarkerCluster().add_to(map1)
        for index, location_info in df_categoria.iterrows():
            folium.Marker([location_info["Latitude"], location_info["Longitude"]],
                          popup=location_info["Aluno"]).add_to(map_cluster1)
        # Cria mapa
        folium_static(map1, width=870, height=550)  # Printa o gráfico
        # Cria tabela
        st.write(df_categoria)  # imprime a tabela de abandonos para escola selecionada

    else:
        # Adicionando alunos no mapa
        map_cluster1 = MarkerCluster().add_to(map1)
        for index, location_info in abandono.iterrows():
            folium.Marker([location_info["Latitude"], location_info["Longitude"]],
                          popup=location_info["Aluno"]).add_to(map_cluster1)
        # cria mapa
        folium_static(map1, width=870, height=550)  # Printa o gráfico
        # Cria planilha
        st.write(abandono)  # imprime a tabela de abandonos para todas escolas

else:
    # Filtro Para o mapa 2
    rtype_label1 = escolas.Nivel.unique().tolist()
    room_type_filter1 = st.multiselect(
        label="Filtre a escola pelo nível de ensino oferado",
        options=rtype_label1,
        default=rtype_label1
    )
    escolas_filtrado1 = escolas.query('Nivel == @room_type_filter1')  # filtra por tipo de escola

    # Filtro Para o mapa 3
    rtype_label2 = abandono.Nível.unique().tolist()
    room_type_filter2 = st.multiselect(
        label="Filtre os alunos pelo nível escolar",
        options=rtype_label2,
        default=rtype_label2
    )
    abandono_filtrado1 = abandono.query('Nível ==@room_type_filter2')  # filtra por nível escolas
    # Criando mapa e definindo o zoom
    map = folium.Map(location=[abandono.Latitude.mean(), abandono.Longitude.mean()], zoom_start=14, control_scale=True,
                     attr='Mapbox')
    col01, col02 = st.columns(2)
    with col01:
        aluno_invisivel1 = st.checkbox("Mostrar alunos",
                                       True,
                                       help="Desmarque essa opção para ocultar os alunos no mapa")
        if aluno_invisivel1:
            # Adicionando alunos no mapa
            map_cluster = MarkerCluster().add_to(map)
            for index, location_info in abandono_filtrado1.iterrows():
                folium.Marker([location_info["Latitude"], location_info["Longitude"]],
                              popup=location_info["Aluno"]).add_to(map_cluster)

    with col02:
        escola_invisivel = st.checkbox("Mostrar escolas",
                                       True,
                                       help="Desmarque essa opção para ocultar os alunos no mapa")
        if escola_invisivel:
            # Adicionando Escolas no Mapa
            for index, location_info in escolas_filtrado1.iterrows():
                folium.Marker([location_info["Latitude"], location_info["Longitude"]],
                              icon=folium.Icon(color="red", icon="info-sign"),
                              popup=location_info["Escola"]).add_to(map)
    folium_static(map, width=870, height=550)  # Printa o gráfico
    st.write(abandono_filtrado1)
