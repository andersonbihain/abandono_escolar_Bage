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

def main3():
    data3 = pd.read_csv('estadual.csv')
    return data3

def main4():
    data4 = pd.read_csv('municipal.csv')
    return data4

def main5():
    data5 = pd.read_csv('infantil.csv')
    return data5

abandono = main1()
escolas = main2()
estadual = main3()
municipal = main4()
infantil = main5()

st.sidebar.markdown("# Relatório 📊️")

st.write("# Relatório do abandono escolar em Bagé/RS")

st.markdown(""" ## Procedimento de coleta de dados:
Os dados foram coletados mediante questionário on-line que buscou identificar os seguintes dados:
* Dados de identificação da escola
* Número total de alunos por nível de ensino
* Alunos em situação de abandono escolar – identificação de aluno/escola/endereço
* Alunos em ensino remoto – identificação de aluno/escola/endereço

As planilhas com as respostas das escolas podem ser consultadas através do link: [Formulários](https://drive.google.com/drive/folders/1X1j_DNbZ_k6kksiIyOXvtpQmJEwpnjel?usp=sharing)
""")

col1, col2 = st.columns(2)

with col1:
   st.header("Escolas participantes")
   st.write("O levantamento de dados foi realizado nas 75 escolas publicas do município de Bagé, destas, 69 Escolas responderam"
       "o questionários, estando distribuidas da seguinte maneira:")

with col2:
   labels = 'Não respondeu', 'Não indicou abandonos', 'Respondeu e informou abandonos'
   sizes = [6, 42, 27]
   explode = (0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
   fig1, ax1 = plt.subplots()
   ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
           shadow=True, startangle=90)
   ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
   st.pyplot(fig1)

st.markdown(""" 17 Escolas Estaduais: 
___
        1. COL ESTADUAL WALDEMAR AMORETTY MACHADO; 2. ESC EST ENS FUN ARTHUR DAME; 3. ESC EST ENS FUN DR ARNALDO FARIAS; 4. ESC EST ENS FUN DR MARIO OLIVE SUNE;
    5. ESC EST ENS FUN FELIX CONTREIRAS RODRIGUES; 6. ESC EST ENS FUN MARTINHO SARAIVA; 7. ESC EST ENS FUN MONSENHOR COSTABILE HIPOLITO; 8. ESC EST ENS FUN PROF JULINHA COSTA TABORDA;
    9. ESC EST ENS FUN SENADOR GETULIO VARGAS; 10. ESC EST ENS MED DR CARLOS ANTONIO KLUWE; 11. ESC EST ENS MED DR LUIZ MARIA FERRAZ; 12. ESC EST ENS MED DR LUIZ MERCIO TEIXEIRA;
    13. ESC EST ENS MED FARROUPILHA; 14. ESC EST ENS MED FREI PLACIDO; 15. ESC EST ENS MED JOSE GOMES FILHO; 16. ESC EST ENS MED PROF LEOPOLDO MAIERON CAIC;
    16. ESC EST ENS MED SILVEIRA MARTINS
___
52 Escolas Municipais (36 EMEF e 16 EMEI):
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

Ainda 6 escolas não responderam o questionário: 
* ESC EST ED BAS PROFESSOR JUSTINO COSTA QUINTANA
* ESC EST ENS FUN SAO JUDAS TADEU
* EMEF MANOELA TEITELROIT
* EMEI FREDERICO PETRUCCI
* EMEI LUIZ MARIA FERRAZ
* EMREF ALFREDO VIEIRA
""")

st.markdown(""" ## Informações Relevantes""")

st.markdown(""" ### Estatísticas Gerais""")
est_tot_fund = estadual['Total Fundamental'].sum() #total de alunos no ensino fundamental no estado
est_tot_med = estadual['Total Médio'].sum() #total de alunos no ensino médio no estado

#exemplo = escolas.loc[escolas['Tipo'] == 'Estadual', 'Alunos'].sum()

st.write("De acordo com as respostas das escolas publicas do município de Bagé, existem", estadual['Total Alunos'].sum()+municipal['Total Alunos'].sum(),
         "alunos matriculados, distribuidos da seguinte maneira:", estadual['Total Alunos'].sum(),
         "em escolas estaduais e", municipal['Total Alunos'].sum() , "em escolas municipais. Esses alunos estão distribuidos"
         "por série de acordo com a tabela abaixo:")
total_pre=municipal['Pré I'].sum()+municipal['Pré II'].sum()
total_fundamental=municipal['1°'].sum()+estadual['1°'].sum()+municipal['2°'].sum()+estadual['2°'].sum()+municipal['3°'].sum()+estadual['3°'].sum()+municipal['4°'].sum()+estadual['4°'].sum()+municipal['5°'].sum()+estadual['5°'].sum()+municipal['6°'].sum()+estadual['6°'].sum()+municipal['7°'].sum()+estadual['7°'].sum()+municipal['8°'].sum()+estadual['8°'].sum()+municipal['9°'].sum()+estadual['9°'].sum()
total_medio=estadual['1° Médio'].sum()+estadual['2° Médio'].sum()+estadual['3° Médio'].sum()
tabela=pd.DataFrame(([["Pré-Escola",total_pre],
                      ["Pré I", municipal['Pré I'].sum()],
                      ["Pré II", municipal['Pré II'].sum()],
                      ["Ensino Fundamental",total_fundamental],
                      ["1°", municipal['1°'].sum()+estadual['1°'].sum()],
                      ["2°", municipal['2°'].sum()+estadual['2°'].sum()],
                      ["3°", municipal['3°'].sum()+estadual['3°'].sum()],
                      ["4°", municipal['4°'].sum()+estadual['4°'].sum()],
                      ["5°", municipal['5°'].sum()+estadual['5°'].sum()],
                      ["6°", municipal['6°'].sum()+estadual['6°'].sum()],
                      ["7°", municipal['7°'].sum()+estadual['7°'].sum()],
                      ["8°", municipal['8°'].sum()+estadual['8°'].sum()],
                      ["9°", municipal['9°'].sum()+estadual['9°'].sum()],
                      ["Ensino Médio", total_medio],
                      ["1°", estadual['1° Médio'].sum()],
                      ["2°", estadual['2° Médio'].sum()],
                      ["3°", estadual['3° Médio'].sum()]]),
                    columns=['Turma', 'Número de alunos'])
st.table(tabela) #imprime tabela das escolas

use_escolas_detalhado = st.checkbox(
    "Ver matriculas por escola", False, help="Use esse botão para ver a distribuição de alunos matriculados por escola em cada turma"
)

if use_escolas_detalhado:
    juntar = pd.concat([municipal, estadual])
    categorias2 = list(juntar['Escola'].unique())  # lista as escolas para escolher
    categoria2 = st.selectbox('Clique na lista para escolher uma escola', options=categorias2)
    df_categoria2 = juntar.query('Escola == @categoria2')  # filtra por nome da escola
    st.write(df_categoria2)

st.markdown(""" ### Localização das escolas de ensino médio em Bagé
A cartografia indicou que, a maior parte das escolas de ensino médio do município de Bagé, ficam localizadas na região central 
da cidade, existindo bairros descobertos por escolas com essa oferta, o que pode condicionar a situação de abandono, em 
especial, na pandemia, que agravou a situação econômica de muitas familias""")

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

st.markdown(""" ### Sugestões
Os resultados da cartografia sugerem algumas ações possíveis, a serem avaliadas pelo Ministério Público e secretarias 
municipal e estadual de educação. São elas: 

> 1. Necessidade de sistemas interligados de comunicação sobre informações educacionais das diferentes redes do município;

> 2. Ações de resgate dos estudantes em situação de abandono, antes do período de matrícula, de forma a garantir a realização de matrícula para 2023;

> 3. Ações articuladas com Conselho Tutelar para busca ativa dos estudantes em situação de abandono, bem como, de 
acompanhamento preventivo aos estudantes, como forma de evitar novos abandonos;

> 4. Ações de conscientização e responsabilização dos pais em virtude da ocorrência de crime de abandono intelectual;

> 5. Planejamento de ações com vistas a recuperação da aprendizagem de alunos em situação de abandono;

""")
