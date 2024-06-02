# Solicita as idades de Juliana e Cris
idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))

# Verifica se ambas são maiores de 17 anos
maiores_de_idade = idade_juliana > 17 and idade_cris > 17

# Imprime o resultado
print(maiores_de_idade)