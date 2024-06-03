# Solicita a distância da entrega em quilômetros
distancia = float(input("Digite a distância da entrega em quilômetros: "))

# Solicita o peso do pacote em quilogramas
peso = float(input("Digite o peso do pacote em quilogramas: "))

# Inicializa o custo do frete
custo_frete = 0

# Calcula o custo do frete com base na distância
if distancia <= 100:
    custo_frete = peso * 1
elif distancia <= 300:
    custo_frete = peso * 1.50
else:
    custo_frete = peso * 2

# Adiciona taxa extra se o peso do pacote for superior a 10 kg
if peso > 10:
    custo_frete += 10

# Imprime o valor do frete
print(f"O valor do frete é: R${custo_frete:.2f}")