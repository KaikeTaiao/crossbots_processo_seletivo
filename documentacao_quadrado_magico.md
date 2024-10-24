# Documentação do Programa: Quadrado Mágico

Oi, pessoal! Neste projeto, criei um programa em Python que verifica se uma matriz é um quadrado mágico. Vou explicar um pouco sobre como funciona.

## O que é um quadrado mágico?

Um quadrado mágico é uma matriz quadrada onde a soma dos números em cada linha, cada coluna e nas duas diagonais é sempre a mesma. É um conceito bem legal da matemática!

## Como o programa funciona?

1. **Solicitação da ordem do quadrado:** O programa começa pedindo para você digitar a ordem do quadrado mágico (ou seja, o tamanho da matriz). Você pode escolher um número entre 2 e 10. Se o número não estiver dentro desse intervalo, ele te avisa e pede para tentar de novo.

2. **Entrada dos elementos:** Depois disso, você precisa inserir os elementos de cada linha da matriz. Para facilitar, é só separar os números por espaço. Mas atenção: cada linha precisa ter o mesmo número de elementos que a ordem que você escolheu.

3. **Verificação:** Assim que a matriz estiver completa, o programa faz uma série de verificações:
   - Primeiro, ele pega a soma da primeira linha como referência.
   - Em seguida, verifica se todas as linhas têm a mesma soma.
   - Depois, ele checa as colunas e as duas diagonais para garantir que elas também têm a mesma soma.

4. **Resultado:** No final, se tudo estiver certo, o programa te informa que a matriz é um quadrado mágico e mostra a soma. Caso contrário, ele diz que não é um quadrado mágico e imprime "-1".

## Erros e Tratamento

O programa também cuida de possíveis erros. Se você tentar inserir algo que não seja um número inteiro ou se a matriz não tiver o tamanho correto, ele te avisa e pede para tentar novamente.
