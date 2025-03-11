#!/usr/bin/env bash

# ----------------------------------------------------------------------------
# Programa em shell para calcular a data futura após adicionar um número específico de dias
#
# Descrição: Este script calcula a data que será após adicionar um número de dias
# a partir de uma data inicial fornecida.
#
# Versão: 2.1.0
# Data de criação: 11/03/2022
# Autor: Matheus Martins - 3mhenrique@gmail.com
# ----------------------------------------------------------------------------

input="$1"
today=$(date +"%Y-%m-%d %H:%M:%S")

# Função para validar a entrada do usuário
validate_user_input() {
    if [ -z "$input" ]; then
        echo -n "Insira uma data no formato (AAAA-MM-DD) ou um valor maior que 1 para calcular diferença de dias: "
        IFS= read -r input
    fi

    [[ "$input" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]] && choice="D" && return 0
    [[ "$input" =~ ^[1-9][0-9]*$ ]] && choice="N" && return 0
    [[ "$input" =~ ^[qQ] ]] && echo "Bye.." && return 0

    return 1
}

# Função para calcular a diferença entre duas datas
calculate_date_diff() {
    local start_date="$1"
    local end_date="$2"

    # Obtém a diferença total em dias
    diff_days=$(( ($(date -d "$end_date" +%s) - $(date -d "$start_date" +%s)) / 86400 ))

    # Obtém a diferença exata de anos, meses e dias
    local start_year=$(date -d "$start_date" +%Y)
    local end_year=$(date -d "$end_date" +%Y)
    local start_month=$(date -d "$start_date" +%m)
    local end_month=$(date -d "$end_date" +%m)
    local start_day=$(date -d "$start_date" +%d)
    local end_day=$(date -d "$end_date" +%d)

    local year_diff=$((end_year - start_year))
    local month_diff=$((end_month - start_month))
    local day_diff=$((end_day - start_day))

    # Ajusta valores negativos corretamente
    if [ "$day_diff" -lt 0 ]; then
        month_diff=$((month_diff - 1))
        # Obtém o número de dias do mês anterior
        local prev_month_last_day=$(date -d "$end_date -$(date -d "$end_date" +%d) days" +%d)
        day_diff=$((day_diff + prev_month_last_day))
    fi

    if [ "$month_diff" -lt 0 ]; then
        year_diff=$((year_diff - 1))
        month_diff=$((month_diff + 12))
    fi

    # Monta a diferença formatada, ignorando valores zero
    local result=""
    [ "$year_diff" -gt 0 ] && result+="$year_diff ano(s), "
    [ "$month_diff" -gt 0 ] && result+="$month_diff mês(es), "
    [ "$day_diff" -gt 0 ] && result+="$day_diff dia(s) "

    # Remove a vírgula final, se houver
    result="${result%, }"

    # Retorna a diferença formatada
    echo "$result"
}

# Função para calcular datas futuras ou passadas
calculate_future_past_dates() {
    local days="$1"
    echo "Hoje: $today ($(date -d "$today" +%A))"
    echo "$days dias de adiante será: $(date -d "+$days days" +"%Y-%m-%d (%A)")"
    echo "$days dias de atrás foi: $(date -d "-$days days" +"%Y-%m-%d (%A)")"
}

# Função para exibir uma data com o dia da semana
format_date_with_weekday() {
    local date="$1"
    echo "$date ($(date -d "$date" +%A))"
}

# Exibe o cabeçalho do script
echo "
    ,╔╦╗┬┌─┐┌─┐   ,╔╦╗┌─┐┌┬┐┌─┐   ,
  ,'  ║║│├┤ ├┤  ,'  ║║├─┤ │ ├┤  ,' 
 '   ═╩╝┴└  └  '   ═╩╝┴ ┴ ┴ └─┘'   
"

# Valida a entrada do usuário e executa a lógica correspondente
if validate_user_input "$input"; then
    case "$choice" in
    D)
        start_date=$(date +%Y-%m-%d)
        end_date=$(date -d "$input" +%Y-%m-%d)
        echo "Diferença entre hoje $(format_date_with_weekday "$start_date") e $(format_date_with_weekday "$end_date") é de: "
        calculate_date_diff "$start_date" "$end_date"
        echo "Total de $diff_days dia(s)"
        ;;
    N)
        calculate_future_past_dates "$input"
        ;;
    esac
else
    echo "Entrada inválida. Insira uma data no formato AAAA-MM-DD ou um número inteiro maior ou igual a 1."
    exit 1
fi
