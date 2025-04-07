import streamlit as st
import pandas as pd
import re
from datetime import date

def gravar_dados(nome, data_cad, idade, tel, tipo, sexo):
    if nome and data_cad <= date.today():
        with open("cliente.csv","a", encoding="utf-8") as file:
            file.write(f"{nome},{data_cad},{idade},{tel},{tipo},{sexo}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False    

st.set_page_config(
    page_title="Cadastro de clientes",
    page_icon="📕"
)

st.title("Cadastro de clientes")
st.divider()

nome = st.text_input("Digite o nome do cliente",
                     key="nome_cliente")

data_cad  = st.date_input("Digite a data de cadastro",
                           format="DD/MM/YYYY")

idade = st.number_input("Selecione a idade",
                        min_value=18,
                        max_value=90)

tel = st.text_input("Digite o numero de telefone:")
padrao = r"^\+?[1-9]\d{1,14}$"

if tel:
    if re.match(padrao, tel):
        st.success("Número válido!")
    else:
        st.error("Número inválido. Use o formato correto, por exemplo: +5511999999999.")


tipo = st.selectbox("Tipo do cliente",
                   ["Pessoa fisica", "Pessoa juridica"] ) 

sexo = st.selectbox("Selecione seu sexo",
                        ["Masculino", "Feminino"])

btn_cadastrar = st.button("Cadastrar",
                          on_click=gravar_dados,
                          args=[nome, data_cad, idade, tel, tipo, sexo])

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!",
                   icon="✅")
        
    else:
        st.error("Houve algum problema no cacadstro!",
                 icon="❌")
            
            
        