from cores import Cores
import pygame
from grid import Grid

pygame.init()

grid = Grid()

largura_janela = grid.num_colunas * grid.tamanho_celula
altura_janela = grid.num_linhas * grid.tamanho_celula
window = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption('Pac Man')

title_font = pygame.font.Font(None, 40)
show_start_screen = True
game = True

class Player:
    def __init__(self, linha, coluna, tamanho=30, velocidade=0.1):
        self.linha = linha
        self.coluna = coluna
        self.tamanho = tamanho
        self.velocidade = velocidade
        self.tamanho_celula = grid.tamanho_celula

    def move(self, keys):
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.coluna > 0:
            self.coluna -= self.velocidade
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.coluna < grid.num_colunas - 1:
            self.coluna += self.velocidade
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.linha > 0:
            self.linha -= self.velocidade
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.linha < grid.num_linhas - 1:
            self.linha += self.velocidade

    def draw(self, screen):
        x = self.coluna * self.tamanho_celula
        y = self.linha * self.tamanho_celula
        pygame.draw.rect(screen, (255, 0, 0), (x, y, self.tamanho, self.tamanho))

player = Player(0, 0, tamanho=grid.tamanho_celula)

def draw_start_screen():
    window.fill((0, 0, 0))
    start_text = title_font.render("Pressione qualquer tecla para iniciar", True, Cores.branco)
    window.blit(start_text, start_text.get_rect(center=(largura_janela // 2, altura_janela // 2)))
    pygame.display.update()

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if show_start_screen and event.type == pygame.KEYDOWN:
            show_start_screen = False

    keys = pygame.key.get_pressed()

    if show_start_screen:
        draw_start_screen()
    else:
        window.fill((255, 255, 255))
        grid.draw(window)
        player.move(keys)
        player.draw(window)

    pygame.display.update()

pygame.quit()
