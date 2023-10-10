from limite.telaAbstrata import TelaAbstrata

class TelaEvento(TelaAbstrata):

    def opcoes(self):
        print("-----EVENTOS-----")
        print("1 - Incluir Evento")
        print("2 - Alterar Evento")
        print("3 - Excluir Evento")
        print("4 - Listar Eventos")
        print("5 - Olhar um Evento")
        print("0 - Retornar")

        return int(input("Escolha a opção: "))      # verificar

    def pega_dados(self):
        print("-----DADOS-----")
        nome = input("Nome: ")
        data = input("Data: ")
        codigo = input("Código: ")          # verificar

        return {'nome': nome, 'data': data, 'codigo': codigo}

    def mostra(self, dados):
        print("Nome: ", dados['nome'])
        print("Data: ", dados['data'])
        print("Código: ", dados['codigo'])
        print("\n")

    def seleciona(self):
        return input("Código do evento a selecionar: ")     # verificar

    def mensagem(self, msg):
        print(msg)

    def mostra_um_evento(self, evento):
        print("Nome: ", evento.nome)
        print("Data: ", evento.data)
        print("Amigos no Evento: ", evento.amigos)
        print("Compras no Evento: ", evento.compras)        # listar mostrando as infos

    def opcoes_um_evento(self):
        print("-----OPÇÕES-----")
        print("1 - Adicionar Amigo")
        print("2 - Adicionar Compra")
        print("3 - Remover Amigo")
        print("4 - Remover Compra")
        print("5 - Quitar Evento")
        print("0 - Retornar")

        return int(input("Escolha a opção: "))  # verificar