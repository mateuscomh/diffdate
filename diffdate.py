# ----------------------------------------------------------------------------
# Programa para calcular a data futura após adicionar um número específico de dias
#
# Descrição: Este programa calcula a data que será após adicionar um número de dias
# a partir de uma data inicial fornecida. 
#
# Versão: 1.1.2
# Data de criação: 11/03/2022
# Autor: Matheus Martins - 3mhenrique@gmail.com
# ----------------------------------------------------------------------------
from datetime import datetime, timedelta
import sys

def validate_user_input(user_input):
    """
    Valida a entrada do usuário.
    Retorna uma tupla (tipo, valor) onde:
    - tipo: "data" se for uma data no formato DD-MM-AAAA 
        "dias" se for um número inteiro 
        "sair" se for 'q' ou 'Q', ou None se inválido.
    - valor: a data, o número de dias, ou None.
    """
    if user_input.lower() in ('q', 'Q'):
        return "sair", None

    try:
        # Verifica se é uma data no formato DD-MM-AAAA
        datetime.strptime(user_input, "%d-%m-%Y")
        return "data", user_input
    except ValueError:
        try:
            # Verifica se é um número inteiro
            dias = int(user_input)
            if dias > 0:
                return "dias", dias
        except ValueError:
            pass
    return None, None

def calculate_date_diff(start_date, end_date):
    """
    Calcula a diferença entre duas datas em anos, meses e dias.
    Retorna uma string formatada com a diferença.
    """
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%d-%m-%Y")
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, "%d-%m-%Y")

    diff_days = (end_date - start_date).days

    year_diff = end_date.year - start_date.year
    month_diff = end_date.month - start_date.month
    day_diff = end_date.day - start_date.day

    if day_diff < 0:
        month_diff -= 1
        prev_month_last_day = (end_date.replace(day=1) - timedelta(days=1)).day
        day_diff += prev_month_last_day

    if month_diff < 0:
        year_diff -= 1
        month_diff += 12

    result = []
    if year_diff != 0:
        result.append(f"{year_diff} ano(s)")
    if month_diff != 0:
        result.append(f"{month_diff} mês(es)")
    if day_diff != 0:
        result.append(f"{day_diff} dia(s)")

    result.append(f"\nTotal de {abs(diff_days)} dia(s)")
    return ", ".join(result)

def calculate_future_past_dates(days):
    """
    Calcula a data futura ou passada com base em um número de dias.
    Retorna uma string formatada com as datas (no formato DD-MM-AAAA).
    """
    today = datetime.today()
    future_date = today + timedelta(days=days)
    past_date = today - timedelta(days=days)
    return (
        f"Hoje: {today.strftime('%d-%m-%Y (%A)')}\n"
        f"{days} dias à frente será: {future_date.strftime('%d-%m-%Y (%A)')}\n"
        f"{days} dias atrás foi: {past_date.strftime('%d-%m-%Y (%A)')}"
    )

def main():
    """
    Função principal do script.
    """
    print(
        """
    ,╔╦╗┬┌─┐┌─┐   ,╔╦╗┌─┐┌┬┐┌─┐   ,
  ,'  ║║│├┤ ├┤  ,'  ║║├─┤ │ ├┤  ,' 
 '   ═╩╝┴└  └  '   ═╩╝┴ ┴ ┴ └─┘'   
        """
    )

    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        user_input = input("Insira uma data no formato (DD-MM-AAAA) ou um valor maior que 1 para calcular diferença de dias (ou 'q' para sair): ")

    tipo, valor = validate_user_input(user_input)

    if tipo == "data":
        start_date = datetime.today()
        end_date = datetime.strptime(valor, "%d-%m-%Y")
        print(
            f"Diferença entre hoje {start_date.strftime('%d-%m-%Y (%A)')} "
            f"e {end_date.strftime('%d-%m-%Y (%A)')} é de:\n"
            f"{calculate_date_diff(start_date, end_date)}"
        )
    elif tipo == "dias":
        print(calculate_future_past_dates(valor))
    elif tipo == "sair":
        print("Saindo...")
        sys.exit(0)
    else:
        print(
            "Entrada inválida. Insira uma data no formato DD-MM-AAAA ou\n"
            "um número inteiro maior ou igual a 1 (ou 'q'/'Q' para sair)."
        )

if __name__ == "__main__":
    main()
