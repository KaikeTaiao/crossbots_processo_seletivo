def exibir_pauzinhos(n):
    """Exibe a quantidade de pauzinhos restantes."""
    print(" ".join(["|"] * n))  # Mostra os pauzinhos como barras verticais

def jogador_2_retira(n):
    """Calcula quantos pauzinhos o bot deve retirar."""
    if n % 4 == 0:
        return 1  # Se o número de pauzinhos é múltiplo de 4, o bot retira 1
    else:
        return n % 4  # Caso contrário, retira o que faz o total ficar múltiplo de 4

def jogo_dos_pauzinhos():
    # Solicita a quantidade inicial de pauzinhos
    n = int(input("Digite a quantidade inicial de pauzinhos: "))
    
    while n > 0:  # Enquanto ainda houver pauzinhos
        # Mostra a quantidade atual de pauzinhos
        exibir_pauzinhos(n)
        
        # Jogador 1 faz sua jogada
        jogada1 = int(input("Jogador 1, quantos pauzinhos você vai retirar (1 a 3)? "))
        
        # Verifica se a jogada é válida
        while jogada1 < 1 or jogada1 > 3 or jogada1 > n:
            jogada1 = int(input(f"Jogada inválida! Você deve retirar de 1 a 3 pauzinhos (restantes: {n}): "))
        
        n -= jogada1  # Remove os pauzinhos escolhidos pelo jogador 1
        
        # Checa se o jogador 1 venceu
        if n <= 0:
            exibir_pauzinhos(n)
            print("Jogador 1 venceu! 🎉")
            break
        
        # Jogador 2 (bot) faz sua jogada
        jogada2 = jogador_2_retira(n)
        print(f"Jogador 2 (bot) retirou {jogada2} pauzinhos.")
        n -= jogada2  # Remove os pauzinhos escolhidos pelo bot
        
        # Checa se o bot venceu
        if n <= 0:
            exibir_pauzinhos(n)
            print("Jogador 2 (bot) venceu! 🤖")
            break

# Inicia o jogo
jogo_dos_pauzinhos()
