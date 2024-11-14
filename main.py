from cores import Cores
import pygame
from grid import Grid
import random
from collections import deque

pygame.init()
clock = pygame.time.Clock()

# Layout do labirinto: 1 representa uma parede e 0 representa um caminho
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
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
score_font = pygame.font.Font(None, 30)
show_start_screen = True
game = True

# Variável para armazenar a pontuação
score = 0

class Player:
    def __init__(self, linha, coluna, tamanho=30, velocidade=1):
        self.linha = linha
        self.coluna = coluna
        self.tamanho = tamanho
        self.velocidade = velocidade
        self.tamanho_celula = grid.tamanho_celula
        self.direcao = None
        self.direcao_desejada = None
        self.teclas_ativas = {pygame.K_LEFT: False, pygame.K_RIGHT: False, pygame.K_UP: False, pygame.K_DOWN: False,
                              pygame.K_a: False, pygame.K_d: False, pygame.K_w: False, pygame.K_s: False}

    def set_direcao(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in self.teclas_ativas:
                if event.key in [pygame.K_LEFT, pygame.K_a]:
                    self.direcao_desejada = 'esquerda'
                elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                    self.direcao_desejada = 'direita'
                elif event.key in [pygame.K_UP, pygame.K_w]:
                    self.direcao_desejada = 'cima'
                elif event.key in [pygame.K_DOWN, pygame.K_s]:
                    self.direcao_desejada = 'baixo'
                self.teclas_ativas[event.key] = True

        elif event.type == pygame.KEYUP and event.key in self.teclas_ativas:
            self.teclas_ativas[event.key] = False

    def move(self):
        if self.direcao_desejada:
            if self.pode_mover(self.direcao_desejada):
                self.direcao = self.direcao_desejada

        if self.direcao and self.pode_mover(self.direcao):
            if self.direcao == 'esquerda':
                self.coluna -= self.velocidade
            elif self.direcao == 'direita':
                self.coluna += self.velocidade
            elif self.direcao == 'cima':
                self.linha -= self.velocidade
            elif self.direcao == 'baixo':
                self.linha += self.velocidade

    def pode_mover(self, direcao):
        nova_linha, nova_coluna = self.linha, self.coluna
        if direcao == 'esquerda' and self.coluna > 0:
            nova_coluna -= self.velocidade
        elif direcao == 'direita' and self.coluna < grid.num_colunas - 1:
            nova_coluna += self.velocidade
        elif direcao == 'cima' and self.linha > 0:
            nova_linha -= self.velocidade
        elif direcao == 'baixo' and self.linha < grid.num_linhas - 1:
            nova_linha += self.velocidade

        return maze[nova_linha][nova_coluna] == 0

    def draw(self, screen):
        x = self.coluna * self.tamanho_celula
        y = self.linha * self.tamanho_celula
        pygame.draw.rect(screen, Cores.vermelho, (x, y, self.tamanho_celula, self.tamanho_celula))


class Bolinhas:
    def __init__(self):
        # Cria uma lista com as posições iniciais de todas as bolinhas
        self.posicoes = [
            (linha, coluna)
            for linha in range(len(maze))
            for coluna in range(len(maze[0]))
            if maze[linha][coluna] == 0
        ]

    def draw(self, screen):
        for linha, coluna in self.posicoes:
            x = coluna * grid.tamanho_celula + grid.tamanho_celula // 2
            y = linha * grid.tamanho_celula + grid.tamanho_celula // 2
            pygame.draw.circle(screen, Cores.amarelo, (x, y), grid.tamanho_celula // 6)

    def coletar(self, linha, coluna):
        global score
        if (linha, coluna) in self.posicoes:
            self.posicoes.remove((linha, coluna))
            score += 10  # Incrementa a pontuação


# Cria uma instância das bolinhas
bolinhas = Bolinhas()

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

def draw_score(screen):
    score_text = score_font.render(f"Pontos: {score}", True, Cores.branco)
    screen.blit(score_text, (10, 10))

class Enemy:
    def __init__(self, linha, coluna, tamanho=30, velocidade=1, tempo_espera_inicial=60):
        self.linha = linha
        self.coluna = coluna
        self.tamanho = tamanho
        self.velocidade = velocidade
        self.tamanho_celula = grid.tamanho_celula
        self.rota = []  # Lista de passos para seguir
        self.tempo_espera = tempo_espera_inicial  # Tempo de espera inicial antes de começar a se mover
        self.perseguindo = False  # Indica se o inimigo está perseguindo o jogador

    def calcula_rota(self, destino_linha, destino_coluna):
        inicio = (self.linha, self.coluna)
        destino = (destino_linha, destino_coluna)
        fila = deque([inicio])
        visitados = set()
        caminhos = {inicio: []}

        while fila:
            atual = fila.popleft()
            if atual == destino:
                return caminhos[atual]

            for direcao in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Direções: direita, baixo, esquerda, cima
                nova_linha = atual[0] + direcao[0]
                nova_coluna = atual[1] + direcao[1]
                novo_pos = (nova_linha, nova_coluna)

                if (0 <= nova_linha < len(maze) and
                    0 <= nova_coluna < len(maze[0]) and
                    maze[nova_linha][nova_coluna] == 0 and
                    novo_pos not in visitados):

                    visitados.add(novo_pos)
                    fila.append(novo_pos)
                    caminhos[novo_pos] = caminhos[atual] + [novo_pos]

        return []  # Retorna rota vazia se não houver caminho

    def pode_ver_player(self, player):
        if self.linha == player.linha:  # Mesma linha
            menor_coluna, maior_coluna = sorted([self.coluna, player.coluna])
            for coluna in range(menor_coluna + 1, maior_coluna):
                if maze[self.linha][coluna] == 1:  # Há uma parede no caminho
                    return False
            return True
        elif self.coluna == player.coluna:  # Mesma coluna
            menor_linha, maior_linha = sorted([self.linha, player.linha])
            for linha in range(menor_linha + 1, maior_linha):
                if maze[linha][self.coluna] == 1:  # Há uma parede no caminho
                    return False
            return True
        return False

    def move(self, player):
        if self.tempo_espera > 0:  # Se ainda está no tempo de espera
            self.tempo_espera -= 1
            return

        if self.pode_ver_player(player):
            self.perseguindo = True
            self.rota = self.calcula_rota(player.linha, player.coluna)
        elif not self.perseguindo or not self.rota:
            # Comportamento padrão: recalcula a rota para uma posição aleatória
            self.perseguindo = False
            if not self.rota:
                destino = random.choice([
                    (linha, coluna)
                    for linha in range(grid.num_linhas)
                    for coluna in range(grid.num_colunas)
                    if maze[linha][coluna] == 0
                ])
                self.rota = self.calcula_rota(destino[0], destino[1])

        if self.rota:
            proxima_linha, proxima_coluna = self.rota[0]
            self.linha, self.coluna = proxima_linha, proxima_coluna
            self.rota.pop(0)

    def draw(self, screen):
        x = self.coluna * self.tamanho_celula
        y = self.linha * self.tamanho_celula
        pygame.draw.rect(screen, Cores.verde, (x, y, self.tamanho_celula, self.tamanho_celula))


# Lista para armazenar todos os inimigos
enemies = []

# Criar múltiplos inimigos com tempos de espera individuais
tempos_espera = [10, 20, 30, 40]  # Tempos de espera em ticks
posicoes_iniciais = [
    (num_linhas // 2, num_colunas // 2),  # Centro do mapa
    (1, num_colunas - 2),  # Canto superior direito
    (num_linhas - 2, 1),  # Canto inferior esquerdo
    (num_linhas - 2, num_colunas - 2)  # Canto inferior direito
]

for i in range(4):  # Criar 4 inimigos
    linha, coluna = posicoes_iniciais[i]
    enemy = Enemy(linha, coluna, tamanho=grid.tamanho_celula, velocidade=1)
    enemy.tempo_espera = tempos_espera[i]  # Configurar o tempo de espera inicial
    enemies.append(enemy)

while game:
    clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if show_start_screen and event.type == pygame.KEYDOWN:
            show_start_screen = False
        elif not show_start_screen:
            player.set_direcao(event)

    if not show_start_screen:
        window.fill((255, 255, 255))
        draw_maze(window)  # Desenha o labirinto
        bolinhas.draw(window)  # Desenha as bolinhas
        player.move()
        bolinhas.coletar(player.linha, player.coluna)  # Remove bolinhas quando o jogador passa por elas
        player.draw(window)  # Desenha o jogador

        # Atualizar e desenhar todos os inimigos
        for enemy in enemies:
            if enemy.tempo_espera <= 0:
                enemy.move(player)  # Move o inimigo
            else:
                enemy.tempo_espera -= 1  # Aguarda antes de começar a se mover
            enemy.draw(window)  # Desenha o inimigo


        draw_score(window)  # Desenha a pontuação

    pygame.display.update()

pygame.quit()