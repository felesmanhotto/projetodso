
class TelaSistema():

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
        print("-----OPÇÕES-----")
        print("1 - Menu de Amigos")
        print("2 - Menu de Eventos")
        print("3 - Menu de Produtos")
        print("4 - Menu de Relatórios")
        print("8 - Encerrar Sistema")

        return self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 4, 8])      # verificar

# UML: NAO HERDA DA TELA ABSTRATA