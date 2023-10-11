from entidade.produto import Produto
from limite.telaProduto import TelaProduto

class ControladorProduto:

    def __int__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__produtos = []
        self.__tela_produto = TelaProduto()

    def pega_produto(self, codigo):
        for p in self.__produtos:
            if p.codigo == codigo:
                return p
        return None

    def inclui_produto(self):
        dados = self.__tela_produto.pega_dados()  #add parametros
        produto = Produto(dados['nome'], dados['codigo'], dados['preco'])  # verificar
        self.__produtos.append(produto)

    def lista_produtos(self):
        for p in self.__produtos:
            self.__tela_produto.mostra({'nome': p.nome, 'codigo': p.codigo, 'preco': p.preco})

    def altera_produto(self):
        self.lista_produtos()
        codigo_produto = self.__tela_produto.seleciona()   #add parametros
        produto = self.pega_produto(codigo_produto)

        novos_dados = self.__tela_produto.pega_dados()    #add parametros
        produto.nome = novos_dados['nome']
        produto.preco = novos_dados['preco']      # verificar

    def excluir_produto(self):
        self.lista_produtos()
        codigo_produto = self.__tela_produto.seleciona()  # add parametros
        produto = self.pega_produto(codigo_produto)

        self.__produtos.remove(produto)  # verificar

    def mostra_produto(self):
        self.__tela_produto.mostra()

    def retorna(self):
        self.__controlador_sistema.abre_tela

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_produto(), 2: self.altera_produto(), 3: self.excluir_produto(),
                        4: self.mostra_produto(),5: self.lista_produtos, 0: self.retorna}

        while True:
            lista_opcoes[self.__tela_amigo.opcoes()]()