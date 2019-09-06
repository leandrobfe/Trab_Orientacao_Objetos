from terreno import Terreno
from formato import Triangulo, Retangulo, Trapezio
from casa import Casa
from apartamento import Apartamento
from catalogo import Catalogo
from especificacao_resultados import Especificacao


def get_linha_formatada(file):
    return file.readline().rstrip()


def get_int_from_linha_arquivo(file):
    linha = file.readline().rstrip()
    return int(linha)


def get_float_from_linha_arquivo(file):
    linha = file.readline().rstrip()
    return float(linha)


def formatatar_linha(linha):
    return linha.rstrip()


def ler_espaco_entre_imoveis(file):
    file.readline()


def criar_terreno(file, categoria, ident, nome_proprietario):
    tipo_solo = get_linha_formatada(file)
    preco_m2 = get_linha_formatada(file)
    arg1 = get_linha_formatada(file)
    arg2 = get_linha_formatada(file)
    args = []
    args.append(arg1)
    args.append(arg2)
    if categoria == 'trapez':
        args.append(get_linha_formatada(file))

    return Terreno(categoria, ident, nome_proprietario, tipo_solo, preco_m2, *args)


def criar_casa(file, ident, nome_proprietario,
               quantidade_quartos, quantidade_vagas):
    quantidade_pavimentos = get_linha_formatada(file)
    area_pavimento = get_linha_formatada(file)
    preco_m2_area_pavimento = get_linha_formatada(file)
    area_livre = get_linha_formatada(file)
    preco_m2_area_livre = get_linha_formatada(file)

    return Casa(ident, nome_proprietario, quantidade_quartos, quantidade_vagas, quantidade_pavimentos,
                area_pavimento, preco_m2_area_pavimento, area_livre, preco_m2_area_livre)


def criar_apartamento(file, ident, nome_proprietario, quantidade_quartos, quantidade_vagas):
    andar = get_linha_formatada(file)
    area_construida = get_linha_formatada(file)
    preco_m2_area_construida = get_linha_formatada(file)
    lazer = get_linha_formatada(file)
    quantidade_andares = get_linha_formatada(file)
    return Apartamento(
        ident, nome_proprietario, quantidade_quartos, quantidade_vagas, andar, area_construida, preco_m2_area_construida, lazer, quantidade_andares)


def criar_imovel(file, categoria, ident):
    nome_proprietario = get_linha_formatada(file)
    if categoria in ('retang', 'triang', 'trapez'):
        return criar_terreno(file, categoria, ident, nome_proprietario)
    elif categoria in ("casa", "apto"):
        quantidade_quartos = get_linha_formatada(file)
        quantidade_vagas = get_linha_formatada(file)
        if categoria == "casa":
            return criar_casa(file, ident, nome_proprietario,
                              quantidade_quartos, quantidade_vagas)
        elif categoria == "apto":
            return criar_apartamento(
                file, ident, nome_proprietario, quantidade_quartos, quantidade_vagas)


def print_catalogo(catalogo):
    for imovel in catalogo:
        imovel.print()
        print("")  # linha separadora de saida


def obter_catalogo(arquivo_catalogo):
    lista_imoveis = []
    with open(arquivo_catalogo, 'r') as file:
        for line in file:
            categoria = formatatar_linha(line)
            ident = get_linha_formatada(file)
            lista_imoveis.append(criar_imovel(file, categoria, ident))
            ler_espaco_entre_imoveis(file)
        file.close()
    return Catalogo(lista_imoveis)


def remover_imovel(catalogo, ident):
    for imovel in catalogo:
        if imovel.get_id() == ident:
            catalogo.remove(imovel)


def alterar_catalogo(arquivo_alteracao, catalogo):
    lista_imoveis = catalogo.get_lista_imoveis()
    with open(arquivo_alteracao, "r") as file:
        for line in file:
            tipo_alteracao = formatatar_linha(line)
            if tipo_alteracao in ("i", "a"):
                categoria = get_linha_formatada(file)
                ident = get_linha_formatada(file)
                imovel = criar_imovel(file, categoria, ident)
                if tipo_alteracao == "a":
                    remover_imovel(lista_imoveis, ident)
                lista_imoveis.append(imovel)
            elif tipo_alteracao == "e":
                ident = get_linha_formatada(file)
                remover_imovel(lista_imoveis, ident)
    file.close()


def obter_especificacoes(arquivo_especificacao):
    with open(arquivo_especificacao, "r") as file:
        percentual_imoveis_caros = get_int_from_linha_arquivo(file)
        percentual_menores_argilosos = get_int_from_linha_arquivo(file)
        area_limite = get_float_from_linha_arquivo(file)
        preco_limite = get_float_from_linha_arquivo(file)
        i = get_int_from_linha_arquivo(file)
        j = get_int_from_linha_arquivo(file)
        k = get_int_from_linha_arquivo(file)
    file.close()
    return Especificacao(percentual_imoveis_caros, percentual_menores_argilosos, area_limite, preco_limite, i, j, k)
