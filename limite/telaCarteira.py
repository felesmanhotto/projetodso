
class TelaCarteira():

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

    def opcoes(self, amigo):
        print("\n")
        print(f"-----Carteira De {amigo.nome}-----")
        print(f"Dinheiro: R${amigo.carteira.dinheiro}")
        print("1 - Pagar")
        print("2 - Receber")
        print("3 - Verificar dívidas")
        print("0 - Retornar")
        return self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 0])

    def pega_valor(self):
        try:
            return float(input("Digite o valor (R$): "))
        except ValueError:
            self.mensagem("Valor inválido.")

    def pega_cpf_credor(self):
        return input("CPF do credor (Para verificar dívida total, deixe vazio): ")

    def mensagem(self, msg):
        print(msg)