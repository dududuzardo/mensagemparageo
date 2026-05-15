import streamlit as st
from datetime import date

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="TE AMO GEO", page_icon="🫀", layout="centered")

# 2. ESTÉTICA DO SITE
st.markdown("""
    <style>
    /* Cor de fundo da página inteira */
    .stApp {
        background-color: #fcf4f8; 
    }
    
    /* Cor do texto do título */
    h1 {
        color: #634b5c !important; 
    }

    /* Estilizar o botão */
    .stButton>button { 
        border-radius: 30px; 
        height: 3em;
        background-color: #e5a4bc; 
        color: white !important; 
        border: none;
        font-size: 18px;
        font-weight: bold;
        transition: 0.3s;
        box-shadow: 0 4px 10px rgba(229, 164, 188, 0.4); 
    }
    
    /* Efeito quando passa o mouse no botão */
    .stButton>button:hover {
        background-color: #d188a3;
        transform: scale(1.05);
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. O SEU "BANCO DE DADOS" DE MENSAGENS
mensagens_diarias = {
    "2026-05-15": "Oiiiiiii, essa é a primeira mensagem pra vc geovanna vasconcelos, ou melhor, amor da minha vida. Volte amanhã",
    "2026-05-16": "nada por aqui hj princesa, volte amanhã",
    "2026-05-17": "Hmmmmmmmmm, ainda não, volte AMANHÃ...",
    "2026-05-18": "FELIZ NOSSO DIA, eu te amo ininitamente meu amor, e criaria mais infinitos sites pra dizer isso. BEIJOOOOS. já tô com sdd..."
}

# 4. INTERFACE DO SITE
st.markdown("<h1 style='text-align: center; margin-bottom: 30px;'>mensagem do dia para o meu amor</h1>", unsafe_allow_html=True)

# CRIANDO COLUNAS PARA PRENDER O BOTÃO NO CENTRO
# A proporção [1, 1.5, 1] cria um espaço ideal no meio para o botão
col1, col2, col3 = st.columns([1, 1.5, 1])

# Colocamos o botão apenas na coluna do meio
with col2:
    # use_container_width=True força o botão a preencher a coluna do meio de forma simétrica
    clicou = st.button('Ler a mensagem de hoje', use_container_width=True)

# Ação que acontece ao clicar
if clicou:
    hoje = str(date.today())
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if hoje in mensagens_diarias:
        msg = mensagens_diarias[hoje]
        
        # Cartão da mensagem centralizado (margin: 0 auto faz o trabalho aqui)
        st.markdown(f"""
            <div style='background-color: #ffffff; padding: 40px; border-radius: 20px; text-align: center; box-shadow: 0 8px 20px rgba(229, 164, 188, 0.15); border: 1px solid #fae6f0; max-width: 600px; margin: 0 auto;'>
                <h3 style='color: #634b5c; line-height: 1.6; font-weight: 500; margin: 0;'>{msg}</h3>
            </div>
        """, unsafe_allow_html=True)
        
    else:
        st.markdown("""
            <div style='background-color: #ffffff; padding: 20px; border-radius: 15px; text-align: center; border: 1px solid #e2e8f0; max-width: 500px; margin: 0 auto;'>
                <p style='color: #a08b98; margin: 0; font-size: 18px;'>Ainda não há mensagem para hoje. Volte amanhã! 🕰️</p>
            </div>
        """, unsafe_allow_html=True)
