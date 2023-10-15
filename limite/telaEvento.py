from limite.telaAbstrata import TelaAbstrata

class TelaEvento(TelaAbstrata):

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
        print()
        print("-----EVENTOS-----")
        print("1 - Incluir Evento")
        print("2 - Alterar Evento")
        print("3 - Excluir Evento")
        print("4 - Listar Eventos")
        print("5 - Olhar um Evento")
        print("0 - Retornar")

        return self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 4, 5, 0])      # verificar

    def pega_dados(self):
        print("-----DADOS-----")
        nome = input("Nome: ")
        data = input("Data: ")
        codigo = input("Código: ")

        return {'nome': nome, 'data': data, 'codigo': codigo}

    def mostra(self, dados):
        print()
        print("Nome: ", dados['nome'])
        print("Data: ", dados['data'])
        print("Código: ", dados['codigo'])
        print()

    def seleciona(self):
        return input("Código do evento a selecionar: ")     # verificar

    def mensagem(self, msg):
        print(msg)

    def mostra_um_evento(self, evento):
        print()
        print("Nome: ", evento.nome)
        print("Data: ", evento.data)

        print("Amigos no Evento: ", [amigo.nome for amigo in evento.amigos])
        print("Compras no Evento: ", [f"Compra código {compra.codigo}" for compra in evento.compras])

    def opcoes_um_evento(self):
        print("-----OPÇÕES-----")
        print("1 - Adicionar Amigo")
        print("2 - Adicionar Compra")
        print("3 - Remover Amigo")
        print("4 - Remover Compra")
        print("5 - Quitar Compra")
        print("6 - Quitar Evento")
        print("0 - Retornar")

        return self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 4, 5, 6, 0])  # verificar