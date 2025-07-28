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
            valores = linha.split("|")
            if usuario == valores[0].strip():
                print("Usuario existente.")
                Cadastro()
        arquivo.close()


        tarefasFazer = []
        tarefasFeitas = []
        tarefasExcluidas = []
        cadastrar = open("usuarios.txt", "a")
        cadastrar.write(f'{usuario} | {senha} | {tarefasFazer} | {tarefasFeitas} | {tarefasExcluidas}\n')
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
            valores = linha.split("|")
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

    novas_linhas = []

    for linha in linhas:
        #nova_lista = [expressao for item in lista] -- list comprehension
        #pega cada item da lista, aplica a expressao nele e guarda o resultado em uma nova lista
        valores = [v.strip() for v in linha.strip().split("|")]

        if valores[0] == usuario_logado:
            senha = valores[1]
            tarefasFazer = ast.literal_eval(valores[2])
            tarefasFeitas = ast.literal_eval(valores[3])
            tarefasExcluidas = ast.literal_eval(valores[4])

            tarefasFazer.append(tarefaAdicionada.capitalize())

            nova_linha = f"{usuario_logado} | {senha} | {repr(tarefasFazer)} | {repr(tarefasFeitas)} | {repr(tarefasExcluidas)}\n"
            novas_linhas.append(nova_linha)
        else:
            novas_linhas.append(linha)

    with open("usuarios.txt", "w") as arquivo:
        arquivo.writelines(novas_linhas)

    print("Tarefa adicionada!")
    Menu(usuario_logado)

def concluirTarefa(usuario_logado):
    with open("usuarios.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        
    novas_linhas = []
        
    for linha in linhas:
        valores = [v.strip() for v in linha.strip().split("|")]
        
        if valores[0] == usuario_logado:
            senha = valores[1]
            tarefasFazer = ast.literal_eval(valores[2])
            tarefasFeitas = ast.literal_eval(valores[3])
            tarefasExcluidas = ast.literal_eval(valores[4])
            
            print(' | '.join(tarefasFazer))
            tarefaConcluida = input("Digite a tarefa que deseja concluir: ")
            
            if tarefaConcluida.capitalize() in tarefasFazer:
                    tarefasFazer.remove(tarefaConcluida.capitalize())
                    tarefasFeitas.append(tarefaConcluida.capitalize())
                    nova_linha = f"{usuario_logado} | {senha} | {repr(tarefasFazer)} | {repr(tarefasFeitas)} | {repr(tarefasExcluidas)}\n"
                    novas_linhas.append(nova_linha)
                    print("Parabens! Tarefa concluida!")
            else:
                print("Tarefa nao encontrada.")
                concluirTarefa(usuario_logado)
                return
            
        else:
            novas_linhas.append(linha)
                
    with open("usuarios.txt", "w") as arquivo:
        arquivo.writelines(novas_linhas)
        
    Menu(usuario_logado)
    
def excluirTarefa(usuario_logado):
    with open("usuarios.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        
        novas_linhas = []
        
    for linha in linhas:
        valores = [v.strip() for v in linha.strip().split("|")]
        if valores[0] == usuario_logado:
            senha = valores[1]
            tarefasFazer = ast.literal_eval(valores[2])
            tarefasFeitas = ast.literal_eval(valores[3])
            tarefasExcluidas = ast.literal_eval(valores[4])
            
            print(' | '.join(tarefasFazer))
            tarefaExcluida = input("Digite a tarefa que deseja excluir: ")
            
            if tarefaExcluida.capitalize() in tarefasFazer:
                    tarefasFazer.remove(tarefaExcluida.capitalize())
                    tarefasExcluidas.append(tarefaExcluida.capitalize())
                    nova_linha = f"{usuario_logado} | {senha} | {repr(tarefasFazer)} | {repr(tarefasFeitas)} | {repr(tarefasExcluidas)}\n"
                    novas_linhas.append(nova_linha)
                    print("Tarefa excluida!")
            else:
                print("Tarefa nao encontrada.")
                excluirTarefa(usuario_logado)
                return
            
        else:
            novas_linhas.append(linha)
                
    with open("usuarios.txt", "w") as arquivo:
        arquivo.writelines(novas_linhas)
        
    Menu(usuario_logado)

def verTarefa(usuario_logado):
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
            concluirTarefa(usuario_logado)
            break
        elif escolhaMenu == "3":
            excluirTarefa(usuario_logado)
            break
        elif escolhaMenu == "4":
            verTarefa(usuario_logado)
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