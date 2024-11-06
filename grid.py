import pygame

class Grid:
    def __init__(self):
        self.num_linhas = 20
        self.num_colunas = 10
        self.tamanho_celula = 30
        self.grade = [[0 for _ in range(self.num_colunas)] for _ in range(self.num_linhas)]
