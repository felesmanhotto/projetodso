from limite.telaCarteira import TelaCarteira
from entidade.carteira import Carteira
from excecao.saldo_negativo import SaldoNegativoException

class ControladorCarteira:

    def __init__(self, controlador_sistema):
        self.__tela_carteira = TelaCarteira()
        self.__controlador_sistema = controlador_sistema

    def paga(self, amigo):
        valor = self.__tela_carteira.pega_valor()
        try:
            if valor < amigo.carteira.dinheiro:
                amigo.carteira.somar_dinheiro(-valor)
            else:
                raise SaldoNegativoException(amigo)
        except SaldoNegativoException as e:
            self.__tela_carteira.mensagem(e)

    def recebe(self, amigo):
        valor = self.__tela_carteira.pega_valor()
        amigo.carteira.somar_dinheiro(valor)

    def recebe_valor(self, amigo, valor):
        amigo.carteira.somar_dinheiro(valor)

    def verifica_divida(self, amigo):
        cpf_credor = self.__tela_carteira.pega_cpf_credor()
        credor = self.__controlador_sistema.controlador_amigo.pega_amigo(cpf_credor)
        divida = 0
        try:
            if cpf_credor and not credor:
                raise KeyError
            elif not cpf_credor:
                for c in self.__controlador_sistema.controlador_compra.compras:
                    if not c.quitada:
                        if c.pagante == amigo:
                            divida -= (c.valor_total() - c.valor_parcial())
                        elif amigo in c.evento.amigos:
                            divida += c.valor_parcial()
                self.__tela_carteira.mensagem(f"Dívida total: R${round(divida,2)}")
                return divida
            else:
                for c in self.__controlador_sistema.controlador_compra.compras:
                    if not c.quitada and amigo.cpf != credor.cpf:
                        if amigo == c.pagante and credor in c.evento.amigos:
                            divida -= c.valor_parcial()
                        elif amigo in c.evento.amigos and credor == c.pagante:
                            divida += c.valor_parcial()
                self.__tela_carteira.mensagem(f"Dívida parcial para {credor.nome}: R${round(divida,2)}")
                return divida
        except KeyError:
            self.__tela_carteira.mensagem("Amigo credor não existente.")

    def retorna(self, _):
        self.__controlador_sistema.controlador_amigo.abre_tela()

    def abre_tela(self, amigo):
        lista_opcoes = {1: self.paga, 2: self.recebe, 3:self.verifica_divida, 0: self.retorna}

        while True:
            lista_opcoes[self.__tela_carteira.opcoes(amigo)](amigo)
