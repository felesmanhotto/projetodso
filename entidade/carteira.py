class Carteira:
    def __init__(self, dinheiro):
        self.__dinheiro = float(dinheiro)

    @property
    def dinheiro(self):
        return self.__dinheiro

    @dinheiro.setter
    def dinheiro(self, dinheiro):
        self.__dinheiro = dinheiro

    def somar_dinheiro(self, valor):
        self.__dinheiro += float(valor)