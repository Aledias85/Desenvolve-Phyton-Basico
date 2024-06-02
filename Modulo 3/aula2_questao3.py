# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

# Solicita se o usuário já jogou pelo menos 3 jogos de tabuleiro. Deve se responder true ou false
jogou_3_ou_mais_jogos = input("Já jogou pelo menos 3 jogos de tabuleiro? ").strip().lower() == "true"

# Solicita quantos jogos já venceu
jogos_vencidos = int(input("Quantos jogos já venceu? "))

# Verifica as condições para admissão no clube
pode_ingressar = (16 <= idade <= 18) and jogou_3_ou_mais_jogos and (jogos_vencidos > 0)

# Imprime o resultado
print("Apto para ingressar no clube de jogos de tabuleiro:", pode_ingressar)