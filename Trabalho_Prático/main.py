import csv

# Estrutura para armazenar usuários e produtos em memória
usuarios = []
produtos = []

# Função para carregar dados dos arquivos CSV
def carregar_dados():
    global usuarios, produtos
    
    # Carregar usuários
    try:
        with open('usuarios.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            usuarios = [row for row in reader]
    except FileNotFoundError:
        print("Arquivo 'usuarios.csv' não encontrado.")
    
    # Carregar produtos
    try:
        with open('produtos.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            produtos = [row for row in reader]
    except FileNotFoundError:
        print("Arquivo 'produtos.csv' não encontrado.")

# Função para salvar dados nos arquivos CSV
def salvar_dados():
    # Salvar usuários
    with open('usuarios.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'nome', 'senha', 'permissao']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(usuarios)
    
    # Salvar produtos
    with open('produtos.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'nome', 'preco', 'quantidade']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(produtos)

# Funções CRUD para Usuários
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
            if nome:
                usuario['nome'] = nome
            if senha:
                usuario['senha'] = senha
            if permissao:
                usuario['permissao'] = permissao
            salvar_dados()
            return

def deletar_usuario(id):
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario['id'] != id]
    salvar_dados()

# Funções CRUD para Produtos
def criar_produto(id, nome, preco, quantidade):
    produto = {'id': id, 'nome': nome, 'preco': preco, 'quantidade': quantidade}
    produtos.append(produto)
    salvar_dados()

def ler_produtos():
    for produto in produtos:
        print(produto)

def atualizar_produto(id, nome=None, preco=None, quantidade=None):
    for produto in produtos:
        if produto['id'] == id:
            if nome:
                produto['nome'] = nome
            if preco:
                produto['preco'] = preco
            if quantidade:
                produto['quantidade'] = quantidade
            salvar_dados()
            return

def deletar_produto(id):
    global produtos
    produtos = [produto for produto in produtos if produto['id'] != id]
    salvar_dados()

# Funções adicionais para Produtos
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

# Função principal
def main():
    carregar_dados()
    
    # Exemplo de uso das funções
    criar_usuario('1', 'Gerente', '1234', 'gerente')
    criar_usuario('2', 'Funcionario', 'abcd', 'funcionario')
    
    criar_produto('1', 'Livro A', '10.00', '100')
    criar_produto('2', 'Livro B', '15.00', '200')
    
    print("Usuários:")
    ler_usuarios()
    
    print("\nProdutos:")
    ler_produtos()
    
    atualizar_usuario('2', senha='nova_senha')
    deletar_produto('1')
    
    print("\nUsuários após atualização:")
    ler_usuarios()
    
    print("\nProdutos após exclusão e atualização:")
    ler_produtos()
    
    print("\nBuscar produto por nome 'Livro B':")
    buscar_produto_por_nome('Livro B')
    
    print("\nProdutos ordenados por nome:")
    listar_produtos_ordenados_por_nome()
    
    print("\nProdutos ordenados por preço:")
    listar_produtos_ordenados_por_preco()

if __name__ == "__main__":
    main()