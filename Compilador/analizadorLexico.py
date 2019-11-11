import ply.lex as lex
import re
import codecs
import os
import sys

reservadas = ['BEGIN','END','IF','THEN','WHILE','DO','CALL','CONST',
              'VAR','PROCEDURE']

tokens = reservadas+['VARIABLE','NUMERO','SUMA','RESTA','MULTIPLICA','DIVIDE',
                     'IMPAR','ASIGNA','COMA','PUNTO_Y_COMA','UPDATE','COMENTARIO']



#Reglas de Expresiones Regulares

t_ignore = '\t '
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICA = r'\*'
t_DIVIDE = r'/'
t_IMPAR = r'%'
t_ASIGNA = r'='
t_COMA = r','
t_PUNTO_Y_COMA = r';'
t_UPDATE = r':='

#Funciones
#


def t_VARIABLE(x):
    r'[a-zA-Z_][a-zA-Z0-9_]*' #Lenguaje regular la variable puede empezar por una minuscula, mayuscula o guion bajo
    if x.value.upper() in reservadas:
        x.value = x.value.upper()
        x.type = x.value

    return x


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_COMENTARIO(t):
    r'\#.*'
    pass


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_error(t):
    print("caracter ilegal'%s'" % t.value[0])
    t.lexer.skip(1)


def buscarCode(directorio):
    ficheros =[]
    numArchivo = ""
    respuesta = False
    cont=1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print (str(cont)+"."+file)
        cont = cont+1

    while respuesta==False:
        numArchivo = input('\nNumero de la prueba')
        for file in files:
            if file == files[int(numArchivo)-1]:
                respuesta=True
                break
    print("Has escogido \"%s\" \n" % files[int(numArchivo) - 1])

    return files[int(numArchivo) - 1]

"""directorio = '/Users/fernando/documents/analizador 1/tst/'
archivo = buscarCode(directorio)
tst = directorio+archivo
fp = codecs.open(tst,"r","utf-8")
cadena = fp.read()
fp.close()"""

analizador = lex.lex()
"""analizador.input(cadena)

while True:
   tok = analizador.token()
   if not tok: break
   print (tok)
   print("\n")"""


