def data_por_extenso(data_nascimento):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    dia, mes, ano = data_nascimento.split("/")
    mes_extenso = meses[int(mes) - 1]
    print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")

data_nascimento_usuario = input("Digite uma data de nascimento (dd/mm/aaaa): ")
data_por_extenso(data_nascimento_usuario)