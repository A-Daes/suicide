##Laboratorio #2 Dise;o de Lenguajes de Programacion
##Diego Javier Alvarez 14104



from os import popen
import time

class Automata:
    ##Representa un Automata, incluye estados, inicio, final tabla de transiciones y lenguaje.

    def __init__(self, language = set(['0', '1'])):
        self.states = set()
        self.startstate = None
        self.finalstates = []
        self.transitions = dict()
        self.language = language

    @staticmethod
    ##Definimos el simbolo para epsilon desde adentro.
    def epsilon():
        return ":e:"

    def setstartstate(self, state):
        self.startstate = state
        self.states.add(state)

    ##En Finalstates introducimos los estados a la lista de estados y el final lo asignamos como el de aceptacion.
    def addfinalstates(self, state):
        if isinstance(state, int):
            state = [state]

        for s in state:
            if s not in self.finalstates:
                self.finalstates.append(s)

    ## se crean las transiciones, verificando para cada estado si este se conecta a otro y con que input especifico.
    def addtransition(self, fromstate, tostate, inp):
        if isinstance(inp, str):
            inp = set([inp])

        self.states.add(fromstate)
        self.states.add(tostate)

        if fromstate in self.transitions:
            if tostate in self.transitions[fromstate]:
                self.transitions[fromstate][tostate] = self.transitions[fromstate][tostate].union(inp)

            else:
                self.transitions[fromstate][tostate] = inp

        else:
            self.transitions[fromstate] = {tostate : inp}

    ## Se genera un dicionario de transiciones.
    def addtransition_dict(self, transitions):
        for fromstate, tostates in transitions.items():
            for state in tostates:
                self.addtransition(fromstate, state, tostates[state])

    #Se encuentran los estados de transicion y se agregan a una lista
    def gettransitions(self, state, key):
        if isinstance(state, int):
            state = [state]

        trstates = set()

        for st in state:
            if st in self.transitions:
                for tns in self.transitions[st]:
                    if key in self.transitions[st][tns]:
                        trstates.add(tns)

        return trstates

    ## Se encuentra la cerradura-Epsilon, viendo en cada estado que transiciones tiene utilizando epsilon.
    def getEClose(self, findstate):
        allstates = set()
        states = set([findstate])
        while len(states)!= 0:
            state = states.pop()
            allstates.add(state)

            if state in self.transitions:
                for tns in self.transitions[state]:
                    if Automata.epsilon() in self.transitions[state][tns] and tns not in allstates:
                        states.add(tns)

        return allstates

    ##Funcion para mostrar los atributos del automata generado
    def display(self, f):
        print >> f, "Estados:", self.states
        print >> f, "Inicio: ", self.startstate
        print >> f, "Aceptacion:", self.finalstates
        print >> f, "Transiciones:"

        for fromstate, tostates in self.transitions.items():
            for state in tostates:
                for char in tostates[state]:
                    print >> f, "{  ",fromstate, "->", state, "Utilizando '"+char+"'}\n",
            print

    ##Se encuentra el numero de inicio para reconstruir como AFD
    def newBuildFromNumber(self, startnum):
        translations = {}

        for i in list(self.states):
            translations[i] = startnum
            startnum += 1

        rebuild = Automata(self.language)
        rebuild.setstartstate(translations[self.startstate])
        rebuild.addfinalstates(translations[self.finalstates[0]])

        for fromstate, tostates in self.transitions.items():
            for state in tostates:
                rebuild.addtransition(translations[fromstate], translations[state], tostates[state])

        return [rebuild, startnum]
    
    ##Se reconstruye el automata como AFD usando estados equivalentes.
    def newBuildFromEquivalentStates(self, equivalent, pos):
        rebuild = Automata(self.language)

        for fromstate, tostates in self.transitions.items():
            for state in tostates:
                rebuild.addtransition(pos[fromstate], pos[state], tostates[state])

        rebuild.setstartstate(pos[self.startstate])

        for s in self.finalstates:
            rebuild.addfinalstates(pos[s])

        return rebuild


class BuildAutomata:
    #Crea un Automata (Estructura para cada operacion). Esto sirve para dividir el automata en varios sub-automatas y poder construirlo.

    #Estructura para simbolo independiente. 
    @staticmethod
    def basicstruct(inp):
        state1 = 1
        state2 = 2
        basic = Automata()
        basic.setstartstate(state1)
        basic.addfinalstates(state2)
        basic.addtransition(1, 2, inp)
        return basic

    #Estructura para + (or).
    @staticmethod
    def plusstruct(a, b):
        [a, m1] = a.newBuildFromNumber(2)
        [b, m2] = b.newBuildFromNumber(m1)
        state1 = 1
        state2 = m2
        plus = Automata()
        plus.setstartstate(state1)
        plus.addfinalstates(state2)
        plus.addtransition(plus.startstate, a.startstate, Automata.epsilon())
        plus.addtransition(plus.startstate, b.startstate, Automata.epsilon())
        plus.addtransition(a.finalstates[0], plus.finalstates[0], Automata.epsilon())
        plus.addtransition(b.finalstates[0], plus.finalstates[0], Automata.epsilon())
        plus.addtransition_dict(a.transitions)
        plus.addtransition_dict(b.transitions)
        return plus

    @staticmethod
    ##Estructura para concatenacion (.)
    def dotstruct (a, b):
        [a, m1] = a.newBuildFromNumber(1)
        [b, m2] = b.newBuildFromNumber(m1)
        state1 = 1
        state2 = m2-1
        dot = Automata()
        dot.setstartstate(state1)
        dot.addfinalstates(state2)
        dot.addtransition(a.finalstates[0], b.startstate, Automata.epsilon())
        dot.addtransition_dict(a.transitions)
        dot.addtransition_dict(b.transitions)
        return dot

    ##Estructura para kleene
    @staticmethod
    def starstruct(a):
        [a, m1] = a.newBuildFromNumber(2)
        state1 = 1
        state2 = m1
        star = Automata()
        star.setstartstate(state1)
        star.addfinalstates(state2)
        star.addtransition(star.startstate, a.startstate, Automata.epsilon())
        star.addtransition(star.startstate, star.finalstates[0], Automata.epsilon())
        star.addtransition(a.finalstates[0], star.finalstates[0], Automata.epsilon())
        star.addtransition(a.finalstates[0], a.startstate, Automata.epsilon())
        star.addtransition_dict(a.transitions)
        return star


class DFAfromNFA:
   ##Crea un DFA desde el NFA ya generado.

   ##Al inicializar el DFA, este mismo se crea y se minimiza en un solo paso.
   def __init__(self, nfa):
       self.buildDFA(nfa)
       self.minimise()

   ##Metodos para retornar el dfa original y el minimizado
   def getDFA(self):
       return self.dfa

   def getMinimisedDFA(self):
       return self.minDFA


   ##Metodos para MOSTRAR el dfa original y el minimizadio=
   def displayDFA(self, f):
       self.dfa.display(f)

   def displayMinimisedDFA(self, f):
       self.minDFA.display(f)


    ##Metodo para armar el dfa utilizando el nfa anterior.

   def buildDFA(self, nfa):
       allstates = dict()
       eclose = dict()
       count = 1
       state1 = nfa.getEClose(nfa.startstate)
       eclose[nfa.startstate] = state1
       dfa = Automata(nfa.language)
       dfa.setstartstate(count)
       states = [[state1, count]]

       ##El primer estado es el mismo en ambos automatas
       allstates[count] = state1
       count +=  1

       ##Se hace un while mientras la lista de estados del nfa aun contenga elementos.
       ##El procedimiento es similar a una tabla de transiciones: primero se detecta en cada estado sus transiciones y para ellas detecta si
       #### esta transicion ya existe para otro estado anterior. De ser asi, las juntas dentro de un conjunto de estados nuevos que tienen esa
       #### misa transicion.
       while len(states) != 0:
           [state, fromindex] = states.pop()

           for char in dfa.language:

               trstates = nfa.gettransitions(state, char)
               for s in list(trstates)[:]:
                   if s not in eclose:
                       eclose[s] = nfa.getEClose(s)
                   trstates = trstates.union(eclose[s])

               if len(trstates) != 0:
                   if trstates not in allstates.values():
                       states.append([trstates, count])
                       allstates[count] = trstates
                       toindex = count
                       count +=  1

                   else:
                       toindex = [k for k, v in allstates.iteritems() if v  ==  trstates][0]
                   dfa.addtransition(fromindex, toindex, char)

       for value, state in allstates.iteritems():
           if nfa.finalstates[0] in state:
               dfa.addfinalstates(value)
       self.dfa = dfa

   def acceptsString(self, string):
   ##Se detecta si una string es aceptada en un DFA. Si logra llegar al final en cualquier string, es aceptada.
       currentstate = self.dfa.startstate

       for ch in string:
           if ch==":e:":
               continue
           st = list(self.dfa.gettransitions(currentstate, ch))
           if len(st) == 0:
               accepts = "No"

           currentstate = st[0]

       if currentstate in self.dfa.finalstates:
           accepts = "Si"
       accepts = "No"


   ##Funcion para minimizar el DFA utilizando metodo de 'tablita'. 
   def minimise(self):
       states = list(self.dfa.states)
       n = len(states)
       unchecked = dict() ##Estados aun no verificados (no se sabe si son distinguibles o no)
       count = 1
       distinguished = []
       equivalent = dict(zip(range(len(states)), [{s} for s in states])) ##Estados equivalentes
       pos = dict(zip(states,range(len(states))))

       ##Para cada estado, verificar si las transiciones son distinguibles o no.
       for i in range(n-1):
           for j in range(i+1, n):
               ##Si las transiciones aun no estan marcadas como distinguibles  (ab o ba son iguales en este caso), se verifica la cantidad de transiciones a las que se conecta. Si ambas tienen la misma cantidad
               ## de transiciones, se toma como un posible estado distinguible.
               if not ([states[i], states[j]] in distinguished or [states[j], states[i]] in distinguished):
                   eq = 1
                   toappend = []
                   for char in self.dfa.language:
                       s1 = self.dfa.gettransitions(states[i], char)
                       s2 = self.dfa.gettransitions(states[j], char)
                       if len(s1) != len(s2):
                           eq = 0
                           break
                       
                       if len(s1) > 1:
                           raise BaseException("Se encontraron varias transiciones en el DFA.")
                      
                       elif len(s1) == 0:
                           continue
                     
                       s1 = s1.pop()
                       s2 = s2.pop()

                       ##Si las transiciones son distintas pero una de ellas es distinguible, se agrega a la lista de distinguibles. De lo contrario, se agrega a la lista de posibles y se repite el ciclo para detectar
                       ## otras posibles parejas con el mismo estado A. Si s1 = s2, significa que son equivalentes.
                       if s1 != s2:
                           if [s1, s2] in distinguished or [s2, s1] in distinguished:
                               eq = 0
                               break
                       
                           else:
                               toappend.append([s1, s2, char])
                               eq = -1
                
                   ## Si se paso el 'check' de distincion, se agrega a la lista de distinguibles.
                   if eq == 0:
                       distinguished.append([states[i], states[j]])

                   ## Si no se paso el check, se agrega a la lista de posibles distinciones
                   elif eq == -1:
                       s = [states[i], states[j]]
                       s.extend(toappend)
                       unchecked[count] = s
                       count += 1

                   ## Si se detecto una equivalencia, se agrega a la lista de equivalentes. 
                   else:
                       p1 = pos[states[i]]
                       p2 = pos[states[j]]
                       if p1 != p2:
                           st = equivalent.pop(p2)
                           for s in st:
                               pos[s] = p1
                           equivalent[p1] = equivalent[p1].union(st)
                           
       ##Se asume que hay nuevos estados sin revisar 
       newFound = True

       ##Mientras hayan estados sin revisar, verificar si estos pueden ser distinguibles por transitividady hasta que se acaben. De ser asi, se agregan y se termina el chequeo. De lo contrario se sigue.
       while newFound and len(unchecked) > 0:
           newFound = False
           toremove = set()
         
           for p, pair in unchecked.items():
               for tr in pair[2:]:
                   if [tr[0], tr[1]] in distinguished or [tr[1], tr[0]] in distinguished:
                       unchecked.pop(p)
                       distinguished.append([pair[0], pair[1]])
                       newFound = True
                       break

       ## Se crean los grupos de equivalentes para poder generar el nuevo dfa minimizado.
       for pair in unchecked.values():
           p1 = pos[pair[0]]
           p2 = pos[pair[1]]
          
           if p1 != p2:
               st = equivalent.pop(p2)
               for s in st:
                   pos[s] = p1
               equivalent[p1] = equivalent[p1].union(st)
       
       if len(equivalent) == len(states):
           self.minDFA = self.dfa
       
       else:
           self.minDFA = self.dfa.newBuildFromEquivalentStates(equivalent, pos)

class NFAfromRegex:
    ## Se construye una NFA de una expresion regular
    ## Se definen los simbolos 'reservados'
    def __init__(self, regex):
        self.star = '*'
        self.plus = '+'
        self.dot = '.'
        self.openingBracket = '('
        self.closingBracket = ')'
        self.operators = [self.plus, self.dot]
        self.regex = regex

        ##El alfabeto se define como solamente algunos caracteres en ascii.
        self.alphabet = [chr(i) for i in range(65,91)]
        self.alphabet.extend([chr(i) for i in range(97,123)])
        self.alphabet.extend([chr(i) for i in range(48,58)])
        self.buildNFA()

    def getNFA(self):
        return self.nfa

    def displayNFA(self, f):
        self.nfa.display(f)

    def buildNFA(self):
        language = set()
        self.stack = []
        self.automata = []
        previous = ":e:"
        
        for char in self.regex:
        	##Se agrega al lenguaje cada simbolo que no exista aun, si este no es un operador.
            if char in self.alphabet:
                language.add(char)
                #Si el simbolo anterior no es ningun operador, se agrega el operador punto al stack y aparte se agrega una
                ##estructura basica al automata generado.
                if previous != self.dot and (previous in self.alphabet or previous in [self.closingBracket,self.star]):
                    self.addOperatorToStack(self.dot)
                self.automata.append(BuildAutomata.basicstruct(char))


            ##Si se detecta un parentesis abierto, se agrega el operador punto al stack y ademas se agrega el caracter al stack
            elif char  ==  self.openingBracket:
                if previous != self.dot and (previous in self.alphabet or previous in [self.closingBracket,self.star]):
                    self.addOperatorToStack(self.dot)
                self.stack.append(char)


            ##Si el simbolo es un parentesis cerrando, se verifica que se encuentre despues de un simbolo valido.
            elif char  ==  self.closingBracket:
                if previous in self.operators:
                    raise BaseException("Error al procesar '%s' despues de '%s', no se permiten operadores antes de un parentesis cerrado." % (char, previous))

                ##Mientras hayan elementos en el stack (generado por otro operador), se procesara el operador dentro de este hasta llegar al
                ### parentesis de apertura.
                while(1):
                    if len(self.stack) == 0:
                        raise BaseException("Error al procesar '%s'. El stack esta vacio." % char)
                    o = self.stack.pop()
                    if o == self.openingBracket:
                        break
                    elif o in self.operators:
                        self.processOperator(o)

            ##Si el simbolo es una estrella:
            ####Si el anerior es un operador invalido (estrella, opening bracket, +, .), mostrar error. De lo contrario, se procesa
            #### el caracter como se debe.
            elif char == self.star:
                if previous in self.operators or previous  == self.openingBracket or previous == self.star:
                    raise BaseException("Error al procesar '%s' despues de '%s'. Estos dos operadores no se permiten en secuencia." % (char, previous))
                self.processOperator(char)

            ####Si el caracter es un operador, agregarlo al stack EXCEPTO si el anterior es otro operador o unparentesis de apertura.
            elif char in self.operators:
                if previous in self.operators or previous  == self.openingBracket:
                    raise BaseException("Error al procesar '%s' despues de '%s'. Estos dos operadores no se permiten en secuencia." % (char, previous))
                else:
                    self.addOperatorToStack(char)
            
            ## SI por alguna razon el simbolo no se encuentra dentro de los caracteres aceptados en el rango ascii definido
            #### matar el programa.
            else:
                raise BaseException("Este simbolo no se permite: '%s.'" % char)

            previous = char
        while len(self.stack) != 0:
        ##Mientras el stack tenga contenido, procesarlo.  
            op = self.stack.pop()
            self.processOperator(op)
        if len(self.automata) > 1:
            print self.automata
            raise BaseException("Error al parsear el regex. Revisarlo.")
        self.nfa = self.automata.pop()
        self.nfa.language = language

    def addOperatorToStack(self, char):
        while(1):
        	##Mientras el stack tenga contenido, procesarlo
            if len(self.stack) == 0:
                break
            ##SI el padre es un parentesis abierto, significa que ya termino
            top = self.stack[len(self.stack)-1]
            if top == self.openingBracket:
                break
            #Si el padre es el mismo caracter o un ., quitarlo del stack y procesarlo 
            if top == char or top == self.dot:
                op = self.stack.pop()
                self.processOperator(op)
            else:
                break
        self.stack.append(char)
        ##Si no es el mismo, agregarlo al stack para ser procesado despues.

    def processOperator(self, operator):

    	##Si por alguna razon el stack llegara a estar vacio, ocurrio un error.
        if len(self.automata) == 0:
            raise BaseException("Stack vacio. '%s' no se pudo procesar." % operator)
        ##Si el operador es un kleene, sacarlo del stack y generar una estructura para kleene dentro del automata.
        if operator == self.star:
            a = self.automata.pop()
            self.automata.append(BuildAutomata.starstruct(a))
        ##Si el operador es + o , si el stack tiene menos de dos elementos, ocurrio un error. de lo contrario, se hace el 
        ## proceso de generar una estructura + o . dependiendo del operador detectado.
        elif operator in self.operators:
            if len(self.automata) < 2:
                raise BaseException("%s contiene un operador inadecuado." % operator)
            a = self.automata.pop()
            b = self.automata.pop()
            if operator == self.plus:
                self.automata.append(BuildAutomata.plusstruct(b,a))
            elif operator == self.dot:
                self.automata.append(BuildAutomata.dotstruct(b,a))

## Si el simbolo no esta agregado a la lista de estos, se agrega.
def getSymbols(regex):
        symbols = []
        for x in range(0, (len(regex))):
                if (regex[x] not in {"*", "+", ")", "("}) and (regex[x] not in symbols):
                        symbols.append(regex[x])                                         
                else:
                        pass
        return(symbols)


def acceptsString(automata, string):
    ##Se detecta si una string es aceptada en un DFA. Si logra llegar al final en cualquier string, es aceptada.
       currentstate = automata.startstate

       for ch in string:
           if ch==":e:":
               continue
           st = list(automata.gettransitions(currentstate, ch))
           if len(st) == 0:
               return "No"

           currentstate = st[0]

       if currentstate in automata.finalstates:
           return "Si"
       return "No"

def decompressString(string):
	## Detectamos si se utilizaron expresiones como i-j (i a j)
	newString = ""
	for x in range(0, len(string)-1):
		if x != len(string)-1:
			if string[x+1] == "-":
				a=ord(string[x])
				b=ord(string[x+2])
				for i in range(a, b+1):
					if i != b+1:
						newString+=(str(chr(i)) + "+")
					else:
						newString+=(str(chr(i)))
				x=x+2
			else:
				newString+=string[x]
		print newString
	return newString

