import random
import math

def main():
    # Solicita ao usuário o valor de n
    n = int(input("Digite a quantidade de valores inteiros aleatórios a serem gerados: "))
    
    # Gera n valores inteiros aleatórios entre 0 e 100
    valores = [random.randint(0, 100) for _ in range(n)]
    
    # Calcula a soma dos valores gerados
    soma_valores = sum(valores)
    
    # Calcula a raiz quadrada da soma dos valores
    raiz_quadrada_soma = math.sqrt(soma_valores)
    
    # Exibe os valores gerados, a soma e a raiz quadrada da soma
    print(f"Valores gerados: {valores}")
    print(f"Soma dos valores: {soma_valores}")
    print(f"Raiz quadrada da soma dos valores: {raiz_quadrada_soma:.2f}")

if __name__ == "__main__":
    main()
