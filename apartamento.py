from residencia import Residencia


class Apartamento(Residencia):
    def __init__(self, ident, proprietario, qtd_quartos, qtd_vagas, andar, area_construida, preco_m2_area_construida, lazer, qtd_andares):
        super().__init__(ident, proprietario, qtd_quartos,
                         qtd_vagas, preco_m2_area_construida)
        self.andar = andar
        self.area_construida = area_construida
        self.lazer = lazer
        self.quantidade_andares = qtd_andares
        self.preco = self.calcular_preco()

    def get_json(self):
        atributos_residencia = super().get_json()
        ac = self.get_area_construida()
        andar = self.get_andar()
        qtd_andares = self.get_quantidade_andares()
        lazer = self.get_lazer()
        return f'{atributos_residencia}\n"andar": {andar}\n"area_construida": {ac}\n"lazer": "{lazer}"\n"quantidade_andares": {qtd_andares}'+"}"

    def __str__(self):
        atributos_residencia = super().__str__()
        ac = self.get_area_construida()
        andar = self.get_andar()
        qtd_andares = self.get_quantidade_andares()
        lazer = self.get_lazer()
        return f'{atributos_residencia}\n"andar": {andar}\n"area_construida": {ac}\n"lazer": "{lazer}"\n"quantidade_andares": {qtd_andares}'

    def print(self):
        ident = self.get_id()
        proprietario = self.get_nome_proprietario()
        qtd_quartos = self.get_quantidade_quartos()
        vagas_garagem = self.get_quantidade_vagas_garagem()
        preco_m2_ac = self.get_preco_metro_quadrado_area_construida()

        ac = self.get_area_construida()
        andar = self.get_andar()
        qtd_andares = self.get_quantidade_andares()
        lazer = self.get_lazer()
        print(f'apto\n{ident}\n{proprietario}\n{qtd_quartos}\n{vagas_garagem}\n{andar}\n{ac}\n{preco_m2_ac}\n{lazer}\n{qtd_andares}')

    def get_andar(self):
        return self.andar

    def get_area_construida(self):
        return self.area_construida

    def get_lazer(self):
        return self.lazer

    def get_quantidade_andares(self):
        return self.quantidade_andares

    def get_fator_lazer(self):
        lazer = self.get_lazer()
        if lazer is 'S':
            return 1.15
        elif lazer is 'N':
            return 1

    def calcular_preco(self):
        preco_m2_ac = self.get_preco_metro_quadrado_area_construida()
        ac = self.get_area_construida()
        andar = self.get_andar()
        qtd_andares = self.get_quantidade_andares()
        fator_L = self.get_fator_lazer()
        return preco_m2_ac * ac * (0.9 + andar/qtd_andares) * fator_L
