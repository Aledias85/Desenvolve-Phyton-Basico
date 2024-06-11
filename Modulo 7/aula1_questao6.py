from itertools import permutations

def encontrar_anagramas(frase, palavra_objetivo):
   
    palavra_objetivo = palavra_objetivo.replace(" ", "").lower()
    
    # Inicializar uma lista para armazenar os anagramas encontrados
    anagramas = []
    
  
    permutacoes = permutations(palavra_objetivo)
    
    # Transformar as permutações em strings e verificar se estão na frase
    for permutacao in permutacoes:
        anagrama = "".join(permutacao)
        if anagrama in frase:
            anagramas.append(anagrama)
    
    return anagramas

# Ler a frase do usuário
frase = input("Digite uma frase: ")

# Ler a palavra objetivo do usuário
palavra_objetivo = input("Digite a palavra objetivo: ")

# Encontrar os anagramas da palavra objetivo na frase
anagramas = encontrar_anagramas(frase, palavra_objetivo)

# Exibir os anagramas encontrados
print("Anagramas:", anagramas)