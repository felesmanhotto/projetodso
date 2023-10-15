class CpfInvalidoException(Exception):
    def __init__(self):
        self.mensagem = "CPF inválido."
        super().__init__(self.mensagem)