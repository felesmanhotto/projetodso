from entidade.compra import Compra
from limite.telaCompra import TelaCompra
from excecao.saldo_negativo import SaldoNegativoException
import copy

class ControladorCompra:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__compras = []
        self.__tela_compra = TelaCompra()

    @property
    def tela_compra(self):
        return self.__tela_compra

    @property
    def compras(self):
        return self.__compras

    def pega_compra(self, codigo):
        for c in self.__compras:
            if c.codigo == codigo:
                return c
        return None

    def inclui_compra(self, evento):
        self.__controlador_sistema.controlador_amigo.lista_amigos_evento(evento)
        dados = self.__tela_compra.pega_dados()
        if self.pega_compra(dados['codigo']):
            self.__tela_compra.mensagem("Compra já existente")
            raise KeyError
        elif self.__controlador_sistema.controlador_amigo.pega_amigo(dados['cpf']) not in evento.amigos:
            self.__tela_compra.mensagem("Amigo não está no evento.")
            raise KeyError

        pagante = self.__controlador_sistema.controlador_amigo.pega_amigo(dados['cpf'])
        compra = Compra(dados['codigo'], evento, pagante)
        while True:
            self.__controlador_sistema.controlador_produto.lista_produtos()
            self.__tela_compra.mensagem('')
            self.__controlador_sistema.controlador_produto.lista_produtos_compra(compra)
            self.__tela_compra.mensagem('')
            codigo_produto = self.__controlador_sistema.controlador_produto.tela_produto.seleciona()
            if not codigo_produto:
                if compra.produtos:
                    break
                self.__tela_compra.mensagem("A compra precisa ter ao menos 1 produto.")
            elif not self.__controlador_sistema.controlador_produto.pega_produto(codigo_produto):
                self.__tela_compra.mensagem("Produto não existente.")
            else:
                compra.add_produto(self.__controlador_sistema.controlador_produto.pega_produto(codigo_produto))
            self.__tela_compra.mensagem("Deixe vazio para finalizar")
        if pagante.carteira.dinheiro < compra.valor_total():
            raise SaldoNegativoException(pagante)

        self.__controlador_sistema.controlador_carteira.recebe_valor(compra.pagante, -compra.valor_total())
        self.__compras.append(compra)
        return compra

    def lista_compras_evento(self, evento):
        try:
            self.__tela_compra.mensagem("Compras no evento: ")
            if evento.compras:
                for c in self.__compras:
                    if c.evento == evento:
                        self.__tela_compra.mostra({'codigo': c.codigo, 'pagante': c.pagante,
                                                   'produtos': [produto.nome for produto in c.produtos],
                                                   'valor': c.valor_total(),
                                                   'quitada': c.quitada})  #add parametros
            else:
                raise KeyError
        except KeyError:
            self.__tela_compra.mensagem("Não há nenhuma compra cadastrada.")


    def exclui_compra(self, evento):
        self.lista_compras_evento(evento)
        codigo_compra = self.__tela_compra.seleciona()   #add parametros
        compra = self.pega_compra(codigo_compra)
        if compra in evento.compras:
            self.__compras.remove(compra)
            self.__controlador_sistema.controlador_carteira.recebe_valor(compra.pagante,
                                                                         compra.valor_total())
            return compra
        else:
            raise KeyError


    def quita_compra(self, compra):
        try:
            if compra.quitada == False:
                valor_parcial = compra.valor_parcial()
                lista_devedores = copy.copy(compra.evento.amigos)
                lista_devedores.remove(compra.pagante)

                for d in lista_devedores:
                    if d.carteira.dinheiro < valor_parcial:
                        raise SaldoNegativoException

                for a in compra.evento.amigos:
                    self.__controlador_sistema.controlador_carteira.recebe_valor(
                        a, -(valor_parcial)
                    )

                self.__controlador_sistema.controlador_carteira.recebe_valor(
                    compra.pagante, compra.valor_total()
                )
                compra.quitada = True
            else:
                raise KeyError
        except KeyError:
            self.__tela_compra.mensagem("Compra já está quitada.")
        except SaldoNegativoException as e:
            self.__tela_compra.mensagem(e)