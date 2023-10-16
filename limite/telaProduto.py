from limite.telaAbstrata import TelaAbstrata
from excecao.dinheiro_negativo import DinheiroNegativoException

class TelaProduto (TelaAbstrata):

    def le_num_inteiro(self, msg='', inteiros_validos=[]):
        while True:
            entrada = input(msg)
            try:
                inteiro = int(entrada)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor inválido")
                print()

    def opcoes(self):
        print("\n")
        print("-------- Opções Produto ----------")
        print("1 - Incluir Produto")
        print("2 - Alterar Produto")
        print("3 - Exclui Produtos")
        print("4 - Lista Produtos")
        print("0 - Retornar")

        return self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 4, 0])

    def pega_dados(self):
        try:
            print("-----DADOS-----")
            nome = input("Nome do produto: ")
            codigo = input("Codigo do produto: ")
            if not codigo:
                raise KeyError
            preco = float(input("Preço do produto (R$): "))
            if preco < 0:
                raise DinheiroNegativoException
            return {'nome': nome, 'codigo': codigo, 'preco': preco}
        except ValueError:
            self.mensagem("Preço inválido.")
        except DinheiroNegativoException as e:
            self.mensagem(e)
        except KeyError:
            self.mensagem("Código não pode ser nulo")

    def mostra(self, dados):
        print("\n")
        print("Nome: ", dados['nome'])
        print("Codigo: ", dados['codigo'])
        print("Preço: R$", round(dados['preco'],2))
        print("\n")

    def seleciona(self):
        return input("Codigo do produto selecionado: ")


    def mensagem(self, msg):
        print(msg)