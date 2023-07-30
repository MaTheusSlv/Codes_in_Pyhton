#Criar 2 conexões:
#   -psycopg2
#   -sqlalchemy
# Fazer select nas vendas de dois meses seguidos um do outro;
# Mostrar a diferença entre eles com o st.metrics;
#
#Algumas implementações com relação a tarefa comparacao

import streamlit as st
from sqlalchemy import create_engine, text
import pandas as pd

st.set_page_config(
    page_title="Comparação de Vendas",
    page_icon=":chart_with_upwards_trend:",
    menu_items={'About': "App criado por Matheus Silva"}
)

st.title("Comparação de Vendas :chart_with_upwards_trend:")
st.caption("Faça a comparação das vendas feitas na sua rede")

st.divider()

#Iniciar conexão com o banco
engine = create_engine('postgresql+psycopg2://chinchila:chinchila@192.168.1.111:5432/techjoin_comercial')
conexao = engine.connect()

#BARRA LATERAL
with st.sidebar:
    
    #Seleção do Ano e Mês
    st.header("Selecione os anos e os meses para a comparação")
    txt_anos = text(f"SELECT DISTINCT EXTRACT(year FROM datahorafechamento)::int FROM venda ORDER BY 1")
    queryano = pd.read_sql_query(txt_anos, conexao)
    
    escolha_mes1 = st.selectbox("Selecione o Mês 1",
                 ("Janeiro","Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"))
    escolha_ano1 = st.selectbox("Selecione o Ano do Mês 1", queryano['extract'][1:4], key="key")
    
    st.divider()

    escolha_mes2 = st.selectbox("Selecione o Mês 2",
                 ("Janeiro","Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"))
    escolha_ano2 = st.selectbox("Selecione o Ano do Mês 2", queryano['extract'][1:4], key="key2")
    
#Condição do 1° mês selecionado
if escolha_mes1 == "Janeiro" : mes_selecionado1 = "01"
if escolha_mes1 == "Fevereiro" : mes_selecionado1 = "02"
if escolha_mes1 == "Março" : mes_selecionado1 = "03"
if escolha_mes1 == "Abril" : mes_selecionado1 = "04"
if escolha_mes1 == "Maio" : mes_selecionado1 = "05"
if escolha_mes1 == "Junho" : mes_selecionado1 = "06"
if escolha_mes1 == "Julho" : mes_selecionado1 = "07"
if escolha_mes1 == "Agosto" : mes_selecionado1 = "08"
if escolha_mes1 == "Setembro" : mes_selecionado1 = "09"
if escolha_mes1 == "Outubro" : mes_selecionado1 = "10"
if escolha_mes1 == "Novembro" : mes_selecionado1 = "11"
if escolha_mes1 == "Dezembro" : mes_selecionado1 = "12"
#Condição do 2° mês selecionado
if escolha_mes2 == "Janeiro" : mes_selecionado2 = "01"
if escolha_mes2 == "Fevereiro" : mes_selecionado2 = "02"
if escolha_mes2 == "Março" : mes_selecionado2 = "03"
if escolha_mes2 == "Abril" : mes_selecionado2 = "04"
if escolha_mes2 == "Maio" : mes_selecionado2 = "05"
if escolha_mes2 == "Junho" : mes_selecionado2 = "06"
if escolha_mes2 == "Julho" : mes_selecionado2 = "07"
if escolha_mes2 == "Agosto" : mes_selecionado2 = "08"
if escolha_mes2 == "Setembro" : mes_selecionado2 = "09"
if escolha_mes2 == "Outubro" : mes_selecionado2 = "10"
if escolha_mes2 == "Novembro" : mes_selecionado2 = "11"
if escolha_mes2 == "Dezembro" : mes_selecionado2 = "12"

#Querys das vendas
txt_query1 = text(f"SELECT COUNT(id) FROM venda WHERE datahorafechamento BETWEEN /*Primeiro dia do mês*/ date_trunc('month','{escolha_ano1}-{mes_selecionado1}-01'::date)::date AND /*último dia do mês*/ (date_trunc('month','{escolha_ano1}-{mes_selecionado1}-01'::date)+interval '1 month'-interval '1 day')::date")
query1 = pd.read_sql_query(txt_query1, conexao)
resultado1 = int(query1['count'][0])

txt_query2 = text(f"SELECT COUNT(id) FROM venda WHERE datahorafechamento BETWEEN /*Primeiro dia do mês*/ date_trunc('month','{escolha_ano2}-{mes_selecionado2}-01'::date)::date AND /*último dia do mês*/ (date_trunc('month','{escolha_ano2}-{mes_selecionado2}-01'::date)+interval '1 month'-interval '1 day')::date")
query2 = pd.read_sql_query(txt_query2, conexao)
resultado2 = int(query2['count'][0])

#Calculos das diferenças
diferenc = abs(resultado1 - resultado2)
delta = int((resultado2 - resultado1)/resultado1 * 100)

#DASHBOARD
col1, col2 = st.columns(2)
col1.metric(f"Vendas do Mês de {escolha_mes1} de {escolha_ano1}", resultado1, "Mês 1", "off")
col2.metric(f"Vendas do Mês de {escolha_mes2} de {escolha_ano2}", resultado2, "Mês 2", "off")

st.divider()
col1, col2, col3 = st.columns(3)
col1.text(" ")
col2.metric("A diferença foi de:", diferenc, f"{delta} %")
col3.text(" ")