//Prelab 1 Programacion de Microprocesadores
//Diego Javier ALvarez Cruz C14014

#include <iostream>
#include <string>

using namespace std;

//Declaracion de Funciones
int[] getStates(const string& cadena1);
char[] getSymbols(const string& cadena1);

int main() {

	return 0;
}


//***********************************************
//*****************INCOMPLETO********************
//***********************************************
//Funcion para obtener lista de estados
int[] getStates(const string& cadena1){

	int stts[];
	for(string::size_type i = 0; i < cadena1.size();){
		int a = 0;
		//si empieza un parentesis ver que tiene adentro y hacer el chequeo para todo lo de adentro
		if (str[i] == "("){
			//Funcion para parentesis
		} 
		else{
			if (str[i]== "*" || str[i]== "|"){
				//error
			}
			//Si el siguiente caracter es una operacion * o |, agregar el estado a la lista pero saltarse el siguiente caracter.
			else if (str[i+1]== "*" || str[i+1]== "|"){
				if (str[i+1] == "*"){
					stts[a] = a;
					a++
					i= i+2;
				}
				//Si es un |, verificar que la otra opcion no sea un parentesis, y si lo es, hacer la verificacion del parentesis
				else if (str [i+1] == "|"){
					if(str[i+1] == "("){
						//Funcion para parentesis
					}
					else{
						stts[i] = i;
						i = i+3	
					}
				}
			}
			else{
				stts[a] = a;
				a++
				i++;
			}
		}

	}
return stts[];
}
//***********************************************
//*****************INCOMPLETO********************
//***********************************************

//***********************************************
//*****************INCOMPLETO********************
//***********************************************
//Funcion para obtener todos los simbolos de la expresion
char[] getSymbols(const string& cadena1){
	//Si el caracter es (, ), *, |, epsilon o ya essta en la lista, ir al siguiente caracter
	char symbs[];
	int a = 0;
	for(string::size_type i = 0; i<cadena1.size(); i++){
		if (str[i]== "*" || str[i]== "|"  || str[i] == ")" || str[i] == "(")
		{
		//No hacer nada
		}
		else{
			found = str[i].find(symbs[])
			//Si ya esta el simbolo en la lista, ignorarlo
			if(found!=string::npos){
				//No hacer nada
			}
			else {
				symbs[a] = str[i];
			}
	}
	return char[];
}