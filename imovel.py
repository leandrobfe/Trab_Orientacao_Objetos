class Imovel:
    def __init__(self, identificador, nome_proprietaro):
        self.__id = identificador
        self.nome_proprietario = nome_proprietaro

    def get_id(self):
        return self.__id

    def get_nome_proprietario(self):
        return self.nome_proprietario

    def get_json(self):
        return '{\n'+'    "__id": {}\n    "nome_proprietario": "{}"'.format(self.get_id(), self.get_nome_proprietario())

    def __str__(self):
        return f'"identificador": {self.get_id()},\n"nome_proprietario": {self.get_nome_proprietario()}'
