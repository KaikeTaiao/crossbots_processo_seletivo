import random

# Função para jogar a Roleta
def jogar_roleta(saldo, aposta):
    print("\n--- Roleta ---")
    while True:
        try:
            numero_apostado = input("Aposte em um número de 0 a 36: ")
            if numero_apostado.isdigit():
                numero_apostado = int(numero_apostado)
                if numero_apostado < 0 or numero_apostado > 36:
                    print("Por favor, escolha um número entre 0 e 36.")
                    continue
                break
            else:
                print("Entrada inválida. Por favor, insira um número válido.")
        except ValueError:
            print("Erro. Insira um número válido.")

    numero_sorteado = random.randint(0, 36)
    print(f"Número sorteado: {numero_sorteado}")
    
    if numero_apostado == numero_sorteado:
        ganho = aposta * 35
        print(f"Você ganhou! Você recebeu R$ {ganho:.2f}.")
        saldo += ganho
    else:
        print("Você perdeu a aposta.")
        saldo -= aposta
    
    return saldo

# Função para jogar Blackjack
def jogar_blackjack(saldo, aposta):
    print("\n--- Blackjack ---")
    
    jogador = random.randint(16, 21)
    casa = random.randint(16, 21)
    
    print(f"Sua pontuação: {jogador}")
    print(f"Pontuação da casa: {casa}")
    
    if jogador > 21:
        print("Você estourou e perdeu a aposta.")
        saldo -= aposta
    elif jogador > casa or casa > 21:
        print("Você ganhou!")
        saldo += aposta
    else:
        print("Você perdeu!")
        saldo -= aposta
    
    return saldo

# Função para jogar Caça-Níquel
def jogar_caca_niquel(saldo, aposta):
    print("\n--- Caça-Níquel ---")
    
    simbolos = ["Cereja", "Limão", "Melancia", "7", "BAR"]
    sorteados = [random.choice(simbolos) for _ in range(3)]
    
    print(f"Símbolos sorteados: {' | '.join(sorteados)}")
    
    if len(set(sorteados)) == 1:
        ganho = aposta * 10
        print(f"Você ganhou! Você recebeu R$ {ganho:.2f}.")
        saldo += ganho
    else:
        print("Você perdeu a aposta.")
        saldo -= aposta
    
    return saldo

# Função para converter texto em número
def converter_valor(valor_texto):
    valor_texto = valor_texto.replace(",", ".")
    try:
        return float(valor_texto)
    except ValueError:
        return None

# Função principal para o cassino
def cassino():
    print("Bem-vindo ao Cassino CrossBets!")

    # Valida a entrada do saldo inicial, aceitando texto
    while True:
        saldo_texto = input("Informe o saldo inicial: R$ ")
        saldo = converter_valor(saldo_texto)
        if saldo is None or saldo <= 0:
            print("Por favor, insira um valor numérico positivo.")
        else:
            break

    while saldo > 0:
        print("\nEscolha o jogo:")
        print("1. Roleta")
        print("2. Blackjack")
        print("3. Caça-Níquel")
        print("ou digite o nome do jogo correspondente (Roleta, Blackjack, Caça-Níquel).")

        escolha = input("Digite o número do jogo ou 'sair' para encerrar: ").strip().lower()

        # Aceita tanto o número quanto o nome do jogo
        if escolha in ["1", "roleta"]:
            # Aqui, a aposta deve ser definida antes de chamar a função.
            aposta = definir_aposta(saldo)
            saldo = jogar_roleta(saldo, aposta)
        elif escolha in ["2", "blackjack"]:
            aposta = definir_aposta(saldo)
            saldo = jogar_blackjack(saldo, aposta)
        elif escolha in ["3", "caça-níquel"]:
            aposta = definir_aposta(saldo)
            saldo = jogar_caca_niquel(saldo, aposta)
        elif escolha == "sair":
            print(f"Você saiu com R$ {saldo:.2f} de saldo. Obrigado por jogar!")
            break
        else:
            print("Escolha inválida. Tente novamente.")
            continue

        print(f"Seu saldo atual é: R$ {saldo:.2f}")

        if saldo <= 0:
            print("Seu saldo zerou! Jogo encerrado.")

def definir_aposta(saldo):
    while True:
        aposta_texto = input("Informe o valor da aposta: R$ ")
        aposta = converter_valor(aposta_texto)
        if aposta is None or aposta <= 0:
            print("A aposta deve ser um número maior que 0.")
        elif aposta > saldo:
            print("Você não pode apostar mais do que o saldo disponível.")
        else:
            return aposta

# Execução do programa
cassino()
