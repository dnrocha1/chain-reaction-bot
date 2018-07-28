import copy
import time

# -*- coding: utf-8 -*-

sgn = lambda n: 0 if n == 0 else n/abs(n)
'''Funcao sinal
sgn(n) = -1 se n < 0
sgn(n) = 0 se n = 0
sgn(n) = 1 se n > 0

 '''

class Tabuleiro():
    
    
	def __init__(self, colunas=6, linhas=9, novo_movimento=1):
		'''Construtor do tabuleiro.
		
		Como iremos trabalhar com um tabuleiro 9x6, os valores serao predefinidos no proprio
		construtor, sem possibilidade de alteracaoo. Lembrando que a eficiencia dos algoritmos
		depende, tambem, do tamanho do tabuleiro, qualquer alteracao pode compromete-la.
		
		'''
		self.linhas = linhas
		self.colunas = colunas
		self.tabuleiro = [[0 for i in xrange(self.colunas)] for i in xrange(self.linhas)]
		self.novo_movimento = novo_movimento
    
	def __getitem__(self, posicao):
		return self.tabuleiro[posicao[0]][posicao[1]]
		
	def __setitem__(self, posicao, valor):
		self.tabuleiro[posicao[0]][posicao[1]] = valor 
		
	def __str__(self):
		s = ""
		for i in xrange(self.linhas):
			for j in xrange(self.colunas):
				s += str(self[(i,j)])
				s += " "
			s += "\n"
		return s
	
	def hash(self):
		return str(self.tabuleiro)+str(self.novo_movimento)

		
	def massa_critica(self,posicao):
		'''Essa funcao retorna a massa critica de uma determinada casela do grid
		
		Args:
			posicao (tuple): Tupla com as coordenadas da casela
			
		Return:
			int: Massa critica da casela
		
		'''
		if posicao == (0,0) or posicao == (self.linhas - 1, self.colunas - 1) or posicao == (self.linhas - 1, 0) or posicao == (0, self.colunas - 1):
			return 2
		elif posicao[0] == 0 or posicao[0] == self.linhas-1 or posicao[1] == 0 or posicao[1] == self.colunas-1:
			return 3
		else:
			return 4
	
	def vizinhos(self,posicao):
		'''Essa funcao retorna uma lista com os vizinhos de uma casela.
		
		Args:
			posicao (tuple): Tupla com as coordenadas da casela
			
		Return:
			list: vizinhos da tupla
			
		'''
		vizinhos = []
		possiveis_vizinhos = [(posicao[0],posicao[1]+1), (posicao[0],posicao[1]-1), (posicao[0]+1,posicao[1]), (posicao[0]-1,posicao[1])]
		for i in possiveis_vizinhos:
			if 0 <= i[0] < self.linhas and 0 <= i[1] < self.colunas:
				vizinhos.append(i)
		return vizinhos
		
def movimento(tabuleiro, posicao):
	'''Essa funcao realiza um movimento no tabuleiro.
	
	Obs.: Ela se preocupa com o estado das caselas que ficarao instaveis com o movimento. As reacoes futuras nao
	sao tratadas aqui.
		
	Args:
		tabuleiro (tabuleiro): tabuleiro antes do movimento
		posicao (tuple): Tupla com as coordenadas da casela
		
	Return:
		tabuleiro: estado do tabuleiro imediatamente apos o movimento
			
	'''
	tabuleiro = copy.deepcopy(tabuleiro)
	assert tabuleiro.novo_movimento == sgn(tabuleiro[posicao]) or 0 == sgn(tabuleiro[posicao])
	tabuleiro[posicao] = tabuleiro[posicao] + tabuleiro.novo_movimento
	t = time.time()
	while True:
		instavel = []
		for posicao in [(x,y) for x in xrange(tabuleiro.linhas) for y in xrange(tabuleiro.colunas)]:
			if abs(tabuleiro[posicao]) >= tabuleiro.massa_critica(posicao):
				instavel.append(posicao)
		if time.time() - t >= 3:
			break
		if not instavel:
			break
		for posicao in instavel:
			tabuleiro[posicao] -= tabuleiro.novo_movimento*tabuleiro.massa_critica(posicao)
			for i in tabuleiro.vizinhos(posicao):
				tabuleiro[i] = sgn(tabuleiro.novo_movimento)*(abs(tabuleiro[i])+1)
	tabuleiro.novo_movimento *= -1
	return tabuleiro
	
	'''Funcao para calcular quando deve existir reacao devido a explosao de orbes '''
def reacao(tabuleiro, jogador):
	tabuleiro = copy.deepcopy(tabuleiro)
	quantidade = []
	for pos in [(x,y) for x in xrange(tabuleiro.linhas) for y in xrange(tabuleiro.colunas)]:
		if abs(tabuleiro[pos]) == (tabuleiro.massa_critica(pos) - 1) and sgn(tabuleiro[pos]) == jogador:
			l = 0
			pilha_visita = []
			pilha_visita.append(pos)
			while pilha_visita:
				pos = pilha_visita.pop()
				tabuleiro[pos] = 0
				l += 1
				for i in tabuleiro.vizinhos(pos):
					if abs(tabuleiro[i]) == (tabuleiro.massa_critica(i) - 1) and sgn(tabuleiro[i]) == jogador:
						pilha_visita.append(i)
			quantidade.append(l)
	return quantidade
	



	'''Funcao para calcular qual jogador foi o vencendo'''
def pontuacao(tabuleiro, jogador):
	pontos =0 
	orbes_jogador, orbes_ia = 0, 0
	for posicao in [(x,y) for x in xrange(tabuleiro.linhas) for y in xrange(tabuleiro.colunas)]:
		if sgn(tabuleiro[posicao]) == jogador:
			orbes_jogador += abs(tabuleiro[posicao])
			estaVuneravel = True
			
			for i in tabuleiro.vizinhos(posicao):
				if sgn(tabuleiro[i]) == -jogador and (abs(tabuleiro[i]) == tabuleiro.massa_critica(i) - 1):
					pontos -= 5-tabuleiro.massa_critica(posicao)
					estaVuneravel = False
	
			if estaVuneravel:
				#The edge Heuristic
				if tabuleiro.massa_critica(posicao) == 3:
					pontos += 2
				#The corner Heuristic
				elif tabuleiro.massa_critica(posicao) == 2:
					pontos += 3
				#The unstability Heuristic
				if abs(tabuleiro[posicao]) == tabuleiro.massa_critica(posicao) - 1:
					pontos += 2
				#The vulnerablity Heuristic
		else:
			orbes_ia += abs(tabuleiro[posicao])
			
	pontos += orbes_jogador
	#You win when the enemy has no orbs
	if orbes_ia == 0 and orbes_jogador > 1:
		return 10000
		
	#You loose when you have no orbs
	elif orbes_jogador == 0 and orbes_ia > 1:
		return -10000
	
	pontos += sum([2*i for i in reacao(tabuleiro,jogador) if i > 1])
	return pontos

