# Função para calcular a mediana de um vetor
def calcular_mediana(vetor):
    tamanho = len(vetor)
    if tamanho % 2 == 1:
        # Se o tamanho for ímpar, a mediana é o elemento central
        return vetor[tamanho // 2]
    else:
        # Se o tamanho for par, a mediana é a média dos dois elementos centrais
        meio1 = vetor[tamanho // 2 - 1]
        meio2 = vetor[tamanho // 2]
        return (meio1 + meio2) / 2

# Solicitar o primeiro vetor ao usuário
vetor1 = list(map(int, input("Digite os elementos do primeiro vetor (separados por espaço): ").split()))

# Solicitar o segundo vetor ao usuário
vetor2 = list(map(int, input("Digite os elementos do segundo vetor (separados por espaço): ").split()))

# Ordenar os vetores individuais
vetor1_ordenado = sorted(vetor1)
vetor2_ordenado = sorted(vetor2)

# Unir os dois vetores, remover duplicatas e ordenar
vetor_unido = sorted(set(vetor1 + vetor2))

# Exibir os vetores individuais ordenados
print(f"\nVetor 1 ordenado: {vetor1_ordenado}")
print(f"Vetor 2 ordenado: {vetor2_ordenado}")

# Exibir a união dos vetores ordenados
print(f"\nVetor unido e ordenado: {vetor_unido}")

# Calcular a mediana dos vetores individuais e do vetor unido
mediana_vetor1 = calcular_mediana(vetor1_ordenado)
mediana_vetor2 = calcular_mediana(vetor2_ordenado)
mediana_vetor_unido = calcular_mediana(vetor_unido)

# Exibir as medianas
print(f"\nMediana do vetor 1: {mediana_vetor1}")
print(f"Mediana do vetor 2: {mediana_vetor2}")
print(f"Mediana do vetor unido: {mediana_vetor_unido}")