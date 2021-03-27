import ply.lex as lex
from os import sys

#Inicialización de tokens 

tokens = ['COMA', 'PUNTOCOMA','IGUAL', 'LPAREN', 'RPAREN', #Símbolos exclusivos
          'ID', 'NUMERO',
          'DIFERENTE', 'MAYOR', 'MENOR', 'MAYORIGUAL', 'MENORIGUAL', 'SUMA','RESTA', 'MULTI', 'DIV', 'ASSIGN'] #Operadores

#Inicialización de palabras reservadas

reservadas = {
    'Def':'DEF' , 'Put': 'PUT', 'Add':'ADD', 'ContinueUp':'CONTINUEUP', 'ContinueDown': 'CONTINUEDOWN',
    'ContinuRight': 'CONTINUERIGHT', 'ContinueLeft':'CONTIUELEFT', 'Pos': 'POS',
    'PosX': 'POSX', 'PosY':'POSY', 'UseColor':'USECOLOR', 'Down': 'DOWN', 'Begin':'BEGIN',
    'Speed': 'SPEED', 'Run': 'RUN', 'Repeat': 'REPEAT', 'If':'IF', 'IfElse':'IFELSE',
    'Until':'UNTIL', 'While':'WHILE', 'Equal':'EQUAL', 'And':'AND', 'Or': 'OR',
    'Greater':'GREATER', 'Smaller':'SMALLER', 'Substr':'SUBSTR', 'Random':'RANDOM','Mult':'MULT',
    'Fin': 'FIN', 'Para': 'PARA'
}

#Creación de lista de tokens y palabras reservadas

tokens = list(reservadas.values()) + tokens

#Asignación de simbolos a tokens

t_ignore = ' \t'  #Espacio en blanco

t_COMA = r','
t_PUNTOCOMA = r';'
t_IGUAL = r'='
t_ASSIGN = r'=='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DIFERENTE = r'\!='
t_MAYOR = r'>'
t_MENOR = r'<'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTI = r'\*'
t_DIV = r'\/'

def t_Para(t):
    r'Para'
    t.value = "PARA"
    t.type = t.value
    return t

def t_Fin(t):
    r'fin'
    t.value = "FIN"
    t.type = t.value
    return t


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
    print("Caracter ilegal: Error de sintaxis in line"+ str(t.lexer.lineno)+"'%s'" % t.value[0])       
    #t.lexer.skip(1)
    sys.exit(0)

        

def t_COMMENT(t):
    r'\--.*'
    pass

def lexicalAnalizer(cadena):
    analizador = lex.lex()
    analizador.input(cadena)
    prints=[]
    while True:
        tok = analizador.token()
        if not tok: break
        prints.append(tok)
    return prints



