Algoritmo Ejercicio_9
	Escribir "Ingrese una palabra: "
	Leer palabra
	palabraMinuscula <- Minusculas(palabra)  
	palabraReversa <- ""
	
	Para i <- Longitud(palabraMinuscula) Hasta 1 Con Paso -1 Hacer
		palabraReversa <- palabraReversa + Subcadena(palabraMinuscula, i, i)
	FinPara
	
	Si palabraMinuscula = palabraReversa Entonces
		Escribir "Es un pal�ndromo"
	Sino
		Escribir "No es un pal�ndromo"
	FinSi
	
FinAlgoritmo


