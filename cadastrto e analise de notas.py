alunos = {}

def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    alunos[nome] = [nota1, nota2, nota3]

def calcular_media(notas):
    return sum(notas) / 3

def verificar_situacao(media):
    return "Aprovado" if media >= 7 else "Reprovado"

def exibir_boletim():
    nome = input("Nome do aluno: ")
    if nome in alunos:
        notas = alunos[nome]
        media = calcular_media(notas)
        situacao = verificar_situacao(media)
        print(f"Notas: {notas}, Média: {media:.2f}, Situação: {situacao}")
    else:
        print("Aluno não encontrado!")

def menu():
    while True:
        opcao = input("\n1 - Cadastrar\n2 - Boletim\n3 - Sair\nEscolha: ")
        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            exibir_boletim()
        elif opcao == "3":
            break
        else:
            print("Opção inválida!")

menu()