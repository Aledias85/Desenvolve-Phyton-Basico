n = int(input("Digite o número de idades: "))

# Inicializar as variáveis
soma = 0  # resultado -> soma
cont = 0  # variável de controle do laço

while cont < n:
    idade = int(input("Digite a idade: "))
    soma += idade  # soma = soma + idade

    # Atualizando a variável do controle do laço
    cont += 1  # cont = cont + 1

# Imprimir soma e média após a conclusão do laço
print(f"Soma das idades: {soma}")
print(f"A média das idades é {soma / n:.0f} anos")
