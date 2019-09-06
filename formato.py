from abc import ABC, abstractmethod


class Formato(ABC):
    @abstractmethod
    def get_area(self):
        pass


class Triangulo(Formato):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def set_base(self, base):
        self.base = base

    def set_altura(self, altura):
        self.altura = altura

    def get_base(self):
        return self.base

    def get_altura(self):
        return self.altura

    def get_area(self):
        return (self.get_base() * self.get_altura()) / 2

    def __str__(self):
        return f'"base": {self.get_base()},\n"altura": {self.get_altura()}'


class Retangulo(Formato):
    def __init__(self, lado1, lado2):
        self.lado1, self.lado2 = lado1, lado2

    def __str__(self):
        return f'"lado1": {self.get_lado1()},\n"lado2": {self.get_lado2()}'

    def get_lado1(self):
        return self.lado1

    def get_lado2(self):
        return self.lado2

    def get_area(self):
        return self.get_lado1() * self.get_lado2()


class Trapezio(Formato):
    def __init__(self, base1, base2, altura):
        self.base1 = base1
        self.base2 = base2
        self.altura = altura

    def __str__(self):
        return f'"base1": {self.get_base1()},\n"base2": {self.get_base2()},\n"altura": {self.get_altura()}'

    def set_base1(self, base1):
        self.base1 = base1

    def set_base2(self, base2):
        self.base2 = base2

    def set_altura(self, altura):
        self.altura = altura

    def get_base1(self):
        return self.base1

    def get_base2(self):
        return self.base2

    def get_altura(self):
        return self.altura

    def get_area(self):
        B = self.get_base1()
        b = self.get_base2()
        h = self.get_altura()
        return ((B + b) * h) / 2
