# Solicitar o nome do usuário
nome = input("Digite seu nome: ")

# Imprimir o nome em forma de escada
for i in range(1, len(nome) + 1):
    print(nome[:i])