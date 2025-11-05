# ----------------------------------------------------------------------------
# Programa para cálculos avançados com datas
#
# Descrição: Este programa calcula a diferença entre datas, dias úteis,
#            e datas futuras/passadas de forma interativa.
#
# Versão: 2.4.0
# Data de criação: 11/03/2022
# Autor: Matheus Martins - 3mhenrique@gmail.com
# Modificado em: 05/11/2025
#
# --- REQUISITOS E INSTRUÇÕES ---
#
# REQUISITOS:
#    - Python 3.6 ou superior.
#    - Biblioteca 'python-dateutil'.
#    - (Opcional) Locale 'pt_BR.UTF-8' instalado no sistema para nomes dos
#      dias da semana em português.
#
# INSTALAÇÃO DA BIBLIOTECA:
#    Abra seu terminal ou prompt de comando e execute:
#    pip install python-dateutil
#
# COMO EXECUTAR:
#    1. Certifique-se de que os requisitos acima estão atendidos.
#    2. Salve este código em um arquivo (ex: diffdate.py).
#    3. Navegue até o diretório do arquivo pelo terminal.
#    4. Execute o comando: python diffdate.py
#
# ----------------------------------------------------------------------------
from datetime import datetime, timedelta
import sys
import locale
from dateutil.relativedelta import relativedelta

try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
except locale.Error:
    print("Locale 'pt_BR.UTF-8' não encontrado. Usando locale padrão.")

# --- NOVO: Feriados Nacionais Fixos ---
# (Não inclui feriados móveis como Carnaval, Páscoa, Corpus Christi)
FERIADOS_FIXOS = {
    "01-01",  # Confraternização Universal
    "21-04",  # Tiradentes
    "01-05",  # Dia do Trabalhador
    "07-09",  # Independência
    "12-10",  # Nossa Sra. Aparecida
    "02-11",  # Finados
    "15-11",  # Proclamação da República
    "25-12",  # Natal
}
# ------------------------------------

def print_header():
    """Imprime o cabeçalho ASCII art do programa."""
    print(
        r"""
      __  _____   _   __    __        __  _____         _          __
     / / |  __ \ (_) / _|  / _|      / / |  __ \        | |         / /
    / /  | |  | | _ | |_  | |_      / /  | |  | |  __ _ | |_  ___   / / 
   / /   | |  | || ||  _| |  _|    / /   | |  | | / _` || __|/ _ \ / /  
  / /    | |__| || || |   | |     / /    | |__| || (_| || |_|  __/ / /   
 /_/     |_____/ |_||_|   |_|    /_/     |_____/  \__,_| \__|\___|/_/    
                                                                      
        """
    )
# ------------------------------------

def parse_input(user_input):
    """
    Analisa a entrada do usuário para determinar a ação a ser tomada.
    Retorna uma tupla (comando, valores).
    """
    if user_input.lower() == 'q':
        return "sair", None

    parts = user_input.split()

    if len(parts) == 1:
        try:
            dias = int(parts[0])
            if dias > 0:
                return "dias", dias
        except ValueError:
            pass

    try:
        dates = [datetime.strptime(p.replace("/", "-"), "%d-%m-%Y") for p in parts]
        if len(dates) == 1:
            return "data_unica", dates[0]
        if len(dates) == 2:
            return "duas_datas", sorted(dates)
    except ValueError:
        return "invalido", None

    return "invalido", None


def calculate_date_diff(start_date, end_date):
    """
    Calcula a diferença entre duas datas usando dateutil para maior precisão.
    Retorna uma string formatada.
    """
    delta = relativedelta(end_date, start_date)
    total_days = (end_date - start_date).days

    result = []
    if delta.years > 0:
        plural = "s" if delta.years > 1 else ""
        result.append(f"{delta.years} ano{plural}")
    if delta.months > 0:
        plural = "es" if delta.months > 1 else ""
        result.append(f"{delta.months} mês{plural}")
    if delta.days > 0:
        plural = "s" if delta.days > 1 else ""
        result.append(f"{delta.days} dia{plural}")

    if not result:
        return "As datas são as mesmas."

    diff_str = ", ".join(result)
    return f"{diff_str}\n(Total de {total_days} dias corridos)"


def get_business_days_count(start_date, end_date):
    """
    Calcula o número de dias úteis (Seg-Sex, exceto feriados fixos) 
    ENTRE duas datas (incluindo o dia inicial e final).
    Retorna um inteiro.
    """
    if start_date > end_date:
        start_date, end_date = end_date, start_date

    business_days = 0
    # MUDANÇA: Voltando a incluir a data inicial (lógica v2.2.0)
    current_date = start_date 
    
    while current_date <= end_date:
        # Checa se é dia de semana (0-4)
        is_weekday = current_date.weekday() < 5
        # MUDANÇA: Checa se NÃO é um feriado fixo
        is_not_holiday = current_date.strftime('%d-%m') not in FERIADOS_FIXOS
        
        if is_weekday and is_not_holiday:
            business_days += 1
            
        current_date += timedelta(days=1)
    
    return business_days


def calculate_future_past_dates(days):
    """
    Calcula a data futura ou passada com base em um número de dias,
    incluindo dias úteis.
    """
    today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    future_date = today + timedelta(days=days)
    past_date = today - timedelta(days=days)

    # MUDANÇA: Calcular dias úteis para o futuro (do dia SEGUINTE até a data futura)
    future_business_days = get_business_days_count(today + timedelta(days=1), future_date)
    # MUDANÇA: Calcular dias úteis para o passado (da data passada até ONTEM)
    past_business_days = get_business_days_count(past_date, today - timedelta(days=1))

    return (
        f"A partir de hoje: {today.strftime('%d-%m-%Y (%A)').capitalize()}\n"
        f"-> Daqui a {days} dias corridos será: {future_date.strftime('%d-%m-%Y (%A)').capitalize()}\n"
        f"   (Total de {future_business_days} dias úteis nesse período)\n"
        f"-> {days} dias corridos atrás foi:  {past_date.strftime('%d-%m-%Y (%A)').capitalize()}\n"
        f"   (Total de {past_business_days} dias úteis nesse período)"
    )


def main():
    """
    Função principal do script, agora com um loop interativo.
    """
    print_header()
    print(
        """
    Bem-vindo ao DiffDate 2.4!
    ---------------------------------------------------------
    COMO USAR:
    - Digite um número de dias (ex: 30)
    - Digite uma data para comparar com hoje (ex: 25-12-2025)
    - Digite duas datas para comparar entre si (ex: 01-01-2025 31-12-2025)
    - Digite 'q' para sair.
    ---------------------------------------------------------
        """
    )
    while True:
        user_input = input("\n> Digite o comando: ")
        command, values = parse_input(user_input)

        if command == "sair":
            print("Até mais!")
            break
        
        elif command == "dias":
            print(calculate_future_past_dates(values))
        
        elif command == "data_unica":
            today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
            date = values
            print(f"--- Comparando {today.strftime('%d-%m-%Y')} com {date.strftime('%d-%m-%Y')} ---")
            print(calculate_date_diff(today, date))
            
            # A função get_business_days_count agora é INCLUSIVA
            business_days_count = get_business_days_count(today, date)
            print(f"Total de {business_days_count} dias úteis (Seg-Sex, exceto feriados fixos).")
        
        elif command == "duas_datas":
            start_date, end_date = values[0], values[1]
            print(f"--- Comparando {start_date.strftime('%d-%m-%Y')} com {end_date.strftime('%d-%m-%Y')} ---")
            print(calculate_date_diff(start_date, end_date))
            
            # A função get_business_days_count agora é INCLUSIVA
            business_days_count = get_business_days_count(start_date, end_date)
            print(f"Total de {business_days_count} dias úteis (Seg-Sex, exceto feriados fixos).")
        
        elif command == "invalido":
            print_header()
            print(">>> Comando não reconhecido. Por favor, verifique o formato e tente novamente.")

if __name__ == "__main__":
    main()
