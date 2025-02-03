#!/bin/bash

# ----------------------------------------------------------------------------
# Script para calcular a data futura após adicionar um número específico de dias
#
# Descrição: Este script calcula a data que será após adicionar um número de dias
# a partir de uma data inicial fornecida.
#
# Versão: 1.0
# Data de criação: 11/03/2022
# Autor: Matheus Martins - 3mhenrique@gmail.com
# ----------------------------------------------------------------------------

input="$1"
today=$(date +"%Y-%m-%d")  
validate_user_input() {
  if [ -z "$input" ]; then 
    echo -n "Insira uma data no formato (AAAA-MM-DD) ou um valor maior que 1 para calcular diferença de dias: "
    IFS= read -r input
  fi

  [[ "$input" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]] && choice="D" && return 0
  [[ "$input" =~ ^[1-9][0-9]*$ ]] && choice="N" && return 0

  return 1
  }

echo "
    ,╔╦╗┬┌─┐┌─┐   ,╔╦╗┌─┐┌┬┐┌─┐   ,
  ,'  ║║│├┤ ├┤  ,'  ║║├─┤ │ ├┤  ,' 
 '   ═╩╝┴└  └  '   ═╩╝┴ ┴ ┴ └─┘'   
"
  if validate_user_input "$input"; then
    case "$choice" in
    D)
      diff_dias=$((($(date +%s --date "$input") - $(date +%s)) / (86400))) &&
        echo "Diferença de dias entre hoje $today e $input é de: $diff_dias dias."
      ;;
    N)
      echo "$input dias adiante será: $(date -d "$today + $input days")"
      echo "$input dias atrás foi: $(date -d "$today - $input days")"
      ;;
    esac
  else
    echo "Entrada inválida. Insira uma data no formato AAAA-MM-DD ou um número inteiro maior ou igual a 1."
    exit 1
  fi
