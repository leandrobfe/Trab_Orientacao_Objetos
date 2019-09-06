from especificacao_resultados import Especificacao
from math import trunc


class Catalogo:
    def __init__(self, imoveis):
        self.lista_imoveis = imoveis

    def get_lista_imoveis(self):
        return self.lista_imoveis

    def get_quantidade_imoveis(self):
        imoveis = self.get_lista_imoveis()
        return len(imoveis)

    def calcular_quantidade_imoveis_caros(self, especificacao):
        percentual_lido = especificacao.get_percentual_imoveis_caros()
        total_imoves = self.get_quantidade_imoveis()
        return trunc(percentual_lido*total_imoves/100)

    def get_lista_identificadores_imoveis(self):
        imoveis = self.get_lista_imoveis()
        lista = []
        for i in imoveis:
            lista.append(i.get_id())
        return lista

    def get_lista_imoveis_caros(self, espec):
        imoveis = self.get_lista_imoveis()
        print(self.get_lista_imoveis())
        imoveis.sort(key=lambda imovel: imovel.preco, reverse=True)
