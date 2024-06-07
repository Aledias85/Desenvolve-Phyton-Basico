# Leia os valores de n1, n2 e n3
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))

# Calcule a média
M = (n1 + n2 + n3) / 3
print(M)

# Verifique as condições e imprima os resultados apropriados
if M > 60:
    print("aprovado")
elif M > 40:
    print("recuperação")
else:
    print("reprovado")

# Imprima "fim"
print("fim")