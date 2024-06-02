# Solicita as idades de Juliana e Cris
idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))

# Verifica se pelo menos uma das pessoas é maior de 17 anos
podem_entrar = idade_juliana > 17 or idade_cris > 17

# Imprime o resultado
print(podem_entrar)