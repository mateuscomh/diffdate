# ----------------------------------------------------------------------------
# Programa para calcular a data futura após adicionar um número específico de dias
#
# Descrição: Este programa calcula a data que será após adicionar um número de dias
# a partir de uma data inicial fornecida.
#
# Versão: 1.3.0
# Data de criação: 11/03/2022
# Autor: Matheus Martins - 3mhenrique@gmail.com
# Modificado em: 15/07/2025
# ----------------------------------------------------------------------------
from datetime import datetime, timedelta
import sys
import locale

# Configura o locale para Português do Brasil para nomes de dias da semana
# Isso pode requerer que o locale 'pt_BR' esteja instalado no sistema operacional
try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
except locale.Error:
    print("Locale 'pt_BR.UTF-8' não encontrado. Usando locale padrão.")


def validate_user_input(user_input):
    """
    Valida a entrada do usuário.
    Retorna uma tupla (tipo, valor) onde:
    - tipo: "data" se for uma data no formato DD-MM-AAAA (também aceita DD/MM/AAAA)
            "dias" se for um número inteiro
            "sair" se for 'q' ou 'Q', ou None se inválido.
    - valor: a data (como string no formato padronizado), o número de dias, ou None.
    """
    if user_input.lower() == 'q':
        return "sair", None

    # Normaliza separador de datas
    normalized = user_input.replace("/", "-")

    try:
        # Verifica se é uma data no formato DD-MM-AAAA
        date_obj = datetime.strptime(normalized, "%d-%m-%Y")
        return "data", date_obj.strftime("%d-%m-%Y")
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

    # Guarda a diferença total original em dias
    total_diff_days = (end_date - start_date).days

    # Garante que a data mais antiga seja a primeira para o cálculo
    if start_date > end_date:
        d1 = end_date
        d2 = start_date
    else:
        d1 = start_date
        d2 = end_date

    year_diff = d2.year - d1.year
    month_diff = d2.month - d1.month
    day_diff = d2.day - d1.day

    if day_diff < 0:
        month_diff -= 1
        # Pega o último dia do mês anterior para o empréstimo
        prev_month_last_day = (d2.replace(day=1) - timedelta(days=1)).day
        day_diff += prev_month_last_day

    if month_diff < 0:
        year_diff -= 1
        month_diff += 12

    result = []
    if year_diff > 0:
        plural = "s" if year_diff > 1 else ""
        result.append(f"{year_diff} ano{plural}")
    if month_diff > 0:
        plural = "es" if month_diff > 1 else ""
        result.append(f"{month_diff} mês{plural}")
    if day_diff > 0:
        plural = "s" if day_diff > 1 else ""
        result.append(f"{day_diff} dia{plural}")

    # Se a diferença for 0, informa isso.
    if not result:
        result.append("0 dia(s)")
        
    # Usa o valor absoluto para a frase final
    plural_total = "s" if abs(total_diff_days) != 1 else ""
    result.append(f"\nTotal de {abs(total_diff_days)} dia{plural_total}")
    
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
        f"Hoje: {today.strftime('%d-%m-%Y (%A)').capitalize()}\n"
        f"{days} dias à frente será: {future_date.strftime('%d-%m-%Y (%A)').capitalize()}\n"
        f"{days} dias atrás foi: {past_date.strftime('%d-%m-%Y (%A)').capitalize()}"
    )


def main():
    """
    Função principal do script.
    """
    print(
        """
     ,╔╦╗┬┌─┐┌─┐   ,╔╦╗┌─┐┌┬┐┌─┐   ,
   ,'  ║║│├┤ ├┤   ,'  ║║├─┤ │ ├┤   ,' 
  '    ═╩╝┴└─┘└─┘'    ═╩╝┴ ┴ ┴ └─┘'   
        """
    )

    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        user_input = input("Insira uma data (DD-MM-AAAA) ou um número de dias (ou 'q' para sair): ")

    tipo, valor = validate_user_input(user_input)

    if tipo == "data":
#        start_date = datetime.today()
        start_date = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = datetime.strptime(valor, "%d-%m-%Y")
        print(
            f"Diferença entre hoje {start_date.strftime('%d-%m-%Y (%A)').capitalize()} "
            f"e {end_date.strftime('%d-%m-%Y (%A)').capitalize()} é de:\n"
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
            "um número inteiro maior que 0 (ou 'q'/'Q' para sair)."
        )


if __name__ == "__main__":
    main()
