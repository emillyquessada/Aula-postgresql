import streamlit as st
from crud import criar_aluno, listar_alunos, atualizar_idade, deletar_aluno
#python -m streamlit run app.py
st.set_page_config(page_title= "Gerenciamento de alunos", page_icon= "👥")

st.title("Sistema de alunos com PostgreSQL")

menu = st.sidebar.radio("Menu",["Cadastrar", "Listar", "Atualizar", "Deletar"])

if menu == "Cadastrar":
    st.subheader("➕ Cadastrar alunos")
    nome = st.text_input("Nome", placeholder= "Seu nome")
    idade = st.number_input("Idade", min_value=16, step=1)
    if st.button("Cadastrar"):
        if nome.strip() != "":
            criar_aluno(nome, idade)
            st.success(f"Aluno {nome} cadastrado com sucesso!")
        else: 
            st.warning("O campo nome não pode ser vazio...s")