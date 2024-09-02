# FIAP
# ADS - 2° semestre de 2024
# Prof. Fernando Almeida

# Checkpoint 4
# Arquivo: jogo_da_velha(1).py

# Eduarda Tiemi Akamini Machado
# Gustavo de Oliveira Turci Sandrini
# Vitor Viniciues Almeida de Araujo

# 1 de Setembro de 2024

import random  

# Define os jogadores
jogadores = ['X', 'O']
usuario = 0  
usuario2 = 0  

# Função para inicializar o tabuleiro
def inicializarTabuleiro():
    tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    return tabuleiro

# Função para imprimir o tabuleiro no console
def imprimirTabuleiro(tabuleiro):
    print(f"{tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]}")
    print("--+---+--")
    print(f"{tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]}")
    print("--+---+--")
    print(f"{tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]}")

# Função para imprimir o menu principal
def imprimirMenuPrincipal():
    print('Bem-vindo ao jogo da velha!')

# Função para o usuário escolher o modo de jogo
def escolherModoJogo():
    print("Escolha o modo de jogo:")
    print("1 - Jogar contra outro jogador")
    print("2 - Jogar contra a máquina (Modo Fácil)")
    print("3 - Jogar contra a máquina (Modo Difícil)")
    while True:
        escolha = input("Digite o número do modo desejado: ")
        if escolha in ['1', '2', '3']:
            return int(escolha)
        else:
            print("Escolha inválida. Tente novamente.")

# Função para verificar se o jogador atual venceu o jogo
def verificaVencedor(tabuleiro, jogadorAtual):
    # Verifica as linhas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogadorAtual:
            return True
    # Verifica as colunas
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogadorAtual:
            return True
    # Verifica as diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogadorAtual:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogadorAtual:
        return True
    return False

# Função para verificar se deu velha
def verificaVelha(tabuleiro, jogadas):
    if jogadas == 9:  # Se todas as posições estiverem preenchidas
        imprimirTabuleiro(tabuleiro)
        print('Deu velha!')  # Informa que o jogo terminou empatado

# Função para converter o movimento (1-9) em índices de linha e coluna
def movimentoIndice(movimento):
    movimento -= 1  # Ajusta para índices começarem em 0
    linha = movimento // 3  # Calcula a linha
    coluna = movimento % 3  # Calcula a coluna
    return linha, coluna

# Função para jogar no modo jogador vs. jogador
def jogar(tabuleiro, jogadores, usuario):
    jogadas = 0  # Contador de jogadas
    while jogadas < 9:
        imprimirTabuleiro(tabuleiro)
        jogadorAtual = jogadores[usuario]  # Alterna entre 'X' e 'O'
        movimento = int(input(f"Jogador {jogadorAtual}, escolha uma posição (1-9): "))

        if 1 <= movimento <= 9:  # Verifica se o movimento é válido
            linha, coluna = movimentoIndice(movimento)
            if tabuleiro[linha][coluna] == ' ':
                tabuleiro[linha][coluna] = jogadorAtual
                jogadas += 1
                if verificaVencedor(tabuleiro, jogadorAtual):  # Verifica se houve um vencedor
                    imprimirTabuleiro(tabuleiro)
                    print(f"Jogador {jogadorAtual} venceu!")
                    return
                usuario = 1 - usuario  # Alterna o jogador
            else:
                print("Essa posição já está ocupada, tente novamente.")
        else:
            print("Movimento inválido, tente novamente.")

    verificaVelha(tabuleiro, jogadas)  # Verifica se deu empate

# Função para jogar no modo fácil contra a máquina
def modoFacil(tabuleiro, jogadores, usuario, usuario2):
    jogadas = 0  # Contador de jogadas
    while jogadas < 9:
        imprimirTabuleiro(tabuleiro)
        
        jogadorAtual = jogadores[usuario]
        movimento = int(input(f"Jogador {jogadorAtual}, escolha uma posição (1-9): "))
        
        if 1 <= movimento <= 9:  # Verifica se o movimento é válido
            linha, coluna = movimentoIndice(movimento)
            if tabuleiro[linha][coluna] == ' ':
                tabuleiro[linha][coluna] = jogadorAtual
                jogadas += 1
                if verificaVencedor(tabuleiro, jogadorAtual):  # Verifica se houve um vencedor
                    imprimirTabuleiro(tabuleiro)
                    print(f"Jogador {jogadorAtual} venceu!")
                    return
            else:
                print("Essa posição já está ocupada, tente novamente.")
                continue
        else:
            print("Movimento inválido, tente novamente.")
            continue
        
        if jogadas >= 9:  # Se todas as posições estiverem preenchidas, sai do loop
            break

        # Movimento da máquina (aleatório)
        jogadorVirtual = jogadores[usuario2]
        while True:
            movimentoMaqui = random.randint(1, 9)  # Gera um movimento aleatório
            linha, coluna = movimentoIndice(movimentoMaqui)
            if tabuleiro[linha][coluna] == ' ':
                tabuleiro[linha][coluna] = jogadorVirtual
                jogadas += 1
                if verificaVencedor(tabuleiro, jogadorVirtual):  # Verifica se a máquina venceu
                    imprimirTabuleiro(tabuleiro)
                    print(f"Jogador {jogadorVirtual} venceu!")
                    return
                break

    verificaVelha(tabuleiro, jogadas)  # Verifica se deu empate

# Função para jogar no modo difícil contra a máquina
def modoDificil(tabuleiro, jogadores, usuario, usuario2):
    jogadas = 0  # Contador de jogadas
    while jogadas < 9:
        imprimirTabuleiro(tabuleiro)
        
        jogadorAtual = jogadores[usuario]
        movimento = int(input(f"Jogador {jogadorAtual}, escolha uma posição (1-9): "))
        
        if 1 <= movimento <= 9:  # Verifica se o movimento é válido
            linha, coluna = movimentoIndice(movimento)
            if tabuleiro[linha][coluna] == ' ':
                tabuleiro[linha][coluna] = jogadorAtual
                jogadas += 1
                if verificaVencedor(tabuleiro, jogadorAtual):  # Verifica se houve um vencedor
                    imprimirTabuleiro(tabuleiro)
                    print(f"Jogador {jogadorAtual} venceu!")
                    return
            else:
                print("Essa posição já está ocupada, tente novamente.")
                continue
        else:
            print("Movimento inválido, tente novamente.")
            continue
        
        if jogadas >= 9:  # Se todas as posições estiverem preenchidas, sai do loop
            break

        # Movimento inteligente da máquina
        jogadorVirtual = jogadores[usuario2]
        movimentoMaqui = movimentoInteligente(tabuleiro, jogadorVirtual, jogadorAtual)
        linha, coluna = movimentoIndice(movimentoMaqui)
        tabuleiro[linha][coluna] = jogadorVirtual
        jogadas += 1
        if verificaVencedor(tabuleiro, jogadorVirtual):  # Verifica se a máquina venceu
            imprimirTabuleiro(tabuleiro)
            print(f"Jogador {jogadorVirtual} venceu!")
            return

    verificaVelha(tabuleiro, jogadas)  

# Função para determinar o movimento inteligente da máquina no modo difícil
def movimentoInteligente(tabuleiro, jogadorVirtual, jogadorUsuario):
    # Tenta ganhar
    for i in range(1, 10):
        linha, coluna = movimentoIndice(i)
        if tabuleiro[linha][coluna] == ' ':
            tabuleiro[linha][coluna] = jogadorVirtual
            if verificaVencedor(tabuleiro, jogadorVirtual):
                return i
            tabuleiro[linha][coluna] = ' '

    # Tenta bloquear o adversário
    for i in range(1, 10):
        linha, coluna = movimentoIndice(i)
        if tabuleiro[linha][coluna] == ' ':
            tabuleiro[linha][coluna] = jogadorUsuario
            if verificaVencedor(tabuleiro, jogadorUsuario):
                tabuleiro[linha][coluna] = ' '
                return i
            tabuleiro[linha][coluna] = ' '

    # Se não puder ganhar ou bloquear, faz um movimento aleatório
    movimento = random.randint(1, 9)
    while tabuleiro[movimentoIndice(movimento)[0]][movimentoIndice(movimento)[1]] != ' ':
        movimento = random.randint(1, 9)
    return movimento

# Função principal para iniciar o jogo
def iniciarJogo():
    imprimirMenuPrincipal()  
    modo = escolherModoJogo()  
    tabuleiro = inicializarTabuleiro()  
    
    # Executa o modo de jogo escolhido
    if modo == 1:
        jogar(tabuleiro, jogadores, usuario)
    elif modo == 2:
        modoFacil(tabuleiro, jogadores, usuario, 1)
    elif modo == 3:
        modoDificil(tabuleiro, jogadores, usuario, 1)
    
# Inicia o jogo chamando a função iniciarJogo
iniciarJogo()