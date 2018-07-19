import pygame
import base

linhas, colunas = 9, 6

pygame.init()
surface = pygame.display.set_mode((50*colunas, 50*linhas))
pygame.display.set_caption('Chain Reaction')

def desenhaTabuleiro(tabuleiro=base.Tabuleiro()):
	surface.fill((0,0,0))
	font = pygame.font.Font('Font.ttf', 48)
	for pos in [(x,y) for x in xrange(tabuleiro.linhas) for y in xrange(tabuleiro.colunas)]:
		cor = (90,90,90)
		texto = font.render(str(tabuleiro[pos])[-1], 1, cor)
		texto_pos = texto.get_rect(centerx = pos[1]*50 + 25, centery = pos[0]*50 + 25)
		surface.blit(texto, texto_pos)
	pygame.display.update()
	print "Finalizou execucao"


def main():
	global linhas,colunas,surface

	tela_inicial()
	is_redPlayer = escolher_jogador()
	depth = escolher_profundidade()
	rows = getNumLinhas()
	columns = getNumColunas()


	#inicializa o basico e a janela do jogo
	linhas, colunas = rows, columns
	surface = pygame.display.set_mode((50*colunas, 50*linhas))
	pygame.display.set_caption('Chain Reaction')
	tabuleiro = base.Tabuleiro(linhas=linhas,colunas=colunas)
	total_moves = 0

	#game screen
	desenhaTabuleiro(tabuleiro)

def getNumColunas():
    surface.fill((0,0,0))
    font = pygame.font.Font('Font.ttf', 18)
    texto = font.render("Quantas colunas?", 1, (100,100,100))
    texto_pos = texto.get_rect(centerx = 25*colunas, centery = 12*linhas)
    surface.blit(texto, texto_pos)
    font = pygame.font.Font('Font.ttf', 48)
    columns = 6
    texto = font.render(str(columns),1,(255,255,0))
    texto_pos = texto.get_rect(centerx = 25*colunas, centery = 25*linhas)
    surface.blit(texto, texto_pos)
    pygame.display.update()

    flag = True
    while flag:
		for event in pygame.event.get():
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or event.type == pygame.MOUSEBUTTONDOWN:
				flag = False
			elif event.type == pygame.KEYDOWN:
				if event.key < 256 and chr(event.key) in '1234567890':
					rect = pygame.Rect(12*linhas,25*colunas,100,100)
					pygame.draw.rect(surface,(0,0,0),rect,0)
					pygame.display.update()
					columns = int(chr(event.key))
					texto = font.render(str(columns),1,(255,255,0))
					texto_pos = texto.get_rect(centerx = 25*colunas, centery = 25*linhas)
					surface.blit(texto, texto_pos)
					pygame.display.update()
    return columns

def getNumLinhas():
    surface.fill((0,0,0))
    font = pygame.font.Font('Font.ttf', 18)
    texto = font.render("Quantas linhas?", 1, (100,100,100))
    texto_pos = texto.get_rect(centerx = 25*colunas, centery = 12*linhas)
    surface.blit(texto, texto_pos)
    font = pygame.font.Font('Font.ttf', 48)
    rows = 9
    texto = font.render(str(rows),1,(255,255,0))
    texto_pos = texto.get_rect(centerx = 25*colunas, centery = 25*linhas)
    surface.blit(texto, texto_pos)
    pygame.display.update()

    flag = True
    while flag:
		for event in pygame.event.get():
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or event.type == pygame.MOUSEBUTTONDOWN:
				flag = False
			elif event.type == pygame.KEYDOWN:
				if event.key < 256 and chr(event.key) in '1234567890':
					rect = pygame.Rect(12*linhas,25*colunas,100,100)
					pygame.draw.rect(surface,(0,0,0),rect,0)
					pygame.display.update()
					rows = int(chr(event.key))
					texto = font.render(str(rows),1,(255,255,0))
					texto_pos = texto.get_rect(centerx = 25*colunas, centery = 25*linhas)
					surface.blit(texto, texto_pos)
					pygame.display.update()
    return rows

def escolher_profundidade():
    surface.fill((0,0,0))
    font = pygame.font.Font('Font.ttf', 18)
    texto = font.render("Qual a profundidade de busca?", 1, (100,100,100))
    texto_pos = texto.get_rect(centerx = 25*colunas, centery = 12*linhas)
    surface.blit(texto, texto_pos)
    font = pygame.font.Font('Font.ttf', 48)
    depth = 3
    texto = font.render(str(depth),1,(255,255,0))
    texto_pos = texto.get_rect(centerx = 25*colunas, centery = 25*linhas)
    surface.blit(texto, texto_pos)
    pygame.display.update()

    flag = True
    while flag:
		for event in pygame.event.get():
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or event.type == pygame.MOUSEBUTTONDOWN:
				flag = False
			elif event.type == pygame.KEYDOWN:
				if event.key < 256 and chr(event.key) in '1234567890':
					rect = pygame.Rect(12*linhas,25*colunas,100,100)
					pygame.draw.rect(surface,(0,0,0),rect,0)
					pygame.display.update()
					depth = int(chr(event.key))
					texto = font.render(str(depth),1,(255,255,0))
					texto_pos = texto.get_rect(centerx = 25*colunas, centery = 25*linhas)
					surface.blit(texto, texto_pos)
					pygame.display.update()
    return depth

def escolher_jogador():
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                y = pygame.mouse.get_pos()[1]
                if y < 25*linhas:
                    is_redPlayer = True
                else:
                    is_redPlayer = False
                flag = False
    return is_redPlayer

"""Funcao para exibir a tela incial. Exibindo as opcoes de cores para jogadores"""
def tela_inicial():
    font = pygame.font.Font('Font.ttf', 72)
    texto = font.render("Vermelho", 1, (255,0,0))
    texto_pos = texto.get_rect(centerx = 25*colunas, centery = 12*linhas)
    surface.blit(texto, texto_pos)
    texto = font.render("Verde", 1, (0,255,0))
    texto_pos = texto.get_rect(centerx = 25*colunas, centery = 36*linhas)
    surface.blit(texto, texto_pos)
    font = pygame.font.Font('Font.ttf', 24)
    texto = font.render("Escolha uma cor", 1, (100,100,100))
    texto_pos = texto.get_rect(centerx = 25*colunas, centery = 23*linhas)
    surface.blit(texto, texto_pos)
    pygame.display.update()


if __name__ == "__main__":
	main()
