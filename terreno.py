from imovel import Imovel
from formato import Triangulo, Retangulo, Trapezio


class Terreno(Imovel):

    def __init__(self, categoria, identificador, proprietario, tipo_solo, preco_m2, *args):
        super().__init__(identificador, proprietario)
        self.tipo_solo_predominante = tipo_solo
        self.preco_metro_quadrado = preco_m2
        self.set_formato(categoria, *args)
        self.preco = self.calcular_preco()

    ##
    def initbkp(self, identificador, proprietario, tipo_solo, preco_m2):
        super().__init__(identificador, proprietario)
        self.tipo_solo_predominante = tipo_solo
        self.preco_metro_quadrado = preco_m2
        self.formato = None

    def get_id(self):
        return super().get_id()

    def get_tipo_solo_predominante(self):
        return self.tipo_solo_predominante

    def get_preco_metro_quadrado(self):
        return self.preco_metro_quadrado

    def __str__(self):
        atributos_imovel = super().__str__()
        dados_formato = self.formato.__str__()
        return f'{atributos_imovel},\n"tipo de solo": {self.tipo_solo_predominante},\n"preco_metro_quadrado": {self.preco_metro_quadrado},\n{dados_formato}'

    def print(self):
        ident = self.get_id()
        proprietario = self.get_nome_proprietario()
        tipo_solo = self.get_tipo_solo_predominante()
        preco_m2 = self.get_preco_metro_quadrado()
        dados_formato = ""
        if self.is_retangulo():
            print('retang')
            dados_formato += f'{self.formato.get_lado1()}\n{self.formato.get_lado2()}'
        elif self.is_triangulo():
            print('triang')
            dados_formato += f'{self.formato.get_base()}\n{self.formato.get_altura()}'
        elif self.is_trapezio():
            print('trapez')
            dados_formato += f'{self.formato.get_base1()}\n{self.formato.get_base2()}\n{self.formato.get_altura()}'
        print(f'{ident}\n{proprietario}\n{tipo_solo}\n{preco_m2}\n{dados_formato}')

    def set_formato(self, categoria, *args):
        if categoria == "retang":
            self.set_formato_retangulo(args[0], args[1])
        elif categoria == "triang":
            self.set_formato_triangulo(args[0], args[1])
        elif categoria == "trapez":
            self.set_formato_trapezio(args[0], args[1], args[2])

    def set_formato_retangulo(self, lado1, lado2):
        retangulo = Retangulo(lado1, lado2)
        self.formato = retangulo

    def set_formato_triangulo(self, base, altura):
        self.formato = Triangulo(base, altura)

    def set_formato_trapezio(self, base1, base2, altura):
        self.formato = Trapezio(base1, base2, altura)

    def is_retangulo(self):
        if self.formato:
            return isinstance(self.formato, Retangulo)

    def is_triangulo(self):
        if self.formato:
            return isinstance(self.formato, Triangulo)

    def is_trapezio(self):
        if self.formato:
            return isinstance(self.formato, Trapezio)

    def get_area(self):
        return self.formato.get_area()

    def get_fator_multiplicativo(self):
        tipo_solo = self.get_tipo_solo_predominante()
        if tipo_solo == "A":
            return 0.9
        elif tipo_solo == "G":
            return 1.3
        elif tipo_solo == "R":
            return 1.1

    def calcular_preco(self):
        preco_m2 = self.get_preco_metro_quadrado()
        area = self.get_area()
        fator_multiplicativo = self.get_fator_multiplicativo()
        return preco_m2 * area * fator_multiplicativo
