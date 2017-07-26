##Laboratorio #2 Dise;o de Lenguajes de Programacion
##Diego Javier Alvarez 14104


def getStates(Automata):
        states = []
        currentstate = 0
        for x in range(0, (len(Automata)-1)):
                print (x)
                if (Automata[x] not in {")", "*"}):
                        if(Automata[x] == "(") :
                                x= x+1
                                parenthesend = False
                                while (parenthesend == False):
                                        if (Automata[x] != ")" ):
                                                x = x + 1
                                        else:
                                                parenthesend = True
                        elif(Automata[x+1] != "|" ):
                                states.append(currentstate)
                                currentstate=currentstate+1
                        else:
                                x=x+1
                                print("Ignoring value " + str(Automata[x]))

                                
                else:
                        print("Ignoring value " + str(Automata[x]))
                    

        return(states)

def getSymbols(Automata):
        symbols = []
        for x in range(0, (len(Automata)-1)):
                if (Automata[x] not in {"*", "|", ")", "("}) and (Automata[x] not in symbols):
                        symbols.append(Automata[x])
                                         
                else:
                        pass
        return(symbols)


def getStart(Automata):
        x = 0
        currentstate = 0
        slist = []
        end =False
        print (Automata[x:])
        while end == False:
                if (Automata[x+1] != "*"):
                        slist.append(currentstate)
                        currentstate = currentstate + 1
                        end = True
                else:
                        x= x+2
                        slist.append(currentstate)
                        currentstate = currentstate + 1
        return(slist)
                
                
        





Input = input("Ingrese una cadena usando cualquier simbolo. Los Operadores son: | (or), * (kleene) y se aceptan parentesis. Aun no hay funcionalidad para epsilon: ")

sts = getStates(Input)
syms = getSymbols(Input)
start= getStart(Input)
print ("States = {" + str(sts) + "}")
print ("Symbols = {" + str(syms) + "}")
print ("Start = {" + str(start) + "}")



