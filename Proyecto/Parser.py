import ply.yacc as yacc
import os
import codecs
from pip._vendor.distlib.compat import raw_input
from lexer import tokens
from lexer import lexicalAnalizer
from Semantic import runSemanticAnalizer
import random

from sys import stdin


def p_Start(p):
    '''
    Start : code
    '''
    # runSemanticAnalizer(p[1])

def p_Code(p):
    '''
    code : START DOSPUNTOS cuerpo END PUNTOCOMA procedimiento
    '''
    p[0] = (p[3], p[6])
    #print(p[3])
    


def p_cuerpo(p):
    '''
    cuerpo : variable
           | expresion
           
           
            
    '''
    p[0] = p[1]


def p_Variable(p):
    '''
    variable : variable1 cuerpo
            | variable2 cuerpo
            | variable3 cuerpo
            | variable4 cuerpo
            | empty empty
    '''
    if (p[2] != '$'):
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]


def p_Variable1(p):
    '''
    variable1 : DEF ID PUNTOCOMA
    '''
    p[0] = (p[1], p[2])
    print(p[1], p[2])


def p_Variable2(p):
    '''
    variable2 : DEF ID IGUAL NUMERO PUNTOCOMA
              
    '''
    p[0] = (p[1], p[2], p[3], p[4])
    print(p[2], p[3], p[4])


def p_Variable3(p):
    '''
    variable3 : PUT ID IGUAL NUMERO PUNTOCOMA
              
    '''
    p[0] = (p[1], p[2], p[3], p[4])
    print(p[2], p[3], p[4])

def p_Variable4(p):
    '''
    variable4 : PUT ID IGUAL expresion_alge1 PUNTOCOMA
              | PUT ID IGUAL expresion_alge2 PUNTOCOMA
              
    '''
    p[0] = (p[1], p[2], p[3], p[4])
    print(p[2], p[3], p[4])

    



def p_expresion(p):
    '''
    expresion : NUMERO
              | funcion expresion
              | condicion expresion
              | expresion_alge1 expresion
              | expresion_alge2 expresion
              | Sum expresion
              | Substr expresion
              | Mult expresion
              | Div expresion
              | Power expresion
              | empty empty
                        
    '''

    if (p[2] != '$'):
        p[0] = (p[1], p[2])
    else:
        p[0] = p[1]
        

def p_funcion(p):
    '''
    funcion : Random
            | Begin
            | ContinueUp
            | ContinueDown
            | ContinueRight
            | ContinueLeft
            | Up
            | Down
            | Speed
            | Pos
            | PosX
            | PosY
            
            
            
    '''
    p[0] = p[1]


def p_condicion(p):
    '''
    condicion : Equal expresion
              | Greater expresion
              | Smaller expresion
              | Igual expresion
              | Diferente expresion
              | Mayor expresion
              | Menor expresion
              | Mayorigual expresion
              | Menorigual expresion 

    '''
    


def expresion_alge(p):
    '''
    expresion_alge : expresion_alge1
                   | expresion_alge2
                   
                   | 
    '''
    

    

def p_expresion_alge1(p):

    '''
    expresion_alge1 : NUMERO SUMA NUMERO 
                   | NUMERO RESTA NUMERO 
                   | NUMERO MULTIPLICA NUMERO 
                   | NUMERO DIVIDE NUMERO
                   | NUMERO POTENCIA NUMERO
                   
    '''

    if p[2] == '+' : p[0] = p[1]+p[3]
    elif p[2] == '-' : p[0] = p[1]-p[3]
    elif p[2] == '*' : p[0] = p[1]*p[3]
    elif p[2] == '/' : p[0] = p[1]/p[3]
    elif p[2] == '^' : p[0] = p[1]**p[3]

    print(p[0])

def p_expresion_alge2(p):

    '''
    expresion_alge2 : PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER SUMA PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER
                   | PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER RESTA PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER
                   | PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER MULTIPLICA PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER
                   | PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER DIVIDE PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER
                   | PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER POTENCIA PARENTESIS_IZQ expresion_alge1 PARENTESIS_DER
                   
    '''

    if p[4] == '+' : p[0] = p[2]+p[6]
    elif p[4] == '-' : p[0] = p[2]-p[6]
    elif p[4] == '*' : p[0] = p[2]*p[6]
    elif p[4] == '/' : p[0] = p[2]/p[6]
    elif p[4] == '^' : p[0] = p[2]**p[6]
    

def p_Sum(p):
    '''
    Sum : SUM PARENTESIS_IZQ NUMERO COMA NUMERO PARENTESIS_DER
        | SUM PARENTESIS_IZQ expresion_alge1 COMA expresion_alge1 PARENTESIS_DER
        | SUM PARENTESIS_IZQ NUMERO COMA ID PARENTESIS_DER
    '''

    p[0] = p[3] + p[5]
    print(p[0])

def p_Substr(p):
    '''
    Substr : SUBSTR PARENTESIS_IZQ NUMERO COMA NUMERO PARENTESIS_DER
    '''

    p[0] = p[3] - p[5]
    print(p[0])

def p_Mult(p):
    '''
    Mult : MULT PARENTESIS_IZQ NUMERO COMA NUMERO PARENTESIS_DER
    '''

    p[0] = p[3] * p[5]
    print(p[0])

def p_Div(p):
    '''
    Div : DIV PARENTESIS_IZQ NUMERO COMA NUMERO PARENTESIS_DER
    '''

    p[0] = p[3] / p[5]
    print(p[0])

def p_Power(p):
    '''
    Power  : POWER PARENTESIS_IZQ NUMERO COMA NUMERO PARENTESIS_DER
    '''

    p[0] = p[3] ** p[5]
    print(p[0])



def p_Equal(p):
    '''
    Equal : EQUAL PARENTESIS_IZQ NUMERO COMA NUMERO PARENTESIS_DER PUNTOCOMA
    '''

    if p[3] == p[5]:
        p[0] = True
    else:
        p[0] = False

    print(p[0])

def p_Greater(p):
    '''
    Greater : GREATER PARENTESIS_IZQ NUMERO COMA NUMERO PARENTESIS_DER PUNTOCOMA
    '''
    
    if p[3] > p[5]:
        p[0] = True
    else:
        p[0] = False

    print(p[0])


def p_Smaller(p):
    '''
    Smaller : SMALLER PARENTESIS_IZQ NUMERO COMA NUMERO PARENTESIS_DER PUNTOCOMA
    '''
    
    if p[3] < p[5]:
        p[0] = True
    else:
        p[0] = False

    print(p[0])



#def p_And(p):


#def p_Or(p):


def p_Igual(p):
    '''
    Igual : NUMERO SIMILAR NUMERO
          | ID SIMILAR ID
          | NUMERO SIMILAR ID
          | ID SIMILAR NUMERO
    '''

    if p[1] == p[3]:
        p[0] = True
    else:
        p[0] = False

    print(p[0])


def p_Diferente(p):
    '''
    Diferente : NUMERO DIFERENTE NUMERO
          | ID DIFERENTE ID
          | NUMERO DIFERENTE ID
          | ID DIFERENTE NUMERO
    '''

    if p[1] != p[3]:
        p[0] = True
    else:
        p[0] = False

    print(p[0])


def p_Mayor(p):
    '''
    Mayor : NUMERO MAYOR NUMERO
          | ID MAYOR ID
          | NUMERO MAYOR ID
          | ID MAYOR NUMERO
    '''

    if p[1] > p[3]:
        p[0] = True
    else:
        p[0] = False

    print(p[0])

def p_Menor(p):
    '''
    Menor : NUMERO MENOR NUMERO
          | ID MENOR ID
          | NUMERO MENOR ID
          | ID MENOR NUMERO
    '''

    if p[1] < p[3]:
        p[0] = True
    else:
        p[0] = False

    print(p[0])

def p_Mayorigual (p):
    '''
    Mayorigual  : NUMERO MAYORIGUAL NUMERO
          | ID MAYORIGUAL ID
          | NUMERO MAYORIGUAL ID
          | ID MAYORIGUAL NUMERO
    '''

    if p[1] >= p[3]:
        p[0] = True
    else:
        p[0] = False

    print(p[0])

def p_Menorigual (p):
    '''
    Menorigual  : NUMERO MENORIGUAL NUMERO
          | ID MENORIGUAL ID
          | NUMERO MENORIGUAL ID
          | ID MENORIGUAL NUMERO
    '''

    if p[1] <= p[3]:
        p[0] = True
    else:
        p[0] = False

    print(p[0])
    

def p_procedimiento(p):
    
    '''
        procedimiento : PROC ID PARENTESIS_IZQ parametro PARENTESIS_DER PARA  PUNTOCOMA procedimiento
                     | empty empty empty empty empty empty empty empty empty empty empty
    '''
    if p[11] != '$':
        p[0] = (p[1], p[2], p[4], p[6], p[8], p[9], p[11])
    elif p[11] == '$' and p[1] != '$':
        p[0] = (p[1], p[2], p[4], p[6], p[8], p[9])
    else:
        p[0] = p[1]


def p_parametro(p):
    '''
    parametro : ID COMA parametro
              | ID empty empty
              | NUMERO COMA parametro
              | NUMERO empty empty
              | empty empty empty

    '''
    if p[3] != '$' and p[2] != '$':
        p[0] = (p[1], p[3])
    else:
        p[0] = p[1]

def p_begin(p):
    '''
    Begin : BEGIN PUNTOCOMA
    '''
    p[0] = p[1]
    print("Begin")

def p_random(p):
    '''
    Random : RANDOM PARENTESIS_IZQ NUMERO PARENTESIS_DER PUNTOCOMA'''
    
    p[0] = random.randrange(p[3])
    print(p[0])


def p_ContinueUp(p):
    '''
    ContinueUp : CONTINUEUP NUMERO PUNTOCOMA
    '''

    p[0] = p[2]
    print("ContinueUp " + str(p[2]))

def p_ContinueDown(p):
    '''
    ContinueDown : CONTINUEDOWN NUMERO PUNTOCOMA
    '''

    p[0] = p[2]
    print("ContinueDown " + str(p[2]))

def p_ContinueRight(p):
    '''
    ContinueRight : CONTINUERIGHT NUMERO PUNTOCOMA
    '''

    p[0] = p[2]
    print("ContinueRight " + str(p[2]))

def p_ContinueLeft(p):
    '''
    ContinueLeft : CONTINUELEFT NUMERO PUNTOCOMA
    '''

    p[0] = p[2]
    print("ContinueLeft " + str(p[2]))


def p_Up(p):
    '''
    Up : UP PUNTOCOMA
    '''

    p[0] = p[1]
    print(p[0])

def p_Down(p):
    '''
    Down : DOWN PUNTOCOMA
    '''

    p[0] = p[1]
    print(p[0])

def p_Speed(p):
    '''
    Speed : SPEED NUMERO PUNTOCOMA
    '''

    p[0] = p[2]
    print("Velocidad = " + str(p[2]))

def p_Pos(p):
    '''
    Pos : POS PARENTESIS_IZQ NUMERO COMA NUMERO PARENTESIS_DER PUNTOCOMA
    '''

    p[0] = (p[3],p[5])
    print ("Coordenada X = "+ str(p[3]))
    print("Coordenada Y = "+ str(p[5]))

def p_PosX(p):
    
    '''
    PosX : POSX  NUMERO  PUNTOCOMA
    '''

    p[0] = p[2]
    print ("Coordenada X = "+ str(p[2]))
 

def p_PosY(p):
    
    '''
    PosY : POSY  NUMERO  PUNTOCOMA
    '''

    p[0] = p[2]
    print ("Coordenada Y = "+ str(p[2]))
 

def p_empty(p):
    '''
    empty :
    '''
    p[0] = '$'


def p_error(p):
    print("error de sintaxis " + str(p))
    print("error en la linea " + str(p.lineno))


def sintacticAnalizer(cadena):
    parser = yacc.yacc()
    parser.parse(cadena)


#################################### tester ############################################

def buscarFichero(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1
    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)
    for file in files:
        print(str(cont) + ". " + file)
        cont += 1
    while respuesta == False:
        numArchivo = raw_input('\n')
        for file in files:
            if file == files[int(numArchivo) - 1]:
                respuesta = True
                break
    return files[int(numArchivo) - 1]


#def test():
    # directorio = os.path.dirname(os.getcwd()) + "/Tests/"
    # archivo = buscarFichero(directorio)
    # test = directorio + archivo


 #   fp = codecs.open('C:/Users/Familia/Documents/Gabo/Lenguajes y Compi/Compi/Proyecto/Prueba.txt', "r", "utf-8")
  #  cadena = fp.read()
   # fp.close()

 #   lexicalAnalizer(cadena)
  #  sintacticAnalizer(cadena)

# documentar esta funcion si va a probar codigo en el GUI
#\Users\Familia\Documents\Gabo\Lenguajes y Compi\Copia\Tests/test2
#test()

    


