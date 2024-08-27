# FIAP
# ADS - 2° semestre de 2024
# Prof. Fernando Almeida

# Checkpoint 4
# Arquivo: jogo_da_velha(1).py

# Eduarda Tiemi Akamini Machado
# Gustavo de Oliveira Turci Sandrini
# Vitor Viniciues Almeida de Araujo

# 1 de Setembro de 2024

jogadores = ['X','O']
usuario = 0
usuario2 = 0
import random


def inicializarTabuleiro():
    # Função que inicializa o tabuleiro, isto é, prepara o tabuleiro a jogada
    tabuleiro = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]
    return tabuleiro

def imprimirTabuleiro(tabuleiro):
    # Função que imprime o tabuleiro do jogo da velha para o usuário. Se ele já estiver preenchido, imprimir com esses símbolos
    print(f"{tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]}")
    print("--+---+--")
    print(f"{tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]}")
    print("--+---+--")
    print(f"{tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]}")

def imprimirMenuPrincipal():
    # Função que imprime o menu principal do jogo
    print('Bem-vindo ao jogo da velha!')    

# def leiaCoordenadaLinha():
#     # Função sem parâmetro lê e devolve ao usuário a coordenada da linha

# def leiaCoordenadaColuna():
#         # Função sem parâmetro lê e devolve ao usuário a coordenada da coluna

# def imprimePontuacao():


#def posicaoValida():
    

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
    

def verificaVelha(tabuleiro, jogadas):
    if jogadas == 9:
        imprimirTabuleiro(tabuleiro)
        print('Deu velha!')

#def modoJogador():


# def modoDificil():

def movimentoIndice(movimento):
    movimento -= 1
    linha = movimento // 3
    coluna = movimento % 3
    return linha, coluna


# def jogar(tabuleiro, jogadores, usuario):
#     jogadas = 0
#     while jogadas < 9:
#         imprimirTabuleiro(tabuleiro)
#         jogadorAtual = jogadores[usuario]
#         movimento = int(input(f"Jogador {jogadorAtual}, escolha uma posição (1-9): "))


#         if 1 <= movimento <= 9:
#             linha, coluna = movimentoIndice(movimento)
#             if tabuleiro[linha][coluna] == ' ':
#                 tabuleiro[linha][coluna] = jogadorAtual
#                 jogadas += 1
#                 if verificaVencedor(tabuleiro, jogadorAtual):
#                     imprimirTabuleiro(tabuleiro)
#                     print(f"Jogador {jogadorAtual} venceu!")
#                     return
#                 usuario = 1 - usuario
#             else:
#                 print("Está posição já está ocupada, tente novamente.")
#         else:
#             print("Movimento inválido, tente novamente.")
    
#     verificaVelha(tabuleiro, jogadas)

#     return movimento, jogadas


def modoFacil(tabuleiro, jogadores, usuario, usuario2):
    jogadas = 0
    while jogadas < 9:
        imprimirTabuleiro(tabuleiro)
        
        # Movimento do usuário
        jogadorAtual = jogadores[usuario]
        movimento = int(input(f"Jogador {jogadorAtual}, escolha uma posição (1-9): "))
        
        if 1 <= movimento <= 9:
            linha, coluna = movimentoIndice(movimento)
            if tabuleiro[linha][coluna] == ' ':
                tabuleiro[linha][coluna] = jogadorAtual
                jogadas += 1
                if verificaVencedor(tabuleiro, jogadorAtual):
                    imprimirTabuleiro(tabuleiro)
                    print(f"Jogador {jogadorAtual} venceu!")
                    return
            else:
                print("Essa posição já está ocupada, tente novamente.")
                continue
        else:
            print("Movimento inválido, tente novamente.")
            continue
        
        if jogadas >= 9:
            break  # Se o tabuleiro estiver cheio, saia do loop.

        # Movimento da máquina
        jogadorVirtual = jogadores[usuario2]
        while True:
            movimentoMaqui = random.randint(1, 9)
            linha, coluna = movimentoIndice(movimentoMaqui)
            if tabuleiro[linha][coluna] == ' ':
                tabuleiro[linha][coluna] = jogadorVirtual
                jogadas += 1
                if verificaVencedor(tabuleiro, jogadorVirtual):
                    imprimirTabuleiro(tabuleiro)
                    print(f"Jogador {jogadorVirtual} venceu!")
                    return
                break  # Saia do loop da máquina se a jogada foi válida
            else:
                movimentoMaqui = random.randint(1, 9)  # Tente novamente com outro número

    verificaVelha(tabuleiro, jogadas)

    return jogadas

# def jogadaUsuario():

# def jogadaMaquinaFacil():

# def jogadaMaquinaDificil():

imprimirMenuPrincipal()
tabuleiro = inicializarTabuleiro()
#jogo = jogar(tabuleiro, jogadores, usuario)
jogo = modoFacil(tabuleiro, ['X', 'O'], 0, 1)
imprimirTabuleiro(tabuleiro)