import os

def criar_quadrado_magico():
    while True:
        # Limpa a tela para deixar tudo mais organizado
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            # Pede pro usuário digitar a ordem do quadrado mágico
            tamanho = int(input('Digite a ordem do quadrado mágico (mínimo 2 e máximo 10): '))
            
            # Verifica se o tamanho está dentro do esperado
            if tamanho < 2 or tamanho > 10:
                print('A matriz deve ter tamanho entre 2x2 e 10x10.')
                input('Pressione ENTER para tentar novamente.')
                continue
            
            matriz = []
            for i in range(tamanho):
                # Pede pra digitar os elementos da linha
                linha_input = input(f'Digite os elementos da linha {i + 1} (separados por espaço): ')
                linha = []
                
                # Divide a entrada em elementos e transforma em inteiro
                for elemento in linha_input.split():
                    linha.append(int(elemento))
                
                # Checa se a linha tem o número certo de elementos
                if len(linha) != tamanho:
                    print(f'Cada linha deve ter exatamente {tamanho} elementos.')
                    input('Pressione ENTER para tentar novamente.')
                    break
                    
                matriz.append(linha)  # Adiciona a linha à matriz
            
            else:  # Isso só roda se não houver erro anterior
                # Pega a soma da primeira linha como referência
                soma = sum(matriz[0])
                quadrado_magico = True  # Assume que é um quadrado mágico até prova em contrário

                # Verifica se todas as linhas têm a mesma soma
                for linha in matriz:
                    if sum(linha) != soma:
                        quadrado_magico = False  # Se uma linha não bate, não é quadrado mágico
                        break

                # Checa se todas as colunas têm a mesma soma
                for coluna in range(tamanho):
                    soma_coluna = 0
                    for linha in range(tamanho):
                        soma_coluna += matriz[linha][coluna]
                    if soma_coluna != soma:
                        quadrado_magico = False
                        break
                
                # Verifica a soma da diagonal principal
                soma_diagonal_principal = 0
                for i in range(tamanho):
                    soma_diagonal_principal += matriz[i][i]
                if soma_diagonal_principal != soma:
                    quadrado_magico = False
                
                # Verifica a soma da diagonal secundária
                soma_diagonal_secundaria = 0
                for i in range(tamanho):
                    soma_diagonal_secundaria += matriz[i][tamanho - 1 - i]
                if soma_diagonal_secundaria != soma:
                    quadrado_magico = False

                # Se tudo estiver certo, é um quadrado mágico
                if quadrado_magico:
                    print("A matriz é um quadrado mágico!")
                    print(f"A soma de cada linha, coluna e diagonal é: {soma}")
                    for linha in matriz:
                        print(" ".join(str(x) for x in linha))  # Mostra a matriz de forma bonita
                else:
                    print("A matriz não é um quadrado mágico.")
                    print("-1")
                break  # Sai do loop principal
        except ValueError:
            print('Por favor, digite apenas números inteiros.')
            input('Pressione ENTER para tentar novamente.')

# Chama a função principal
criar_quadrado_magico()
