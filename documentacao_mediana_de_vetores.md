
# Calculadora de Mediana de Vetores

Este programa calcula a mediana de dois vetores fornecidos pelo usuário. Além disso, ele une os dois vetores, remove duplicatas e calcula a mediana do vetor resultante.

## Funcionalidades

- Solicita dois vetores do usuário.
- Ordena cada vetor individualmente.
- Une os dois vetores, remove elementos duplicados e ordena o vetor resultante.
- Calcula e exibe a mediana de cada vetor individual e do vetor unido.

## Como o Programa Funciona

1. **Entrada dos Vetores**:
   - Ao iniciar, o programa solicita ao usuário que insira os elementos do primeiro vetor, separados por espaço.
   ```python
   Digite os elementos do primeiro vetor (separados por espaço): 3 1 2
   ```
   - Em seguida, o usuário é solicitado a inserir os elementos do segundo vetor.
   ```python
   Digite os elementos do segundo vetor (separados por espaço): 5 3 6
   ```

2. **Ordenação dos Vetores**:
   - Os vetores inseridos são ordenados em ordem crescente.

3. **União dos Vetores**:
   - Os dois vetores são unidos em um único vetor, removendo quaisquer elementos duplicados.
   - O vetor resultante é então ordenado.

4. **Cálculo da Mediana**:
   - A mediana é calculada para cada vetor individual e para o vetor unido.
   - Se o número de elementos for ímpar, a mediana é o elemento central.
   - Se o número de elementos for par, a mediana é a média dos dois elementos centrais.

5. **Exibição dos Resultados**:
   - O programa exibe os vetores ordenados e as medianas calculadas.

## Exemplo de Uso

1. Ao iniciar o programa, você será solicitado a inserir os elementos do primeiro vetor.
   ```python
   Digite os elementos do primeiro vetor (separados por espaço): 3 1 2
   ```

2. Em seguida, insira os elementos do segundo vetor.
   ```python
   Digite os elementos do segundo vetor (separados por espaço): 5 3 6
   ```

3. O programa exibirá os vetores ordenados e a mediana de cada vetor, bem como a mediana do vetor unido:
   ```
   Vetor 1 ordenado: [1, 2, 3]
   Vetor 2 ordenado: [3, 5, 6]
   Vetor unido e ordenado: [1, 2, 3, 5, 6]

   Mediana do vetor 1: 2
   Mediana do vetor 2: 5
   Mediana do vetor unido: 3
   ```

## Detalhes de Implementação

### Função `calcular_mediana(vetor)`

Esta função recebe um vetor como parâmetro e retorna a mediana do vetor.

- Se o vetor tiver um número ímpar de elementos, a função retorna o elemento central.
- Se o vetor tiver um número par de elementos, a função retorna a média dos dois elementos centrais.

### Entrada e Validação

- O programa valida as entradas, garantindo que os elementos inseridos sejam números inteiros.
- Se a entrada não for válida, uma mensagem de erro será exibida, e o usuário será solicitado a tentar novamente.