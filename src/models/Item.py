class Item:
    def __init__(self, id, nome, porcoes, tamanhoPorcao, vegano):
        self.id = id
        self.nome = nome
        self.porcoes = porcoes
        self.tamanhoPorcao = tamanhoPorcao
        self.vegano = vegano

    def disponibilidade(self, quantidade):
        return self.porcoes >= quantidade