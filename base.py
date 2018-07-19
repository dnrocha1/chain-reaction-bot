# -*- coding: utf-8 -*-

class Board():
    
    """Construtor do tabuleiro"""
	def __init__(self, n=6, m=9, new_move=1):
		self.m = m
		self.n = n
		self.board = [[0 for i in xrange(self.n)] for i in xrange(self.m)]
		self.new_move = new_move
    
    """Getters e setters de itens do tabuleiro
    
    Argumentos: pos -- as coordenadas do tabuleiro (é uma tupla)
    """
	def __getitem__(self, pos):
		return self.board[pos[0]][pos[1]]
	def __setitem__(self, pos, value):
		self.board[pos[0]][pos[1]]=value
    
    """tostring"""
	def __str__(self):
		s = ""
		for i in xrange(self.m):
			for j in xrange(self.n):
				s += str(self[(i,j)])
				s += " "
			s += "\n"
		return s
	
	# [to do: Não entendi o que era esse aqui]
	def hash(self):
		return str(self.board)+str(self.new_move)

	"""Identifica pontos limites do tabuleiro"""		
	def pontos_limites(self,pos):
		if pos == (0,0) or pos == (self.m - 1, self.n - 1) or pos == (self.m - 1, 0) or pos == (0, self.n - 1):
			return 2
		elif pos[0] == 0 or pos[0] == self.m-1 or pos[1] == 0 or pos[1] == self.n-1:
			return 3
		else:
			return 4
	
	def vizinhos(self,pos):
		n = []
		lista_vizinhos = [(pos[0],pos[1]+1), (pos[0],pos[1]-1), (pos[0]+1,pos[1]), (pos[0]-1,pos[1])]
		for i in vizinhos:
			if 0 <= i[0] < self.m and 0 <= i[1] < self.n:
				n.append(i)
		return n