from base import *
from random import shuffle, randint, choice

def gerar_cantos(tabuleiro):
    c = tabuleiro.colunas
    l = tabuleiro.linhas
    cantos = [(0,0), (0, c - 1), (l - 1, 0), (l - 1, c - 1)]
    return cantos

def alcancar_cantos(tabuleiro):
    cantos = gerar_cantos(tabuleiro)
    shuffle(cantos)
    for pos in cantos:
        if(tabuleiro[pos] <= 0):
            return pos
    return outras_posicoes(tabuleiro)

def outras_posicoes(tabuleiro):
    posicoes_livres = []
    for pos in [(x, y) for x in xrange(tabuleiro.linhas) for y in xrange(tabuleiro.colunas)]:
        if (tabuleiro[pos] <= 0):
            posicoes_livres.append(pos)
    return choice(posicoes_livres)

def adhoc(tabuleiro):
    n_magico = randint(0, 1)
    if(n_magico == 0):
        return outras_posicoes(tabuleiro)
    return alcancar_cantos(tabuleiro)
