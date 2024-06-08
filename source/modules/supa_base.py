import os
import random
import string
from supabase import create_client, Client
from supabase_metrics.metricas import MetricasClient

class SupabaseClient:
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key
        self.client = create_client(url, api_key)
        self.metricas_client = MetricasClient(self)

    def gera_id(self):
        while True:
            id = random.randint(1, 1000)
            n = self.client.table("Registros").select("ID").eq("ID", id).execute()
            if len(n.data) == 0:
                return id
          
    def gera_api_key(self):
        while True:
            api_key_length = random.randint(5, 20)
            characters = string.ascii_letters + string.digits
            api_key = ''.join(random.choice(characters) for _ in range(api_key_length))
            n = self.client.table("Registros").select("APIKey").eq("APIKey", api_key).execute()
            if len(n.data) == 0:
                return api_key

    def insere_dados(self, nome, email, senha, chat_pdf_api_key):
        try:
            result = self.client.table("Registros").select("ID").eq("Email", email).execute()
            if len(result.data) > 0:
                print("Email já cadastrado")
                return False
            
            id = self.gera_id()
           
            data = {
                "ID": id,
                "Nome": nome,
                "Email": email,
                "Senha": senha,
                "APIKey": chat_pdf_api_key
            }
            insert_response = self.client.table("Registros").insert(data).execute()
            self.metricas_client.insere_id(id)
            print("Registro inserido com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao inserir os dados: {e}")
            return False


    def deleta_dados(self, email, senha):
        # Verificar se o email está cadastrado
        email_result = self.client.table("Registros").select("ID", "Senha").eq("Email", email).execute()
        if len(email_result.data) == 0:
            print("Email não cadastrado")
            return
        
        # Verificar se a senha corresponde ao ID do email
        record = email_result.data[0]
        if record["Senha"] != senha:
            print("senha incorreta")
            return
        
        # Deletar a linha se a senha corresponder
        record_id = record["ID"]
        self.client.table("Registros").delete().eq("ID", record_id).execute()

        # Deletar o ID na tabela Metricas
        self.metricas_client.deleta_id(record_id)

        print(f"Registro deletado com sucesso para o email {email}")

    def atualiza_dados(self, email, senha):
        # Verificar se o email está cadastrado e a senha está correta
        result = self.client.table("Registros").select("ID", "Nome", "Email", "Senha", "APIKey").eq("Email", email).execute()
        if len(result.data) == 0 or result.data[0]["Senha"] != senha:
            print("Email ou senha inválidos")
            return
        
        # Pedir novos dados ao usuário
        novo_nome = input("Insira o novo nome: ")
        novo_email = input("Insira o novo email: ")
        nova_senha = input("Insira a nova senha: ")
        novo_apikey = input("Insira seu APIKey: ")
        
        # Atualizar o registro mantendo o mesmo ID e APIKey
        record = result.data[0]
        data = {
            "Nome": novo_nome,
            "Email": novo_email,
            "Senha": nova_senha,
            "APIKey": novo_apikey
        }
        self.client.table("Registros").update(data).eq("ID", record["ID"]).execute()

        # Atualizar a tabela Metricas
        self.metricas_client.atualizar_alteracoes(record["ID"])

        print("Dados atualizados com sucesso.")

    def autentica_dados(self, email, senha):
        # Verificar se o email está cadastrado
        result = self.client.table("Registros").select("ID", "Senha", "APIKey").eq("Email", email).execute()
        if len(result.data) == 0:
            print("Usuário não cadastrado")
            return False, None
        
        # Verificar se a senha corresponde ao email
        record = result.data[0]
        if record["Senha"] != senha:
            print("Senha inválida")
            return False, None
        
        # Atualizar a tabela Metricas
        self.metricas_client.atualizar_acessos(record["ID"])
    
        print("Acesso liberado")
        return True, record["APIKey"]

