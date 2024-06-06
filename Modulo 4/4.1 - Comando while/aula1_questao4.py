# Leia o valor de n
n = int(input("Digite o valor de n: "))

# Inicialize a variável maior
maior = 0

# Verifique se n é maior que 0
while n > 0:
    # Leia o valor de x
    x = int(input("Digite um número: "))
    
    # Verifique se x é maior que maior
    if x > maior:
        maior = x
    
    # Decrementa o valor de n
    n -= 1

# Imprima o maior valor encontrado
print("Maior:", maior)