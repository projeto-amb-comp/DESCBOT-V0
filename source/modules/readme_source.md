# ChatPDFAPI

## Visão Geral
Este é um módulo Python desenvolvido para interagir com a API ChatPDF. Ele permite enviar perguntas em formato PDF para a API e receber respostas com base no conteúdo do PDF.

## Requisitos
- Python 3.x
- Biblioteca `requests`

## Instalação
1. Clone este repositório para o seu ambiente local:
    ```
    git clone https://github.com/seu_usuario/seu_repositorio.git
    ```
2. Certifique-se de ter o Python instalado em sua máquina. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).
3. Instale a biblioteca `requests` usando o seguinte comando:
    ```
    pip install requests
    ```

## Utilização
Para usar o módulo, siga estas etapas:

1. **Inicialização do Objeto `ChatPDFAPI`**:
   
   ```python
   from ChatPDFAPI import ChatPDFAPI

   # Inicialização do objeto ChatPDFAPI
   api_key = 'SUA_API_KEY_AQUI'
   file_path = 'Caminho/para/seu/arquivo.pdf'
   api = ChatPDFAPI(api_key, file_path)

Substitua 'SUA_API_KEY_AQUI' pela sua chave de API fornecida pela ChatPDF e 'Caminho/para/seu/arquivo.pdf' pelo caminho do seu arquivo PDF.

Enviar uma pergunta para o PDF:

pergunta = "Qual é a resposta para a pergunta?"
resposta = api.pergunta_pdf(pergunta)
print(resposta)


## Métodos Principais

__init__(self, api_key, file_path=None, file_content=None)
Inicializa o objeto ChatPDFAPI com a chave da API fornecida e o caminho do arquivo PDF ou conteúdo do arquivo.

**api_key:** Sua chave de API fornecida pela ChatPDF.

**file_path:** O caminho para o arquivo PDF.

**file_content:** O conteúdo do arquivo PDF.

**pergunta_pdf(self, pergunta)**

Envia uma pergunta para o PDF e retorna a resposta.

**pergunta:** A pergunta a ser feita ao PDF.

pergunta_pdf_with_context(self, pergunta)

Envia uma pergunta para o PDF com contexto adicional e retorna a resposta.

**pergunta:** A pergunta a ser feita ao PDF com contexto adicional.
