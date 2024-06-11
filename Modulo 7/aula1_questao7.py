import random

def encrypt(nomes):
    # Gerar um valor aleatório entre 1 e 10 para a chave de criptografia
    chave_aleatoria = random.randint(1, 10)
    
    # Inicializar uma lista para armazenar os nomes criptografados
    nomes_cript = []
    
    # Percorrer cada nome na lista de nomes
    for nome in nomes:
        nome_criptografado = ""
        # Criptografar cada caractere do nome
        for caractere in nome:
            # Calcular o valor do caractere criptografado
            valor_criptografado = ord(caractere) + chave_aleatoria
            # Verificar se o valor criptografado está dentro do intervalo de caracteres visíveis
            if valor_criptografado > 126:
                valor_criptografado -= 94  # Voltar ao início do intervalo
            nome_criptografado += chr(valor_criptografado)
        nomes_cript.append(nome_criptografado)
    
    # Retornar os nomes criptografados e a chave de criptografia
    return nomes_cript, chave_aleatoria

# Lista de nomes
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

# Criptografar os nomes
nomes_cript, chave_aleatoria = encrypt(nomes)

# Exibir os nomes criptografados e a chave de criptografia
print("Nomes criptografados:", nomes_cript)
print("Chave de criptografia:", chave_aleatoria)
