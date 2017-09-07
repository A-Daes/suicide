import time
import json
from collections import Counter


class Compiler:
	##En ella tendremos los conjuntos generados.

        def __init__(self, name):
                self.compilerName = name
                self.charSets = {}
                self.keywSets = {}
                self.tokenSets ={}
                self.whiteSpace = {}
                self.productionSets = {}

        def setSets(self, setType, setName, setDefinition):
                if setType == "CHARACTERS":
                        self.charSets[setName] = setDefinition
                if setType == "KEYWORDS":
                        self.keywSets[setName] = setDefinition
                if setType == "TOKENS":
                        self.tokenSets[setName] = setDefinition
                if setType == "WHITESPACE":
                        self.whiteSpace[setName] = setDefinition
                if setType == "PRODUCTIONS":
                        self.productionSets[setName]= setDefinition
        def display(self):
                print "Nombre de Compilador: ", self.compilerName
                print "Caracteres: "
                print json.dumps(self.charSets, indent=4)
                print "KeyWords: "
                print json.dumps(self.keywSets, indent=4)
                print "Tokens: "
                print json.dumps(self.tokenSets, indent=4)
                print "White space: "
                print json.dumps(self.whiteSpace, indent=4)
                print "Producciones: "
                print json.dumps(self.productionSets, indent=4)
class Analyze:

        def __init__(self, Compiler):
                self.compiler = Compiler
                self.currentsegment = "N/A"
                self.usedSegments = []


	##inputFile sera lines en main. lines = f.readlines()
        def checkWholeFile(self, inputFile):
                for i in range (0, len(inputFile)):
                        if i == 0:
                                print "Buscando declaracion de compilador"
                                print ("Linea encontrada" + inputFile[i])
                                if inputFile[i].startswith("COMPILER") == False:
                                        raise BaseException("Linea inicial 'compiler' no encontrada. Linea no. '%s'" % (1) )
                                elif len(inputFile[i].split()) < 2:
                                        raise BaseException ("Declaracion de compilador no tiene nombre.")
                                elif len(inputFile[i].split()) > 2:
                                        raise BaseException("Se encontraron elementos extras en declaracion de compilador")
                                else:
                                        self.compiler.compilerName = inputFile[i].split()[-1]

                        elif i == (len(inputFile) -1 ):
                                if inputFile[i].startswith("END") == False:
                                        raise BaseException("Falta linea END al final de archivo, o existe una linea adicional al final del archivo en linea: "+ str(i))
                                elif len(inputFile[i].split()) != 2:
                                        raise BaseException("La linea final tiene mas de dos elementos, o le falta un elemento.")
                                elif (inputFile[i].split())[1] != self.compiler.compilerName:
                                        raise BaseException("El nombre del compilador en la linea END no concuerda con el nombre indicado al inicio, nombre inicial es: '" + self.compiler.compilerName + "' y el nombre final aparece como: '"  + inputFile[i].split()[1] + "'")
                                else:
                                        ##Linea Final correcta
                                        pass
                        else:
                                self.analyzeLine(inputFile[i], str(i))


        def showResults(self):
                self.compiler.display()
                print "Si estas viendo este mensaje, toda la sintaxis esta correcta."

        def analyzeLine(self, inputLine, lineNo):
                line = inputLine.split()
                if len(line) == 1:
                        ## Si solo tiene un elemento, puede que sea comentario o inicio de segmento.
                                if line[0][0] in ["(", ")", "-", "/", "."]:
                                        pass
                                else:
                                        if line[0] in ["CHARACTERS", "PRODUCTIONS", "KEYWORDS", "TOKENS", "WHITESPACE"]:
                                                if line[0] in self.usedSegments:
                                                        ##Evitar que se pueda declarar inicio de seccion dos veces en un archivo.
                                                        raise BaseException("Se detecto inicio de declaracion " + line[0] + " por segunda vez en el archivo en linea: " + lineNo + ". ")
                                                else:
                                        ##Si es una de las declaraciones, poner current como el set indicado, otherwise, no se reconoce.
                                                        self.currentsegment = line[0]
                                                        self.usedSegments.append(line[0])
                                        else:
                                                raise BaseException ("No se reconoce el elemento: " + line[0]  + " En linea: " + lineNo)

                elif len(line) == 0: 
                        ##Linea Vacia
                        pass
                elif len(line) == 4:
                        ## Si contiene cuatro elementos (contando el .), debe ser un set de algo. 
                        if line[1] != "=":
                             ##Si el segundo elemento de la linea NO es un signo =, no se esta ingresando un set correctamente.
                            raise BaseException ("Falta un =, o hay un elemento extra en linea no." + lineNo)
                        elif line[3] != ".":
                            ##Si tiene cuatro elementos pero el ultimo no es un punto, decir que falta el punto.
                            raise BaseException ("Falta un . al final de linea no." + lineNo )
                        else:
                            ##De Lo contrario, es casi seguro que el input este bien.
                                try:
                                            self.compiler.setSets(self.currentsegment, line[0], line[2])
                                except addError:
                                        ##Este error nunca se deberia producir
                                            print("Se produjo un error al agregar al diccionario de '%s'" %(currentsegment))
                else:
                        if line[0][0] in ["(", ")", "-", "/", "."]:
                                ##Si La linea inicia con estos caracteres lo mas probable es que sea comentario, ingorarla
                                pass
                        elif line[0].startswith("END"):
                                raise BaseException("Se encontro la Linea END antes del final del archivo en linea: " + lineNo)
                        else:
                                raise BaseException("No se reconocio la linea - " + str(line) + " - (Linea no,"+lineNo + ") , puede que la sintaxis este incorrecta: \nPosibles Errores: \nFalta algun simbolo (Signo igual, punto al final de linea.)\nHay un elemento de mas en la linea\nEl elemento de la linea simplemente esta mal." )
                        
class fliePrinter:
        ##Clase con recursos para imprimir a nuevo archivo.
        
