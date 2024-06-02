# Solicita a classe do personagem
classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ").strip().lower()

# Solicita os pontos de força
forca = int(input("Digite os pontos de força (de 1 a 20): "))

# Solicita os pontos de magia
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

# Variável para armazenar se os atributos são consistentes com a classe escolhida
atributos_consistentes = False

# Verifica a consistência dos atributos de acordo com a classe escolhida
if classe == "guerreiro":
    atributos_consistentes = forca >= 15 and magia <= 10
elif classe == "mago":
    atributos_consistentes = forca <= 10 and magia >= 15
elif classe == "arqueiro":
    atributos_consistentes = 5 < forca <= 15 and 5 < magia <= 15

# Imprime o resultado
print("Pontos de atributo consistentes com a classe escolhida:", atributos_consistentes)