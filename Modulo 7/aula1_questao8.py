def validar_cpf(cpf):
    # Remover pontos e traço do CPF fornecido pelo usuário
    cpf_limpo = cpf.replace(".", "").replace("-", "")
    
    # Verificar se o CPF tem 11 dígitos
    if len(cpf_limpo) != 11:
        return False
    
    # Calcular o primeiro dígito verificador
    soma = 0
    multiplicador = 10
    for i in range(9):
        soma += int(cpf_limpo[i]) * multiplicador
        multiplicador -= 1
    resto = soma % 11
    if resto < 2:
        primeiro_digito_verificador = 0
    else:
        primeiro_digito_verificador = 11 - resto
    
    # Verificar se o primeiro dígito verificador está correto
    if int(cpf_limpo[9]) != primeiro_digito_verificador:
        return False
    
    # Calcular o segundo dígito verificador
    soma = 0
    multiplicador = 11
    for i in range(10):
        soma += int(cpf_limpo[i]) * multiplicador
        multiplicador -= 1
    resto = soma % 11
    if resto < 2:
        segundo_digito_verificador = 0
    else:
        segundo_digito_verificador = 11 - resto
    
    # Verificar se o segundo dígito verificador está correto
    if int(cpf_limpo[10]) != segundo_digito_verificador:
        return False
    
    # Se passou por todas as verificações, o CPF é válido
    return True

# Solicitar CPF ao usuário
cpf_usuario = input("Digite o CPF na forma XXX.XXX.XXX-XX: ")

# Validar o CPF
if validar_cpf(cpf_usuario):
    print("CPF válido")
else:
    print("CPF inválido")
