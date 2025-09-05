import streamlit as st

st.title("Formulário de Exemplo")

# Criando um formulário
with st.form(key="meu_form"):
    nome = st.text_input("Digite seu nome:")
    idade = st.number_input("Digite sua idade:", min_value=0, max_value=120, step=1)
    opcao = st.selectbox("Escolha uma opção:", ["Opção A", "Opção B", "Opção C"])
    comentario = st.text_area("Deixe um comentário:")

    # Botão de envio
    enviar = st.form_submit_button("Enviar")

# O que acontece depois de enviar
if enviar:
    st.success(f"Obrigado, {nome}! ✅")
    st.write(f"- Idade: {idade}")
    st.write(f"- Opção escolhida: {opcao}")
    st.write(f"- Comentário: {comentario}")