# Funcion para correr el analizador semantico

def runSemanticAnalizer(parse):
    try:
        inicio(parse[1])
        procedimientos(parse[3])
    except:
        print('error de estructura')


def inicio(body):
    print(body)
    print(1)
    for i in body:
        print(i)
        print('\n')
    print(2)


def procedimientos(body):
    print(body)
