# Calculadora de Distâncias entre Cidades

Este programa permite que você insira o número de cidades e as distâncias entre elas, e depois calcula a distância total de um itinerário especificado. O usuário pode também verificar se a distância total informada está correta.

## Funcionalidades

- Solicita o número de cidades.
- Permite a inserção das distâncias entre as cidades, formando uma matriz de distâncias.
- Permite que o usuário informe um itinerário, que é uma sequência de cidades a serem visitadas.
- Calcula a distância total com base no itinerário fornecido.
- Compara a distância calculada com a distância informada pelo usuário e verifica se estão corretas.

## Como o programa funciona

1. **Entrada do Número de Cidades**: O programa começa solicitando que o usuário insira o número de cidades. É realizada uma validação para garantir que a entrada seja um número positivo.

2. **Criação da Matriz de Distâncias**:
   - O programa pede ao usuário que informe as distâncias entre cada par de cidades.
   - As distâncias devem ser não negativas. Se o usuário inserir uma distância negativa, será solicitado que ele insira um valor válido.

3. **Exibição da Matriz**: Após a inserção das distâncias, a matriz de distâncias é exibida em um formato legível.

4. **Entrada do Itinerário**:
   - O usuário pode informar um itinerário, que é uma lista de cidades separadas por espaço. O programa valida se as cidades informadas são válidas (ou seja, se estão dentro do intervalo das cidades existentes).
   - O usuário pode encerrar o programa digitando `sair`.

5. **Cálculo da Distância Total**: Para cada par de cidades no itinerário, o programa calcula a distância total percorrida.

6. **Comparação de Distâncias**:
   - O usuário é solicitado a informar a distância total esperada do itinerário.
   - O programa então compara a distância total calculada com a distância informada e informa se estão corretas.

## Exemplo de Uso

1. Ao iniciar o programa, você será solicitado a inserir o número de cidades.
2. Em seguida, insira as distâncias entre cada cidade.
3. Após inserir a matriz de distâncias, você pode informar um itinerário.
4. O programa calculará a distância total e solicitará que você informe a distância esperada.
5. Por fim, ele informará se a distância calculada e a distância informada estão corretas.

### Observações

- O programa garante que as entradas sejam válidas, evitando erros de inserção.
- A matriz de distâncias é apresentada de forma organizada para facilitar a visualização.

