# Função para ler uma lista de números do usuário
def ler_lista(tamanho):
    lista = []
    for i in range(tamanho):
        elemento = int(input(f"Digite o {i+1}º elemento: "))
        lista.append(elemento)
    return lista

# Ler a quantidade de elementos da lista 1
qtde_lista1 = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {qtde_lista1} elementos da lista 1:")
lista1 = ler_lista(qtde_lista1)

# Ler a quantidade de elementos da lista 2
qtde_lista2 = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {qtde_lista2} elementos da lista 2:")
lista2 = ler_lista(qtde_lista2)

# Combinar as listas de forma alternada
lista_intercalada = []
i = 0
while i < len(lista1) or i < len(lista2):
    if i < len(lista1):
        lista_intercalada.append(lista1[i])
    if i < len(lista2):
        lista_intercalada.append(lista2[i])
    i += 1

# Imprimir a lista intercalada
print("Lista intercalada:", " ".join(map(str, lista_intercalada)))