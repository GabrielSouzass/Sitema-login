from auth import cadastrar_usuario, login

while True:
    
    print("\n1 - Cadastrar")
    print("2 - Login")
    print("3 - Sair")
    
    opcao = input("Escolha a opção desejada! ")
    
    if opcao == "1":
        nome = input("Insira seu nome de usuário: ")
        senha = input("Insira a sua senha de acesso: ")
        
        if cadastrar_usuario(nome, senha):
            print("Usuário cadastrado com sucesso!")
        else:
            print("Este usuário já existe!")
            
    elif opcao == "2":
        nome = input("Insira seu usuário: ")
        senha = input("Insira sua senha: ")
        
        if login(nome, senha):
            print("Login realizado com sucesso!")
        else:
            print("Usuário ou senha incorretos!")
            
    elif opcao == "3":
        print("Encerrando sistema...")
        break
    