from math import trunc


class Especificacao:
    def __init__(self, percentual_imoveis_caros, percentual_menores_argilosos, area_limite, preco_limite, i, j, k):
        self.percentual_imoveis_caros = percentual_imoveis_caros
        self.percentual_menores_argilosos = percentual_menores_argilosos
        self.area_limite = area_limite
        self.preco_limite = preco_limite
        self.i = i
        self.j = j
        self.k = k

    def get_percentual_imoveis_caros(self):
        return self.percentual_imoveis_caros

    def get_k(self):
        return self.k
