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

# BusinessError

## Visão Geral
`BusinessError` é uma exceção personalizada em Python usada para representar erros de negócio em uma aplicação. Esta classe pode ser utilizada para lançar exceções específicas relacionadas a regras de negócio ou lógica empresarial que não são cobertas pelas exceções padrão do Python.

## Instalação
Como `BusinessError` é uma classe personalizada, ela pode ser incluída diretamente em seu projeto. Basta definir a classe em um arquivo Python dentro do seu projeto.

## Utilização
Aqui está um exemplo de como utilizar a classe `BusinessError` em seu código:

1. **Definição da Classe `BusinessError`**:

   ```python
   class BusinessError(Exception):
       """Exceção personalizada para erros de negócio."""

       def __init__(self, message):
           super().__init__(message)
           self.message = message
   
## Métodos Principais

## __init__(self, message)

Inicializa a exceção BusinessError com uma mensagem específica.
message: A mensagem de erro a ser associada à exceção.

# SupabaseClient

## Visão Geral
`SupabaseClient` é uma classe Python desenvolvida para interagir com um banco de dados Supabase. Esta classe fornece métodos para gerar IDs e chaves de API exclusivas, inserir, deletar, atualizar e autenticar registros no banco de dados.

## Requisitos
- Biblioteca `supabase`
- Biblioteca `supabase_metrics`

## Instalação
1. Clone este repositório para o seu ambiente local:

2. Instale as bibliotecas necessárias usando os seguintes comandos:
    ```
    pip install supabase
    pip install supabase_metrics
    ```

## Utilização
Aqui está um exemplo de como utilizar a classe `SupabaseClient`:

1. **Inicialização do Objeto `SupabaseClient`**:

   ```python
   from SupabaseClient import SupabaseClient

   url = "SUA_URL_SUPABASE"
   api_key = "SUA_API_KEY_SUPABASE"
   client = SupabaseClient(url, api_key)

## Exemplos de uso

1. **Inserir Dados**:
   
nome = "João"
email = "joao@example.com"
senha = "senha123"
chat_pdf_api_key = "API_KEY_CHAT_PDF"
client.insere_dados(nome, email, senha, chat_pdf_api_key)

2. **Deletar Dados**:

email = "joao@example.com"
senha = "senha123"
client.deleta_dados(email, senha)

3. **Atualizar Dados:**
   
email = "joao@example.com"
senha = "senha123"
client.atualiza_dados(email, senha)

4. **Autenticar Dados:**:

email = "joao@example.com"
senha = "senha123"
sucesso, api_key = client.autentica_dados(email, senha)
if sucesso:
    print("Acesso liberado")


## Métodos Principais
__init__(self, url, api_key)
Inicializa o objeto SupabaseClient com a URL e a chave de API do Supabase.

**url:** A URL do seu projeto Supabase.

**api_key:** A chave de API do seu projeto Supabase.
gera_id(self)
Gera um ID único que não está presente no banco de dados.
gera_api_key(self)
Gera uma chave de API única que não está presente no banco de dados.
insere_dados(self, nome, email, senha, chat_pdf_api_key)
Insere um novo registro no banco de dados.

**nome:** O nome do usuário.

**chat_pdf_api_key:** A chave de API do Chat PDF.

**deleta_dados(self, email, senha)** Deleta um registro do banco de dados baseado no email e na senha.

**email:** O email do usuário.

**senha:** A senha do usuário.
