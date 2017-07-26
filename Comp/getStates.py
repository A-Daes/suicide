def getStates(Automata):
	states = {}
	ctr = 0
	for currentc in Automata(0,len()):
		##Si es parentesis, hacer una cosa, si es or o kleene, hacer otra, de lo contrario, seguir adelante.
		##Caso en el que es PARENTESIS
		if Automata[currentc] == "(":
			#funcion parentesis

		##Caso en el que es OR o KLEENE	
		##Si el siguiente es un or, hacer algo, si es kleene, hacer otra cosa.
		elif (Automata[currentc +1] == "*" or Automata[currentc + 1] == "|"):
			
			#Verificar si esta kleeneado o es parte de un OR
			##Caso en el que es un KLEENE
			if Automata[currentc+1] == "*":
				#Si es kleeneado, tomarlo como un estado y saltar una posicion.
				states[a] = a
				ctr = ctr+1
				currentc = currentc+2

			##Caso en el que es un OR
			elif Automata[currentc +1] == "|":
				
				#Si es parte de un OR, tomarlo como un estado y saltar dos posiciones (excepto si el siguiente es un parentesis o un or o kleene)
				##Caso en el que es un PARENTESIS
				if Automata[currentc+1] == "(":
					#si el siguiente caracer es un parentesis, hacer lo que se debe hacer con parentesis
					#Funcion parentesis
				
				##Caso en el que es un OR o un KLEENE (error)
				elif (Automata[currentc+1] == "*" or Automata[currentc+1] "|"):
					#No tendria sentido que el siguiente sea otro OR o Kleene, entonces ignoramos eso.
					print("Ignoring current character (at pos:" + currentc + "), since it's not valid.")
					#Esto significa que hay un error de redaccion y se ignora.
				
				##Caso en el que es un Caracter Valido
				else: 
					state[ctr] = ctr
					ctr = ctr +1
					currentc = currentc+2


		else:
			states[ctr] = ctr
			ctr = ctr+1
			currentc = currentc+1
	return states





