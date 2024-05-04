#Leitura de dados (Entrada)
comprimento = int(input("Digite o comprimento: ")) #cálculo do comprimento
largura = int(input("Digite a largura: ")) #cálculo da largura
preço_m2 = float(input("Valor do m2: ")) # cálculo do m2

#Processamento
area = comprimento * largura #m2
preço_total = area * preço_m2

#impressão de dados (Saída)
print (f"O terreno possui {area}m2 e custa R${preço_total:,.2f}"), # o.2f será a formatação e o numero de casas decimais