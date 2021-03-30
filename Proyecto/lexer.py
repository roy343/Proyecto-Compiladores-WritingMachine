import ply.lex as lex

tokens = [
    'COMA', 'PUNTOCOMA', 'DOSPUNTOS', 'LLAVE_IZQ', 'LLAVE_DER', 'IGUAL', 'PARENTESIS_IZQ', 'PARENTESIS_DER',  # SIMBOLOS

    'ID', 'NUMERO',  # IDENTIDFICADOR, NUMERO

    'DIFERENTE', 'MAYOR', 'MENOR', 'MAYORIGUAL', 'MENORIGUAL', 'SUMA'  # CONDICONES
]
                
reservadas = {
    'Def': 'DEF', 'DEFAULT': 'DEFAULT', 'Inicio': 'INICIO',
    'EnCaso': 'ENCASO', 'Cuando': 'CUANDO', 'EnTons': 'ENTONS', 'SiNo': 'SINO',
    'Fin-EnCaso': 'FINENCASO', 'Repita': 'REPITA', 'HastaEncontar': 'HASTAENCONTRAR', 'Desde': 'DESDE',
    'Hasta': 'HASTA', 'Haga': 'HAGA', 'Fin-Desde': 'FINDESDE', 'Fin': 'FIN', 'fin': 'FINPROC', 'inicio': 'INICIOPROC',
    'Inc': 'INC', 'Dec': 'DEC', 'Ini': 'INI', 'Mover': 'MOVER', 'Aleatorio': 'ALEATORIO', 'Proc': 'PROC',
    'Llamar': 'LLAMAR'}
                                                                                
movimientos = {'AF': 'AF', 'F': 'F', 'DFA': 'DFA', 'IFA': 'IFA', 'DFB': 'DFB', 'IFB': 'IFB',
               'A': 'A', 'DAA': 'DAA', 'IAA': 'IAA', 'DAB': 'DAB', 'IAB': 'IAB', 'AA': 'AA'}

reservadas.update(movimientos)

tokens = list(reservadas.values()) + tokens

t_ignore = '  \t'

t_COMA = r','
t_PUNTOCOMA = r';'
t_DOSPUNTOS = r':'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_IGUAL = r'='
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_DIFERENTE = r'<>'
t_MAYOR = r'>'
t_MENOR = r'<'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_SUMA = r'\+'


def t_InicioProc(t):
    r'inicio'
    t.value = "INICIOPROC"
    t.type = t.value
    return t


def t_FinProc(t):
    r'fin'
    t.value = "FINPROC"
    t.type = t.value
    return t


def t_FinDesde(t):
    r'Fin-Desde'
    t.value = "FINDESDE"
    t.type = "FINDESDE"
    return t


def t_FinEnCaso(t):
    r'Fin-EnCaso'
    t.value = "FINENCASO"
    t.type = t.value
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_#@]*'
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
    r'\#.*'
    pass
    # No return value. Token discarded


def lexicalAnalizer(cadena):
    analizador = lex.lex()
    analizador.input(cadena)
    # while True:
    #     tok = analizador.token()
    #     if not tok: break
    #     print(tok)


#def lexicalAnalizer(cadena):
 #   analizador = lex.lex()
  #  analizador.input(cadena)
   # prints=[]
    #while True:
     #   tok = analizador.token()
      #  if not tok: break
       # prints.append(tok)
    #return prints



