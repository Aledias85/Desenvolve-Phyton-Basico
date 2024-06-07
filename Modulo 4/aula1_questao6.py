# Entrada de dados
n = int(input("Digite a quantidade de experimentos: "))  # quantidade de experimentos

# Inicializar as variáveis resultado e controle
cont = 0 
soma_sapo, soma_rato, soma_coelho = 0, 0, 0

# Iterações
while cont < n:
    quantia = int(input("Digite a quantidade de cobaias: "))
    tipo = input("Digite o tipo de cobaia (S para sapo, R para rato, C para coelho): ").upper()

    if tipo == 'S':
        soma_sapo += quantia
    elif tipo == 'R':
        soma_rato += quantia
    elif tipo == 'C':
        soma_coelho += quantia

    cont += 1

total_cobaias = soma_sapo + soma_rato + soma_coelho

print("Total de cobaias:", total_cobaias)
print("Total de sapos:", soma_sapo)
print("Total de ratos:", soma_rato)
print("Total de coelhos:", soma_coelho)