# importações 
import pygame
import random
import sys
import time
import math
import os

# Inicializa o Pygame
pygame.init()
pygame.mixer.init()


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

# Configuração de FPS
clock = pygame.time.Clock()
FPS = 60

# Função principal do jogo
def jogo():
    rodando = True
    while rodando:
        # Verifica eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        # Captura as teclas pressionadas
        teclas = pygame.key.get_pressed()
        global x_quadrado, y_quadrado
        
        # Movimento do quadrado
        if teclas[pygame.K_a] and x_quadrado > 0:
            x_quadrado -= velocidade
        if teclas[pygame.K_d] and x_quadrado < largura_tela - largura_quadrado:
            x_quadrado += velocidade
        if teclas[pygame.K_w] and y_quadrado > 0:
            y_quadrado -= velocidade
        if teclas[pygame.K_s] and y_quadrado < altura_tela - altura_quadrado:
            y_quadrado += velocidade
        if teclas[pygame.K_LEFT] and x_quadrado > 0:
            x_quadrado -= velocidade
        if teclas[pygame.K_RIGHT] and x_quadrado < largura_tela - largura_quadrado:
            x_quadrado += velocidade
        if teclas[pygame.K_UP] and y_quadrado > 0:
            y_quadrado -= velocidade
        if teclas[pygame.K_DOWN] and y_quadrado < altura_tela - altura_quadrado:
            y_quadrado += velocidade

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