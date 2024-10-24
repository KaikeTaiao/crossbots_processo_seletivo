# Jogo dos Pauzinhos

Este programa implementa o clássico Jogo dos Pauzinhos, onde dois jogadores (um humano e um bot) se revezam retirando pauzinhos até que não reste nenhum. O jogador que retirar o último pauzinho vence a partida.

## Funcionalidades

- O usuário define a quantidade inicial de pauzinhos.
- O Jogador 1 (humano) pode retirar entre 1 a 3 pauzinhos por turno.
- O Jogador 2 (bot) utiliza uma estratégia simples para retirar os pauzinhos restantes.
- O jogo termina quando não há mais pauzinhos disponíveis, e o vencedor é anunciado.

## Como o programa funciona

1. **Exibir Pauzinhos**: A função `exibir_pauzinhos(n)` é responsável por mostrar a quantidade atual de pauzinhos na tela, representando cada pauzinho como uma barra vertical (`|`).

2. **Jogada do Bot**: A função `jogador_2_retira(n)` decide quantos pauzinhos o bot deve retirar com base no número de pauzinhos restantes. O bot tenta sempre deixar um número que seja múltiplo de 4 para dificultar a jogada do humano.

3. **Fluxo do Jogo**:
   - O programa solicita ao jogador a quantidade inicial de pauzinhos.
   - O jogo entra em um loop onde os jogadores se alternam para retirar pauzinhos.
   - O Jogador 1 faz sua jogada e o programa valida se a jogada é permitida (1 a 3 pauzinhos e não mais do que os disponíveis).
   - O bot então faz sua jogada, retirando um número de pauzinhos conforme sua estratégia.
   - O jogo termina quando um dos jogadores retira o último pauzinho, e o vencedor é anunciado.

## Exemplo de uso

Para jogar, basta executar o programa e seguir as instruções na tela. O jogador deve informar quantos pauzinhos deseja retirar, e o bot fará o seu movimento automaticamente.

