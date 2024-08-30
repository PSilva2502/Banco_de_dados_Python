import pymysql.cursors
import time

con = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    port=3306,
    db="aulapythonfull",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)

def criarTabela(criar):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"{criar}")
            time.sleep(2)
        print('\nTabela criada com sucesso')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

def deletarTabela(nomeTabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"DROP TABLE {nomeTabela}")
            time.sleep(2)
        print('\nTabela deletada com sucesso')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

def inserirDados(dados):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"{dados}") 
            time.sleep(2)
        print('\nDados Inseridos com sucesso')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

def Select(selecionar):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"{selecionar}")
            resultado = cursor.fetchall()
            for i in resultado:
                print(i)
            time.sleep(2)
        print('\nQUERY bem sucedida')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

def update(query):
    try:
        with con.cursor() as cursor:
            cursor.execute(query)
            time.sleep(1)
        print('\nUPDATE bem sucedido')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

def deletar(delete):
    try:
        with con.cursor() as cursor:
            cursor.execute(delete)
            time.sleep(1)
        print('\nDELETADO com sucesso')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

while True:
    print("\nEscolha uma opção:")
    print("1. Criar Tabela")
    print("2. Deletar Tabela")
    print("3. Inserir Dados")
    print("4. SELECT de Tabela")
    print("5. UPDATE")
    print("6. DELETE de Tabela")
    print("7. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        criar = input("Digite a query para criar uma tabela com colunas: ")
        time.sleep(2)
        criarTabela(criar)

    elif opcao == '2':
        nomeTabela = input("Digite o nome da tabela a ser deletada: ")
        time.sleep(2)
        deletarTabela(nomeTabela)

    elif opcao == '3':
        dados = input("Digite um INSERT INTO: ")
        time.sleep(2)
        inserirDados(dados)

    elif opcao == '4':
        selecionar = input("Digite a QUERY: ")
        time.sleep(2)
        Select(selecionar)

    elif opcao == '5':
        query = input("Digite a QUERY de UPDATE: ")
        time.sleep(2)
        update(query)

    elif opcao == '6':
        delete = input("Digite a QUERY de DELETE: ")
        time.sleep(2)
        deletar(delete)


    elif opcao == '7':
        print("Encerrando o programa...")
        time.sleep(2)
        break

    else:
        print("Opção inválida. Tente novamente.")

con.close()
