import unittest
import filecmp
from catalogo import Catalogo
from residencia import Residencia
from apartamento import *
from casa import Casa
from terreno import Terreno
from io_catalogo import obter_catalogo, alterar_catalogo, obter_especificacoes, print_catalogo
import json


class TestTrab (unittest.TestCase):
    def test_residencia(self):
        # Residencia (ident, proprietario, qtd_quartos, qtd_vagas_garagem, preco_m2_area_construida)
        resid = Residencia(2, 'Robson Farias', 4, 2, 200)
        self.assertEqual(resid.get_id(), 2)
        self.assertEqual(resid.get_nome_proprietario(), 'Robson Farias')
        self.assertEqual(resid.get_quantidade_quartos(), 4)
        self.assertEqual(resid.get_quantidade_vagas_garagem(), 2)
        self.assertEqual(resid.get_preco_metro_quadrado_area_construida(), 200)

    def test_class_apartamento(self):
        # Apartamento(ident, proprietario, qtd_quartos, qtd_vagas, andar, area_construida,
        #                 preco_m2_area_construida, lazer, qtd_andares)
        ap = Apartamento(1, 'Jose', 3, 2, 4, 100, 50, 'S', 8)
        ident = ap.get_id()
        #apj = json.dumps(ap)
        # print(apj)
        self.assertIsInstance(ap, Apartamento)
        self.assertIsInstance(ident, int)
        self.assertIsInstance(ap.nome_proprietario, str)
        self.assertIsInstance(ap.quantidade_quartos, int)
        self.assertIsInstance(ap.quantidade_vagas_garagem, int)
        self.assertIsInstance(ap.andar, int)
        self.assertIsInstance(ap.area_construida, int)
        self.assertIsInstance(ap.preco_metro_quadrado_area_construida, int)
        self.assertIsInstance(ap.lazer, str)
        self.assertIsInstance(ap.quantidade_andares, int)

    def test_preco_apartamento(self):
        ap = Apartamento(1, 'Jose', 3, 2, 4, 100, 50, 'S', 8)
        preco = ap.calcular_preco()
        #50*100*(0.9 + 4/8)*1.15
        self.assertEqual(round(preco), 8050)

    def test_preco_casa(self):
        # identificador, proprietario, quantidade_quartos, quantidade_vagas_garagem, quantidade_pavimentos, area_pavimento
                 # , preco_m2_area_pavimento, area_livre, preco_m2_area_livre
        casa1 = Casa(48251, 'Eduardo Pelegrineti Targueta',
                     4, 9, 3, 688.3, 310, 309.2, 3945)
        preco_casa1 = casa1.calcular_preco()
        self.assertEqual(preco_casa1, 1859913.0)

    def test_preco_terreno(self):
        #(self, categoria, identificador, proprietario, tipo_solo, preco_m2, *args)
        terreno_retang1 = Terreno(
            "retang", 49038, "Luiz Felipe Mota Santana", "R", 7298, 508.6, 152.6)
        terreno_triang1 = Terreno(
            "triang", 87190, "Pedro Francisco Iguatemy Lopes", "G", 704, 709.5, 160.9)
        terreno_trapez1 = Terreno(
            "trapez", 72649, "Marcelo Borlini Testa", "A", 2182, 24.0, 878.3, 370.9)
        preco_retang1 = terreno_retang1.calcular_preco()
        preco_triang1 = terreno_triang1.calcular_preco()
        preco_trapez1 = terreno_trapez1.calcular_preco()
        self.assertEqual(623056503.608, preco_retang1)
        self.assertEqual(52238952.480000004, preco_triang1)
        self.assertEqual(328605668.43299997, preco_trapez1)

    def test_catalogo(self):
        path = "D:\\Programação\\TrabC++2014\\testes\\"
        catalogo = obter_catalogo(path+"catalogo_teste.txt")
        alterar_catalogo(
            "D:\\Programação\\TrabC++2014\\testes\\atual_teste.txt", catalogo)
        spec = obter_especificacoes(
            "D:\\Programação\\TrabC++2014\\testes\\espec.txt")
        # catalogo.escrever_saida()
        saidas_iguais = filecmp.cmp(path+"espec.txt", path+"espec.txt")

        self.assertEqual(catalogo.get_quantidade_imoveis(), 2)
        self.assertEqual(spec.get_k(), 6)
        self.assertEqual(saidas_iguais, True)


if __name__ == '__main__':
    unittest.main()
