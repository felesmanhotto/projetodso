from entidade.produto import Produto
from limite.tela_produto import TelaProduto
from excecao.dinheiro_negativo import DinheiroNegativoException

class ControladorProduto:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__produtos = []
        self.__tela_produto = TelaProduto()

    @property
    def produtos(self):
        return self.__produtos

    @property
    def tela_produto(self):
        return self.__tela_produto

    def pega_produto(self, codigo):
        for p in self.__produtos:
            if p.codigo == codigo:
                return p
        return None

    def inclui_produto(self):
        try:
            dados = self.__tela_produto.pega_dados()
            codigo = dados['codigo']
            produto = self.pega_produto(codigo)
            if produto == None:
                produto_incluir = Produto(dados['nome'], dados['codigo'], dados['preco'])
                self.__produtos.append(produto_incluir)
            else:
                raise ValueError
        except KeyError:
            self.__tela_produto.mensagem('Código inválido.')
        except ValueError:
            self.__tela_produto.mensagem("Preço inválido.")
        except DinheiroNegativoException as e:
            self.__tela_produto.mensagem(e)

    def lista_produtos(self):
        try:
            self.__tela_produto.mensagem("Lista de produtos: ")
            if self.__produtos:
                for p in self.__produtos:
                    self.__tela_produto.mostra({'nome': p.nome, 'codigo': p.codigo, 'preco': p.preco})
            else:
                raise KeyError
        except KeyError:
            self.__tela_produto.mensagem('Não há nenhum produto cadastrado.')
            self.__tela_produto.mensagem('')

    def lista_produtos_compra(self, compra):
        self.__tela_produto.mensagem("Produtos na compra: ")
        for p in compra.produtos:
            self.__tela_produto.mensagem(p.nome)

    def altera_produto(self):
        try:
            self.lista_produtos()
            codigo_produto = self.__tela_produto.seleciona()
            produto = self.pega_produto(codigo_produto)
            if produto:
                novos_dados = self.__tela_produto.pega_dados()
                if self.pega_produto(novos_dados['codigo']) and not self.pega_produto(novos_dados['codigo']) == produto:
                    raise KeyError
                produto.nome = novos_dados['nome']
                produto.codigo = novos_dados['codigo']
                produto.preco = novos_dados['preco']
            else:
                raise KeyError
        except KeyError:
            self.tela_produto.mensagem('Código inválido.')

    def excluir_produto(self):
        self.lista_produtos()
        codigo_produto = self.__tela_produto.seleciona()  # add parametros
        produto = self.pega_produto(codigo_produto)
        try:
            if produto:
                self.__produtos.remove(produto)  # verificar
            else:
                raise KeyError
        except KeyError:
            self.__tela_produto.mensagem('Produto não existente. ')


    def retorna(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_produto, 2: self.altera_produto, 3: self.excluir_produto,
                        4: self.lista_produtos, 0: self.retorna}

        while True:
            lista_opcoes[self.__tela_produto.opcoes()]()
