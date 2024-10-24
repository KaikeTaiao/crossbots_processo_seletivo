# Cassino CrossBets

Este programa simula um cassino com três jogos: Roleta, Blackjack e Caça-Níquel. O jogador começa com um saldo inicial e pode escolher em qual jogo apostar. O saldo é atualizado de acordo com os resultados dos jogos.

## Estrutura do Programa

### 1. Importação de Módulos

```python
import random
```

O módulo `random` é importado para gerar resultados aleatórios nos jogos.

### 2. Função `jogar_roleta(saldo, aposta)`

Esta função simula o jogo de roleta.

- **Entrada**: `saldo` (o saldo atual do jogador) e `aposta` (o valor apostado).
- **Processo**:
  - O jogador aposta em um número entre 0 e 36.
  - Um número aleatório é sorteado.
  - Se o número apostado for igual ao número sorteado, o jogador ganha 35 vezes o valor da aposta.
  - Caso contrário, o valor da aposta é subtraído do saldo.
- **Saída**: O saldo atualizado.

### 3. Função `jogar_blackjack(saldo, aposta)`

Esta função simula o jogo de blackjack.

- **Entrada**: `saldo` e `aposta`.
- **Processo**:
  - O jogador e a casa recebem pontuações aleatórias entre 16 e 21.
  - Se o jogador estourar (pontuação acima de 21), perde a aposta.
  - Se o jogador tiver uma pontuação maior que a da casa, ele ganha a aposta.
  - Caso contrário, ele perde.
- **Saída**: O saldo atualizado.

### 4. Função `jogar_caca_niquel(saldo, aposta)`

Esta função simula um jogo de caça-níquel.

- **Entrada**: `saldo` e `aposta`.
- **Processo**:
  - Três símbolos são sorteados aleatoriamente de uma lista de símbolos.
  - Se todos os três símbolos forem iguais, o jogador ganha 10 vezes o valor da aposta.
  - Caso contrário, o jogador perde a aposta.
- **Saída**: O saldo atualizado.

### 5. Função `converter_valor(valor_texto)`

Converte uma string de entrada em um valor numérico (float). Isso é útil para tratar entradas de saldo e apostas.

### 6. Função Principal `cassino()`

Esta é a função principal que orquestra o funcionamento do cassino.

- **Processo**:
  - Solicita ao jogador um saldo inicial, garantindo que seja um valor numérico positivo.
  - Permite que o jogador escolha entre os três jogos disponíveis.
  - Para cada jogo, o jogador é solicitado a fazer uma aposta, que não pode exceder o saldo disponível.
  - Atualiza o saldo após cada jogo e informa o jogador sobre seu saldo atual.
  - O jogador pode sair a qualquer momento e o saldo final será exibido.
  - O jogo termina quando o saldo chega a zero ou o jogador decide sair.

### 7. Função `definir_aposta(saldo)`

Solicita ao jogador um valor para a aposta e garante que seja um valor válido (não pode ser maior que o saldo disponível e deve ser um número positivo).

### Execução do Programa

O programa é iniciado chamando a função `cassino()`, que inicia a experiência do jogador no cassino.

## Exemplo de Uso

Ao executar o programa, o jogador verá um prompt solicitando o saldo inicial e, em seguida, poderá escolher os jogos e fazer suas apostas:

```plaintext
Bem-vindo ao Cassino CrossBets!
Informe o saldo inicial: R$ 100
Escolha o jogo:
1. Roleta
2. Blackjack
3. Caça-Níquel
ou digite o nome do jogo correspondente (Roleta, Blackjack, Caça-Níquel).
Digite o número do jogo ou 'sair' para encerrar: Roleta
Informe o valor da aposta: R$ 10
Aposte em um número de 0 a 36: 5
Número sorteado: 22
Você perdeu a aposta.
Seu saldo atual é: R$ 90.00
```

O jogador pode continuar jogando até decidir sair ou até que seu saldo chegue a zero.