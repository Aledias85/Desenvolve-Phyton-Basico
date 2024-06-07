from datetime import datetime

def main():
    # Obtém a data e hora atuais
    agora = datetime.now()
    
    # Formata a data e hora
    data_formatada = agora.strftime("Data: %d/%m/%Y")
    hora_formatada = agora.strftime("Hora: %H:%M")
    
    # Exibe a data e hora formatadas
    print(data_formatada)
    print(hora_formatada)

if __name__ == "__main__":
    main()