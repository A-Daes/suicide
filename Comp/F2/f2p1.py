#Proyecto fase 2
#Diego Javier Alvarez Cruz
#14104

from Analyze import *

def main():
	print "Iniciando lectura de archivo"
	text_file=open("CocoFile.txt", "r")
	print "Archivo abierto correctamente"
	file2check=text_file.readlines()
	print "Conviertiendo archivo a strings"


	## Crear el objeto 'compilador'. Parte general del proyecto
	compObj = Compiler("Cocofile")
	print "Objeto compilador creado"


	################################################
	 #########Generar el Analyzador - Inicia lab 5 ########
	################################################
	analyzeObj = Analyze(compObj)
	print "Obejto Analizador creado"
	print "Analizando archivo.."
	analyzeObj.checkWholeFile(file2check)
	analyzeObj.showResults()
	##############################################
	 ################Termina lab 5##################
	##############################################

if __name__ == '__main__':

	try:
		main()
	except BaseException as e:
		print e
	except addError as a:
		print a

