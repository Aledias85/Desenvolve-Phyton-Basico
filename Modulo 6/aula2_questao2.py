import random

# Construção da lista de valores aleatórios
lista1, lista2 = [], []

for i in range(20):
    lista1.append(random.randint(0, 50))
    lista2.append(random.randint(0, 50))

print("Lista 1 ordenada:", sorted(lista1))
print("Lista 2 ordenada:", sorted(lista2))

inters = []
# Caminhar em uma lista e verificar a participação
# de cada elemento na segunda lista
for elemento in lista1:
    if elemento in lista2:
        inters.append(elemento)

inters.sort()

for i in inters:
    print(f"{i}: ({lista1.count(i)}, {lista2.count(i)})")