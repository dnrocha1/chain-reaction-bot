import pygame
import base,minimax
import thread


linhas, colunas = 9, 6

pygame.init()
surface = pygame.display.set_mode((50*colunas, 50*linhas))
pygame.display.set_caption('Chain Reaction')
lock = thread.allocate_lock()
def desenhaTabuleiro(tabuleiro=base.Tabuleiro()):
	surface.fill((0,0,0))
	font = pygame.font.Font('Font.ttf', 48)
	for pos in [(x,y) for x in xrange(tabuleiro.linhas) for y in xrange(tabuleiro.colunas)]:
		if abs(tabuleiro[pos]) >= tabuleiro.massa_critica(pos):
			cor = (255,255,0)
		elif base.sgn(tabuleiro[pos]) == 0:
			cor = (90,90,90)
		elif base.sgn(tabuleiro[pos]) == 1:
			cor = (255,0,0)
		else:
			cor = (0,255,0)
		texto = font.render(str(tabuleiro[pos])[-1], 1, cor)
		texto_pos = texto.get_rect(centerx = pos[1]*50 + 25, centery = pos[0]*50 + 25)
		surface.blit(texto, texto_pos)
	pygame.display.update()
	print "Finalizou execucao"

def inicia_reacao(tabuleiro, pos):
	tabuleiro = base.copy.deepcopy(tabuleiro)
	assert tabuleiro.novo_movimento == base.sgn(tabuleiro[pos]) or 0 == base.sgn(tabuleiro[pos])
	tabuleiro[pos] = tabuleiro[pos] + tabuleiro.novo_movimento
	while True:
		desenhaTabuleiro(tabuleiro)
		pygame.time.wait(250)
		instavel = []
		for pos in [(x,y) for x in xrange(tabuleiro.linhas) for y in xrange(tabuleiro.colunas)]:
			if abs(tabuleiro[pos]) >= tabuleiro.massa_critica(pos):
				instavel.append(pos)
		if not instavel:
			break
		for pos in instavel:
			tabuleiro[pos] -= tabuleiro.novo_movimento * tabuleiro.massa_critica(pos)
			for viz in tabuleiro.vizinhos(pos):
				tabuleiro[viz] = base.sgn(tabuleiro.novo_movimento) * (abs(tabuleiro[viz]+1))
	desenhaTabuleiro(tabuleiro)
	lock.release()

def exibe_movimento(pos):
    quad = pygame.Rect(pos[1]*50,pos[0]*50,50,50)
    pygame.draw.rect(surface,(255,255,0),quad,0)
    pygame.display.update()
    pygame.time.wait(250)

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
	total_movimento = 0

	#tela de jogo
	desenhaTabuleiro(tabuleiro)
	
	if not is_redPlayer:
		novo_movimento = minimax.minimax(tabuleiro)[0]
		lock.acquire()
		thread.start_new_thread(inicia_reacao, (tabuleiro, novo_movimento))
		tabuleiro = base.movimento(tabuleiro, novo_movimento)
		total_movimento += 1

	this_loop = True
	while this_loop:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				x,y = pygame.mouse.get_pos()
				x,y = x/50,y/50
				if not (tabuleiro.novo_movimento == base.sgn(tabuleiro[(y,x)]) or 0 == base.sgn(tabuleiro[(y,x)])):
					continue
				#tabuleiro[(y,x)] = tabuleiro[(y,x)] + tabuleiro.novo_movimento
				exibe_movimento((y,x))
				#desenhaTabuleiro(tabuleiro)
				#inicia_reacao(tabuleiro,(y,x))
				lock.acquire()
				thread.start_new_thread(inicia_reacao, (tabuleiro,(y,x)))
				tabuleiro = base.movimento(tabuleiro,(y,x))
				total_movimento += 1
				if total_movimento >= 2:
					if base.pontuacao(tabuleiro,tabuleiro.novo_movimento*(-1)) == 10000:
						vencedor = tabuleiro.novo_movimento*(-1)
						this_loop = False
						break
				novo_movimento = minimax.minimax(tabuleiro,depth)[0]
				#precisa trocar o nome de depth
				exibe_movimento(novo_movimento)
				lock.acquire()
				thread.start_new_thread(inicia_reacao, (tabuleiro, novo_movimento))
				tabuleiro = base.movimento(tabuleiro, novo_movimento)
				total_movimento += 1
				if total_movimento >= 2:
					if base.pontuacao(tabuleiro,tabuleiro.novo_movimento*(-1)) == 10000:
						vencedor = tabuleiro.novo_movimento*(-1)
						this_loop = False
						break

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

"""Funcao para  a tela incial. Exibindo as opcoes de cores para jogadores"""
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
