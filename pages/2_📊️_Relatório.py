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

st.markdown(""" ## Procedimento de coleta de dados:
Os dados foram coletados mediante questionário on-line que buscou identificar os seguintes dados:
* Dados de identificação da escola
* Número total de alunos por nível de ensino
* Alunos em situação de abandono escolar – nominalmente indicando aluno /endereço
* Alunos ainda em ensino remoto – nominalmente indicando aluno /endereço

As planilhas com as respostas das escolas podem ser consultadas através do link: [Formulários] (https://drive.google.com/drive/folders/1X1j_DNbZ_k6kksiIyOXvtpQmJEwpnjel?usp=sharing)

O levantamento de dados foi realizado nas escolas estaduais e municipais do município de Bagé.

Escolas que responderam o questionário: 

Escolas Estaduais: 

___
        1. COL ESTADUAL WALDEMAR AMORETTY MACHADO; 2. ESC EST ENS FUN ARTHUR DAME; 3. ESC EST ENS FUN DR ARNALDO FARIAS; 4. ESC EST ENS FUN DR MARIO OLIVE SUNE;
    5. ESC EST ENS FUN FELIX CONTREIRAS RODRIGUES; 6. ESC EST ENS FUN MARTINHO SARAIVA; 7. ESC EST ENS FUN MONSENHOR COSTABILE HIPOLITO; 8. ESC EST ENS FUN PROF JULINHA COSTA TABORDA;
    9. ESC EST ENS FUN SENADOR GETULIO VARGAS; 10. ESC EST ENS MED DR CARLOS ANTONIO KLUWE; 11. ESC EST ENS MED DR LUIZ MARIA FERRAZ; 12. ESC EST ENS MED DR LUIZ MERCIO TEIXEIRA;
    13. ESC EST ENS MED FARROUPILHA; 14. ESC EST ENS MED FREI PLACIDO; 15. ESC EST ENS MED JOSE GOMES FILHO; 16. ESC EST ENS MED PROF LEOPOLDO MAIERON CAIC;
    16. ESC EST ENS MED SILVEIRA MARTINS
___

Escolas Municipais:
___
        1. EMEF ANTONIO FUED KALIL; 2. EMEF ANTONIO SA; 3. EMEF DR ANTENOR GONCALVES PEREIRA (Geteco); 4. EMEF DR CANDIDO BASTOS; 5. EMEF DR DARCY AZAMBUJA; 6. EMEF DR JOAO SEVERIANO DA FONSECA;
    7. EMEF DR JOAO THIAGO DO PATROCINIO; 8. EMEF DR NICANOR PENA; 9. EMEF DR TELMO CANDIOTA DA ROSA; 10. EMEF FUNDACAO BIDART; 11. EMEF GABRIELA MISTRAL; 12. EMEF GENERAL EMILIO LUIZ MALLET;
    13. EMEF JOSE OTAVIO GONCALVES; 14. EMEF KALIL A KALIL; 15. EMEF MAL JOSE DE ABREU; 16. EMEF MAL MASCARENHAS DE MORAES; 17. EMEF NOSSA SENHORA DAS GRACAS; 18. EMEF PADRE EDGAR AQUINO ROCHA;
    19. EMEF PADRE GERMANO; 20. EMEF PAULO FREIRE; 21. EMEF PEROLA GONCALVES; 22. EMEF PROF PERI CORONEL; 23. EMEF PROFESSOR MANOEL ARIDEU MONTEIRO; 24. EMEF PROFESSOR MIRANDA;
    25. EMEF PROFESSORA MARIA DE LOURDES MACHADO MOLINA; 26. EMEF PROFESSORA RENY DA ROSA COLLARES; 27. EMEF ROBERTO MADUREIRA BURNS; 28. EMEF SANTOS DUMONT; 29. EMEF SAO PEDRO; 30. EMEF TEO VAZ OBINO;
    31. EMEF VEREADOR CARLOS MARIO MERCIO DA SILVEIRA; 32. EMEF VISCONDE RIBEIRO DE MAGALHAES;
___
        33. EMEI ANELISE ABBOTT RAVAZA; 34. EMEI DENER BRAZ ASSUNCAO; 35. EMEI DR JOAO DE DEUS LIMA GALVAO; 36. EMEI FILOMENA KALIL; 37. EMEI JULIETA VILLAMIL BALESTRO; 38. EMEI MANOELINHA ARAUJO; 
    39. EMEI MARIA ALVES PERACA; 40. EMEI MARIANINHA LOPES; 41. EMEI NOSSA SENHORA DO CARMO; 42. EMEI PROFESSOR ANALIO; 43. EMEI PROFESSORA IRIA DE JESUS MACHADO; 44. EMEI PROFESSORA ZITA FERRANDO DE VARGAS; 
    45. EMEI SENADOR DARCY RIBEIRO; 46. EMEI TUPY SILVEIRA; 47. EMEI ANNA MOGLIA; 48. EMEI ZEZE TAVARES; 49. EMREF FAVORINO MERCIO; 50. EMREF LIBIO VINHAS;
    51. EMREF SIMOES PIRES; 52. EMEF PROFESSORA CREUSA BRITO GIORGIS;
___



Escolas que não responderam o questionário: 
* ESC EST ED BAS PROFESSOR JUSTINO COSTA QUINTANA
* ESC EST ENS FUN SAO JUDAS TADEU
* EMEF MANOELA TEITELROIT
* EMEI FREDERICO PETRUCCI
* EMEI LUIZ MARIA FERRAZ
* EMREF ALFREDO VIEIRA


""")

st.markdown(""" ## Informações Relevantes""")

st.markdown(""" ### Localização das escolas de ensino médio em Bagé
A cartografia indica que a maior parte das escolas de ensino médio do município de Bagé ficam localizadas na região central 
da cidade, existindo bairros descobertos por escolas com essa oferta, o que pode condicionar a situação de abandono, em 
especial na pandemia que agravou a situação econômica da população""")

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

st.markdown(""" ### Escolas com numero pequeno de alunos""")

