# Todos os números pares entre 20 e 50
numeros_pares = [num for num in range(20, 51) if num % 2 == 0]
print("Números pares entre 20 e 50:", numeros_pares)

# Os quadrados de todos os valores da lista [1, 2, 3, 4, 5, 6, 7, 8, 9]
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrados = [valor ** 2 for valor in valores]
print("Quadrados dos valores de 1 a 9:", quadrados)

# Todos os números entre 1 e 100 que sejam divisíveis por 7
divisiveis_por_7 = [num for num in range(1, 101) if num % 7 == 0]
print("Números entre 1 e 100 divisíveis por 7:", divisiveis_por_7)

# Para todos os valores em range(0, 30, 3), escreva "par" ou "ímpar" dependendo da paridade do elemento
paridade = ["par" if num % 2 == 0 else "ímpar" for num in range(0, 30, 3)]
print("Paridade dos valores em range(0, 30, 3):", paridade)