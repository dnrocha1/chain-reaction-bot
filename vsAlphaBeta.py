import pygame
import alphabeta, base
import thread

m, n = 9, 6

pygame.init()
surface = pygame.display.set_mode((50*n, 50*m))
pygame.display.set_caption('Chain Reaction')
lock = thread.allocate_lock()

def desenha_tabuleiro(tabuleiro=base.Tabuleiro()):
	surface.fill((0,0,0))
	font = pygame.font.Font('Font.ttf', 48)
	for pos in [(x,y) for x in xrange(tabuleiro.linhas) for y in xrange(tabuleiro.colunas)]:
		if abs(tabuleiro[pos]) >= tabuleiro.massa_critica(pos):
			color = (255,255,0)
		elif base.sgn(tabuleiro[pos]) == 0:
			color = (90,90,90)
		elif base.sgn(tabuleiro[pos]) == 1:
			color = (255,0,0)
		else:
			color = (0,255,0)
		text = font.render(str(tabuleiro[pos])[-1], 1, color)
		textpos = text.get_rect(centerx = pos[1]*50 + 25, centery = pos[0]*50 + 25)
		surface.blit(text, textpos)
	pygame.display.update()

def inicia_reacao(tabuleiro, pos):
	tabuleiro = base.copy.deepcopy(tabuleiro)
	assert tabuleiro.novo_movimento == base.sgn(tabuleiro[pos]) or 0 == base.sgn(tabuleiro[pos])
	tabuleiro[pos] = tabuleiro[pos] + tabuleiro.novo_movimento
	while True:
		desenha_tabuleiro(tabuleiro)
		pygame.time.wait(250)
		unstable = []
		for pos in [(x,y) for x in xrange(tabuleiro.linhas) for y in xrange(tabuleiro.colunas)]:
			if abs(tabuleiro[pos]) >= tabuleiro.massa_critica(pos):
				unstable.append(pos)
		#raw_input()
		if not unstable:
			break
		for pos in unstable:
			tabuleiro[pos] -= tabuleiro.novo_movimento*tabuleiro.massa_critica(pos)
			for i in tabuleiro.vizinhos(pos):
				tabuleiro[i] = base.sgn(tabuleiro.novo_movimento)*(abs(tabuleiro[i])+1)
	desenha_tabuleiro(tabuleiro)
	lock.release()

def exibe_movimento(pos):
	rect = pygame.Rect(pos[1]*50,pos[0]*50,50,50)
	pygame.draw.rect(surface,(255,255,0),rect,0)
	pygame.display.update()
	pygame.time.wait(250)


def main():
	global m,n, surface

	#start screen
	font = pygame.font.Font('Font.ttf', 72)
	text = font.render("Red", 1, (255,0,0))
	textpos = text.get_rect(centerx = 25*n, centery = 12*m)
	surface.blit(text, textpos)
	text = font.render("Green", 1, (0,255,0))
	textpos = text.get_rect(centerx = 25*n, centery = 36*m)
	surface.blit(text, textpos)
	font = pygame.font.Font('Font.ttf', 12)
	text = font.render("Choose a Color", 1, (100,100,100))
	textpos = text.get_rect(centerx = 25*n, centery = 25*m)
	surface.blit(text, textpos)
	pygame.display.update()

	this_loop = True
	while this_loop:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				y = pygame.mouse.get_pos()[1]
				if y < 25*m:
					player_first = True
				else:
					player_first = False
				this_loop = False

	#depth screen
	surface.fill((0,0,0))
	font = pygame.font.Font('Font.ttf', 12)
	text = font.render("How deep should I look?", 1, (100,100,100))
	textpos = text.get_rect(centerx = 25*n, centery = 12*m)
	surface.blit(text, textpos)
	font = pygame.font.Font('Font.ttf', 48)
	depth = 3
	text = font.render(str(depth),1,(255,255,0))
	textpos = text.get_rect(centerx = 25*n, centery = 25*m)
	surface.blit(text, textpos)
	pygame.display.update()

	this_loop = True
	while this_loop:
		for event in pygame.event.get():
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or event.type == pygame.MOUSEBUTTONDOWN:
				this_loop = False
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

	#rows screen
	surface.fill((0,0,0))
	font = pygame.font.Font('Font.ttf', 12)
	text = font.render("How many rows?", 1, (100,100,100))
	textpos = text.get_rect(centerx = 25*n, centery = 12*m)
	surface.blit(text, textpos)
	font = pygame.font.Font('Font.ttf', 48)
	rows = 9
	text = font.render(str(rows),1,(255,255,0))
	textpos = text.get_rect(centerx = 25*n, centery = 25*m)
	surface.blit(text, textpos)
	pygame.display.update()

	this_loop = True
	while this_loop:
		for event in pygame.event.get():
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or event.type == pygame.MOUSEBUTTONDOWN:
				this_loop = False
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

	#columns screen
	surface.fill((0,0,0))
	font = pygame.font.Font('Font.ttf', 12)
	text = font.render("How many columns?", 1, (100,100,100))
	textpos = text.get_rect(centerx = 25*n, centery = 12*m)
	surface.blit(text, textpos)
	font = pygame.font.Font('Font.ttf', 48)
	columns = 6
	text = font.render(str(columns),1,(255,255,0))
	textpos = text.get_rect(centerx = 25*n, centery = 25*m)
	surface.blit(text, textpos)
	pygame.display.update()

	this_loop = True
	while this_loop:
		for event in pygame.event.get():
			if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN) or event.type == pygame.MOUSEBUTTONDOWN:
				this_loop = False
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


	#some initialization code
	m, n = rows, columns
	surface = pygame.display.set_mode((50*n, 50*m))
	pygame.display.set_caption('Chain Reaction')
	tabuleiro = base.Tabuleiro(linhas=m,colunas=n)
	total_movimentos = 0

	#game screen
	desenha_tabuleiro(tabuleiro)

	if not player_first:
		novo_movimento = alphabeta.alphabeta(tabuleiro)[0]
		lock.acquire()
		thread.start_new_thread(inicia_reacao, (tabuleiro, novo_movimento))
		tabuleiro = base.movimento(tabuleiro, novo_movimento)
		total_movimentos += 1

	this_loop = True
	while this_loop:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				x,y = pygame.mouse.get_pos()
				x,y = x/50,y/50
				if not (tabuleiro.novo_movimento == base.sgn(tabuleiro[(y,x)]) or 0 == base.sgn(tabuleiro[(y,x)])):
					print "Illegal movimento!"
					continue
				exibe_movimento((y,x))
				lock.acquire()
				thread.start_new_thread(inicia_reacao, (tabuleiro,(y,x)))
				tabuleiro = base.movimento(tabuleiro,(y,x))
				total_movimentos += 1
				if total_movimentos >= 2:
					if base.pontuacao(tabuleiro,tabuleiro.novo_movimento*(-1)) == 10000:
						vencedor = tabuleiro.novo_movimento*(-1)
						this_loop = False
						break
				novo_movimento = alphabeta.alphabeta(tabuleiro,depth)[0]
				exibe_movimento(novo_movimento)
				lock.acquire()
				thread.start_new_thread(inicia_reacao, (tabuleiro, novo_movimento))
				tabuleiro = base.movimento(tabuleiro, novo_movimento)
				total_movimentos += 1
				if total_movimentos >= 2:
					if base.pontuacao(tabuleiro,tabuleiro.novo_movimento*(-1)) == 10000:
						vencedor = tabuleiro.novo_movimento*(-1)
						this_loop = False
						break

	#winning screen
	while lock.locked():
		continue
	m, n = 9, 6
	surface = pygame.display.set_mode((50*n, 50*m))
	font = pygame.font.Font('Font.ttf', 72)
	pygame.display.set_caption('Chain Reaction')
	if vencedor == 1:
		text = font.render("Red", 1, (255,0,0))
	else:
		text = font.render("Green", 1, (0,255,0))
	textpos = text.get_rect(centerx = 25*n, centery = 12*m)
	surface.blit(text, textpos)
	font = pygame.font.Font('Font.ttf', 48)
	text = font.render("Wins!", 1, (100,100,100))
	textpos = text.get_rect(centerx = 25*n, centery = 25*m)
	surface.blit(text, textpos)
	pygame.display.update()


if __name__ == "__main__":
	main()
