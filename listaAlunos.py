

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
            cadastarAluno()
    elif opcao == "2":
            listaSala()
    elif opcao == "3":
            alunoTransferido() 
    elif opcao == '4':
            buscarAluno()  
    elif opcao =='5':
            sair()
    else:
            print ("Erro!") 


def cadastarAluno(): 
    materias = ["História", "Física"]
    notas = []
    nome = input ("Informe o nome do contato: ") 
    for i in range (2):
        notas_materia = list(input)
    try:
        lista = open("lista.txt", "a")
        dados = f'{nome};{historia};{fisica};\n'
        lista.write(dados)
        lista.close()
        print(f'Cadastro atualizado com sucesso!!')
    except:
        print('ERRO!! Aluno NÃO gravado no sistema.')    
   
    

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
    nomeDeletado = input("Informe o nome transofr: ")
    lista = open ("lista.txt", "r")
    aux = []
    aux2 = []
    for i in lista:
        aux.append(i)
    for i in range (0, len(aux)):
        if nomeDeletado.upper() not in aux [i].upper():
            aux2.append(aux[i])   
    lista = open("lista.txt", "w")
    for i in aux2:
        lista.write(i)
    print(f'Nome removido removido da lista.')
#     listarContato

def buscarAluno():
    nome = input(f"Infome o nome a ser procurado: ").upper()
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