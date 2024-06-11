import random

def escolhe_palavra():
    with open("gabarito_forca.txt", "r") as arquivo:
        palavras = arquivo.read().splitlines()
    return random.choice(palavras)

def carrega_estagios_enforcado():
    with open("gabarito_enforcado.txt", "r") as arquivo:
        estagios = arquivo.read().split("===")
    return estagios

def imprime_enforcado(erros, estagios):
    print(estagios[erros])

def jogo_forca():
    palavra = escolhe_palavra()
    estagios = carrega_estagios_enforcado()
    palavra_oculta = ["_"] * len(palavra)
    tentativas = 0
    letras_usadas = set()

    while tentativas < 6 and "_" in palavra_oculta:
        print("Palavra:", " ".join(palavra_oculta))
        print("Letras usadas:", " ".join(sorted(letras_usadas)))
        letra = input("Digite uma letra: ").lower()

        if letra in letras_usadas:
            print("Você já usou essa letra.")
            continue

        letras_usadas.add(letra)

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    palavra_oculta[i] = letra
        else:
            tentativas += 1
            imprime_enforcado(tentativas, estagios)

    if "_" not in palavra_oculta:
        print("Parabéns! Você acertou a palavra:", palavra)
    else:
        imprime_enforcado(tentativas, estagios)
        print("Você perdeu! A palavra era:", palavra)

jogo_forca()
