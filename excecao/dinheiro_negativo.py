class DinheiroNegativoException(Exception):
    def __init__(self):
        self.mensagem = "Dinheiro não pode ser negativo"
        super().__init__(self.mensagem)