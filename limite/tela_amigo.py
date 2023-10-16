from limite.tela_abstrata import TelaAbstrata
from excecao.cpf_invalido import CpfInvalidoException
from excecao.dinheiro_negativo import DinheiroNegativoException

class TelaAmigo(TelaAbstrata):

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
        print("-----AMIGOS-----")
        print("1 - Incluir Amigo")
        print("2 - Alterar Amigo")
        print("3 - Excluir Amigo")
        print("4 - Listar Amigos")
        print("5 - Olhar Carteira")
        print("0 - Retornar")

        return self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 4, 5, 0])     # verificar

    def pega_dados(self):
        print("-----DADOS-----")
        nome = input("Nome: ")
        cpf = input("CPF (apenas digitos): ")

        cpf_validar = [int(char) for char in cpf]
        if len(cpf_validar) != 11:
            raise CpfInvalidoException
        if cpf_validar == cpf_validar[::-1]:
            raise CpfInvalidoException
        for i in range(9, 11):
            valor = sum((cpf_validar[num] * ((i + 1) - num) for num in range(0, i)))
            digito = ((valor * 10) % 11) % 10
            if digito != cpf_validar[i]:
                raise CpfInvalidoException

        dinheiro = float(input("Dinheiro (R$): "))

        if float(dinheiro) < 0:
            raise DinheiroNegativoException

        print("\n")
        return {'nome': nome, 'cpf': cpf, 'dinheiro': dinheiro}

    def mostra(self, dados):
        print("\n")
        print("Nome: ", dados['nome'])
        print("CPF: ", dados['cpf'])
        print("Dinheiro: R$", round(dados['dinheiro'],2))
        print("\n")

    def seleciona(self):
        return input("CPF do amigo a selecionar: ")

    def mensagem(self, msg):
        print(msg)