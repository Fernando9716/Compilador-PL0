codigopY = " "



class Nodo():
    pass


class Null(Nodo):
    def __init__(self):
        self.type = 'void'

    def imprimir(self, ident):
        print(ident + "nodo nulo")



class program(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)



class block(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):


        if type(self.son1) == type(tuple()):
            print("entro tupla")
            self.son1[0].imprimir("SOY EL IF " + ident)

        else:

            self.son1.imprimir(" " + ident)
            print("Hola")

        if type(self.son2) == type(tuple()):
            # print "entro tupla"
            self.son2[0].imprimir(" " + ident)

        else:

            self.son2.imprimir(" " + ident)


        if type(self.son3) == type(tuple()):

            self.son3[0].imprimir(" " + ident)

        else:

            self.son3.imprimir(" " + ident)


        if type(self.son4) == type(tuple()):

            self.son4[0].imprimir(" " + ident)

        else:

            self.son4.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)


class constDecl(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):

        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)



class constAssignmentList1(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)


class constAssignmentList2(Nodo):
    def __init__(self, son1, son2, son3, son4, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)
        self.son4.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)



class varDecl1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)



class identList1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)


class identList2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)


class procDecl1(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):

        if type(self.son1) == type(tuple()):
            self.son1[0].imprimir(" " + ident)
        else:
            self.son1.imprimir(" " + ident)

        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)


class statement1(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)



class statement2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)



class statement3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)



class statement4(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)



class statement5(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        if type(self.son2) == type(tuple()):
            self.son2[0].imprimir(" " + ident)
        else:
            self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)


class statementList1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)



class statementList2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)



class condition1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)



class condition2(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)




class relation1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)




class relation2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)




class relation3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)




class relation4(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)




class relation5(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)




class relation6(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)




class expression1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)




class expression2(Nodo):
    def __init__(self, son1, son2, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)




class expression3(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)




class addingOperator1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)




class addingOperator2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)




class term1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)




class term2(Nodo):
    def __init__(self, son1, son2, son3, name):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)
        self.son2.imprimir(" " + ident)
        self.son3.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)




class multiplyingOperator1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)




class multiplyingOperator2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)



class factor1(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)



class factor2(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)




class factor3(Nodo):
    def __init__(self, son1, name):
        self.name = name
        self.son1 = son1

    def imprimir(self, ident):
        self.son1.imprimir(" " + ident)

        print(ident + "Nodo: " + self.name)



class Variable(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Variable: " + self.name)




class Asigna(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Asigna: " + self.name)




class Suma(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Suma: " + self.name)




class Resta(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Resta: " + self.name)




class Multiplica(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Multiplica: " + self.name)




class Divide(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Divide: " + self.name)




class Update(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Update: " + self.name)




class Numero(Nodo):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print(ident + "Numbero: " + str(self.name))


