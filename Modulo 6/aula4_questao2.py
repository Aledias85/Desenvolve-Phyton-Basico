# Solicita uma frase do usuário
frase = input("Digite uma frase: ")

# Define as vogais
vogais = "aeiouAEIOU"

# Compreensão de listas para obter vogais da frase, ordenadas alfabeticamente
lista_vogais = sorted([letra for letra in frase if letra in vogais])
print("Vogais:", lista_vogais)

# Compreensão de listas para obter consoantes da frase
lista_consoantes = [letra for letra in frase if letra.isalpha() and letra not in vogais]
print("Consoantes:", lista_consoantes)