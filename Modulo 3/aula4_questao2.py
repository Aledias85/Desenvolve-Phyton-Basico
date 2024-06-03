# Solicita a avaliação do filme ao usuário
avaliacao = int(input("Insira a avaliação do filme (de 1 a 5): "))

# Verifica a avaliação e imprime a mensagem correspondente
if avaliacao == 5:
    print("Excelente!")
elif avaliacao == 4:
    print("Muito Bom!")
elif avaliacao == 3:
    print("Bom!")
elif avaliacao == 2:
    print("Regular.")
elif avaliacao == 1:
    print("Ruim.")
else:
    print("Avaliação inválida. Por favor, insira um número entre 1 e 5.")