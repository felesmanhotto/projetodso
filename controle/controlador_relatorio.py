from entidade.relatorio import Relatorio
from limite.tela_relatorio import TelaRelatorio

class ControladorRelatorio:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__relatorios = []
        self.__tela_relatorio = TelaRelatorio()

    def cria_relatorio(self):
        try:
            mes = self.__tela_relatorio.pega_dados()
            if not [compra for compra in self.__controlador_sistema.controlador_compra.compras
                if (compra.evento.data[3] + compra.evento.data[4]) == mes]:     #Verifica se há compras no mês
                raise KeyError
            amigo_mais_gastou = ''
            maior_valor = 0
            for amigo in self.__controlador_sistema.controlador_amigo.amigos:
                valor_amigo = 0
                for compra in self.__controlador_sistema.controlador_compra.compras:
                    if compra.evento.data[3] + compra.evento.data[4] == mes:
                        if amigo in compra.evento.amigos:
                            if compra.quitada == True:
                                valor_amigo += compra.valor_parcial()
                            elif compra.pagante == amigo:
                                valor_amigo += compra.valor_total()
                if valor_amigo > maior_valor:
                    maior_valor = valor_amigo
                    amigo_mais_gastou = amigo

            produto_mais_comprado = ''
            max_frequencia = 0
            for produto in self.__controlador_sistema.controlador_produto.produtos:
                freq_produto = 0
                for compra in self.__controlador_sistema.controlador_compra.compras:
                    freq_produto += compra.produtos.count(produto)
                if freq_produto > max_frequencia:
                    max_frequencia = freq_produto
                    produto_mais_comprado = produto

            relatorio = Relatorio(mes, amigo_mais_gastou, maior_valor,
                                  produto_mais_comprado, max_frequencia)

            self.__relatorios.append(relatorio)
        except KeyError:
            self.__tela_relatorio.mensagem("Não há nenhuma compra no mês")
        except ValueError:
            self.__tela_relatorio.mensagem("Mês inválido")

    def lista_relatorios(self):
        try:
            self.__tela_relatorio.mensagem("Lista de relatórios: ")
            if self.__relatorios:
                for r in self.__relatorios:
                    self.__tela_relatorio.mostra({'mes': r.mes, 'amigo_mais_gastou': r.pessoa_mais_gastou,
                                                  'valor_gasto': r.valor_gasto,
                                                  'produto_mais_comprado': r.produto_mais_comprado,
                                                  'frequencia_produto': r.frequencia_produto})
            else:
                raise KeyError
        except KeyError:
            self.__tela_relatorio.mensagem("Não há nenhum relatório cadastrado.")
            self.__tela_relatorio.mensagem('')

    def pega_relatorio_mes(self, mes):
        for r in self.__relatorios:
            if r.mes == mes:
                return r
        return None

    def exclui_relatorio(self):
        self.lista_relatorios()
        try:
            relatorio = self.pega_relatorio_mes(self.__tela_relatorio.pega_dados())
            if relatorio:
                self.__relatorios.remove(relatorio)
            else:
                raise KeyError
        except KeyError:
            self.__tela_relatorio.mensagem("Não existe relatório deste mês.")
        except ValueError:
            self.__tela_relatorio.mensagem("Mês inválido.")

    def retorna(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.cria_relatorio, 2: self.exclui_relatorio, 3: self.lista_relatorios,
                        0: self.retorna}

        while True:
            lista_opcoes[self.__tela_relatorio.opcoes()]()