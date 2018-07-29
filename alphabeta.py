from base import *

def melhor_jogada(tabuleiro, colunas = 10):
	configuracao = {}
	for pos in [(x, y) for x in xrange(tabuleiro.linhas) for y in xrange(tabuleiro.colunas)]:
		if tabuleiro.novo_movimento == sgn(tabuleiro[pos]) or 0 == sgn(tabuleiro[pos]): 
			configuracao[pos] = pontuacao(movimento(tabuleiro, pos), tabuleiro.novo_movimento)
			#Retorna somente a posicao vencedora caso encontre
			if configuracao[pos]==10000:
				return [pos]
	return sorted(configuracao, key=configuracao.get, reverse=True)[:colunas]

def alphabeta(tabuleiro, profundidade = 3, largura = 5, alfa = -10000):
	melhores_jogadas = melhor_jogada(tabuleiro, colunas = largura)
	if melhores_jogadas == []:
		return (-1,-1), -10000
	melhor_posicao, melhor_valor = (melhores_jogadas[0], pontuacao(movimento(tabuleiro, melhores_jogadas[0]), tabuleiro.novo_movimento))
	if profundidade == 1:
		return melhor_posicao, melhor_valor
	for nova_posicao in melhor_jogada(tabuleiro):
		novo = movimento(tabuleiro, nova_posicao)
		valor = alphabeta(novo, profundidade = profundidade - 1, alfa = alfa)[1]
		beta = 10000
		if valor > melhor_valor:
			melhor_valor = valor
			melhor_posicao = nova_posicao
		alfa = max(alfa, beta)
		if alfa >= beta:
	   		break
	return melhor_posicao, melhor_valor