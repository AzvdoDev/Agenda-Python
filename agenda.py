def menu():
    voltarMenuPrincipal = 's'
    while voltarMenuPrincipal=='s':
        opcao= input('''
        =========================================================================
                            PROJETO AGENDA EM PYTHON
        MENU:
        
        [1]CADASTRAR CONTATO
        [2]LISTAR CONTATO
        [3]DELETAR CONTATO
        [4]BUSCAR CONTATO PELO NOME
        [5]ATUALIZAR CONTATO
        [6]SAIR
        ========================================================================
        ESCOLHA UMA OPÇÃO ACIMA:
        ''')
    
        if opcao=="1":
            cadastrarContato()
        elif opcao=="2":
            listarContato()
        elif opcao=="3":
            deletarContato()
        elif opcao=="4":
            buscarContatoPeloNome()
        elif opcao=="5":
            atualizarContato()
        else:
            sair()
        voltarMenuPrincipal=input("Deseja voltar ao menu principal? (s/n) ").lower()

def atualizarContato():
    nomeDeletado = input("Digite o nome para ser atualizado: ").lower()
    agenda = open("agenda.txt", "r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDeletado not in aux[i]:
            aux2.append(aux[i].lower())
    agenda = open("agenda.txt", "w")
    for i in aux2:
        agenda.write(i)
    idContato = input("Escolha o Id do seu contato atualizado: ")
    nome = input("Escreva o nome do contato atualizado: ")
    telefone = input("Escreva o telefone do contato atualizado: ")
    email = input("Escreva o email do contato atualizado: ")
    try:
     agenda = open("agenda.txt","a")
     dados = f'{idContato};{nome};{telefone};{email} \n'
     agenda.write(dados)
     agenda.close()
     print(f'Contato atualizado com sucesso!') 
    except:
        print("ERRO na gravação do contato")


def cadastrarContato():
    idContato = input("Escolha o Id do seu contato: ")
    nome = input("Escreva o nome do contato: ")
    telefone = input("Escreva o telefone do contato: ")
    email = input("Escreva o email do contato: ")
    try:
     agenda = open("agenda.txt","a")
     dados = f'{idContato};{nome};{telefone};{email} \n'
     agenda.write(dados)
     agenda.close()
     print(f'Contato gravado com sucesso!') 
    except:
        print("ERRO na gravação do contato")

def listarContato():
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        print(contato)
    agenda.close()

def deletarContato():
    nomeDeletado = input("Digite o nome para ser deletado: ").lower()
    agenda = open("agenda.txt", "r")
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDeletado not in aux[i]:
            aux2.append(aux[i].lower())
    agenda = open("agenda.txt", "w")
    for i in aux2:
        agenda.write(i)
    print(f'contato deletado com sucesso!')
    listarContato()

def buscarContatoPeloNome():
    nome=input(f'digite o nome a ser procutado: ').upper()
    agenda = open("agenda.txt", "r")
    for contato in agenda:
        if nome in contato.split(";")[1].upper():
            print(contato)
    agenda.close()

def sair():
    print(f'Até mais !!')
    exit
def main():
    menu()

main()
