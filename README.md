#  ChatBot UERJ
[![Static Badge](https://img.shields.io/badge/license-MIT-green?style=flat)](https://github.com/projeto-amb-comp/DESCBOT-V0/blob/main/LICENSE)

## Documentação da aplicação

## Índice

1. Descrição Geral 
2. Instalação e Configuração
3. Arquitetura
4. Funcionalidades
5. APIs e Integrações
6. Banco de Dados
7. Segurança
8. Exemplos de uso
9. Manutenção e Contribuição
10. Melhorias
11. FAQ (Perguntas Frequentes)
12. Referências



## 1. Descrição Geral 

Este projeto foi desenvolvido na disciplina de Projeto de Ambiente Computacional do curso de Engenharia Elétrica com ênfase em Sistemas e Computação da UERJ, e tem por objetivo tornar-se uma ferramenta útil para os estudantes do departamento. 

A aplicação é um chatbot interativo que utiliza a API ChatPDF para fornecer respostas baseadas em documentos PDF. Foi desenolvida em Python e utiliza a biblioteca Streamlit para construir a interface de usuário. O banco de dados utilizado para armazenar as informações do usuário foi o Supabase e o código fonte está hospedado no GitHub.

Para acessar o chatbot, [clique aqui](https://descbot-uerj.streamlit.app/).

É necessário realizar cadastro na plataforma para utilização da aplicação.


## 2. Instalação e Configuração

O uso do chatbot pode ser através do [link](https://descbot-uerj.streamlit.app/), ou localmente.

### Requisitos para utilização local
- Python 3.8+;
- Conta no Supabase;
- Conta na API ChatPDF;
- Conta no GitHub.

Para a utilização local, é necessária a criação das tabelas de usuário de métricas (indicadas no item 6. Modelo de dados desta documentação) na sua conta Supabase.

### Passos para preparação do ambiente local

##### 2.1. Clonar o repositório: 
Digite o comando abaixo no terminal:

```sh
git clone https://github.com/projeto-amb-comp/DESCBOT-V0.git
```
##### 2.2. Instalação do Streamlit: 
Execute a instalação do streamlit através do terminal:
```sh
pip install streamlit
```
Valide a instalação executando o app Hello da plataforma Streamlit: 

```sh
streamlit hello
```


##### 2.3. Ativação do ambiente Streamlit: 

Abra o terminal na pasta do projeto

```sh
cd meuprojeto
```

Digite o comando abaixo no terminal

```sh
python -m venv .venv
```

Uma pasta chamada ".venv" irá aparecer no projeto. Esta é a pasta do ambiente virtual.

Para ativar o ambiente, siga os comandos abaixo, dependendo do seu sistema operacional:
```sh
# Windows command prompt
.venv\Scripts\activate.bat

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS and Linux
source .venv/bin/activate
```

Uma vez ativado, o nome do seu ambiente aparecerá no termninal. "(.venv)"


##### 2.4. Executando a aplicação do chatbot: 
Para executar a aplicação, digite o comando abaixo no terminal:
```sh
streamlit run streamlit_app.py
```


## 3. Arquitetura


### 3.1. Interface do usuário 
 - 
 - 
### 3.2. Backend
 - 
 - 
### 3.3. Hospedagem
 - 
 - 


## 4. Funcionalidades

- Interação com o usuário por meio de chat
- Upload de arquivos PDF de até 200MB.
- Quiz gerado a partir do PDF para auxiliar nos estudos. 

## 5. APIs e Integrações
- ChatPDF
- SUPABASE

## 6. Banco de Dados
O banco de dados do aplicativo, implementado na plataforma Supabase, é formado pela tabela de usuários e tabela de métricas.
#### 6.2.1. Tabela de Usuários

A tabela de usuários armazena informações de cadastro de cada usuário registrado na aplicação.

### 6.2.1.1 Modelos de Dados
- `id`: Identificador único do usuário
- `nome`: Nome do usuário
- `email`: Email do usuário
- `senha`   : Senha do usuário
- `APIKey`': API Key do chatPDF do usuário 

### 6.2.1.1 Funções da tabela de usuários
- `adicionar_registro(registro)` - Adiciona o registro de um novo usuário
- `buscar_registro(id)`: Busca um registro pelo ID. - Remove um registro existente a partir do id
-  `buscar_registro(id)`: Busca um registro pelo ID.


#### 6.2.2. Tabela de Métricas

A tabela de métricas tem como objetivo mensurar informações de acessos de usuários à aplicação, tais como quantidade de acessos pelos usuários e alterações realizadas a cada acesso.

- `ID`: Identificador único do usuário
- `Acessos`: Quantidade de acessos realizados pelo usuário;
- `Alterações`: Registra a quantidade de alterações realizadas pelo usuário.


### 6.2.1.1 Funções da tabela de métricas
- `calcular_metricas(dados)` - Calcula métricas a partir de dados fornecidos
- `gerar_relatorio_metricas(metricas)`; Gera um relatório formatdo a partir das métricas



## 7. Segurança
O acesso à plataforma por parte dos usuários é feito através de login e senha. 
Para recuperação de senha, o usuário deve informar a chave APIKey.
Os dados sensíveis não são criptografados, portanto o usuário deve usar uma **senha única** para o serviço. 
O usuário não deve fazer upload de documentos sensíveis, pois o ChatPDF armazena os dados carregados.

## 8. Exemplos de uso 
- Interação com a aplicação por meio de chat
![image](https://github.com/projeto-amb-comp/DESCBOT-V0/assets/76968158/fd3d2d0e-c13e-4a72-89ac-6633f59a824c)



- Perguntas feitas pela plataforma em forma de quiz para auxiliar o estudo
![Perguntas 1](https://github.com/projeto-amb-comp/DESCBOT-V0/assets/76968158/5b5c80bb-7521-4cbe-a707-4332cc7f61bf)
![Perguntas 2](https://github.com/projeto-amb-comp/DESCBOT-V0/assets/76968158/fcc5cd51-0446-4f93-8472-b8bbf9bdcd01)


## 9. Manutenção e Contribuição

Este é um projeto de código aberto e está disponível para contribuições. 

### Como contribuir

1. Fork o repositório: Acesse o repositório no GitHub e faça um fork do projeto para a sua própria conta.
- Link do Repositório: [Github ChatBot UERJ](https://github.com/projeto-amb-comp/DESCBOT-V0.git)

2. Clone o Repositório: Clone o repositório forked para o seu ambiente local.
 ```
git clone https://github.com/seu-usuario/seu-repositorio.git
```


3. Crie um Branch: Crie um branch para suas alterações.   
```
git checkout -b sua-branch
```


4. Faça suas Alterações: Implemente suas alterações ou novas funcionalidades.


5. Commit suas Alterações: Commit suas alterações com uma mensagem clara e descritiva.
 ```
git commit -m "Alterações realizadas"
```

6. Push para o GitHub: Envie suas alterações para o seu repositório forked no GitHub.

```
git push origin sua-branch
```

7. Crie um Pull Request: No GitHub, navegue até a página do seu repositório forked e clique em "Compare & pull request". Explique suas alterações no pull request e submeta para revisão.

### Reportar Problemas
Em caso de bugs encontrados na aplicação, enviar email para projetodeambientecomputacional@gmail.com ou reportar na aba [issues](https://github.com/projeto-amb-comp/DESCBOT-V0/issues) na página do GitHub do projeto.

## 10. Possíveis melhorias
- Migração da base de dados para servidor local.
- Criptografia de dados sensíveis.
- Implementar função de recuperação de senha.

## 11. FAQ (Perguntas Frequentes)
- ### Como faço para obter uma chave para a API ChatPDF?
    Acesse a página do [ChatPDF](https://www.chatpdf.com/), clique em 'My Account' ao final da página e faça login com uma conta Google.
    Um pop-up será aberto contendo o tópico 'Developers', neste tópico está a sua APIKey que deve ser copiada e colada na página da aplicação Chatbot UERJ.

- ### Quais os tipos de arquivos compatíveis com a aplicação?
    Apenas arquivos em PDF são compatíveis com a aplicação. O arquivo deve ter no máximo 200MB.


## 12. Referências
- [Documentação do Streamlit](https://docs.streamlit.io/)
- [Documentação do Supabase](https://supabase.com/docs) 
- [Documentação da API ChatPDF](https://www.chatpdf.com/docs/api/backend)
- [Documentação do GitHub](https://docs.github.com/pt)












































