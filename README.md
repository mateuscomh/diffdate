# DiffDate - Calculadora de Diferença de Datas em Shell

**DiffDate** é um script em Shell que calcula a diferença entre duas datas, exibindo o resultado em anos, meses e dias. Além disso, ele também pode calcular datas futuras ou passadas com base em um número de dias fornecido.

## Funcionalidades

- Calcula a diferença entre duas datas, exibindo o resultado em anos, meses e dias.
- Ignora valores zero (por exemplo, se a diferença for de 0 anos, apenas meses e dias serão exibidos).
- Calcula datas futuras ou passadas com base em um número de dias.
- Exibe o dia da semana para as datas fornecidas.

## Como Usar

### Pré-requisitos

- Bash (testado no Bash 5.x).
- O comando `date` deve estar disponível no sistema.

### Instalação

 Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/diffdate.git
   cd diffdate
   ```
Torne o script executável:
   ```bash
   chmod +x diffdate.sh
   ```
### Uso Básico

#### 1. Calcular Diferença entre Datas

Para calcular a diferença entre a data atual e uma data fornecida, execute o script passando a data no formato `AAAA-MM-DD` como argumento:

   ```bash
./diffdate.sh "2025-11-10"
   ```
**Exemplo de Saída:**
   ```bash
Diferença entre hoje 2025-03-11 (Tuesday) e 2025-11-10 (Monday) é de: 7 mês(es), 30 dia(s).
   ```
#### 2. Calcular Datas Futuras ou Passadas

Para calcular uma data futura ou passada com base em um número de dias, execute o script passando um número inteiro como argumento:
   
   ```bash
./diffdate.sh 100
   ```
**Exemplo de Saída:**
   ```bash
Hoje: 2023-10-05 (Thursday)
100 dias de adiante será: 2024-01-13 (Saturday)
100 dias de atrás foi: 2023-06-27 (Tuesday)
   ```

## Como Contribuir

Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma branch para sua feature (git checkout -b feature/nova-feature).
3. Commit suas mudanças (git commit -m 'Adicionando nova feature').
4. Faça um push para a branch (git push origin feature/nova-feature).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Autor

- **Matheus Martins** - [GitHub](https://github.com/mateuscomh)

---
