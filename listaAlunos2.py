import ast
alunos = dict()
def menu():
    opcao = input('''
.......................................................
                 3º DS
Menu
[1] Cadastar Aluno. 
[2] Lista de Alunos. 
[3] Retirar da chamada.                                             
[4] Buscar Aluno 
[5] Sair.
.......................................................                   
Escolha uma opção acima: ''')
    if opcao == "1":
        cadastrarAluno()
    elif opcao == "2":
        listaSala()
    elif opcao == "3":
        alunoTransferido() 
    elif opcao == '4':
        buscarAluno()  
    elif opcao =='5':
        sair()
    else:
        print ("Erro! Tente novamente.")

def cadastrarAluno(): 
    with open("lista2.txt", "r", encoding="utf-8") as file:
        lista_notas_anterior = file.read()

    alunos = ast.literal_eval(lista_notas_anterior)
    print(alunos)

    materias = ["História", "Física"]
    bimestre = []
    notas = []
    aluno = []

    nome = (input("Informe o nome do aluno: "))

    for b in range (len(materias)):
        for c in range (4):
            bimestre.append(float(input(f"Informe a nota do {c+1}º bimestre em {materias[b]}: ")))
            media = sum(bimestre)/4
        bimestre.append(media)
        aluno.append(bimestre)
        bimestre = []
    alunos[nome] = aluno

    print(alunos)
    with open("lista2.txt", "w", encoding="utf-8") as file:
        file.write(f'{alunos}')

    
    
def listaSala():
    with open('lista.txt', 'r') as f:
        results = [[str(entry) for entry in line.split()] for line in f.readlines()]
        results.sort()
    for itens in results:
        print(itens)

def organizarLista(): 
    with open('lista.txt', 'r') as lista:
        antes_de_organizar = lista.readlines()
        contato_organizados = sorted(antes_de_organizar, key=lambda x: x.split(";"[0]))
        print(contato_organizados)

def alunoTransferido():
    nomeDeletado = input("Informe o nome do aluno(a) transferido(a): ")
    lista = open ("lista.txt", "r")
    aux = []
    aux2 = []
    for i in lista:
        aux.append(i)
    for i in range (0, len(aux)):
        if nomeDeletado.upper() not in aux[i].upper():
            aux2.append(aux[i])
    lista = open("lista.txt", "w")
    for i in aux2:
        lista.write(i)
    print(f'Aluno(a) removido da lista de alunos.')
#     listarContato


def buscarAluno():
    nome = input(f"Infome o nome do aluno(a) a ser procurado: ").upper()
    lista = open ("lista.txt", "r")
    encontrado = False
    for aluno in lista:
        # print(contato.split(";")[0].upper())
        if nome in aluno.split(";")[0].upper():
            encontrado=True
            print(aluno)
    lista.close() 
    if encontrado == False:
         print("\n\33[1;31;40mAluno (a) não encontrado. Tente novamente!\33[m\n")
         buscarAluno()

def sair():
    print(f'Até a próxima!')
    exit()      

def main():
    menu()

main()