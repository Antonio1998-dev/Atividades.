usuarios_filmes = {"João": ["Matrix"]}

def adicionar_filme(usuario, filme):
    usuarios_filmes.setdefault(usuario, []).append(filme)
    print(f"Filme '{filme}' adicionado para {usuario}!")

def remover_filme(usuario, filme):
    if usuario in usuarios_filmes and filme in usuarios_filmes[usuario]:
        usuarios_filmes[usuario].remove(filme)
        print(f"Filme '{filme}' removido de {usuario}!")
    else:
        print("Usuário ou filme não encontrado.")

def ver_filmes(usuario):
    filmes = usuarios_filmes.get(usuario, [])
    print(f"Filmes assistidos por {usuario}: {filmes}")

def ver_todos_usuarios():
    for usuario, filmes in usuarios_filmes.items():
        print(f"{usuario}: {filmes}")

while True:
 
    print("\n=== MENU ===")
    print("1 - Adicionar filme")
    print("2 - Remover filme")
    print("3 - Ver filmes de um usuário")
    print("4 - Ver todos os usuários")
    print("0 - Sair")

    escolha = input("Escolha: ")

    match escolha:
        case "1":
            usuario = input("Nome do usuário: ")
            filme = input("Nome do filme: ")
            adicionar_filme(usuario, filme)
        case "2":
            usuario = input("Nome do usuário: ")
            filme = input("Nome do filme: ")
            remover_filme(usuario, filme)
        case "3":
            usuario = input("Nome do usuário: ")
            ver_filmes(usuario)
        case "4":
            ver_todos_usuarios()
        case "0":
            print("Encerrando...")
            break
        case _:
            print("Opção inválida. Tente novamente!")