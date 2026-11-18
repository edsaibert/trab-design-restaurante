
class ItemCardapio:
    def __init__(self, id, nome, porcoes, tamanhoPorcao, vegano, disponibilidade):
        self.id = id
        self.nome = nome
        self.porcoes = porcoes
        self.tamanhoPorcao = tamanhoPorcao
        self.vegano = vegano
        self.disponibilidade = disponibilidade

    def atualizar_disponibilidade(self):
        self.disponibilidade = self.porcoes == 0