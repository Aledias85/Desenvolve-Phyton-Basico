import csv

# Estruturas de dados para armazenar usuários e produtos
usuarios = []
produtos = []

# Carregar dados dos arquivos CSV
def carregar_dados():
    global usuarios, produtos
    try:
        with open('usuarios.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            usuarios = [row for row in reader]
    except FileNotFoundError:
        print("Arquivo 'usuarios.csv' não encontrado.")
    try:
        with open('produtos.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            produtos = [row for row in reader]
    except FileNotFoundError:
        print("Arquivo 'produtos.csv' não encontrado.")

# Salvar dados nos arquivos CSV
def salvar_dados():
    with open('usuarios.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'nome', 'senha', 'permissao']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(usuarios)
    with open('produtos.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'nome', 'preco', 'quantidade', 'categoria', 'descricao']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(produtos)

# CRUD Usuários
def criar_usuario(id, nome, senha, permissao):
    usuario = {'id': id, 'nome': nome, 'senha': senha, 'permissao': permissao}
    usuarios.append(usuario)
    salvar_dados()

def ler_usuarios():
    for usuario in usuarios:
        print(usuario)

def atualizar_usuario(id, nome=None, senha=None, permissao=None):
    for usuario in usuarios:
        if usuario['id'] == id:
            if nome: usuario['nome'] = nome
            if senha: usuario['senha'] = senha
            if permissao: usuario['permissao'] = permissao
            salvar_dados()
            return

def deletar_usuario(id):
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario['id'] != id]
    salvar_dados()

# CRUD Produtos
def criar_produto(id, nome, preco, quantidade, categoria, descricao):
    produto = {'id': id, 'nome': nome, 'preco': preco, 'quantidade': quantidade, 'categoria': categoria, 'descricao': descricao}
    produtos.append(produto)
    salvar_dados()

def ler_produtos():
    for produto in produtos:
        print(produto)

def atualizar_produto(id, nome=None, preco=None, quantidade=None, categoria=None, descricao=None):
    for produto in produtos:
        if produto['id'] == id:
            if nome: produto['nome'] = nome
            if preco: produto['preco'] = preco
            if quantidade: produto['quantidade'] = quantidade
            if categoria: produto['categoria'] = categoria
            if descricao: produto['descricao'] = descricao
            salvar_dados()
            return

def deletar_produto(id):
    global produtos
    produtos = [produto for produto in produtos if produto['id'] != id]
    salvar_dados()

# Funções adicionais de Produtos
def buscar_produto_por_nome(nome):
    for produto in produtos:
        if produto['nome'] == nome:
            print(produto)

def listar_produtos_ordenados_por_nome():
    for produto in sorted(produtos, key=lambda x: x['nome']):
        print(produto)

def listar_produtos_ordenados_por_preco():
    for produto in sorted(produtos, key=lambda x: float(x['preco'])):
        print(produto)

# Função principal com autenticação
def autenticar():
    id = input("ID: ")
    senha = input("Senha: ")
    for usuario in usuarios:
        if usuario['id'] == id and usuario['senha'] == senha:
            return usuario
    print("ID ou senha inválidos.")
    return None

def menu(usuario):
    while True:
        print("\n### Menu Principal ###")
        if usuario['permissao'] in ['gerente', 'supervisor']:
            print("1. Gerenciar Usuários")
        print("2. Gerenciar Produtos")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1' and usuario['permissao'] in ['gerente', 'supervisor']:
            menu_usuarios()
        elif escolha == '2':
            menu_produtos()
        elif escolha == '3':
            break
        else:
            print("Opção inválida ou acesso negado. Tente novamente.")

def menu_usuarios():
    while True:
        print("\n### Menu Usuários ###")
        print("1. Criar Usuário")
        print("2. Ler Usuários")
        print("3. Atualizar Usuário")
        print("4. Deletar Usuário")
        print("5. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            id = input("ID: ")
            nome = input("Nome: ")
            senha = input("Senha: ")
            permissao = input("Permissão: ")
            criar_usuario(id, nome, senha, permissao)
        elif escolha == '2':
            ler_usuarios()
        elif escolha == '3':
            id = input("ID: ")
            nome = input("Novo Nome (pressione Enter para manter o atual): ")
            senha = input("Nova Senha (pressione Enter para manter a atual): ")
            permissao = input("Nova Permissão (pressione Enter para manter a atual): ")
            atualizar_usuario(id, nome if nome else None, senha if senha else None, permissao if permissao else None)
        elif escolha == '4':
            id = input("ID: ")
            deletar_usuario(id)
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_produtos():
    while True:
        print("\n### Menu Produtos ###")
        print("1. Criar Produto")
        print("2. Ler Produtos")
        print("3. Atualizar Produto")
        print("4. Deletar Produto")
        print("5. Buscar Produto por Nome")
        print("6. Listar Produtos Ordenados por Nome")
        print("7. Listar Produtos Ordenados por Preço")
        print("8. Voltar ao Menu Principal")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            id = input("ID: ")
            nome = input("Nome: ")
            preco = input("Preço: ")
            quantidade = input("Quantidade: ")
            categoria = input("Categoria (Jogo/Console): ")
            descricao = input("Descrição: ")
            criar_produto(id, nome, preco, quantidade, categoria, descricao)
        elif escolha == '2':
            ler_produtos()
        elif escolha == '3':
            id = input("ID: ")
            nome = input("Novo Nome (pressione Enter para manter o atual): ")
            preco = input("Novo Preço (pressione Enter para manter o atual): ")
            quantidade = input("Nova Quantidade (pressione Enter para manter a atual): ")
            categoria = input("Nova Categoria (pressione Enter para manter a atual): ")
            descricao = input("Nova Descrição (pressione Enter para manter a atual): ")
            atualizar_produto(id, nome if nome else None, preco if preco else None, quantidade if quantidade else None, categoria if categoria else None, descricao if descricao else None)
        elif escolha == '4':
            id = input("ID: ")
            deletar_produto(id)
        elif escolha == '5':
            nome = input("Nome: ")
            buscar_produto_por_nome(nome)
        elif escolha == '6':
            listar_produtos_ordenados_por_nome()
        elif escolha == '7':
            listar_produtos_ordenados_por_preco()
        elif escolha == '8':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    carregar_dados()
    usuario = autenticar()
    if usuario:
        menu(usuario)


        #A escolha do tema de games foi imediata devido a minha paixão pelo tema. Tenho ainda um sonho de colocar isso em pratica.
        # Tive bastante dificuldade em gerar o código, já que nunca tive contato nenhum com o Phyton antes, mas tenho certeza que vou conseguir melhorar bastante nos próximos