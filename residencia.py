from imovel import Imovel


class Residencia(Imovel):
    def __init__(self, identificador, proprietario, quantidade_quartos,
                 quantidade_vagas_garagem, preco_metro_quadrado_area_construida):
        super().__init__(identificador, proprietario)
        self.quantidade_quartos = quantidade_quartos
        self.quantidade_vagas_garagem = quantidade_vagas_garagem
        self.preco_metro_quadrado_area_construida = preco_metro_quadrado_area_construida

    def get_json(self):
        atributos_imovel = super().get_json()
        qtd_quartos = self.get_quantidade_quartos()
        vagas_garagem = self.get_quantidade_vagas_garagem()
        preco_m2_ac = self.get_preco_metro_quadrado_area_construida()
        return '{}\n    "quantidade_quartos": {}\n    "quantidade_vagas_garagem": {}\n    "preco_metro_quadrado_area_construida": {}'.format(atributos_imovel, qtd_quartos, vagas_garagem, preco_m2_ac)

    def __str__(self):
        atributos_imovel = super().__str__()
        qtd_quartos = self.get_quantidade_quartos()
        vagas_garagem = self.get_quantidade_vagas_garagem()
        preco_m2_ac = self.get_preco_metro_quadrado_area_construida()
        return f'{atributos_imovel},\n"quantidade_quartos": {qtd_quartos},\n"quantidade_vagas_garagem": {vagas_garagem},\n"preco_metro_quadrado_area_construida": {preco_m2_ac}'

    def get_quantidade_quartos(self):
        return self.quantidade_quartos

    def get_quantidade_vagas_garagem(self):
        return self.quantidade_vagas_garagem

    def get_preco_metro_quadrado_area_construida(self):
        return self.preco_metro_quadrado_area_construida
