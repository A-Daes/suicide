//Ejercicio Practico IStream
//Diego Javier Alvarez Cruz 14104

#include <iostream>
#include <fstream>


int main(){
	char tx2a[256];
	
	std::cout << "Ingrese el nombre del archivo a analizar: ";
	std::cin.get (tx2a, 256);

	std::ifstream is(tx2a);

	std::cout << "Posicion En Memoria	||	Caracter\n";
	char c;
	int * val;
	while(is.get(c)){
		val = (int*)&c;
		std::cout << val;
		std::cout  <<  "	||	" << c << "\n";
}
	is.close();

	return 0;
}
