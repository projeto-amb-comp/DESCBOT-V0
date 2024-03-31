from source.modules.chat_pdf import ChatPDFAPI
import streamlit as st
from dataclasses import dataclass

@dataclass
class MessageData:
    user: str
    texto: str
# Page title
st.set_page_config(page_title='ChatBot Uerj', page_icon='🤖')
st.title('🤖 ChatBot Uerj')

with st.expander('Sobre essa aplicação'):
  st.markdown('*O que essa aplicação pode fazer?*')
  st.info('Este projeto foi desenvolvido para facilitar a extração de informações e interações com documentos PDF por meio de uma interface de chat. Utilizando a biblioteca ChatPDF, é possível realizar operações como leitura de texto, busca por palavras-chave, marcação de trechos relevantes e muito mais, tudo de forma automatizada e intuitiva.')

  st.markdown('**Como usar a aplicação?**')
  st.warning('Para iniciar, basta inserir sua Key do ChatPDF e o Documento que deseja extrair informações. Depois disso, é só perguntar para o chat')


st.subheader('Insira seu Documento e sua Key Para inicializar')
user_key = st.text_input('Digite sua key:', key='chave')
uploaded_file = st.file_uploader('Envie um documento PDF:', type=['pdf'])
if uploaded_file is not None and len(user_key)>0:
    file_contents = uploaded_file.read()
    chat1 = ChatPDFAPI(api_key=user_key,file_content=file_contents)

USER = "user"
ASSISTANT = "assistant"
MESSAGES = "messages"
if (uploaded_file is not None) and (len(user_key)>0):
    if (MESSAGES not in st.session_state):
        st.session_state[MESSAGES] = [MessageData(user=ASSISTANT, texto="Olá !!! O que deseja saber sobre esse Documento?")]

    msg: MessageData
    for msg in st.session_state[MESSAGES]:
        st.chat_message(msg.user).write(msg.texto)

    prompt: str = st.chat_input("Escreva sua dúvida aqui:")

    if prompt and uploaded_file is not None and len(user_key)>0:
        st.session_state[MESSAGES].append(MessageData(user=USER, texto=prompt))
        st.chat_message(USER).write(prompt)
        resposta = chat1.pergunta_pdf(prompt)
        response = f"{resposta}"
        st.session_state[MESSAGES].append(MessageData(user=ASSISTANT, texto=response))
        st.chat_message(ASSISTANT).write(response) 