class SaldoNegativoException(Exception):
    def __init__(self, amigo):
        self.mensagem = f"O amigo {amigo.nome} não tem saldo suficiente."
        super().__init__(self.mensagem)