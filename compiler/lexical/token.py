class Token():
    def __init__(self, classe, lexema, tipo):
        self.classe = classe
        self.lexema = lexema
        self.tipo = tipo

    def __repr__(self) -> str:
        return 'class: ' + self.classe + '\nlexem: ' + self.lexema + '\nType: ' + self.tipo + '\n'
