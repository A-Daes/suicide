
##Laboratorio #2 Dise;o de Lenguajes de Programacion
##Diego Javier Alvarez 14104
## Base del programa: https://github.com/siddharthasahu/automata-from-regex



from l2libextra import *
import sys


def main(text_file):

    inp = raw_input("Ingrese una expresion regular (Se aceptan + * ()). Los datos se imprimiran directamente a output.txt: ")
    inp = decompressString(inp)
    str2check = raw_input("Ingrese una cadena a verificar en el automata: ")
    
    print >> text_file, "Expresion ingresada: ", inp
    print >> text_file, "Cadena a verificar: " ,str2check
    lang=getSymbols(inp)
    
    nfaObj = NFAfromRegex(inp)
    nfa = nfaObj.getNFA()

    dfaObj = DFAfromNFA(nfa)
    dfa = dfaObj.getDFA()

    minDFA = dfaObj.getMinimisedDFA()

    ##Los metodos Display *FA imprimen, por lo que le pedimos directamente que escriba al texto.    

    nfaObj.displayNFA(text_file)
    print  >> text_file, "\nSimbolos: ", lang
    print >> text_file, "\n La cadena ingresada es Aceptada?: " ,acceptsString(nfa, str2check)

    dfaObj.displayDFA(text_file)

    print >> text_file, "\n La cadena ingresada es Aceptada?: " ,acceptsString(dfa, str2check)

   
    dfaObj.displayMinimisedDFA(text_file)

    print >> text_file, "\n La cadena ingresada es Aceptada?: " ,acceptsString(minDFA, str2check)

    print "Detalles del automata han sido satisfactoriamente escritos a Output.txt"


if __name__  ==  '__main__':

    text_file = open("Output.txt", "a")

    t = time.time()
    cont = 1
    while(cont != "0"):
        try:
            main(text_file)
        
        except BaseException as e:
            print >> text_file, "\nError:", e
            print e
        ##Tiempo de ejecucion para el progama completo    
        print >> text_file, "\nTiempo de Ejecucion: ", time.time() - t, "ms para todo el procedimiento"
        cont = raw_input("Ingrese 0 si desea terminar el programa: ")

    text_file.close()

