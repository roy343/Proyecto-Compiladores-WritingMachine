import ply.lex as lex

tokens = [
    'COMA', 'PUNTOCOMA', 'DOSPUNTOS', 'IGUAL', 'PARENTESIS_IZQ', 'PARENTESIS_DER', 'PARENTESISC_IZQ', 'PARENTESISC_DER',  # SIMBOLOS

    'ID', 'NUMERO',  # IDENTIDFICADOR, NUMERO

    'DIFERENTE','SIMILAR', 'MAYOR', 'MENOR', 'MAYORIGUAL', 'MENORIGUAL', # CONDICONES
    
    'SUMA',  'RESTA', 'MULTIPLICA', 'DIVIDE', 'POTENCIA'    
]
                
reservadas = {
    'Def': 'DEF', 'Put': 'PUT' , 'Start': 'START' , 'Add': 'ADD',
    'If': 'IF', 'while': 'WHILE','IfElse': 'IFELSE',
    'EndIf': 'ENDIF', 'Repeat': 'REPEAT', 'Until': 'UNTIL',
    'And': 'AND','Or': 'OR','ContinueRight': 'CONTINUERIGHT',
    'Run': 'RUN', 'Print':'PRINT',
    'End': 'END', 'Fin': 'FIN', 'Para': 'PARA',
    'Random': 'RANDOM',
    'PosX': 'POSX', 'PosY': 'POSY','Pos': 'POS','Speed': 'SPEED',
    'Equal': 'EQUAL','Greater': 'GREATER', 'Smaller': 'SMALLER','Substr': 'SUBSTR',
    'Mult': 'MULT','Power': 'POWER','Div': 'DIV','Sum': 'SUM'
    }
                                                                                
movimientos = {'ContinueUp': 'CONTINUEUP', 'ContinueDown': 'CONTINUEDOWN', 'ContinueLeft': 'CONTINUELEFT',
               'ContinueRight': 'CONTINUERIGHT', 'UseColor': 'USECOLOR', 'Down': 'DOWN','Up': 'UP',
               'Begin': 'BEGIN',
                }

reservadas.update(movimientos)

tokens = list(reservadas.values()) + tokens

t_ignore = '  \t'

t_COMA = r','
t_PUNTOCOMA = r';'
t_DOSPUNTOS = r':'
t_IGUAL = r'='
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_PARENTESISC_IZQ = r'\['
t_PARENTESISC_DER = r'\]'
t_DIFERENTE = r'!='
t_MAYOR = r'>'
t_MENOR = r'<'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_SIMILAR = r'=='
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICA = r'\*'
t_DIVIDE = r'\/'
t_POTENCIA = r'\^'


def t_START(t):
    r'\--.*'
    t.value = "START"
    t.type = t.value
    return t


def t_PARA(t):
    r'Para'
    t.value = "PARA"
    t.type = t.value
    return t


def t_FIN(t):
    r'Fin'
    t.value = "FIN"
    t.type = t.value
    return t




def t_ENDIF(t):
    r'EndIf'
    t.value = "ENDIF"
    t.type = t.value
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_#&@]*'
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
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)


def t_COMMENT(t):
    r'\--.*'
    pass
    # No return value. Token discarded


def lexicalAnalizer(cadena):
    analizador = lex.lex()
    analizador.input(cadena)
    prints = []
    while True:
            
        tok = analizador.token()
        if not tok: break
        prints.append(tok)
    return prints
    



