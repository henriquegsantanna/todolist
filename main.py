def Cadastro():
    while True:
        usuario = input("Digite seu nome de usuario: ")
        senha = input("Digite sua senha: ")
        arquivo = open("usuarios.txt", "r")
        
        for linha in arquivo.readlines():
            valores = linha.split("-")
            if usuario == valores[0].strip():
                print("Usuario existente.")
            continue
        else:
            tarefasFazer = []
            tarefasFeitas = []
            tarefasExcluidas = []
            arquivo.write(' ' ' ' ' ' ' ' ' ', usuario, senha, tarefasFazer, tarefasFeitas, tarefasExcluidas)
            print("Usuario cadastrado!")
            Menu()
            
            
while True:
    print("Bem-Vindo!")
    print("1 - Cadastrar \n2 - Entrar")
    opcao = input("Selecione uma opcao: ")
    
    if opcao == "1":
        Cadastro()
    elif opcao == "2":
        Login()
    else:
        print("Opcao invalida.")
        continue