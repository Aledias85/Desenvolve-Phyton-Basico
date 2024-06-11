import re

with open("frase.txt", "r") as arquivo:
    conteudo = arquivo.read()

palavras = re.findall(r'\b\w+\b', conteudo)

with open("palavras.txt", "w") as arquivo:
    for palavra in palavras:
        arquivo.write(f"{palavra}\n")

with open("palavras.txt", "r") as arquivo:
    print(arquivo.read())