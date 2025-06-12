
estoque = {}

def cadastrar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    quantidade = int(input("Quantidade em estoque: "))
    estoque[nome] = (preco, quantidade)
    print(f"Produto '{nome}' cadastrado com sucesso!")

def consultar_produtos():
    print("\nProdutos disponíveis:")
    for nome, (preco, quantidade) in estoque.items():
        print(f"{nome}: Preço R$ {preco:.2f}, Quantidade: {quantidade}")
    print()

def registrar_venda():
    nome = input("Nome do produto vendido: ")
    if nome in estoque:
        quantidade_vendida = int(input("Quantidade vendida: "))
        preco, quantidade = estoque[nome]
        if quantidade_vendida <= quantidade:
            estoque[nome] = (preco, quantidade - quantidade_vendida)
            print(f"Venda registrada! Estoque atualizado para '{nome}'.")
        else:
            print("Quantidade insuficiente em estoque.")
    else:
        print("Produto não encontrado.")

def gerar_relatorios():
    print("\nRelatórios:")
    print("\nProdutos em estoque:")
    for nome, (preco, quantidade) in estoque.items():
        if quantidade > 0:
            print(f"{nome}: {quantidade} unidades")

    print("\nProdutos esgotados:")
    for nome, (preco, quantidade) in estoque.items():
        if quantidade == 0:
            print(nome)

def menu():
    while True:
        print("\n1. Cadastrar produto")
        print("2. Consultar produtos")
        print("3. Registrar venda")
        print("4. Gerar relatórios")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            consultar_produtos()
        elif opcao == "3":
            registrar_venda()
        elif opcao == "4":
            gerar_relatorios()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()