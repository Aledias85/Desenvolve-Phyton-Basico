import random

def main():
    # Gera um número aleatório entre 1 e 10
    numero_aleatorio = random.randint(1, 10)
    
    while True:
        # Solicita ao usuário que adivinhe o número
        palpite = int(input("Adivinhe o número entre 1 e 10: "))
        
        # Fornece feedback sobre o palpite
        if palpite < numero_aleatorio:
            print("Muito baixo, tente novamente!")
        elif palpite > numero_aleatorio:
            print("Muito alto, tente novamente!")
        else:
            print(f"Correto! O número é {palpite}.")
            break  # Interrompe a execução quando o usuário acerta

if __name__ == "__main__":
    main()