def Cadastro():
    while True:
        usuario = input("Digite seu nome de usuario: ")
        senha = input("Digite sua senha: ")
        arquivo = open("usuarios.txt", "r")
        
        for linha in arquivo.readlines():
            valores = linha.split()
            if usuario == valores[0].strip():
                print("Usuario existente.")
                return


        tarefasFazer = []
        tarefasFeitas = []
        tarefasExcluidas = []
        cadastrar = open("usuarios.txt", "a")
        cadastrar.write(f'{usuario} {senha} {tarefasFazer} {tarefasFeitas} {tarefasExcluidas}\n')
        print("Usuario cadastrado!")
        return
            
def Login():
    while True:
        usuario = input("Digite seu nome de usuario: ")
        senha = input("Digite sua senha: ")
        arquivo = open("usuarios.txt", "r")
        
        for linha in arquivo.readlines():
            valores = linha.split()
            if usuario == valores[0].strip() and senha == valores[1].strip():
                print(f"Bem vindo {usuario}!")
                Menu()
                break
            else:
                print("Usuario ou senha incorreto.")
                continue
            
def Menu():
    while True:
        print("Sucesso.")
        break
            
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