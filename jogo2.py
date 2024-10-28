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
pygame.display.set_caption("Quadrado Móvel com Bolinhas")

# Cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

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

# Configuração das bolinhas
raio_bolinha = 10
num_bolinhas = 10
bolinhas = []

# Função para criar bolinhas aleatórias na tela
def cria_bolinhas():
    for _ in range(num_bolinhas):
        x = random.randint(raio_bolinha, largura_tela - raio_bolinha)
        y = random.randint(raio_bolinha, altura_tela - raio_bolinha)
        bolinhas.append((x, y))

# Detecta colisão entre o quadrado e uma bolinha
def verifica_colisao(bolinha):
    x_bolinha, y_bolinha = bolinha
    return (x_quadrado < x_bolinha < x_quadrado + largura_quadrado) and \
           (y_quadrado < y_bolinha < y_quadrado + altura_quadrado)

# Função principal do jogo
def jogo():
    global x_quadrado, y_quadrado, direcao_x, direcao_y
    
    cria_bolinhas()  # Cria as bolinhas no início
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

        # Verifica colisões e remove bolinhas consumidas
        bolinhas_consumidas = [bolinha for bolinha in bolinhas if verifica_colisao(bolinha)]
        for bolinha in bolinhas_consumidas:
            bolinhas.remove(bolinha)

        # Limpa a tela
        tela.fill(BRANCO)
        
        # Desenha as bolinhas
        for bolinha in bolinhas:
            pygame.draw.circle(tela, AZUL, bolinha, raio_bolinha)
        
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