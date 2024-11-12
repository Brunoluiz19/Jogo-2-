from cores import Cores
import pygame
from grid import Grid

pygame.init()
clock = pygame.time.Clock()

# Layout do labirinto: 1 representa uma parede e 0 representa um caminho
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


# Atualize a instância grid para usar o layout do labirinto
num_linhas = len(maze)
num_colunas = len(maze[0])
grid = Grid()  # Inicializa sem passar num_linhas e num_colunas
grid.num_linhas = num_linhas
grid.num_colunas = num_colunas
grid.tamanho_celula = 30

largura_janela = grid.num_colunas * grid.tamanho_celula
altura_janela = grid.num_linhas * grid.tamanho_celula
window = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption('Pac Man')

title_font = pygame.font.Font(None, 40)
show_start_screen = True
game = True

class Player:
    def __init__(self, linha, coluna, tamanho=30, velocidade=1):
        self.linha = linha
        self.coluna = coluna
        self.tamanho = tamanho
        self.velocidade = velocidade
        self.tamanho_celula = grid.tamanho_celula
        self.direcao = None
        self.teclas_ativas = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_UP: False, pygame.K_DOWN: False,
                              pygame.K_a: False, pygame.K_d: False, pygame.K_w: False, pygame.K_s: False}

    def set_direcao(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in self.teclas_ativas and not self.teclas_ativas[event.key]:
                if event.key in [pygame.K_LEFT, pygame.K_a]:
                    self.direcao = 'esquerda'
                elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                    self.direcao = 'direita'
                elif event.key in [pygame.K_UP, pygame.K_w]:
                    self.direcao = 'cima'
                elif event.key in [pygame.K_DOWN, pygame.K_s]:
                    self.direcao = 'baixo'
                self.teclas_ativas[event.key] = True

        elif event.type == pygame.KEYUP and event.key in self.teclas_ativas:
            self.teclas_ativas[event.key] = False

    def move(self):
        nova_linha, nova_coluna = self.linha, self.coluna
        if self.direcao == 'esquerda' and self.coluna > 0:
            nova_coluna -= self.velocidade
        elif self.direcao == 'direita' and self.coluna < grid.num_colunas - 1:
            nova_coluna += self.velocidade
        elif self.direcao == 'cima' and self.linha > 0:
            nova_linha -= self.velocidade
        elif self.direcao == 'baixo' and self.linha < grid.num_linhas - 1:
            nova_linha += self.velocidade

        # Verifica se a nova posição é um caminho livre
        if maze[nova_linha][nova_coluna] == 0:
            self.linha, self.coluna = nova_linha, nova_coluna

    def draw(self, screen):
        x = self.coluna * self.tamanho_celula
        y = self.linha * self.tamanho_celula
        pygame.draw.rect(screen, (255, 0, 0), (x, y, self.tamanho, self.tamanho))

player = Player(1, 1, tamanho=grid.tamanho_celula)

def draw_start_screen():
    window.fill((0, 0, 0))
    start_text = title_font.render("Pressione qualquer tecla para iniciar", True, Cores.branco)
    window.blit(start_text, start_text.get_rect(center=(largura_janela // 2, altura_janela // 2)))
    pygame.display.update()

def draw_maze(screen):
    for linha in range(len(maze)):
        for coluna in range(len(maze[0])):
            x = coluna * grid.tamanho_celula
            y = linha * grid.tamanho_celula
            if maze[linha][coluna] == 1:
                pygame.draw.rect(screen, Cores.azul, (x, y, grid.tamanho_celula, grid.tamanho_celula))

while game:
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if show_start_screen and event.type == pygame.KEYDOWN:
            show_start_screen = False
        elif not show_start_screen:
            player.set_direcao(event)

    if show_start_screen:
        draw_start_screen()
    else:
        window.fill((255, 255, 255))
        draw_maze(window)  # Desenha o labirinto
        player.move()
        player.draw(window)

    pygame.display.update()

pygame.quit()
