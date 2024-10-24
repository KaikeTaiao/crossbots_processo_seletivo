# Solicita o número de cidades
while True:
    try:
        num_cidades = int(input("Número de cidades: "))
        if num_cidades <= 0:
            print("Por favor, insira um número positivo.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

# Criação da matriz de distâncias
matriz = []

print("Informe as distâncias entre as cidades:")
for i in range(num_cidades):
    linha = []
    for j in range(num_cidades):
        while True:
            try:
                distancia = int(input(f"Distância da cidade {i} para a cidade {j}: "))
                if distancia < 0:
                    print("Por favor, insira uma distância não negativa.")
                    continue
                linha.append(distancia)
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número inteiro.")
    matriz.append(linha)

# Exibição da matriz de distâncias
print("\nMatriz de Distâncias:")
for linha in matriz:
    print(" ".join(map(str, linha)))

# Processamento dos itinerários
while True:
    try:
        itinerario_input = input("\nInforme o itinerário (cidades separadas por espaço, ou 'sair' para encerrar): ")
        if itinerario_input.lower() == 'sair':
            break

        # Processa o itinerário
        itinerario = list(map(int, itinerario_input.split()))

        # Validação do itinerário
        if any(cidade < 0 or cidade >= num_cidades for cidade in itinerario):
            print("Itinerário contém cidades inválidas. Por favor, insira novamente.")
            continue

    except ValueError:
        print("Entrada inválida. Por favor, insira números inteiros separados por espaço.")


    # Cálculo da distância total do itinerário
    distancia_total_calculada = 0

    # Iterar pelas cidades no itinerário
    for i in range(len(itinerario) - 1):
        cidade_atual = itinerario[i]
        proxima_cidade = itinerario[i + 1]
        distancia_total_calculada += matriz[cidade_atual][proxima_cidade]

    # Adicionar a distância de volta à cidade inicial se necessário
    if itinerario[0] == itinerario[-1]:
        distancia_total_calculada += matriz[itinerario[-1]][itinerario[0]]

    # Solicita a distância total esperada do itinerário
    while True:
        try:
            distancia_informada = int(input("Informe a distância total esperada do itinerário: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

    # Exibe os resultados
    print(f"Itinerário: {' -> '.join(map(str, itinerario))}")
    print(f"Distância Total Calculada: {distancia_total_calculada} km")
    print(f"Distância Total Informada: {distancia_informada} km")

    # Verifica se as distâncias estão corretas
    if distancia_total_calculada == distancia_informada:
        print("As distâncias estão corretas.")
    else:
        print("As distâncias estão incorretas.")
