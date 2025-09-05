import streamlit as st
from datetime import date, time
import pandas as pd

st.title("🔹'Formulário de Login/Cadastro'🔹")

# Lista de campos do formulário (usada para inicialização e reset)
campos = ["usuario", "senha", "idade", "perfil", "interesses", "genero", "bio", "termos", "nivel", "aniversario", "hora_preferida"]

# Inicializando a lista de envios no session_state (sempre primeiro)
if "envios" not in st.session_state:
    st.session_state["envios"] = []

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
    perfil = st.selectbox("Selecione seu perfil:", ["Usuário comum", "Administrador", "Convidado"])

    # Multiselect (multiplas seleções)
    interesses = st.multiselect("Selecione seus interesses:", ["Backend", "Frontend", "Python", "Java", "Design"])

    # Radio (escolha única)
    genero = st.radio("Gênero:", ["Masculino", "Feminino", "Outro"])

    # Área de texto (comentários, bio, descrição)
    bio = st.text_area("Fale um pouco sobre você:")

    # Checkbox (termos e condições)
    termos = st.checkbox("Aceito os termos e condições")
    
    # Slider (exemplo de ajuste de preferência)
    nivel = st.slider("Nível de experiência:", 0, 10, 5)

    # Data e hora
    aniversario = st.date_input("Data de nascimento", min_value=date(1900,1,1), max_value=date.today()) # o padrão do streamlit para data é no formato inglês (yyyy/mm/dd)
    hora_preferida = st.time_input("Hora preferida para contato:", value=time(9, 0))

    # Botão de envio
    enviar = st.form_submit_button("Enviar")

# O que acontece depois de enviar
if enviar:
    if not termos:
        st.error("Você precisa aceitar os termos de uso para continuar.")
    else:
        aniversario_formatado = aniversario.strftime("%d/%m/%Y")
        envio = {
            "Usuário": usuario,
            "Idade": idade,
            "Perfil": perfil,
            "Interesses": ", ".join(interesses) if interesses else "Nenhum",
            "Gênero": genero,
            "Bio": bio,
            "Nível": nivel,
            "Aniversário": aniversario_formatado,
            "Hora preferida": hora_preferida.strftime("%H:%M")
        }
        st.session_state.envios.append(envio)
        st.success(f"Bem-vindo, {usuario}! ✅")

        # Resetando os campos do formulário
        for campo in campos:
            if campo in ["usuario"]:
                st.session_state[campo] = ""
            elif campo in ["senha"]:
                st.session_state[campo] = ""
            elif campo in ["idade"]:
                st.session_state[campo] = 0
            elif campo in ["perfil"]:
                st.session_state[campo] = "Usuário comum"
            elif campo in ["interesses"]:
                st.session_state[campo] = []
            elif campo in ["genero"]:
                st.session_state[campo] = "Masculino"
            elif campo in ["bio"]:
                st.session_state[campo] = ""
            elif campo in ["termos"]:
                st.session_state[campo] = False
            elif campo in ["nivel"]:
                st.session_state[campo] = 5
            elif campo in ["aniversario"]:
                st.session_state[campo] = date(2000,1,1)
            elif campo in ["hora_preferida"]:
                st.session_state[campo] = time(9,0)
            else:
                st.session_state[campo] = ""

        st.rerun()  # Recarrega o app para limpar o formulário

# Exibindo tabela de envios
if st.session_state.envios:
    df = pd.DataFrame(st.session_state.envios)
    st.subheader("Tabela de Envios")
    st.dataframe(df)