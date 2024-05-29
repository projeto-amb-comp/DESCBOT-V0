from supabase import create_client

class MetricasClient:
    def __init__(self, supabase_client):
        """
        Inicializa o cliente de métricas com uma instância do cliente Supabase.
        """
        self.supabase_client = supabase_client

    def insere_id(self, user_id):
        """
        Insere um novo ID na tabela de métricas com valores iniciais para 'Acessos', 'Alteracoes' e 'Requisicoes'.
        """
        data = {"ID": user_id, "Acessos": 0, "Alteracoes": 0, "Requisicoes": 0}
        self.supabase_client.client.table("Metricas").insert(data).execute()

    def atualizar_acessos(self, user_id):
        """
        Incrementa o número de acessos para o usuário com o ID fornecido.
        """
        # Obter o valor atual de "Acessos" para o usuário com o ID fornecido
        response = self.supabase_client.client.table("Metricas").select("Acessos").eq("ID", user_id).execute()
        acessos_atuais = response.data[0]["Acessos"] if response.data else 0

        # Atualizar o registro incrementando "Acessos"
        data = {"ID": user_id, "Acessos": acessos_atuais + 1}
        self.supabase_client.client.table("Metricas").upsert(data).execute()

    def atualizar_alteracoes(self, user_id):
        """
        Incrementa o número de alterações e acessos para o usuário com o ID fornecido.
        """
        # Obter o valor atual de "Alteracoes" e "Acessos" para o usuário com o ID fornecido
        response = self.supabase_client.client.table("Metricas").select("Alteracoes", "Acessos").eq("ID", user_id).execute()
        alteracoes_atuais = response.data[0]["Alteracoes"] if response.data else 0
        acessos_atuais = response.data[0]["Acessos"] if response.data else 0

        # Atualizar o registro incrementando "Alteracoes" e "Acessos"
        data = {"ID": user_id, "Acessos": acessos_atuais + 1, "Alteracoes": alteracoes_atuais + 1}
        self.supabase_client.client.table("Metricas").upsert(data).execute()

    def atualizar_requisicoes(self, user_id):
        """
        Incrementa o número de requisições e acessos para o usuário com o ID fornecido.
        """
        # Obter o valor atual de "Requisicoes" e "Acessos" para o usuário com o ID fornecido
        response = self.supabase_client.client.table("Metricas").select("Requisicoes", "Acessos").eq("ID", user_id).execute()
        requisicoes_atuais = response.data[0]["Requisicoes"] if response.data else 0
        acessos_atuais = response.data[0]["Acessos"] if response.data else 0

        # Atualizar o registro incrementando "Requisicoes" e "Acessos"
        data = {"ID": user_id, "Acessos": acessos_atuais + 1, "Requisicoes": requisicoes_atuais + 1}
        self.supabase_client.client.table("Metricas").upsert(data).execute()

    def deleta_id(self, user_id):
        """
        Deleta o registro de métricas para o usuário com o ID fornecido.
        """
        self.supabase_client.client.table("Metricas").delete().eq("ID", user_id).execute()
