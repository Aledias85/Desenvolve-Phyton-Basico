def processar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='latin-1') as arquivo:
        linhas = arquivo.readlines()
        
        # Imprimir as primeiras 25 linhas
        print("Primeiras 25 linhas do arquivo:")
        for linha in linhas[:25]:
            print(linha.strip())
        
        # Número total de linhas
        numero_linhas = len(linhas)
        print(f"\nNúmero total de linhas: {numero_linhas}")
        
        # Linha com maior número de caracteres
        linha_maior = max(linhas, key=len)
        print(f"\nLinha com maior número de caracteres ({len(linha_maior.strip())} caracteres):\n{linha_maior.strip()}")
        
        # Contagem das menções aos nomes "Nonato" e "Íria"
        contagem_nonato = sum(linha.lower().count('nonato') for linha in linhas)
        contagem_iria = sum(linha.lower().count('íria') for linha in linhas if 'íria' in linha.lower().split())
        
        print(f"\nNúmero de menções ao nome 'Nonato': {contagem_nonato}")
        print(f"Número de menções ao nome 'Íria': {contagem_iria}")

# Nome do arquivo a ser processado
nome_arquivo = 'estomago.txt'

# Chamada da função para processar o arquivo
processar_arquivo(nome_arquivo)
