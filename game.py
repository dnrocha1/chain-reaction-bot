import pygame
import base

m, n = 9, 6

pygame.init()
surface = pygame.display.set_mode((50*n, 50*m))
pygame.display.set_caption('Chain Reaction')

def drawBoard(board=base.Tabuleiro()):
	surface.fill((0,0,0))
	font = pygame.font.Font('Font.ttf', 48)
	for pos in [(x,y) for x in xrange(board.m) for y in xrange(board.n)]:
		color = (90,90,90)
		text = font.render(str(board[pos])[-1], 1, color)
		textpos = text.get_rect(centerx = pos[1]*50 + 25, centery = pos[0]*50 + 25)
		surface.blit(text, textpos)
	pygame.display.update()
	print "Finalizou execucao"


def main():
	global m,n, surface

	tela_inicial()

	is_redPlayer = escolher_jogador()

	depth = escolher_profundidade()

	rows = getNumLinhas()

	columns = getNumColunas()


	#inicializa o basico e a janela do jogo
	m, n = rows, columns
	surface = pygame.display.set_mode((50*n, 50*m))
	pygame.display.set_caption('Chain Reaction')
	board = base.Board(m=m,n=n)
	total_moves = 0

	#game screen
	drawBoard(board)

def getNumColunas():
    surface.fill((0,0,0))
    font = pygame.font.Font('Font.ttf', 18)
    text = font.render("Quantas colunas?", 1, (100,100,100))
    textpos = text.get_rect(centerx = 25*n, centery = 12*m)
    surface.blit(text, textpos)
    font = pygame.font.Font('Font.ttf', 48)
    columns = 6
    text = font.render(str(columns),1,(255,255,0))
    textpos = text.get_rect(centerx = 25*n, centery = 25*m)
    surface.blit(text, textpos)
    pygame.display.update()

    flag = True
    while flag:
		for event in pygame.event.get():
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or event.type == pygame.MOUSEBUTTONDOWN:
				flag = False
			elif event.type == pygame.KEYDOWN:
				if event.key < 256 and chr(event.key) in '1234567890':
					rect = pygame.Rect(12*m,25*n,100,100)
					pygame.draw.rect(surface,(0,0,0),rect,0)
					pygame.display.update()
					columns = int(chr(event.key))
					text = font.render(str(columns),1,(255,255,0))
					textpos = text.get_rect(centerx = 25*n, centery = 25*m)
					surface.blit(text, textpos)
					pygame.display.update()
    return columns

def getNumLinhas():
    surface.fill((0,0,0))
    font = pygame.font.Font('Font.ttf', 18)
    text = font.render("Quantas linhas?", 1, (100,100,100))
    textpos = text.get_rect(centerx = 25*n, centery = 12*m)
    surface.blit(text, textpos)
    font = pygame.font.Font('Font.ttf', 48)
    rows = 9
    text = font.render(str(rows),1,(255,255,0))
    textpos = text.get_rect(centerx = 25*n, centery = 25*m)
    surface.blit(text, textpos)
    pygame.display.update()

    flag = True
    while flag:
		for event in pygame.event.get():
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or event.type == pygame.MOUSEBUTTONDOWN:
				flag = False
			elif event.type == pygame.KEYDOWN:
				if event.key < 256 and chr(event.key) in '1234567890':
					rect = pygame.Rect(12*m,25*n,100,100)
					pygame.draw.rect(surface,(0,0,0),rect,0)
					pygame.display.update()
					rows = int(chr(event.key))
					text = font.render(str(rows),1,(255,255,0))
					textpos = text.get_rect(centerx = 25*n, centery = 25*m)
					surface.blit(text, textpos)
					pygame.display.update()
    return rows

def escolher_profundidade():
    surface.fill((0,0,0))
    font = pygame.font.Font('Font.ttf', 18)
    text = font.render("Qual a profundidade de busca?", 1, (100,100,100))
    textpos = text.get_rect(centerx = 25*n, centery = 12*m)
    surface.blit(text, textpos)
    font = pygame.font.Font('Font.ttf', 48)
    depth = 3
    text = font.render(str(depth),1,(255,255,0))
    textpos = text.get_rect(centerx = 25*n, centery = 25*m)
    surface.blit(text, textpos)
    pygame.display.update()

    flag = True
    while flag:
		for event in pygame.event.get():
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or event.type == pygame.MOUSEBUTTONDOWN:
				flag = False
			elif event.type == pygame.KEYDOWN:
				if event.key < 256 and chr(event.key) in '1234567890':
					rect = pygame.Rect(12*m,25*n,100,100)
					pygame.draw.rect(surface,(0,0,0),rect,0)
					pygame.display.update()
					depth = int(chr(event.key))
					text = font.render(str(depth),1,(255,255,0))
					textpos = text.get_rect(centerx = 25*n, centery = 25*m)
					surface.blit(text, textpos)
					pygame.display.update()
    return depth

def escolher_jogador():
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                y = pygame.mouse.get_pos()[1]
                if y < 25*m:
                    is_redPlayer = True
                else:
                    is_redPlayer = False
                flag = False
    return is_redPlayer

"""Funcao para exibir a tela incial. Exibindo as opcoes de cores para jogadores"""
def tela_inicial():
    font = pygame.font.Font('Font.ttf', 72)
    text = font.render("Vermelho", 1, (255,0,0))
    textpos = text.get_rect(centerx = 25*n, centery = 12*m)
    surface.blit(text, textpos)
    text = font.render("Verde", 1, (0,255,0))
    textpos = text.get_rect(centerx = 25*n, centery = 36*m)
    surface.blit(text, textpos)
    font = pygame.font.Font('Font.ttf', 24)
    text = font.render("Escolha uma cor", 1, (100,100,100))
    textpos = text.get_rect(centerx = 25*n, centery = 23*m)
    surface.blit(text, textpos)
    pygame.display.update()


if __name__ == "__main__":
	main()
