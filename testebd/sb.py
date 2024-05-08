from supabase_py import create_client
from os import environ
# Configure a URL do projeto e a chave da API fornecidas pelo Supabase
project_url = environ.get('project_url')
api_key = environ.get('api_key')

# Crie uma instância do cliente Supabase
supabase = create_client(project_url, api_key)


# Função para inserir um novo registro na tabela "Registros"
def insert_record():
    email = input("Insira o email: ")
    senha = input("Insira a senha: ")
    apikey = input("Insira a apikey: ")
    
    data = {"Email": email, "Senha": senha, "APIKey": apikey}
    print("Dados a serem inseridos:", data)
    
    response = supabase.table("Registros").insert(data).execute()
    print("Resposta da inserção:", response)
    
    if response.get("error"):
        print("Erro ao inserir registro:", response.get("error"))
    else:
        print("Registro inserido com sucesso!")



# Função para atualizar um registro na tabela "Registros"
def update_record():
    email = input("Insira o email do registro a ser atualizado: ")
    novo_email = input("Insira o novo email: ")
    nova_senha = input("Insira a nova senha: ")
    nova_apikey = input("Insira a nova apikey: ")
    
    data = {"Email": novo_email, "Senha": nova_senha, "APIKey": nova_apikey}
    response = supabase.table("Registros").update(data).eq("Email", email).execute()
    
    if response.get("error"):
        print("Erro ao atualizar registro:", response.get("error"))
    else:
        print("Registro atualizado com sucesso!")

# Função para deletar um registro na tabela "Registros"
def delete_record():
    email = input("Insira o email do registro a ser deletado: ")
    response = supabase.table("Registros").delete().eq("Email", email).execute()
    
    if response.get("error"):
        print("Erro ao deletar registro:", response.get("error"))
    else:
        print("Registro deletado com sucesso!")

# Função para exibir o menu principal
def main_menu():
    while True:
        print("1. Inserir novo registro")
        print("2. Atualizar registro")
        print("3. Deletar registro")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            insert_record()
        elif opcao == "2":
            update_record()
        elif opcao == "3":
            delete_record()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu principal
main_menu()
