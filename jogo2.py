import pygame
import random
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura_tela = 1000
altura_tela = 805
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Quadrado Móvel com Bolinhas e Inimigos")

# Cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
AMARELO = (255, 255, 0)
ROSA = (255, 0, 255)

# Configuração do quadrado vermelho
largura_quadrado = 25
altura_quadrado = 25
x_quadrado = largura_tela // 2 - largura_quadrado // 2
y_quadrado = altura_tela // 2 - altura_quadrado // 2
velocidade = 4

# Direção inicial
direcao_x = velocidade
direcao_y = 0

# Configuração de FPS
clock = pygame.time.Clock()
FPS = 60

# Configuração das bolinhas
raio_bolinha = 7
num_bolinhas = 30
bolinhas = []

# Configuração dos quadrados inimigos
largura_inimigo = 20
altura_inimigo = 20
velocidade_inimigo = 2
inimigos = [
    {"cor": VERDE, "pos": [random.randint(0, largura_tela - largura_inimigo), random.randint(0, altura_tela - altura_inimigo)], "direcao": [velocidade_inimigo, 0]},
    {"cor": AMARELO, "pos": [random.randint(0, largura_tela - largura_inimigo), random.randint(0, altura_tela - altura_inimigo)], "direcao": [0, velocidade_inimigo]},
    {"cor": ROSA, "pos": [random.randint(0, largura_tela - largura_inimigo), random.randint(0, altura_tela - altura_inimigo)], "direcao": [velocidade_inimigo, 0]},
]

# Função para criar bolinhas aleatórias na tela
def cria_bolinhas():
    for _ in range(num_bolinhas):
        x = random.randint(raio_bolinha, largura_tela - raio_bolinha)
        y = random.randint(raio_bolinha, altura_tela - raio_bolinha)
        bolinhas.append((x, y))

# Detecta colisão entre o quadrado vermelho e uma bolinha
def verifica_colisao(bolinha):
    x_bolinha, y_bolinha = bolinha
    return (x_quadrado < x_bolinha < x_quadrado + largura_quadrado) and \
           (y_quadrado < y_bolinha < y_quadrado + altura_quadrado)

# Verifica colisão entre dois quadrados (usado para inimigos)
def verifica_colisao_inimigos(pos1, pos2, largura, altura):
    return (
        pos1[0] < pos2[0] + largura and
        pos1[0] + largura > pos2[0] and
        pos1[1] < pos2[1] + altura and
        pos1[1] + altura > pos2[1]
    )

# Função para mover os inimigos em direção ao quadrado vermelho
def mover_inimigos():
    for inimigo in inimigos:
        x_inimigo, y_inimigo = inimigo["pos"]
        direcao_x_inimigo, direcao_y_inimigo = inimigo["direcao"]

        # Movimenta o inimigo somente em uma direção
        if direcao_x_inimigo != 0:  # Se está movendo na horizontal
            if x_inimigo < x_quadrado:
                x_inimigo += velocidade_inimigo
            elif x_inimigo > x_quadrado:
                x_inimigo -= velocidade_inimigo
        elif direcao_y_inimigo != 0:  # Se está movendo na vertical
            if y_inimigo < y_quadrado:
                y_inimigo += velocidade_inimigo
            elif y_inimigo > y_quadrado:
                y_inimigo -= velocidade_inimigo

        # Verifica colisão com outros inimigos e ajusta direção se necessário
        for outro_inimigo in inimigos:
            if outro_inimigo != inimigo and verifica_colisao_inimigos([x_inimigo, y_inimigo], outro_inimigo["pos"], largura_inimigo, altura_inimigo):
                # Inverte a direção para evitar colisão
                if direcao_x_inimigo != 0:
                    direcao_x_inimigo = -direcao_x_inimigo
                else:
                    direcao_y_inimigo = -direcao_y_inimigo

        # Atualiza a posição e direção do inimigo
        inimigo["pos"] = [x_inimigo, y_inimigo]
        inimigo["direcao"] = [direcao_x_inimigo, direcao_y_inimigo]

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
        elif teclas[pygame.K_LEFT]:  # Esquerda
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

        # Movimento do quadrado vermelho com limite de bordas
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

        # Move os inimigos na direção do quadrado vermelho
        mover_inimigos()

        # Verifica colisões e remove bolinhas consumidas
        bolinhas_consumidas = [bolinha for bolinha in bolinhas if verifica_colisao(bolinha)]
        for bolinha in bolinhas_consumidas:
            bolinhas.remove(bolinha)

        # Limpa a tela
        tela.fill(BRANCO)
        
        # Desenha as bolinhas
        for bolinha in bolinhas:
            pygame.draw.circle(tela, AZUL, bolinha, raio_bolinha)
        
        # Desenha os inimigos
        for inimigo in inimigos:
            pygame.draw.rect(tela, inimigo["cor"], (*inimigo["pos"], largura_inimigo, altura_inimigo))
        
        # Desenha o quadrado vermelho
        pygame.draw.rect(tela, VERMELHO, (x_quadrado, y_quadrado, largura_quadrado, altura_quadrado))
        
        # Atualiza a tela
        pygame.display.flip()
        
        # Controla a taxa de atualização
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

# Chama a função principal
jogo()