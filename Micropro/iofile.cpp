//Ejercicio Practico IStream
//Diego Javier Alvarez Cruz 14104

#include <iostream>
#include <fstream>
using namespace std;

int main(){
	char tx2a[256];
	
	cout << "Ingrese el nombre del archivo a analizar: ";
	cin.get (tx2a, 256);

	ifstream is(tx2a);

	cout << "Posicion En Memoria	||	Caracter\n";
	char c;
	int * val;
	while(is.get(c)){
		val = (int*)&c;
		cout << oct << val << "	||	" << c << "\n";
}
	is.close();

	return 0;
}
