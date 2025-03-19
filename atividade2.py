def  consultar():
    busca= input ('''
    ..........................................................
       Lista de Alunos 3 ano Desenvolvimento de Sistemas
     
        1 - Cadastar Aluno
        2 - Lista de nome 
        4 - Notas 
    ..........................................................
        Informe a informação a ser acessada: 
    ''')

    if busca ==1:
        cadastarAluno()
    elif busca ==2:
        mostarLista()
#    elif busca ==3:
#         notasAlunos() 

def cadastarAluno():
    numeroChamada = input("Qual é o numero da chamada do Aluno (a): ")
    nome = input ("Informe O nome do Aluno (a): ")

    notas = []
    for i in range (4):
        nota = input(f"Informe a {i}º nota do Aluno (a): ")
        notas.append(nota)
        nota = None
    media = sum(notas)/4
    notas.append(media)
    return(print(notas))



def mostarLista():
    listaAlunos = open("lista.txt", "r")
    for  infromacoes in listaAlunos:
        print(infromacoes)
    listaAlunos.close



       



def main():
    consultar()