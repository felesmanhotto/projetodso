from abc import ABC, abstractmethod

class TelaAbstrata(ABC):

    @abstractmethod
    def le_num_inteiro(self):
        pass

    @abstractmethod
    def opcoes(self):
        pass

    @abstractmethod
    def pega_dados(self):
        pass

    @abstractmethod
    def mostra(self, dados):
        pass

    @abstractmethod
    def seleciona(self):
        pass

    @abstractmethod
    def mensagem(self, msg):
        pass