import csv

# Nome do arquivo CSV
nome_arquivo = "spotify-2023.csv"

# Dicionário para armazenar a música mais tocada de cada ano
musicas_mais_tocadas = {}

# Abrir o arquivo para leitura
with open(nome_arquivo, 'r', encoding='latin-1') as arquivo:
    leitor_csv = csv.DictReader(arquivo)
    
    for linha in leitor_csv:
        try:
            # Extrair as informações necessárias
            track_name = linha['track_name']
            artist_name = linha['artist(s)_name']
            released_year = int(linha['released_year'])
            streams = int(linha['streams'])
            
           
            if 2012 <= released_year <= 2022:
                
                if released_year not in musicas_mais_tocadas or streams > musicas_mais_tocadas[released_year][3]:
                    musicas_mais_tocadas[released_year] = [track_name, artist_name, released_year, streams]
        
        except ValueError:
          
            continue


lista_musicas_mais_tocadas = [musicas_mais_tocadas[ano] for ano in sorted(musicas_mais_tocadas)]


print(lista_musicas_mais_tocadas)
