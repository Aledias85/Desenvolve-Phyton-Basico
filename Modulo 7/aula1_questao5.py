# Ler a frase do usuário
frase = input("Digite uma frase: ")

# Inicializar uma lista para armazenar os índices das vogais
indices_vogais = []

# Inicializar uma variável para contar o número de vogais
num_vogais = 0

# Percorrer cada caractere da frase
for i, letra in enumerate(frase):
    # Verificar se a letra é uma vogal
    if letra.lower() in "aeiou":
        # Incrementar o número de vogais
        num_vogais += 1
        # Adicionar o índice da vogal à lista de índices
        indices_vogais.append(i)

# Exibir o número total de vogais
print(f"{num_vogais} vogais")

# Exibir os índices das vogais
print("Índices", indices_vogais)
