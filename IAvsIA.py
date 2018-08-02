import pygame, random
import alphabeta,minimax, base
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
	print(tabuleiro)
	flag = True
	while flag == True:
		somenteVerdes,somenteVermelhas = True,True #minimax eh vermelho e eh positivo
		#varre procurando se existe somente verdes
		for posicao in [(x,y) for x in xrange(tabuleiro.linhas) for y in xrange(tabuleiro.colunas)]:
			if somenteVerdes == False:
				break
			if total_movimentos >= 2 and tabuleiro[posicao] != 0:
				if tabuleiro[posicao] > 0:
					somenteVerdes = False
		for posicao in [(x,y) for x in xrange(tabuleiro.linhas) for y in xrange(tabuleiro.colunas)]:
			if somenteVermelhas == False:
				break
			if total_movimentos >= 2 and tabuleiro[posicao] != 0:
				if tabuleiro[posicao] < 0:
					somenteVermelhas = False
		if total_movimentos >= 2 and (somenteVerdes == True or somenteVermelhas == True):
			print "SAIU DO LOOP!"
			break
		#print(somenteVerdes)
		print("")
		desenha_tabuleiro(tabuleiro)
		pygame.time.wait(250)
		print("DESENHOU")
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
	font = pygame.font.Font('Font.ttf', 12)
	text = font.render("Iniciando...", 1, (100,100,100))
	textpos = text.get_rect(centerx = 25*n, centery = 25*m)
	surface.blit(text, textpos)
	pygame.display.update()
	depth = 3#random.randrange(4)
	rows = 2#random.randrange(2, 9)
	columns = 2#random.randrange(2, 6)

	#some initialization code
	m, n = rows, columns
	surface = pygame.display.set_mode((50*n, 50*m))
	pygame.display.set_caption('Chain Reaction')
	tabuleiro = base.Tabuleiro(linhas=m,colunas=n)
	global total_movimentos
	total_movimentos = 0

	#game screen
	desenha_tabuleiro(tabuleiro)
	this_loop = True
	while this_loop:
		novo_movimento1 = minimax.minimax(tabuleiro)[0]
		print "Minimax movimentou!"
		#pygame.time.wait(2000)
		exibe_movimento(novo_movimento1)
		lock.acquire()
		thread.start_new_thread(inicia_reacao, (tabuleiro, novo_movimento1))
		tabuleiro = base.movimento(tabuleiro, novo_movimento1)
		total_movimentos += 1
		if total_movimentos >= 2:
			if base.pontuacao(tabuleiro,tabuleiro.novo_movimento*(-1)) == 10000:
				vencedor = tabuleiro.novo_movimento*(-1)
				this_loop = False
				break
		novo_movimento = alphabeta.alphabeta(tabuleiro,depth)[0]
		print "Alphabeta movimentou!"
		#pygame.time.wait(2000)
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
		arq = open('vitoriasMinimax.txt','r')
		vitorias = arq.read()
		v = int(vitorias)
		arq.close()
		arq = open('vitoriasMinimax.txt','w')
		arq.write(str(v+1))

	else:
		text = font.render("Green", 1, (0,255,0))
		arq = open('vitoriasAlphabeta.txt','r')
		vitorias = arq.read()
		v = int(vitorias)
		arq.close()
		arq = open('vitoriasAlphabeta.txt','w')
		arq.write(str(v+1))
	textpos = text.get_rect(centerx = 25*n, centery = 12*m)
	surface.blit(text, textpos)
	font = pygame.font.Font('Font.ttf', 48)
	text = font.render("Wins!", 1, (100,100,100))
	textpos = text.get_rect(centerx = 25*n, centery = 25*m)
	surface.blit(text, textpos)
	pygame.display.update()


if __name__ == "__main__":
	main()
