#!/bin/bash

validate_user_input() {
  local input="$1"

  [[ "$input" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]] && choice="D" && return 0
  [[ "$input" =~ ^[1-9][0-9]*$ ]] && choice="N" && return 0
  
  return 1
}
echo "
┌┬┐┬┌─┐┌─┐╔╦╗┌─┐┌┬┐┌─┐
 │││├┤ ├┤  ║║├─┤ │ ├┤ 
─┴┘┴└  └  ═╩╝┴ ┴ ┴ └─┘
"
read -p "Insira uma data (AAAA-MM-DD) ou um número inteiro maior ou igual a 1: " input

if validate_user_input "$input"; then
  case "$choice" in
  D)
    difference_in_days=$((($(date +%s) - $(date +%s --date "$input")) / (3600 * 24))) && 
    echo "Diferença de dias entre hoje e $input é de: $difference_in_days dias."
    ;;
  N)
    echo "$input dias adiante será: $(date -d "+$input days")"
    echo "$input dias atrás será: $(date -d "-$input days")"
    ;;
  esac
else
  echo "Entrada inválida. Insira uma data no formato AAAA-MM-DD ou um número inteiro maior ou igual a 1."
  exit 1
fi
