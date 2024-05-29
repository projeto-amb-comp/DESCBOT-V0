import os
import random
from supabase import create_client, Client
from dotenv import load_dotenv
from metricas import MetricasClient

load_dotenv('creds.env')

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

class SupabaseClient:
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        self.client = create_client(url, api_key)
        self.metricas_client = MetricasClient(self)

    def gera_id(self):
        # Gera um ID único
        while True:
            id = random.randint(1, 1000)
            n = self.client.table("Registros").select("ID").eq("ID", id).execute()
            if len(n.data) == 0:
                return id

    def valida_email(self, email):
        # Verifica se o email contém "@" e "."
        if "@" in email and "." in email and email.count("@") == 1:
            username, domain = email.split("@")
            # Verifica se há pelo menos um caractere antes e depois do "@", e se termina com ".com" ou ".com.br"
            if len(username) > 0 and domain.count(".") >= 1:
                # Verifica se há pelo menos uma letra após o "@" e antes do ponto "."
                parts = domain.split(".")
                if len(parts[0]) > 0 and parts[0].isalpha():
                    return True
        return False

    def insere_dados(self, nome, email, senha, apikey):
        # Verifica se o email é válido
        if not self.valida_email(email):
            print("Email inválido")
            return

        # Verifica se o email já está cadastrado
        result = self.client.table("Registros").select("ID").eq("Email", email).execute()
        if len(result.data) > 0:
            print("Email já cadastrado")
            return

        # Gera um novo ID e APIKey únicos
        id = self.gera_id()

        data = {"ID": id, "Nome": nome, "Email": email, "Senha": senha, "APIKey": apikey}
        self.client.table("Registros").insert(data).execute()

        # Insere o ID na tabela Metricas
        self.metricas_client.insere_id(id)

        print("Registro inserido com sucesso.")

    def atualiza_dados(self, email, senha):
        # Verifica se o email é válido
        if not self.valida_email(email):
            print("Email inválido")
            return

        # Verifica se o email está cadastrado e a senha está correta
        result = self.client.table("Registros").select("ID", "Nome", "Email", "Senha", "APIKey").eq("Email", email).execute()
        if len(result.data) == 0 or result.data[0]["Senha"] != senha:
            print("Email ou senha inválidos")
            return

        record = result.data[0]
        dados_novos = {}

        while True:
            print("Qual dado você deseja modificar?")
            print("1. Nome")
            print("2. Email")
            print("3. Senha")
            print("4. APIKey")
            print("5. Atualizar e sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                novo_nome = input("Insira o novo nome: ")
                dados_novos["Nome"] = novo_nome
            elif opcao == "2":
                novo_email = input("Insira o novo email: ")
                if self.valida_email(novo_email):
                    dados_novos["Email"] = novo_email
                else:
                    print("Email inválido")
            elif opcao == "3":
                nova_senha = input("Insira a nova senha: ")
                dados_novos["Senha"] = nova_senha
            elif opcao == "4":
                novo_apikey = input("Insira seu novo APIKey: ")
                dados_novos["APIKey"] = novo_apikey
            elif opcao == "5":
                break
            else:
                print("Opção inválida. Tente novamente.")

        if dados_novos:
            target_email = dados_novos.get("Email", email)
            id_result = self.client.table("Registros").select("ID").eq("Email", target_email).execute()
            if len(id_result.data) == 0 or (target_email == email):
                self.client.table("Registros").update(dados_novos).eq("ID", record["ID"]).execute()
                self.metricas_client.atualizar_alteracoes(record["ID"])
                print("Dados atualizados com sucesso.")
            else:
                print("Email já cadastrado")
        else:
            print("Nenhuma alteração feita.")

    def deleta_dados(self, email, senha):
        # Verifica se o email está cadastrado
        email_result = self.client.table("Registros").select("ID", "Senha").eq("Email", email).execute()
        if len(email_result.data) == 0:
            print("Email não cadastrado")
            return

        # Verifica se a senha corresponde ao ID do email
        record = email_result.data[0]
        if record["Senha"] != senha:
            print("Senha incorreta")
            return

        # Deleta a linha se a senha corresponder
        record_id = record["ID"]
        self.client.table("Registros").delete().eq("ID", record_id).execute()

        # Deleta o ID na tabela Metricas
        self.metricas_client.deleta_id(record_id)

        print(f"Registro deletado com sucesso para o email {email}")

    def consulta_registro(self, email, senha):
        # Consulta um registro existente na tabela "Registros"
        result = self.client.table("Registros").select("ID", "Nome", "Email", "Senha", "APIKey").eq("Email", email).execute()
        if len(result.data) == 0 or result.data[0]["Senha"] != senha:
            print("Dados inválidos")
            return

        record = result.data[0]
        print(f"Nome: {record['Nome']}")
        print(f"Email: {record['Email']}")
        print(f"Senha: {record['Senha']}")
        print(f"APIKey: {record['APIKey']}")

        # Atualiza a tabela Metricas
        self.metricas_client.atualizar_requisicoes(record["ID"])

    def autentica_dados(self, email, senha):
        # Autentica um registro existente na tabela "Registros"
        result = self.client.table("Registros").select("ID", "Senha").eq("Email", email).execute()
        if len(result.data) == 0:
            print("Usuário não cadastrado")
            return False

        # Verifica se a senha corresponde ao email
        record = result.data[0]
        if record["Senha"] != senha:
            print("Senha inválida")
            return False

        # Atualiza a tabela Metricas
        self.metricas_client.atualizar_acessos(record["ID"])

        print("Acesso liberado")
        return True

def menu_principal():
    supabase_client = SupabaseClient(url, key)

    while True:
        print("1. Inserir novo registro")
        print("2. Atualizar registro")
        print("3. Deletar registro")
        print("4. Autenticar registro")
        print("5. Consultar registro")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        print("-" * 40)

        if opcao == "1":
            nome = input("Insira o nome: ")
            email = input("Insira o email: ")
            senha = input("Insira a senha: ")
            apikey = input("Insira a apikey: ")

            supabase_client.insere_dados(nome, email, senha, apikey)

        elif opcao == "2":
            email = input("Insira o email: ")
            senha = input("Insira a senha: ")

            supabase_client.atualiza_dados(email, senha)

        elif opcao == "3":
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")

            supabase_client.deleta_dados(email, senha)

        elif opcao == "4":
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")

            supabase_client.autentica_dados(email, senha)

        elif opcao == "5":
            email = input("Digite seu email: ")
            senha = input("Digite sua senha: ")

            supabase_client.consulta_registro(email, senha)

        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_principal()
