import ply.yacc as yacc
import os
import codecs
import re
from analizadorLexico import tokens
from sys import stdin
#from AnalizadorSemantico import *
from AnalizadorSemantico import *

#DICCIONARIO CON LA PRIORIDAD Y PRECEDENCIA DE LOS TOKENS
precedencia = (
    ('rigth', 'VARIABLE','CALL','BEGIN','IF','WHILE'),
    ('rigth','PROCEDURE'),
    ('rigth','VAR'),
    ('rigth', 'ASIGNA'),
    ('rigth', 'UPDATE'),
    ('left','SUMA','RESTA'),
    ('left','MULTIPLICA', 'DIVIDE'),
    ('left','IMPAR')
    )

#funciones Produccion
def p_program(p):
    '''program : block'''
    #print("program")
    p[0] = program(p[1],"program")


def p_block(p):
    '''block : constDecl varDecl procDecl statement'''
    p[0] = block(p[1],p[2],p[3],p[4],"block")
    #print("block")

def p_constDecl(p):
    '''constDecl : CONST constAssignmentList PUNTO_Y_COMA'''
    p[0] = constDecl(p[2],"constDecl")
    #print("constDecl")



def p_constDeclEmpty(p):
    ''' constDecl : empty'''
    p[0] = Null()
    #print("declaracion de constantes vacia")


def p_constAssignmentList1(p):
    '''constAssignmentList : VARIABLE ASIGNA NUMERO'''
    p[0] = constAssignmentList1(Variable(p[1]),Asigna(p[2]),Numero(p[3]),"constAssigmentList")
    #print("constAssignmentList1")


def p_constAssignmentList2(p):
    '''constAssignmentList : constAssignmentList COMA VARIABLE ASIGNA NUMERO'''
    p[0] = constAssignmentList2(p[1],Variable(p[3]),Asigna(p[4]),Numero(p[5]),"constAssignmentList2")
    #print("constAssignmentList2")


def p_varDecl1(p):
    '''varDecl : VAR identList PUNTO_Y_COMA'''
    p[0] = varDecl1(p[2],"Vardecl1")
    #print("varDecl 1")


def p_varDeclEmpty(p):
    '''varDecl : empty'''
    p[0] = Null()
    #print("Declaracion de variables vacia :(")


def p_identList1(p):
    '''identList : VARIABLE'''
    p[0] = identList1(Variable(p[1]),"identList1")
    #print("identList 1")


def p_identList2(p):
     '''identList : identList COMA VARIABLE'''
     p[0] = identList2(p[1],Variable(p[3]),"identList2")
    #print("identList 2")


def p_procDecl1(p):
    '''procDecl : procDecl PROCEDURE VARIABLE PUNTO_Y_COMA block PUNTO_Y_COMA'''
    p[0] = procDecl1(p[1],Variable(p[3]),p[5],"procDecl")
    #print("procDecl 1")

def p_procEmpty(p):
    '''procDecl : empty'''
    p[0] = Null()
    #print("procDecl nulo")

def p_statement1(p):
    '''statement : VARIABLE UPDATE expression'''
    p[0] = statement1(Variable(p[1]),Update(p[2]),p[3],"statement1")
    #print("statement 1")

def p_statement2 (p):
    '''statement : CALL VARIABLE'''
    p[0] = statement2(Variable(p[2]),"statement2")
    #print("statement 2")


def p_statement3 (p):
    '''statement : BEGIN statementList END'''
    p[0] = statement3(p[2],"statement3")
    #print("statement 3")

def p_statement4(p):
    '''statement : IF condition THEN statement'''
    p[0]= statement4(p[2],p[4],"statement4")
    #print("statement 4")


def p_statement5(p):
    '''statement : WHILE condition DO statement'''
    p[0] = statement5(p[2],p[4],"statement5")
    #print("statement 5")


def p_statementEmpty(p):
    '''statement : empty'''
    p[0] = Null()
    #print("statement nulo")


def p_statementList1(p):
    '''statementList : statement'''
    p[0] = statementList1(p[1],"statementList1")
    #print("statementList 1")


def p_statementList2(p):
    '''statementList : statementList PUNTO_Y_COMA statement'''
    p[0] = statementList2(p[1],p[3],"statementList2")
    #print("statementList 2")


def p_condition1(p):
    '''condition : IMPAR expression'''
    p[0] = condition1(p[2],"condition1")
    #print("condition 1")


def p_condition2(p):
    '''condition : expression relation expression'''
    p[0] = condition2(p[1],p[2],p[3],"condition2")
    #print("condition 2")


def p_relation1(p):
    '''relation : ASIGNA'''
    p[0] = relation1(Asigna(p[1]),"relation1")
    #print("relation 1")


def p_expression1(p):
    '''expression : term'''
    p[0] = expression1(p[1],"expression1")
    #print("expression 1")


def p_expression2(p):
    '''expression : addingOperator term'''
    p[0] = expression2(p[1],p[2],"expression2")
    #print("expression 2")


def p_expression3(p):
    '''expression : expression addingOperator term'''
    p[0] = expression3(p[1],p[2],p[3],"expression")
    #print("epxression 3")


def p_addingOperator1(p):
    '''addingOperator : SUMA'''
    p[0] = addingOperator1(Suma(p[1]),"addingOperator1")
    #print("operador suma +")


def p_addingOperator2(p):
    '''addingOperator : RESTA'''
    p[0] = addingOperator2(Resta(p[1]),"addingOperator2")
    #print("operador resta -")


def p_term1(p):
    '''term : factor'''
    p[0] = term1(p[1],"term1")
    #print("term 1")

def p_term2(p):
    '''term : term multiplyingOperator factor'''
    p[0] = term2(p[1],p[2],p[3],"term2")
    #print("term 2")


def p_multiplyingOperator1(p):
    '''multiplyingOperator : MULTIPLICA'''
    p[0] = multiplyingOperator1(Multiplica(p[1]),"multiplyingOperator1")
    #print("Operador multiplicacion")


def p_multiplyingOperator2(p):
    '''multiplyingOperator : DIVIDE'''
    p[0] = multiplyingOperator2(Divide(p[1]),"multiplyingOperator2")
    #print("Operador Divicion")


def p_factor1(p):
    '''factor : VARIABLE'''
    p[0] = factor1(Variable(p[1]),"factor1")
    #print("factor 1")
          #+str(p.lineno))


def p_factor2(p):
    '''factor : NUMERO'''
    p[0] = factor2(Numero(p[1]),"factor2")
    #print("factor 1")



def p_empty(p):
    '''empty :'''
    pass


def p_error(p):
    print("error de sintaxis cerca de", p)
    #print("error en la linea"+str(p.lineno))


def buscarCode(directorio):
    ficheros =[]
    numArchivo = ''
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

directorio = '/Users/fernando/documents/analizador 1/tst/'
archivo = buscarCode(directorio)
tst = directorio+archivo
fp = codecs.open(tst,"r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)

result.imprimir(" ")


#archivo.write(result.imprimir())
#archivo.close()

print(result)