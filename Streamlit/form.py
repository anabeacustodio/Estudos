import streamlit as st
from datetime import date, time

st.title("🔹'Formulário de Login/Cadastro'🔹")

# Criando um formulário
with st.form(key="login_form"):
    st.write("Por favor, preencha os campos abaixo:")

    # Texto (usuário)
    usuario = st.text_input("Usuário:", max_chars=20)

    # Senha (fica escondida)
    senha = st.text_input("Senha:", type="password")

    # Número (idade)
    idade = st.number_input("Digite sua idade:", min_value=0, max_value=120, step=1)

    # Selectbox (seleção única)
    opcao = st.selectbox("Selecione seu perfil:", ["Usuário comum", "Administrador", "Convidado"])

    # Multiselect (multiplas seleções)
    interesses = st.multiselect("Selecione seus interesses:", ["Backend", "Frontend", "Python", "Java", "Design"])

    # Radio (escolha única)
    genero = st.radio("Gênero:", ["Masculino", "Feminino", "Outro"])

    # Área de texto (comentários, bio, descrição)
    comentario = st.text_area("Fale um pouco sobre você:")

    # Checkbox (termos e condições)
    termos = st.checkbox("Aceito os termos e condições")
    
    # Slider (exemplo de ajuste de preferência)
    experiencia = st.slider("Nível de experiência:", 0, 10, 5)

    # Data e hora
    aniversario = st.date_input("Data de nascimento", min_value=date(1900,1,1), max_value=date.today()) # o padrão do streamlit para data é no formato inglês (yyyy/mm/dd)
    hora_preferida = st.time_input("Hora preferida para contato:", value=time(9, 0))

    # Botão de envio
    enviar = st.form_submit_button("Enviar")

# O que acontece depois de enviar
if enviar:
    if not termos:
        st.error("Você precisa aceitar os termos e condições para continuar.")
    else:
        usuario = usuario if usuario else "Anônimo"
        st.success(f"Bem-vindo, {usuario}! ✅")