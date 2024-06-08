# Lista de endereços web (URLs)
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

# Extraindo o nome principal de cada URL
dominios = [url[4:-4] for url in urls]

# Imprimindo os resultados
print("URLs:", urls)
print("dominios:", dominios)