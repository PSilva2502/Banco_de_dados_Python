from controller import ControllerCadastro, ControllerLogin
from time import sleep
while True:
    print("---------- MENU ----------")
    opcao = int(input("Digite 1 para cadastrar\nDigite 2 para logar\nDigite 3 para sair\n"))

    if opcao == 1:
        nome = input('Digite seu nome: ')
        email = input('Digite um email: ')
        senha = input('Digite uma senha com no minimo 6 digitos: ')
        resultado =ControllerCadastro.cadastrar(nome, email, senha)

        if resultado == 2:
            print('Tamanho do nome digitado inválido')
        
        elif resultado == 3:
            print('Email maior que 100 caracteres')

        elif resultado == 4:
            print('Tamanho da senha inválido')

        elif resultado == 5:
            print('Email já cadastrado')

        elif resultado == 6:
            print('Erro interno do sistema')
        
        elif resultado == 1:
            print('Cadastrado com sucesso')
    
    elif opcao == 2:
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')
        resultado = ControllerLogin.login(email, senha)

        if not resultado:
            print('Email ou senha invalidos')
        else:
            print(resultado)
    else:
        print('SAINDO DO SISTEMA...')
        sleep(1)
        break