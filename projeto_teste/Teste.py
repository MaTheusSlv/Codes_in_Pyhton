#Projetinho de teste pra testar o Pythin no streamlit

import streamlit as st
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, text

#título da pagina
st.title("Esse é o Title da página")

#cabeçalho da pagina
st.header("Esse é o Header da página")

#uma imagem de exemplo
st.image(
    '/home/techjoin/Área de Trabalho/Projetos_PY/projeto_teste/streamlit.png',
    caption='Logo do Streamlit',
    )

st.divider()

#lorem ipsum classico
with st.container():
    st.subheader("_Titulo do lorem ipsum_")
    st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vitae erat ac tortor fermentum ultrices non at risus. Aliquam et augue ut lorem efficitur scelerisque. Curabitur imperdiet eu leo vulputate imperdiet. Vivamus at porttitor justo. Pellentesque ut lorem sapien. Fusce quis velit facilisis, tincidunt libero sit amet, sodales orci. Sed ac interdum tortor, eu interdum enim. Maecenas rhoncus iaculis suscipit. Nulla molestie, mi at mollis semper, est lacus eleifend nisl, et sagittis orci elit quis nunc. In eget ligula non ex imperdiet pretium sed vitae enim. Duis condimentum metus elit, sed tincidunt risus pulvinar finibus. Nam semper nisl vitae massa convallis bibendum. Duis semper dictum turpis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris tristique, tortor consectetur pulvinar blandit, leo neque auctor augue, at ullamcorper lacus metus sed ligula")
    
    st.divider()

#lorem ipsum puxado do banco
    st.subheader("_Titulo do lorem ipsum puxado do banco_")

    engine = create_engine('postgresql+psycopg2://postgres:supertux@localhost:5432/projeto_teste')
    conexao = engine.connect()
    txt_query1 = text("SELECT * FROM tabeladeteste")
    query1 = pd.read_sql_query(txt_query1, conexao)
    resultado1 = query1['texto'][0]
    st.write(f"{resultado1}")
    
#Um expansor
st.divider()
expandir=st.expander("**Eu consigo expandir, clique aqui!**")
expandir.write("Você me **expandiu!!!**")
expandir.image('/home/techjoin/Área de Trabalho/Projetos_PY/projeto_teste/soriso.png', width=200)

