from limite.telaAbstrata import TelaAbstrata

class TelaCompra(TelaAbstrata):

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
        print("-----AMIGOS-----")
        print("1 - Incluir Amigo")
        print("2 - Alterar Amigo")
        print("3 - Excluir Amigo")
        print("4 - Listar Amigos")
        print("5 - Olhar Carteira")
        print("0 - Retornar")

        return self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 4, 5, 0])

    def pega_dados(self):
        print("-----DADOS-----")
        codigo = input("Código: ")
        cpf_pagante = input("CPF do amigo pagante: ")

        return {'codigo': codigo, 'cpf': cpf_pagante}

    def mostra(self, dados):
        print("Código: ", dados['codigo'])
        print("Pagante: ", dados['pagante'].nome)
        print("Produtos: ", dados['produtos'])
        print("Valor: R$", dados['valor'])
        print("Quitada: ", dados['quitada'])
        print("\n")

    def seleciona(self):
        return input("Código da compra a selecionar: ")     # verificar

    def mensagem(self, msg):
        print(msg)