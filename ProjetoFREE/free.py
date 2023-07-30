#Projeto de ferramenta de validação de bases usando Streamlit

import streamlit as st
import psycopg2 as ps
from sqlalchemy import create_engine, text
import pymysql
import pandas as pd

st.set_page_config(
    page_title="ProjetoFREE",
    page_icon=":chains:",
    menu_items={'About': "App criado por Matheus Silva"}
)

#Título do App
st.title("ProjetoFREE :chains:")

st.write('Preencha as informações da Base Anterior e da Base Oficial')

#Formulário inicial
col1, col2 =  st.columns(2)
    #Base Anterior
with col1:
    st.header('Base Anterior')
    nomebase1 = st.text_input(label='Nome da base', value='_mysql')
    host1 = st.text_input(label='Host', value='192.168.xx.xx')
    porta1 = st.text_input(label='Porta', value='3306')
    user1 = st.text_input(label='UserName', value='root')
    passwd1 = st.text_input(label='Password', type='password')
    #Base Oficial
with col2:
    st.header('Base Oficial')
    nomebase2 = st.text_input(label='Nome da base', value='_oficial')
    host2 = st.text_input(label='Host', value='192.168.xxx.xxx')
    porta2 = st.text_input(label='Porta', value='5433')
    user2 = st.text_input(label='UserName', value='chinchila')
    passwd2 = st.text_input(label='Password ', type='password')

#Conexões com o banco
def conectarbanco():
    engine1 = create_engine(f'mysql+pymysql://{user1}:{passwd1}@{host1}:{porta1}/{nomebase1}')
    conexao1 = engine1.connect()
    engine2 = create_engine(f'postgresql+psycopg2://{user2}:{passwd2}@{host2}:{porta2}/{nomebase2}')
    conexao2 = engine2.connect()

st.button(label='Começar comparação', on_click=conectarbanco, use_container_width=1)

#DASHBOARD
#Registros entre osProjetoFREEAvaliar Perda ou Importação de Sujeira
st.header('Aqui será a comparação 1')

#Registros com caracteres estranhos - Avaliar a mudança que o tratamento gerou na base do cliente
st.header('Aqui será a comparação 2')

#Cadastros duplicados - Avaliar a mudança que o tratamento de dados gerou na base do cliente
st.header('Aqui será a comparação 3')
