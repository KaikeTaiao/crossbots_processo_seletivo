# Define o tamanho do tabuleiro de Sudoku
tamanho = 9

# Cria uma lista vazia para armazenar as linhas do tabuleiro
tabuleiro = []

# Solicita ao usuário que insira o tabuleiro de Sudoku
print("Por favor, insira o tabuleiro de Sudoku 9x9 (use '.' para indicar células vazias):")
for i in range(tamanho):
    linha = input(f"Linha {i + 1}: ")  # Lê a linha do tabuleiro

    # Verifica se a linha contém exatamente 9 elementos
    while len(linha.split()) != tamanho:
        print(f"Erro: Você deve inserir exatamente {tamanho} números (ou '.' para células vazias). Tente novamente.")
        linha = input(f"Linha {i + 1}: ")  # Pede para o usuário digitar novamente

    # Adiciona a linha à lista do tabuleiro, separando os números e pontos
    tabuleiro.append(linha.split())

# Função para verificar se o tabuleiro de Sudoku é válido
def validar_sudoku(tabuleiro):
    # Usamos conjuntos para rastrear os números já vistos em linhas, colunas e caixas
    linhas = [set() for _ in range(tamanho)]
    colunas = [set() for _ in range(tamanho)]
    caixas = [set() for _ in range(9)]

    # Percorre cada célula do tabuleiro
    for i in range(tamanho):
        for j in range(tamanho):
            num = tabuleiro[i][j]
            if num == '.':  # Se a célula estiver vazia, ignora
                continue
            
            # Verifica se o número já foi encontrado na linha atual
            if num in linhas[i]:
                return False  # Número repetido na mesma linha
            linhas[i].add(num)  # Adiciona o número à lista de vistos da linha

            # Verifica se o número já foi encontrado na coluna atual
            if num in colunas[j]:
                return False  # Número repetido na mesma coluna
            colunas[j].add(num)  # Adiciona o número à lista de vistos da coluna

            # Calcula qual caixa 3x3 o número pertence
            box_index = (i // 3) * 3 + (j // 3)
            if num in caixas[box_index]:
                return False  # Número repetido na mesma caixa
            caixas[box_index].add(num)  # Adiciona o número à lista de vistos da caixa

    return True  # Se tudo estiver certo, o tabuleiro é válido

# Exibe o tabuleiro formatado com separadores
print("\nAqui está o tabuleiro que você inseriu:")
for i in range(tamanho):
    # Adiciona uma linha separadora a cada 3 linhas
    if i % 3 == 0 and i != 0:
        print("- - - - - - - - - - -")

    for j in range(tamanho):
        # Adiciona um separador vertical a cada 3 colunas
        if j % 3 == 0 and j != 0:
            print("|", end=" ")

        print(tabuleiro[i][j], end=" ")  # Imprime o número ou ponto da célula

    print()  # Nova linha após cada linha do tabuleiro

# Verifica se o tabuleiro é válido e exibe o resultado
resultado = "verdadeiro" if validar_sudoku(tabuleiro) else "falso"
print("O tabuleiro é válido?", resultado)
