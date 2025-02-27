def cadastarAluno():
    lista = []
    numeroChamada = input("Qual é o numero da chamada do Aluno (a): ")
    nome = input ("Informe O nome do Aluno (a): ")

    for i in range (1,5):
        nota = int(input(f"Informe a {i}º nota do Aluno (a): "))
        lista.append(nota)
        nota = None
    media = sum(lista)/4
    lista.append(media)
    lista.insert(0, numeroChamada)
    lista.insert(1, nome)
    return(print(lista))

cadastarAluno()