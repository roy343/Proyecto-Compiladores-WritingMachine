import ply.yacc as yacc
import os
import codecs
import re
from lexer import lexicalAnalizer
from sys import stdin

precedence = (

    ('right', 'IGUAL'),
    ('right', 'ASSIGN'),
    ('right','DIFERENTE'),
    ('left','MAYOR','MAYORIGUAL','MENOR','MENORIGUAL'),
    ('left','SUMA','RESTA'),
    ('left','MULTI', 'DIV'),
    ('left', 'LPAREN', 'RPAREN'),
    )


def p_Inicio(p):
    '''
    Inicio : codigo
    '''

def p_Codigo(p):
    '''
    codigo: PARA body FIN
    '''




def p_error(p):
    print("Error de sintaxis "+ str(p)+ " en linea "+ str(p.lineno))

def sibtacticAnalizer(cadena):
    parser = yacc.yacc()
    parser.parse(cadena)






    


