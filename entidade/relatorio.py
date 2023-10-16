from entidade.amigo import Amigo
from entidade.produto import Produto

class Relatorio:

    def __init__(self, mes, pessoa_mais_gastou, valor_gasto,
                 produto_mais_comprado, frequencia_produto):
        self.__mes = mes
        self.__pessoa_mais_gastou = pessoa_mais_gastou
        self.__valor_gasto = valor_gasto
        self.__produto_mais_comprado = produto_mais_comprado
        self.__frequencia_produto = frequencia_produto

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        self.__mes = mes

    @property
    def pessoa_mais_gastou(self):
        return self.__pessoa_mais_gastou

    @pessoa_mais_gastou.setter
    def pessoa_mais_gastou(self, pessoa_mais_gastou):
        self.__pessoa_mais_gastou = pessoa_mais_gastou

    @property
    def valor_gasto(self):
        return self.__valor_gasto

    @valor_gasto.setter
    def valor_gasto(self, valor_gasto):
        self.__valor_gasto = valor_gasto

    @property
    def produto_mais_comprado(self):
        return self.__produto_mais_comprado

    @produto_mais_comprado.setter
    def produto_mais_comprado(self, produto_mais_comprado):
        self.__produto_mais_comprado = produto_mais_comprado

    @property
    def frequencia_produto(self):
        return self.__frequencia_produto

    @frequencia_produto.setter
    def frequencia_produto(self, frequencia_produto):
        self.__frequencia_produto = frequencia_produto