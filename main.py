import ast

def Inicio():
    print("Bem-Vindo!")
    print("1 - Cadastrar \n2 - Entrar \n3 - Sair")
    opcao = input("Selecione uma opcao: ")  
    return opcao

def Cadastro():
    while True:
        print("-"* 10 + "CADASTRO" + "-"* 10)
        usuario = input("Digite seu nome de usuario: ")
        senha = input("Digite sua senha: ")
        
        arquivo = open("usuarios.txt", "r")
        for linha in arquivo.readlines():
            valores = linha.split()
            if usuario == valores[0].strip():
                print("Usuario existente.")
                Cadastro()
        arquivo.close()


        tarefasFazer = []
        tarefasFeitas = []
        tarefasExcluidas = []
        cadastrar = open("usuarios.txt", "a")
        cadastrar.write(f'{usuario} {senha} {tarefasFazer} {tarefasFeitas} {tarefasExcluidas}\n')
        cadastrar.close()
        print("Usuario cadastrado!")
        return Login()
            
def Login():
    while True:
        print("-"* 10 + "LOGIN" + "-"* 10)
        usuario = input("Digite seu nome de usuario: ")
        senha = input("Digite sua senha: ")
        encontrado = False
        
        arquivo = open("usuarios.txt", "r")
        for linha in arquivo.readlines():
            valores = linha.split()
            if usuario == valores[0].strip() and senha == valores[1].strip():
                print(f"Bem vindo {usuario}!")
                encontrado = True
                Menu(usuario)
                return usuario
        arquivo.close()
        if not encontrado:
            print("Usuario ou senha incorreto.")
  
def adicionarTarefa(usuario_logado):
        tarefaAdicionada = input("Digite a tarefa que deseja adicionar: ")
        
        with open("usuarios.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        
        for i, linha in enumerate(linhas):
            valores = linha.strip().split(maxsplit=4)
            if valores[0] == usuario_logado:
                senha = valores[1]
                tarefasFazer = ast.literal_eval(valores[2])
                tarefasFeitas = ast.literal_eval(valores[3])
                tarefasExcluidas = ast.literal_eval(valores[4])
                tarefasFazer.append(tarefaAdicionada)
                nova_linha = f"{usuario_logado} {senha} {repr(tarefasFazer)} {repr(tarefasFeitas)} {repr(tarefasExcluidas)}\n"
                linhas[i] = nova_linha
                print("Tarefa adicionada!")
                break
                
        with open("usuarios.txt", "w") as arquivo:
            arquivo.writelines(linhas)
            
        Menu(usuario_logado)

def concluirTarefa():
    while True:
        print("Funcionando2")
        break

def excluirTarefa():
    while True:
        print("Funcionando3")
        break

def verTarefa():
    while True:
        print("Funcionando4")
        break
            
def Menu(usuario_logado):
    while True:
        print("1 - Adicionar tarefa \n2 - Concluir tarefa \n3 - Excluir tarefa \n4 - Ver tarefas \n5 - Sair")
        escolhaMenu = input("Selecione a opcao que deseja: ")
        
        if escolhaMenu == "1":
            adicionarTarefa(usuario_logado)
            break
        elif escolhaMenu == "2":
            concluirTarefa()
            break
        elif escolhaMenu == "3":
            excluirTarefa()
            break
        elif escolhaMenu == "4":
            verTarefa()
            break
        elif escolhaMenu == "5":
            print("Voce saiu.")
            break
            
while True:
    escolha = Inicio()

    if escolha == "1":
        Cadastro()
        break
    elif escolha == "2":
        Login()
        break
    elif escolha == "3":
        print("Voce saiu.")
        break
    else:
        print("Opcao invalida.")