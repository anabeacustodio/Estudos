import streamlit as st
from datetime import date, time
import pandas as pd

st.set_page_config(layout="wide")
st.title("🔹'Formulário de Login/Cadastro'🔹")

# --- Inicialização da sessão ---
if "envios" not in st.session_state:
    st.session_state["envios"] = []
if "form_key" not in st.session_state:
    st.session_state["form_key"] = 0
# Variável para controlar a exibição da mensagem de sucesso
if "show_success" not in st.session_state:
    st.session_state["show_success"] = False
if "usuario_salvo" not in st.session_state:
    st.session_state["usuario_salvo"] = ""

# --- Formulário ---
# A chave (key) do formulário é crucial para o reset.
# Usamos st.session_state.form_key para que ela mude a cada envio.
with st.form(key=f"login_form_{st.session_state.form_key}"):
    st.write("Por favor, preencha os campos abaixo:")

    # Texto (usuário)
    usuario = st.text_input("Usuário:", max_chars=20)

    # Senha (fica escondida)
    senha = st.text_input("Senha:", type="password")

    # Número (idade)
    idade = st.number_input("Digite sua idade:", min_value=0, max_value=120, step=1, value=0)

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
    aniversario = st.date_input("Data de nascimento", min_value=date(1900,1,1), max_value=date.today(), value=date(2000,1,1)) # o padrão do streamlit para data é no formato inglês (yyyy/mm/dd)
    hora_preferida = st.time_input("Hora preferida para contato:", value=time(9, 0))

    # Botão de envio
    enviar = st.form_submit_button("Enviar")

# --- Lógica de envio ---
if enviar:
    if not termos:
        st.error("Você precisa aceitar os termos de uso para continuar.")
    else:
        # Salva os dados
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

        # Define as variáveis de estado para exibir a mensagem
        st.session_state.show_success = True
        st.session_state.usuario_salvo = usuario

        # Incrementa a chave do formulário e força o recarregamento.
        # Isso faz com que o Streamlit "perceba" que é um novo formulário e o renderize com valores iniciais.
        st.session_state.form_key += 1
        st.rerun()

# --- Exibição da mensagem de sucesso ---
if st.session_state.show_success:
    st.success(f"Bem-vindo, {st.session_state.usuario_salvo}! ✅ Dados salvos. Formulário será limpo para o próximo usuário.")
    # Reseta as variáveis de estado para que a mensagem não apareça novamente
    st.session_state.show_success = False
    st.session_state.usuario_salvo = ""

# --- Exibição da tabela ---
st.write("---")
if st.session_state.envios:
    st.subheader("Tabela de Envios")
    df = pd.DataFrame(st.session_state.envios)
    st.dataframe(df, use_container_width=True)
else:
    st.info("Nenhum envio ainda. Preencha o formulário para adicionar um novo usuário.")