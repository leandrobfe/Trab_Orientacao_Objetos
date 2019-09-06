from residencia import Residencia


class Casa(Residencia):
    def __init__(self, identificador, proprietario, quantidade_quartos,
                 quantidade_vagas_garagem, quantidade_pavimentos, area_pavimento,
                 preco_m2_area_pavimento, area_livre, preco_m2_area_livre):
        super().__init__(identificador, proprietario, quantidade_quartos,
                         quantidade_vagas_garagem, preco_m2_area_pavimento)

        self.quantidade_pavimentos = quantidade_pavimentos
        self.area_pavimento = area_pavimento
        self.area_livre = area_livre
        self.preco_metro_quadrado_area_livre = preco_m2_area_livre
        self.preco = self.calcular_preco()

    def __str__(self):
        atributos_residencia = super().__str__()
        quantidade_pavimentos = self.get_quantidade_pavimentos()
        area_pavimento = self.get_area_pavimento()
        area_livre = self.get_area_livre()
        preco_metro_quadrado_area_livre = self.get_preco_metro_quadrado_area_livre()
        return f'{atributos_residencia},\n"quantidade_pavimentos": {quantidade_pavimentos},\n"area_pavimento": {area_pavimento},\n"area_livre": {area_livre},\n"preco_metro_quadrado_area_livre": {preco_metro_quadrado_area_livre}'

    def print(self):
        ident = self.get_id()
        proprietario = self.get_nome_proprietario()
        qtd_quartos = self.get_quantidade_quartos()
        vagas_garagem = self.get_quantidade_vagas_garagem()
        preco_m2_ac = self.get_preco_metro_quadrado_area_construida()
        quantidade_pavimentos = self.get_quantidade_pavimentos()
        area_pavimento = self.get_area_pavimento()
        area_livre = self.get_area_livre()
        preco_m2_al = self.get_preco_metro_quadrado_area_livre()
        print(f'casa\n{ident}\n{proprietario}\n{qtd_quartos}\n{vagas_garagem}\n{quantidade_pavimentos}\n{area_pavimento}\n{preco_m2_ac}\n{area_livre}\n{preco_m2_al}')

    def get_quantidade_pavimentos(self):
        return self.quantidade_pavimentos

    def get_area_pavimento(self):
        return self.area_pavimento

    def get_area_livre(self):
        return self.area_livre

    def get_preco_metro_quadrado_area_livre(self):
        return self.preco_metro_quadrado_area_livre

    def calcular_preco(self):
        preco_m2_area_construida = self.get_preco_metro_quadrado_area_construida()
        area_pavimento = self.get_area_pavimento()
        qtd_pavimentos = self.get_quantidade_pavimentos()
        preco_m2_area_livre = self.get_preco_metro_quadrado_area_livre()
        area_livre = self.get_area_livre()
        return (preco_m2_area_construida * area_pavimento * qtd_pavimentos) + (preco_m2_area_livre * area_livre)
