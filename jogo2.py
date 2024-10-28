# importações 
import pygame
import random
import sys
import time
import math
import os

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura_tela = 1000
altura_tela = 805
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Quadrado Móvel")

# Cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

# Configuração do quadrado
largura_quadrado = 50
altura_quadrado = 50
x_quadrado = largura_tela // 2 - largura_quadrado // 2
y_quadrado = altura_tela // 2 - altura_quadrado // 2
velocidade = 5

# Direção inicial
direcao_x = velocidade
direcao_y = 0

# Configuração de FPS
clock = pygame.time.Clock()
FPS = 60

# Função principal do jogo
def jogo():
    global x_quadrado, y_quadrado, direcao_x, direcao_y
    rodando = True
    while rodando:
        # Verifica eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        # Captura as teclas pressionadas para mudar a direção
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_a]:  # Esquerda
            direcao_x = -velocidade
            direcao_y = 0
        elif teclas[pygame.K_d]:  # Direita
            direcao_x = velocidade
            direcao_y = 0
        elif teclas[pygame.K_w]:  # Cima
            direcao_x = 0
            direcao_y = -velocidade
        elif teclas[pygame.K_s]:  # Baixo
            direcao_x = 0
            direcao_y = velocidade
        if teclas[pygame.K_LEFT]:  # Esquerda
            direcao_x = -velocidade
            direcao_y = 0
        elif teclas[pygame.K_RIGHT]:  # Direita
            direcao_x = velocidade
            direcao_y = 0
        elif teclas[pygame.K_UP]:  # Cima
            direcao_x = 0
            direcao_y = -velocidade
        elif teclas[pygame.K_DOWN]:  # Baixo
            direcao_x = 0
            direcao_y = velocidade

        # Movimento do quadrado com limite de bordas
        x_quadrado += direcao_x
        y_quadrado += direcao_y

        # Restringe o quadrado às bordas da tela
        if x_quadrado < 0:
            x_quadrado = 0
        elif x_quadrado > largura_tela - largura_quadrado:
            x_quadrado = largura_tela - largura_quadrado
        if y_quadrado < 0:
            y_quadrado = 0
        elif y_quadrado > altura_tela - altura_quadrado:
            y_quadrado = altura_tela - altura_quadrado

        # Limpa a tela
        tela.fill(BRANCO)
        
        # Desenha o quadrado
        pygame.draw.rect(tela, VERMELHO, (x_quadrado, y_quadrado, largura_quadrado, altura_quadrado))
        
        # Atualiza a tela
        pygame.display.flip()
        
        # Controla a taxa de atualização
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

# Chama a função principal
jogo()