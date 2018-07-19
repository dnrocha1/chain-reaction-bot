import pygame
import base

m, n = 9, 6

pygame.init()
surface = pygame.display.set_mode((50*n, 50*m))
pygame.display.set_caption('Chain Reaction')

def main():
	global m,n, surface

	tela_inicial()

	is_redPlayer = escolher_jogador()


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