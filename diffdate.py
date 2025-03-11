
# ----------------------------------------------------------------------------
# Programa para calcular a data futura após adicionar um número específico de dias
#
# Descrição: Este programa calcula a data que será após adicionar um número de dias
# a partir de uma data inicial fornecida.
#
# Versão: 1.1.0
# Data de criação: 11/03/2022
# Autor: Matheus Martins - 3mhenrique@gmail.com
# ----------------------------------------------------------------------------
from datetime import datetime, timedelta

def validate_user_input(user_input):
    """
    Valida a entrada do usuário.
    Retorna uma tupla (tipo, valor) onde:
    - tipo: "data" se for uma data no formato AAAA-MM-DD, "dias" se for um número inteiro, ou None se inválido.
    - valor: a data ou o número de dias.
    """
    try:
        # Verifica se é uma data no formato AAAA-MM-DD
        datetime.strptime(user_input, "%Y-%m-%d")
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
    # Garante que as datas sejam objetos datetime
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # Calcula a diferença total em dias
    diff_days = (end_date - start_date).days

    # Obtém a diferença exata de anos, meses e dias
    year_diff = end_date.year - start_date.year
    year_diff = abs(year_diff)
    month_diff = end_date.month - start_date.month
    month_diff = abs(month_diff)
    day_diff = end_date.day - start_date.day
    day_diff = abs(day_diff)

    # Ajusta valores negativos corretamente
    if day_diff < 0:
        month_diff -= 1
        # Obtém o número de dias do mês anterior
        prev_month_last_day = (end_date.replace(day=1) - timedelta(days=1)).day
        day_diff += prev_month_last_day

    if month_diff < 0:
        year_diff -= 1
        month_diff += 12

    # Monta a diferença formatada, ignorando valores zero
    result = []
    if year_diff != 0:
        result.append(f"{abs(year_diff)} ano(s)")
    if month_diff != 0:
        result.append(f"{abs(month_diff)} mês(es)")
    if day_diff != 0:
        result.append(f"{abs(day_diff)} dia(s)")

    # Retorna a diferença formatada
    return ", ".join(result)

def calculate_future_past_dates(days):
    """
    Calcula a data futura ou passada com base em um número de dias.
    Retorna uma string formatada com as datas.
    """
    today = datetime.today()
    future_date = today + timedelta(days=days)
    past_date = today - timedelta(days=days)
    return (
        f"Hoje: {today.strftime('%Y-%m-%d (%A)')}\n"
        f"{days} dias de adiante será: {future_date.strftime('%Y-%m-%d (%A)')}\n"
        f"{days} dias de atrás foi: {past_date.strftime('%Y-%m-%d (%A)')}"
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

    user_input = input("Insira uma data no formato (AAAA-MM-DD) ou um valor maior que 1 para calcular diferença de dias: ")

    tipo, valor = validate_user_input(user_input)

    if tipo == "data":
        start_date = datetime.today()
        end_date = datetime.strptime(valor, "%Y-%m-%d")
        print(
            f"Diferença entre hoje {start_date.strftime('%Y-%m-%d (%A)')} e {end_date.strftime('%Y-%m-%d (%A)')} é de: "
            f"{calculate_date_diff(start_date, end_date)}"
        )
    elif tipo == "dias":
        print(calculate_future_past_dates(valor))
    else:
        print("Entrada inválida. Insira uma data no formato AAAA-MM-DD ou um número inteiro maior ou igual a 1.")

if __name__ == "__main__":
    main()
