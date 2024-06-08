import random

# Construção da lista de valores aleatórios
lista1, lista2 = [], []

for i in range(20):
    lista1.append(random.randint(0, 50))
    lista2.append(random.randint(0, 50))

print("lista1 -", lista1)
print("lista2 -", lista2)

# Encontrar interseção sem duplicatas
inters = list(set(lista1) & set(lista2))
inters.sort()

print("Interseccao -", inters)
print("Contagem")

for i in inters:
    print(f"{i}: (lista1={lista1.count(i)}, lista2={lista2.count(i)})")