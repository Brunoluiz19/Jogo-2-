import pygame

class Grid:
    def __init__(self):
        self.num_linhas = 20
        self.num_colunas = 30
        self.tamanho_celula = 30
        self.grade = [[0 for _ in range(self.num_colunas)] for _ in range(self.num_linhas)]
        self.cor_linha = (200, 200, 200)  # Cor das linhas da grade

    def imprimir_grade(self):
        for linha in range(self.num_linhas):
            for coluna in range(self.num_colunas):
                print(self.grade[linha][coluna], end=" ")
            print()
    
    def draw(self, screen):
        for linha in range(self.num_linhas):
            for coluna in range(self.num_colunas):
                x = coluna * self.tamanho_celula
                y = linha * self.tamanho_celula
                # Desenha o retângulo para cada célula
                pygame.draw.rect(
                    screen, self.cor_linha, 
                    (x, y, self.tamanho_celula, self.tamanho_celula), 1
                )
