# Lista de alunos e suas respectivas notas
alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]

# Usando compreensão de listas para construir a lista de aprovados
aprovados = [alunos[i] for i in range(len(notas)) if notas[i] >= 60]

print("Aprovados:", aprovados)