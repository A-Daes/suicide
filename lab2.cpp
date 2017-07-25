//Prelab 1 Programacion de Microprocesadores
//Diego Javier ALvarez Cruz C14014

#include <iostream>
#include <string>

using namespace std;

//Declaracion de Funciones
int getStates(string cadena1);

int main() {

	return 0;
}



//Funcion para obtener lista de estados
int getStates(const string& cadena1){

	int stts[];
	for(string::size_type i = 0; i < cadena1.size();){
		//si empieza un parentesis ver que tiene adentro y hacer el chequeo para todo lo de adentro
		if (str[i] == "("){
			//Funcion para parentesis
		} 
		else{
			if (str[i]== "*" or str[i]== "|"){
				//error
			}
			//Si el siguiente caracter es una operacion * o |, agregar el estado a la lista pero saltarse el siguiente caracter.
			else if (str[i+1]== "*" || str[i+1]== "|"){
				if (str[i+1] == "*"){
					stts[i] = i;
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
				stts[i] = i
				i++;
			}
		}

	}

}