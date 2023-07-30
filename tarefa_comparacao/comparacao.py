#Criar 2 conexões:
#   -psycopg2
#   -sqlalchemy
# Fazer select nas vendas de dois meses seguidos um do outro;
# Mostrar a diferença entre eles com o st.metrics;

import streamlit as st
import psycopg2 as ps
from sqlalchemy import create_engine, text
import pandas as pd

st.title("Comparação de Vendas da Rede 2023")

st.divider()

#Iniciar conexão com o banco
engine = create_engine('postgresql+psycopg2://chinchila:chinchila@192.168.1.111:5432/techjoin_comercial')
conexao = engine.connect()

#Executar as querys
txt_query1 = text("SELECT COUNT(id) FROM venda WHERE datahorafechamento BETWEEN '2023-01-01' AND '2023-01-31'")
query1 = pd.read_sql_query(txt_query1, conexao)
resultado1 = int(query1['count'][0])

txt_query2 = text("SELECT COUNT(id) FROM venda WHERE datahorafechamento BETWEEN '2023-02-01' AND '2023-02-28'")
query2 = pd.read_sql_query(txt_query2, conexao)
resultado2 = int(query2['count'][0])

#Calculos das diferenças
diferenc = abs(resultado1 - resultado2)
delta = int((resultado2 - resultado1)/resultado1 * 100)

#DASHBOARD
col1, col2 = st.columns(2)
col1.metric("Vendas do Mês de Janeiro", resultado1)
col2.metric("Vendas do Mês de Fevereiro", resultado2)

st.divider()

col1, col2, col3 = st.columns(3)
col1.text(" ")
col2.metric("A diferença foi de:", diferenc, f"{delta} %")
col3.text(" ")