from time import sleep

# O ROBO anda e marca o percurso e grava na pilha, mas não consegui fazer a volta dele AINDA (quando encurala). Se colocar a posição 1,15 ele funciona kkkk

PAREDE = '#'
CAMINHO_LIVRE = ' '
CAMINHO_PERCORRIDO = "2"
ROBO = "4"
SAIDA = "S"


ESQUERDA = [0, -1]
DIREITA  = [0, 1]
CIMA     = [-1, 0]
BAIXO    = [1, 0]

LABIRINTO = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
    ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#'], 
    ['#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'], 
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

    LABIRINTO[posicao[0]][posicao[1]] = CAMINHO_PERCORRIDO
    LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] = ROBO
    
    return [posicao[0] + direcao[0], posicao[1] + direcao[1]]

def verifica_movimento(posicao: tuple, direcao: list) -> bool:
    nova_posicao = LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]]

    if nova_posicao == PAREDE:
        return False
    elif nova_posicao == CAMINHO_PERCORRIDO:
        return False
    elif nova_posicao == CAMINHO_LIVRE:
        return True
    elif nova_posicao == SAIDA:
        return True

def main():
    POSICAO_INICIAL = [1, 5]
    pilha = [POSICAO_INICIAL]

    LABIRINTO[POSICAO_INICIAL[0]][POSICAO_INICIAL[1]] = ROBO

    print_labirinto()

    POSICAO_ATUAL = POSICAO_INICIAL

    while POSICAO_ATUAL != SAIDA:
        if verifica_movimento(POSICAO_ATUAL, BAIXO):
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, BAIXO)
            pilha.append(POSICAO_ATUAL)
            print_labirinto()
            sleep(1)
            
        elif verifica_movimento(POSICAO_ATUAL, DIREITA): #se a direção for a saída = true
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, DIREITA)
            pilha.append(POSICAO_ATUAL)
            print_labirinto()
            sleep(1)
            
        elif verifica_movimento(POSICAO_ATUAL, ESQUERDA): #se a direção for a saída = true
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, ESQUERDA)
            pilha.append(POSICAO_ATUAL)
            print_labirinto()
            sleep(1)
            
        elif verifica_movimento(POSICAO_ATUAL, CIMA): #se a direção for a saída = true
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, CIMA)
            pilha.append(POSICAO_ATUAL)
            print_labirinto()
            sleep(1)
        else:
            LABIRINTO[POSICAO_ATUAL[0]][POSICAO_ATUAL[1]] = CAMINHO_PERCORRIDO
            pilha.pop()
            POSICAO_ATUAL = pilha[-1]
            LABIRINTO[POSICAO_ATUAL[0]][POSICAO_ATUAL[1]] = ROBO
            print_labirinto()
            sleep(1)
            continue

if __name__ == "__main__":
    main()

