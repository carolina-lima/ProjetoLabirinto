from time import sleep


PAREDE = '#'
CAMINHO_LIVRE = ' '
CAMINHO_PERCORRIDO = "2"
ROBO = "4"
SAIDA = "S"
PILHA = []

ESQUERDA = [0, -1]
DIREITA  = [0, 1]
CIMA     = [-1, 0]
BAIXO    = [1, 0]

LABIRINTO = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
    ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#'], 
    ['#', '#', '#', '#', '#', '#', ' ', ' ', '4', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#'], 
    ['#', '#', '#', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'], 
    ['#', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', '#', ' ', '#'], 
    ['#', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#'], 
    ['#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', '#'], 
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'S', '#']
]


def print_labirinto():
    print("")
    for linha in LABIRINTO:
        print("".join(linha))
    print("")


def movimento(posicao: tuple, direcao: list):

    if  LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] == ' ':

        LABIRINTO[posicao[0]][posicao[1]] = CAMINHO_PERCORRIDO
        LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] = ROBO
        PILHA.append([posicao[0] + direcao[0]],[posicao[1] + direcao[1]])

        return [posicao[0] + direcao[0], posicao[1] + direcao[1]]
    else:
        LABIRINTO[PILHA.pop()] = ROBO

    
def verifica_movimento(posicao: tuple, direcao: list) -> bool:
    if LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] == SAIDA:
        print("SUCESSO")#pq tinha um raise aqui?
        return True
    else:
        return (LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] == CAMINHO_LIVRE) and False


def main():
    POSICAO_INICIAL = [3, 16]
    PILHA = [POSICAO_INICIAL]

    LABIRINTO[POSICAO_INICIAL[0]][POSICAO_INICIAL[1]] = ROBO

    print_labirinto()

    POSICAO_ATUAL = POSICAO_INICIAL

    while POSICAO_ATUAL != SAIDA:
        if verifica_movimento(POSICAO_ATUAL, BAIXO): #se a direção for a saída = true
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, BAIXO)
            print_labirinto()
            sleep(1)
            break
        elif verifica_movimento(POSICAO_ATUAL, CIMA): #se a direção for a saída = true
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, CIMA)
            print_labirinto()
            sleep(1)
            break
        elif verifica_movimento(POSICAO_ATUAL, ESQUERDA): #se a direção for a saída = true
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, ESQUERDA)
            print_labirinto()
            sleep(1)
            break
        elif verifica_movimento(POSICAO_ATUAL, DIREITA): #se a direção for a saída = true
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, DIREITA)
            print_labirinto()
            sleep(1)
            break
        

if __name__ == "__main__":
    main()

