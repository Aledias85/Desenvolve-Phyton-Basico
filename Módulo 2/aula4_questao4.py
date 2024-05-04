# Leitura de dados (enttrada)
valor = int(input("Digite o valor: "))

# Processamento
#### Começar da maior nota (Quantas notas?)
notas_100 = valor //100 # 576 / 100 = 5
#### Atualizar quanto falta depois da maior nota
valor = valor % 100

notas_50 = valor //50  #76 / 50 = 1

valor = valor % 50

notas_20 = valor //20  #26 / 20 = 1

valor = valor % 20

notas_10 = valor //10  # 6 / 10 = 0

valor = valor % 10

notas_5 = valor //5  # 6 / 5 = 1

valor = valor % 5

notas_2 = valor //2  # 1 / 2 = 0

valor = valor % 2

notas_1 = valor //1  # 1 / 1 = 1

valor = valor % 1

print(f"{notas_100} nota(s) de 100")
print(f"{notas_50} nota(s) de 50")
print(f"{notas_20} nota(s) de 20")
print(f"{notas_10} nota(s) de 10")
print(f"{notas_5} nota(s) de 5")
print(f"{notas_2} nota(s) de 2")
print(f"{notas_1} nota(s) de 1")
