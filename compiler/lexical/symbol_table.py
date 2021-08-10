from compiler.lexical.token import Token

symbol_table = []

#The implementation requires a data strucutre containing tokens for the symbols.
symbol_table.append(Token('inicio', 'inicio', 'NULO'))
symbol_table.append(Token('varinicio', 'varinicio', 'NULO'))
symbol_table.append(Token('varfim', 'varfim', 'NULO'))
symbol_table.append(Token('escreva', 'escreva', 'NULO'))
symbol_table.append(Token('leia', 'leia', 'NULO'))
symbol_table.append(Token('se', 'se', 'NULO'))
symbol_table.append(Token('entao', 'entao', 'NULO'))
symbol_table.append(Token('fimse', 'fimse', 'NULO'))
symbol_table.append(Token('repita', 'repita', 'NULO'))
symbol_table.append(Token('fimrepita', 'fimrepita', 'NULO'))
symbol_table.append(Token('fim', 'fim', 'NULO'))
symbol_table.append(Token('inteiro', 'inteiro', 'inteiro'))
symbol_table.append(Token('literal', 'literal', 'literal'))
symbol_table.append(Token('real', 'real', 'real'))

def is_identifier(value):
    for token in symbol_table:
        if token.lexema == value:
            return token

    return False

