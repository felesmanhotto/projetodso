from entidade.amigo import Amigo
from limite.tela_amigo import TelaAmigo
from excecao.dinheiro_negativo import DinheiroNegativoException
from excecao.cpf_invalido import CpfInvalidoException

class ControladorAmigo:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__amigos = []
        self.__tela_amigo = TelaAmigo()

    @property
    def amigos(self):
        return self.__amigos

    @property
    def tela_amigo(self):
        return self.__tela_amigo

    def pega_amigo(self, cpf):
        for a in self.__amigos:
            if a.cpf == cpf:
                return a
        return None

    def inclui_amigo(self):
        try:
            dados = self.__tela_amigo.pega_dados()  #add parametros
            amigo = self.pega_amigo(dados['cpf'])

            if amigo == None:
                amigo_incluir = Amigo(dados['nome'], dados['cpf'], dados['dinheiro'])
                self.__amigos.append(amigo_incluir)
            else:
                raise KeyError
        except KeyError:
            self.__tela_amigo.mensagem("Amigo já existente.")
        except DinheiroNegativoException as e:
            self.__tela_amigo.mensagem(e)
        except CpfInvalidoException as e:
            self.__tela_amigo.mensagem(e)
        except ValueError:
            self.tela_amigo.mensagem("Dados inválidos.")

    def lista_amigos(self):
        try:
            self.__tela_amigo.mensagem("Lista de amigos: ")
            if self.__amigos:
                for a in self.__amigos:
                    self.__tela_amigo.mostra({'nome': a.nome, 'cpf': a.cpf, 'dinheiro': a.carteira.dinheiro})
            else:
                raise KeyError
        except KeyError:
            self.__tela_amigo.mensagem("Não há nenhum amigo cadastrado.")
            self.__tela_amigo.mensagem('')


    def altera_amigo(self):
        self.lista_amigos()
        cpf_amigo = self.__tela_amigo.seleciona()
        amigo = self.pega_amigo(cpf_amigo)
        try:
            if amigo:
                novos_dados = self.__tela_amigo.pega_dados()
                if self.pega_amigo(novos_dados['cpf']) and not self.pega_amigo(novos_dados['cpf']) == amigo:
                    raise CpfInvalidoException
                amigo.nome = novos_dados['nome']
                amigo.cpf = novos_dados['cpf']
                amigo.carteira.dinheiro = novos_dados['dinheiro']
            else:
                raise KeyError
        except KeyError:
            self.__tela_amigo.mensagem("Amigo não existente.")
        except CpfInvalidoException:
            self.__tela_amigo.mensagem("Já existe alguém com este CPF.")
        except ValueError:
            self.__tela_amigo.mensagem("Dados inválidos.")

    def excluir_amigo(self):
        self.lista_amigos()
        cpf_amigo = self.__tela_amigo.seleciona()   #add parametros
        amigo = self.pega_amigo(cpf_amigo)
        try:
            if amigo:
                self.__amigos.remove(amigo)
            else:
                raise KeyError
        except KeyError:
            self.__tela_amigo.mensagem("Amigo não existente.")

    def olha_carteira(self):
        self.lista_amigos()
        cpf_amigo = self.__tela_amigo.seleciona()   #add parametros
        amigo = self.pega_amigo(cpf_amigo)      # verificar
        try:
            if amigo:
                self.__controlador_sistema.controlador_carteira.abre_tela(amigo)
            else:
                raise KeyError
        except KeyError:
            self.__tela_amigo.mensagem("Amigo não existente")

    def lista_amigos_evento(self, evento):
        self.__tela_amigo.mensagem("Amigos no evento: ")
        for a in evento.amigos:
            self.__tela_amigo.mostra({'nome': a.nome, 'cpf': a.cpf, 'dinheiro': a.carteira.dinheiro})



    def retorna(self):
        self.__controlador_sistema.abre_tela()


    def abre_tela(self):
        lista_opcoes = {1: self.inclui_amigo, 2: self.altera_amigo, 3: self.excluir_amigo,
                        4: self.lista_amigos,5: self.olha_carteira, 0: self.retorna}

        while True:
            lista_opcoes[self.__tela_amigo.opcoes()]()
