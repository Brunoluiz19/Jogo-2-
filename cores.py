class Cores:
    cinza_escuro = (30, 35, 45)
    verde = (50, 220, 30)
    vermelho = (240, 30, 30)
    laranja = (230, 120, 25)
    amarelo = (245, 240, 10)
    roxo = (160, 0, 250)
    ciano = (25, 200, 215)
    azul = (20, 70, 225)
    branco = (255, 255, 255)
    azul_escuro = (48, 48, 130)
    azul_claro = (65, 90, 170)
    preto = (0,0,0)

    @classmethod
    def obter_cores_celulas(cls):
        return [cls.cinza_escuro, cls.verde, cls.vermelho, cls.laranja, cls.amarelo, cls.roxo, cls.ciano, cls.azul, cls.preto]
