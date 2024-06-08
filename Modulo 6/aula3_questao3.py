import random

# Gerar uma lista com 20 elementos entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]

print("Original:", lista)

# Encontrar o intervalo com a maior quantidade de números negativos
max_negativos = 0
start_index = 0
end_index = 0

for i in range(len(lista)):
    for j in range(i + 1, len(lista) + 1):
        sublista = lista[i:j]
        num_negativos = sum(1 for x in sublista if x < 0)
        if num_negativos > max_negativos:
            max_negativos = num_negativos
            start_index = i
            end_index = j

# Deletar o intervalo da lista
del lista[start_index:end_index]

print("Editada:", lista)