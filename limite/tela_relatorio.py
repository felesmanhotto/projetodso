class TelaRelatorio:

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
        print("-----RELATÓRIOS-----")
        print("1 - Criar relatório")
        print("2 - Excluir relatórios")
        print("3 - Listar relatórios")
        print("0 - Retornar")

        return self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 0])

    def mostra(self, dados):
        print("\n")
        print("Mês ", dados['mes'])
        print("Amigo que mais gastou: ", dados['amigo_mais_gastou'].nome)
        print("Valor que gastou: R$", round(dados['valor_gasto']))
        print("Produto mais comprado: ", dados['produto_mais_comprado'].nome)
        print("Frequência do produto: ", dados['frequencia_produto'])
        print("\n")

    def pega_dados(self):
        mes = input("Mês que deseja selecionar: ")
        if int(mes) > 13 or int(mes) < 1:
            raise ValueError
        mes_formatado = mes[-2] + mes[-1]
        return mes_formatado


    def mensagem(self, msg):
        print(msg)

