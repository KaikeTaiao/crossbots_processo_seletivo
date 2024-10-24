# Validador de Sudoku

Este programa permite que você insira um tabuleiro de Sudoku 9x9 e verifica se ele é válido. Os números são representados como caracteres, enquanto as células vazias são indicadas por um ponto (`.`).

## Funcionalidades

- Solicita ao usuário que insira as linhas do tabuleiro de Sudoku.
- Verifica se o tabuleiro está dentro das regras do Sudoku:
  - Cada número deve aparecer uma única vez em cada linha.
  - Cada número deve aparecer uma única vez em cada coluna.
  - Cada número deve aparecer uma única vez em cada uma das nove caixas 3x3.
- Exibe o tabuleiro formatado, facilitando a visualização.
- Retorna um resultado indicando se o tabuleiro é válido ou não.

## Como o programa funciona

1. **Entrada do Usuário**: O programa solicita que o usuário insira o tabuleiro de Sudoku. O usuário deve inserir cada linha, usando pontos (`.`) para representar as células vazias. O programa valida se cada linha contém exatamente 9 elementos.

2. **Validação do Tabuleiro**:
   - A função `validar_sudoku(tabuleiro)` percorre cada célula do tabuleiro e usa conjuntos para rastrear os números que já foram vistos em linhas, colunas e caixas 3x3.
   - Se um número repetido for encontrado em qualquer linha, coluna ou caixa, a função retorna `False`, indicando que o tabuleiro não é válido.

3. **Exibição do Tabuleiro**: Após a entrada, o programa exibe o tabuleiro formatado com separadores entre as caixas 3x3, facilitando a visualização.

4. **Resultado**: Após a validação, o programa informa se o tabuleiro é válido ou não.

## Exemplo de Uso

Para usar o programa, execute-o e insira as linhas do tabuleiro de Sudoku. O programa aguardará a entrada de cada linha. Após inserir todas as 9 linhas, ele exibirá o tabuleiro formatado e informará se ele é válido ou não.

