import pygame
import constante
import game
class game:
    def __init__(self):
        # Tela 
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode(constante.LARGURA,constante.ALTURA)
        pygame.display.set_caption(constante.TITULO)
        self.clock = pygame.time.Clock()
        self.rofadndo = True 
    
    def jogo(self):
        # inicia classes 
        self.grupo_sprite = pygame.sprite.Group()
        self.rodar()
    
    def rodar(self):
        # jogo rodando 

        self.jogando = True