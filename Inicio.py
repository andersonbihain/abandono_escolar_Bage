import streamlit as st
from streamlit.logger import get_logger
#A primeira vez tem que rodar com esse comando C:\Users\ander\PycharmProjects\Dash_abandono\main.py [ARGUMENTS]#
#conda install -c conda-forge folium


LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        layout="wide",
        page_title="Início",
        page_icon="👋",
    )

    st.write("# Cartografia dos excluídos da escola: os efeitos do Covid no município de Bagé")
    st.sidebar.success("Selecione uma opção acima.")
    st.markdown("""
        >> Responsáveis
                                        
        > Amélia Rota Borges de Bastos
        
        > Anderson Luís Jeske Bihain
          
    
        Essa pesquisa foi realizada em parceria com o Ministério Público do Rio Grande do Sul (MP) - seção Bagé, e buscou 
        mapear estudantes do município de Bagé, em idade escolar obrigatória que, após a pandemia, não retornaram aos estudos.
        O estudo compõe o projeto do MP intitulado: Busca Ativa e recuperação de Aprendizagem, que tem como objetivo o 
        planejamento de ações com vistas a reintegração dos estudantes ao ambiente escolar, bem como, a recuperação das 
        lacunas educacionais geradas no período pandêmico. O estudo, de característica quantitativa, foi realizado com 
        escolas estaduais e municipais do município e objetivou identificar situação de abandono escolar em ambas as redes,
        de forma a subsidiar o MP nas ações relacionadas ao projeto Busca Ativa.
        
        **👈 Selecione o que deseja visualizar na barra lateral!
        ### Quer saber mais?
        - Amélia Rota Borges [e-mail:](anmeliaborges@unipampa.edu.br)
        - Anderson Luís Jeske Bihain [e-mail:](andersonbihain@unipampa.edu.br)
        - Universidade Federal do Pampa [UNIPAMPA](https://unipampa.edu.br/bage/)
    """
    )

if __name__ == "__Inicio__":
    run()
