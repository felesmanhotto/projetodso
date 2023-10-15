from entidade.evento import Evento
from limite.telaEvento import TelaEvento
from excecao.saldo_negativo import SaldoNegativoException

class ControladorEvento:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_evento = TelaEvento()
        self.__eventos = []


    def pega_evento(self, codigo):
        for e in self.__eventos:
            if e.codigo == codigo:
                return e
        return None

    def inclui_evento(self):
        dados = self.__tela_evento.pega_dados()  #add parametros
        evento = self.pega_evento(dados['codigo'])
        try:
            if evento == None:
                evento_incluir = Evento(dados['nome'], dados['data'], dados['codigo'])  # verificar
                self.__eventos.append(evento_incluir)
            else:
                raise KeyError
        except KeyError:
            self.__tela_evento.mensagem("Evento já existente.")

    def lista_eventos(self):
        try:
            self.__tela_evento.mensagem("Lista de eventos: ")
            if self.__eventos:
                for e in self.__eventos:
                    self.__tela_evento.mostra({'nome': e.nome, 'data': e.data, 'codigo': e.codigo})
            else:
                raise KeyError
        except KeyError:
            self.__tela_evento.mensagem("Não há nenhum evento cadastrado.")


    def altera_evento(self):
        self.lista_eventos()
        codigo_evento = self.__tela_evento.seleciona()   #add parametros
        evento = self.pega_evento(codigo_evento)
        try:
            if evento:
                novos_dados = self.__tela_evento.pega_dados()  # add parametros
                evento.nome = novos_dados['nome']
                evento.data = novos_dados['data']
                evento.codigo = novos_dados['codigo']  # verificar
            else:
                raise KeyError
        except KeyError:
            self.__tela_evento.mensagem("Evento não existente.")

    def exclui_evento(self):
        self.lista_eventos()
        codigo_evento = self.__tela_evento.seleciona()   #add parametros
        evento = self.pega_evento(codigo_evento)
        try:
            if evento:
                self.__eventos.remove(evento)
            else:
                raise KeyError
        except KeyError:
            self.__tela_evento.mensagem("Evento não existente.")


    def olha_evento(self):
        self.lista_eventos()
        codigo = self.__tela_evento.seleciona()
        evento = self.pega_evento(codigo)       # verificar
        try:
            if evento:
                self.__tela_evento.mostra_um_evento(evento)

                lista_opcoes = {1: self.add_amigo, 2: self.add_compra, 3: self.remove_amigo,
                                4: self.remove_compra, 5: self.quita_compra, 6: self.quita_evento,
                                0: self.abre_tela}

                while True:
                    lista_opcoes[self.__tela_evento.opcoes_um_evento()](evento)
            else:
                raise KeyError
        except KeyError:
            self.__tela_evento.mensagem("Evento não existente.")

    def add_amigo(self, evento):
        self.__controlador_sistema.controlador_amigo.lista_amigos()
        try:
            if evento.compras:
                self.__tela_evento.mensagem("Não é possível adicionar amigos em um evento com compras.")
                raise KeyError
            cpf = self.__controlador_sistema.controlador_amigo.tela_amigo.seleciona()
            amigo = self.__controlador_sistema.controlador_amigo.pega_amigo(cpf)
            if not amigo:
                self.__tela_evento.mensagem("Amigo não existente.")
                raise KeyError
            elif amigo in evento.amigos:
                self.__tela_evento.mensagem("Amigo já está no evento")
                raise KeyError
            else:
                evento.add_amigo(amigo)
        except KeyError:
            pass
        self.__tela_evento.mostra_um_evento(evento)


    def add_compra(self, evento):
        try:
            compra = self.__controlador_sistema.controlador_compra.inclui_compra(evento)
            evento.add_compra(compra)
        except KeyError:
            pass
        except SaldoNegativoException as e:
            self.__tela_evento.mensagem(e)

        self.__tela_evento.mostra_um_evento(evento)

    def remove_amigo(self, evento):
        try:
            cpf = self.__controlador_sistema.controlador_amigo.tela_amigo.seleciona()
            if self.__controlador_sistema.controlador_amigo.pega_amigo(cpf) in evento.amigos:
                evento.exc_amigo(cpf)  # verificar
            else:
                raise KeyError
        except KeyError:
            self.__tela_evento.mensagem("Amigo não está no evento.")
        self.__tela_evento.mostra_um_evento(evento)

    def remove_compra(self, evento):
        try:
            compra = self.__controlador_sistema.controlador_compra.exclui_compra(evento)
            evento.exc_compra(compra.codigo)
        except KeyError:
            self.__tela_evento.mensagem("Compra não existente.")
        self.__tela_evento.mostra_um_evento(evento)

    def quita_compra(self, evento):
        self.__controlador_sistema.controlador_compra.lista_compras_evento(evento)
        codigo_compra = self.__controlador_sistema.controlador_compra.tela_compra.seleciona()
        compra = self.__controlador_sistema.controlador_compra.pega_compra(codigo_compra)
        try:
            if compra in evento.compras:
                self.__controlador_sistema.controlador_compra.quita_compra(compra)
            else:
                raise KeyError
        except:
            self.__tela_evento.mensagem("Compra não está no evento.")
        self.__tela_evento.mostra_um_evento(evento)


    def quita_evento(self, evento):
        for c in self.__controlador_sistema.controlador_compra.compras:
            if c.evento == evento:
                self.__controlador_sistema.controlador_compra.quita_compra(c)
        self.__tela_evento.mensagem("Compras do evento quitadas.")
        self.__tela_evento.mostra_um_evento(evento)

    def retorna(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self, evento=''):     # param opcional para poder retornar do "olha evento"
        lista_opcoes = {1: self.inclui_evento, 2: self.altera_evento, 3: self.exclui_evento,
                        4: self.lista_eventos,5: self.olha_evento, 0: self.retorna}

        while True:
            lista_opcoes[self.__tela_evento.opcoes()]()