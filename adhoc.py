from base import *

def alcancar_cantos(tabuleiro):
    if tabuleiro[(0,0)] <= 0:
        if checar_massa_critica(tabuleiro, (0,0)):
            return (0,0)
    elif tabuleiro[(0,5)] <= 0:
        if checar_massa_critica(tabuleiro, (0,5)):
            return (0,5)
    elif tabuleiro[(8,0)] <= 0:
        if checar_massa_critica(tabuleiro, (8,0)):
            return (8,0)
    elif tabuleiro[(8,5)] <= 0:
        if checar_massa_critica(tabuleiro, (8,5)):
            return (8,5)
    else:
        return cantos_bloqueados(tabuleiro)

def checar_massa_critica(tabuleiro, pos):
    if Tabuleiro.massa_critica(tabuleiro, pos) == abs(tabuleiro[pos]) :
        return False
    else:
        return True

def cantos_bloqueados(tabuleiro):
    for pos in [(x, y) for x in xrange(tabuleiro.linhas) for y in xrange(tabuleiro.colunas)]:
        if tabuleiro(pos) <= 0:
            if checar_massa_critica(tabuleiro, pos):
                return pos
    return (-1,-1)

def adhoc(tabuleiro):
    return alcancar_cantos(tabuleiro)
