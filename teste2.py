teste = {'A': [[2.0, 3.0, 6.0, 5.0, 4.0], [5.0, 6.0, 4.0, 6.0, 5.25]]}

if teste.get("A"):
    print("TEM")
nome = input("Digite o nome: ")

if teste.get(nome):
    print("TEM")
else:
    print("NAO TEM")