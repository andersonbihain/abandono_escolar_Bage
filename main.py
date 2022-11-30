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

    st.write("# Abandono escolar Bagé/RS! 👋")
    st.sidebar.success("Selecione uma opção acima.")
    st.markdown(
        """
        Esse relatório dinâmico foi elaborado pelos docentes da UNIPAMPA
        Amélia Rota Borges e Anderson Luís Jeske Bihain
        como parte do projeto ... Título do projeto. em parceria com o MP...
        
        
        **👈 Selecione o que deseja visualizar na barra lateral!
        ### Quer saber mais?
        - Amélia Rota Borges [e-mail:](anmeliaborges@unipampa.edu.br)
        - Anderson Luís Jeske Bihain [e-mail:](andersonbihain@unipampa.edu.br)
        - Universidade Federal do Pampa [UNIPAMPA](https://unipampa.edu.br/bage/)
    """
    )

if __name__ == "__main__":
    run()