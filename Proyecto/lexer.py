import ply.lex as lex

tokens = ['COMA', 'PUNTOCOMA','IGUAL', 'LPAREN', 'RPAREN',
          'ID', 'NUMERO',
          'DIFERENTE', 'MAYOR', 'MENOR', 'MAYORIGUAL', 'MENORIGUAL', 'SUMA']


reservadas = {
    'DEF':'Def' , 'PUT': 'Put', 'ADD':'Add', 'CONTINUEUP':'ContinueUp', 'CONTINUEDOWN': 'ContinueDown',
    'CONTINUERIGHT': 'ContinueRight', 'CONTIUELEFT':'ContinueLeft', 'POS': 'Pos',
    'POSX': 'PosX', 'POSY':'PosY', 'USECOLOR':'UseColor', 'DOWN': 'Down', 'BEGIN':'Begin',
    'SPEED': 'Speed', 'RUN': 'Run', 'REPEAT': 'Repeat', 'IF':'If', 'IFELSE':'IfElse',
    'UNTIL':'Until', 'WHILE':'While', 'EQUAL':'Equal', 'AND':'And', 'OR': 'Or',
    'GREATER':'Greater', 'SMALLER':'Smaller', 'SUBSTR':'Substr', 'RANDOM':'Random','MULT':'Mult'
}

t_ignore = ' \t'

t_COMA = r','
t_PUNTOCOMA = r';'
t_IGUAL = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DIFERENTE = r'\!='
t_MAYOR = r'>'
t_MENOR = r'<'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'


def t_ID(t):

    r'[a-zA-Z][a-zA-Z0-9_#@]*'
    if t.value.upper() in reservadas.values():
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t
    
def t_error(t):
    print("Caracter ilegal" % t.value[0])
    t.lexer.skip(1)

def t_COMMENT(t):
    r'\#.*'
    pass

def lexicalAnalizer(cadena):
    analizador = lex.lex()
    analizador.input(cadena)
    while True:
        tok = analizador.token()
        if not tok: break
        print(tok)



