class Token():
    def __init__(self, classe, lexema, tipo):
        self.classe = classe
        self.lexema = lexema
        self.tipo = tipo

    def __repr__(self) -> str:
        return '\'' + self.lexema + '\'\nclasse: ' + self.classe + ', tipo: ' + self.tipo + '\n'
        # return 'classe: ' + self.classe + ', lexema: ' + self.lexema + ', tipo: ' + self.tipo
