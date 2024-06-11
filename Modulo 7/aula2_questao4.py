def validador_senha(senha):
    if len(senha) < 8:
        return False
    if not any(char.islower() for char in senha):
        return False
    if not any(char.isupper() for char in senha):
        return False
    if not any(char.isdigit() for char in senha):
        return False
    if not any(char in "@#$%^&*()_-+=[]{}|\\:;\"'<>?,./~`" for char in senha):
        return False
    return True

# Exemplo de uso:
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"
print(validador_senha(senha1))  # Saída esperada: True
print(validador_senha(senha2))  # Saída esperada: False
print(validador_senha(senha3))  # Saída esperada: False





