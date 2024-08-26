jogadores = ['X','O']
usuario = 0
jogadas = 0

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


# def posicaoValida():

# def verificaVencedor(tabuleiro, jogadorAtual):

def verificaVelha(tabuleiro):
    if(jogadas == 9):
        imprimirTabuleiro(tabuleiro)
        print('Deu velha!')

# def modoJogador():

# def modoFacil():

# def modoDificil():

def movimentoIndice(movimento):
    mov = int(movimento) - 1


def jogar(tabuleiro, jogadores):
    while jogadas < 9:
        imprimirTabuleiro(tabuleiro)
        jogadorAtual = jogadores[usuario]
        movimento = input(f"Jogador {jogadorAtual}, escolha uma posição (1-9): ")

        if movimento() and int(movimento) in range(1, 10):
            movimento = str(int(movimento))  # Certifica-se de que o movimento é uma string

            if tabuleiro.get(movimento) == ' ':
                tabuleiro[movimento] = jogadorAtual
                jogadas += 1
                if verificarVencedor(tabuleiro, jogadorAtual):
                    imprimirTabuleiro(tabuleiro)
                    print(f"Jogador {jogadorAtual} venceu!")
                return
            # Alternar o jogador
                indiceJogador = 1 - indiceJogador # Alterna entre 0 e 1
            else:
                print("Posição inválida, tente novamente.")
        else:
            print("Entrada inválida. Escolha uma posição entre 1 e 9.")
    return movimento


# def jogadaUsuario():

# def jogadaMaquinaFacil():

# def jogadaMaquinaDificil():

imprimirMenuPrincipal()
tabuleiro = inicializarTabuleiro()
jogo = jogar(tabuleiro, jogadores)
imprimirTabuleiro(tabuleiro)
