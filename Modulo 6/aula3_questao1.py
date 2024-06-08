# Solicitar uma quantidade indefinida de números inteiros do usuário (pelo menos 4 valores)
numeros = []

print("Digite pelo menos 4 números inteiros (digite 'sair' para finalizar):")

while True:
    entrada = input("Digite um número (ou 'sair' para terminar): ")
    if entrada.lower() == 'sair':
        if len(numeros) >= 4:
            break
        else:
            print("Por favor, insira pelo menos 4 números.")
    else:
        try:
            numero = int(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro ou 'sair' para terminar.")

# Usando fatiamento de listas para as operações solicitadas
print("Lista original:", numeros)
print("Os 3 primeiros elementos:", numeros[:3])
print("Os 2 últimos elementos:", numeros[-2:])
print("A lista invertida:", numeros[::-1])
print("Os elementos de índice par:", numeros[::2])
print("Os elementos de índice ímpar:", numeros[1::2])
