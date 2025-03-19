
def cadastrarAluno(qtd_alunos): 
    materias = ["História", "Física"]
    notas_sala = []
    notas_aluno = []
    notas_prov = []

    for a in range (0, qtd_alunos):
        notas_aluno.append(input("Informe o nome do aluno: "))
        for b in range (4):
            notas_prov.append(float(input(f"Informe a nota do {b+1}º bimestre: ")))
        media = sum(notas_prov)/4
        notas_aluno.append(str(notas_prov))
        notas_aluno.append(str(media))

    return print(notas_aluno)

    try:
        lista = open("lista.txt", "a")
        dados = f'{nome};{notas[0]};{notas[1]};{notas[2]};{notas[3]};{notas[4]};\n'
        lista.write(dados)
        lista.close()
        print(f'Cadastro atualizado com sucesso!!')
    except:
        print('ERRO!! Aluno NÃO gravado no sistema.')   

cadastrarAluno(1)

