import pygame

m, n = 9, 6

pygame.init()
surface = pygame.display.set_mode((50*n, 50*m))
pygame.display.set_caption('Chain Reaction')

def main():
	global m,n, surface

	tela_inicial()

	is_redPlayer = escolher_jogador()

	depth = escolher_profundidade()

	
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