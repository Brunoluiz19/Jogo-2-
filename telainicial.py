import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Meu Jogo Pokémon")

# Cores
BRANCO = (255, 255, 255)

# Loop principal do jogo
def main():
    while True:
        # Verifica os eventos (como fechar a janela)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Preenche o fundo com uma cor
        tela.fill(BRANCO)

        # Atualiza o display
        pygame.display.flip()

# Inicia o jogo
if __name__ == "__main__":
    main()