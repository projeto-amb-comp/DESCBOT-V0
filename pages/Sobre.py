import streamlit as st

st.title('🤖 Quem somos?')

st.write(
    "Somos alunos da Universidade do Estado do Rio de Janeiro (UERJ). E desenvolvemos esse chatbot para aa disciplina Projetos de Ambiente Computacional"
)
with st.expander('Sobre essa aplicação'):
    st.markdown('*O que essa aplicação pode fazer?*')
    st.info('Este projeto foi desenvolvido para facilitar a extração de informações e interações com documentos PDF por meio de uma interface de chat. Utilizando a biblioteca ChatPDF, é possível realizar operações como leitura de texto, busca por palavras-chave, marcação de trechos relevantes e muito mais, tudo de forma automatizada e intuitiva.')

    st.markdown('**Como usar a aplicação?**')
    st.warning('Para iniciar, basta fazer login na sua conta e inserir o Documento que deseja extrair informações. Depois disso, é só perguntar para o chat')

