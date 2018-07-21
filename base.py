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
	