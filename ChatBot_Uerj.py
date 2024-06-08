import os
import random
import string
from supabase import create_client, Client
from source.modules.chat_pdf import ChatPDFAPI
from source.modules.supa_base import SupabaseClient
import streamlit as st
from pages.Perguntas_Documento import perguntas_page

if 'config' in st.session_state:
    st.set_page_config(page_title='ChatBot UERJ', page_icon='🤖')
    st.session_state['config']=True

st.title('🤖 ChatBot UERJ')

def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

def login():
    api_key=''
    # Verifica se o usuário já está autenticado
    if 'autenticado' in st.session_state and st.session_state['autenticado']:
        return True
    
    with st.form(key='user_form'):
        email = st.text_input("Digite seu email: ")
        senha = st.text_input("Digite sua senha: ", type="password")
        
        # Botão para autenticar usuário
        submit_button = st.form_submit_button('Autenticar')
        if submit_button:
            success, api_key = supabase_client.autentica_dados(email, senha)
            if success:
                st.success("Login bem-sucedido!")
                st.session_state['autenticado'] = True
                st.session_state['user_key'] =  api_key
                return True
            else:
                st.error("Email ou senha inválidos")
                return False
    # Movendo a criação de novo usuário para fora do formulário de login
    with st.form(key='new_user_form'):
        create_user_button = st.form_submit_button('Criar novo usuário')
        if create_user_button:
            nome = st.text_input("Digite seu nome para registro: ", key='nome_registro')
            email_registro = st.text_input("Digite seu email para registro: ", key='email_registro')
            senha_registro = st.text_input("Digite sua senha para registro: ", type="password", key='senha_registro')
            user_api_key = st.text_input("Digite sua chave API para registro: ", key='user_api_key')
            
            if nome and email_registro and senha_registro and user_api_key:
                result = supabase_client.insere_dados(nome, email_registro, senha_registro, user_api_key)
                if result:
                    st.success("Usuário criado com sucesso! Por favor, autentique-se.")
                else:
                    st.error("E-mail já cadastrado")
            else:
                st.warning("Por favor, preencha todos os campos para registro.")


supabase = init_connection()
supabase_client = SupabaseClient(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False  # Inicializa a sessão como não autenticada
if login():
    if 'indice_pergunta' not in st.session_state:

        with st.expander('Sobre essa aplicação'):
            st.markdown('*O que essa aplicação pode fazer?*')
            st.info('Este projeto foi desenvolvido para facilitar a extração de informações e interações com documentos PDF por meio de uma interface de chat. Utilizando a biblioteca ChatPDF, é possível realizar operações como leitura de texto, busca por palavras-chave, marcação de trechos relevantes e muito mais, tudo de forma automatizada e intuitiva.')

            st.markdown('**Como usar a aplicação?**')
            st.warning('Para iniciar, basta inserir sua Key do framework ChatPDF e o Documento que deseja extrair informações. Depois disso, é só perguntar para o chat')


        st.subheader('Insira seu Documento Para inicializar')
        user_key = st.session_state['user_key']
        uploaded_file = st.file_uploader('Envie um documento PDF:', type=['pdf'])


    if 'indice_pergunta' not in st.session_state or st.session_state['indice_pergunta']>10:

        USER = "user"
        ASSISTANT = "assistant"
        MESSAGES = "messages"
        if (uploaded_file is not None) and (len(user_key)>0):
            if (MESSAGES not in st.session_state):
                file_contents = uploaded_file.read()
                chat1 = ChatPDFAPI(api_key=user_key,file_content=file_contents)
                st.session_state['CHAT']=chat1
                bemvindo="Olá !!! O que deseja saber sobre esse Documento?"
                st.session_state[MESSAGES] =  [{'role': ASSISTANT,'content':bemvindo}]

            for msg in st.session_state[MESSAGES]:
                st.chat_message(msg.get('role')).write(msg.get('content'))

            prompt: str = st.chat_input("Escreva sua dúvida aqui:")

            if prompt and uploaded_file is not None and len(user_key)>0:
                st.session_state[MESSAGES].append({'role': USER,'content':prompt})
                st.chat_message(USER).write(prompt)
                request=st.session_state[MESSAGES]
                if len(st.session_state[MESSAGES])>6:
                    request= st.session_state[MESSAGES][-6:]
                resposta = st.session_state['CHAT'].pergunta_pdf_with_context(request)
                response = f"{resposta}"
                st.session_state[MESSAGES].append({'role': ASSISTANT,'content':resposta})
                st.chat_message(ASSISTANT).write(response) 


    if 'CHAT' in st.session_state:
        if 'PERGUNTAS' not in st.session_state:
            st.session_state['PERGUNTAS'] = st.session_state['CHAT'].pergunta_pdf_with_context([{'role': USER,'content':'Com base nesse documento, crie o máximo de perguntas possíveis sobre a matéria abordada nesse documento'}])
            st.session_state['PERGUNTAS'] = st.session_state['PERGUNTAS'].split("\n")
        if 'indice_pergunta' not in st.session_state:
            st.sidebar.button("Perguntas sobre o Documento", on_click=perguntas_page)
        else:
            if st.session_state['indice_pergunta']<10:
                perguntas_page()
