# Definindo variáveis para armazenar os preços totais de cada produto
total_produto_1 = 0
total_produto_2 = 0
total_produto_3 = 0

# Solicitando informações do produto 1
nome_produto_1 = input('*Digite o nome do produto 1:* ')
preco_unitario_1 = float(input('*Digite o preço unitário do produto 1:* '))
quantidade_1 = int(input('*Digite a quantidade do produto 1:* '))
total_produto_1 = preco_unitario_1 * quantidade_1

# Solicitando informações do produto 2
nome_produto_2 = input('*Digite o nome do produto 2:* ')
preco_unitario_2 = float(input('*Digite o preço unitário do produto 2:* '))
quantidade_2 = int(input('*Digite a quantidade do produto 2:* '))
total_produto_2 = preco_unitario_2 * quantidade_2

# Solicitando informações do produto 3
nome_produto_3 = input('*Digite o nome do produto 3:* ')
preco_unitario_3 = float(input('*Digite o preço unitário do produto 3:* '))
quantidade_3 = int(input('*Digite a quantidade do produto 3:* '))
total_produto_3 = preco_unitario_3 * quantidade_3

# Calculando o preço total da compra
preco_total = total_produto_1 + total_produto_2 + total_produto_3

# Imprimindo o preço total da compra
print('Total: R${:,.2f}'.format(preco_total))