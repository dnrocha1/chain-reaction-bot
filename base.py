import copy
import time

# -*- coding: utf-8 -*-

sgn = lambda n: 0 if n == 0 else n/abs(n)
'''Função sinal
sgn(n) = -1 se n < 0
sgn(n) = 0 se n = 0
sgn(n) = 1 se n > 0

 '''

class Tabuleiro():
    
    
	def __init__(self, colunas=6, linhas=9, novo_movimento=1):
		'''Construtor do tabuleiro.
		
		Como iremos trabalhar com um tabuleiro 9x6, os valores serão predefinidos no próprio
		construtor, sem possibilidade de alteração. Lembrando que a eficiência dos algoritmos
		depende, também, do tamanho do tabuleiro, qualquer alteração pode comprometê-la.
		
		'''
		self.linhas = linhas
		self.colunas = colunas
		self.tabuleiro = [[0 for i in xrange(self.colunas)] for i in xrange(self.linhas)]
		self.novo_movimento = novo_movimento
    
	def __getitem__(self, pos):
		return self.tabuleiro[pos[0]][pos[1]]
		
	def __setitem__(self, pos, valor):
		self.tabuleiro[pos[0]][pos[1]] = valor 
		
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

		
	def massa_critica(self,pos):
		'''Essa função retorna a massa crítica de uma determinada casela do grid
		
		Args:
			pos (tuple): Tupla com as coordenadas da casela
			
		Return:
			int: Massa crítica da casela
		
		'''
		if pos == (0,0) or pos == (self.linhas - 1, self.colunas - 1) or pos == (self.linhas - 1, 0) or pos == (0, self.colunas - 1):
			return 2
		elif pos[0] == 0 or pos[0] == self.linhas-1 or pos[1] == 0 or pos[1] == self.colunas-1:
			return 3
		else:
			return 4
	
	def vizinhos(self,pos):
		'''Essa função retorna uma lista com os vizinhos de uma casela.
		
		Args:
			pos (tuple): Tupla com as coordenadas da casela
			
		Return:
			list: vizinhos da tupla
			
		'''
		vizinhos = []
		possiveis_vizinhos = [(pos[0],pos[1]+1), (pos[0],pos[1]-1), (pos[0]+1,pos[1]), (pos[0]-1,pos[1])]
		for i in possiveis_vizinhos:
			if 0 <= i[0] < self.linhas and 0 <= i[1] < self.colunas:
				vizinhos.append(i)
		return vizinhos
		
def movimento(tabuleiro, pos):
	'''Essa função realiza um movimento no tabuleiro.
	
	Obs.: Ela se preocupa com o estado das caselas que ficarão instáveis com o movimento. As reações futuras não
	são tratadas aqui.
		
	Args:
		tabuleiro (tabuleiro): tabuleiro antes do movimento
		pos (tuple): Tupla com as coordenadas da casela
		
	Return:
		tabuleiro: estado do tabuleiro imediatamente após o movimento
			
	'''
	tabuleiro = copy.deepcopy(tabuleiro)
	assert tabuleiro.novo_movimento == sgn(tabuleiro[pos]) or 0 == sgn(tabuleiro[pos])
	tabuleiro[pos] = tabuleiro[pos] + tabuleiro.novo_movimento
	t = time.time()
	while True:
		instavel = []
		for pos in [(x,y) for x in xrange(tabuleiro.linhas) for y in xrange(tabuleiro.colunas)]:
			if abs(tabuleiro[pos]) >= tabuleiro.massa_critica(pos):
				instavel.append(pos)
		if time.time() - t >= 3:
			break
		if not instavel:
			break
		for pos in instavel:
			tabuleiro[pos] -= tabuleiro.novo_movimento*tabuleiro.massa_critica(pos)
			for i in tabuleiro.vizinhos(pos):
				tabuleiro[i] = sgn(tabuleiro.novo_movimento)*(abs(tabuleiro[i])+1)
	tabuleiro.novo_movimento *= -1
	return tabuleiro

