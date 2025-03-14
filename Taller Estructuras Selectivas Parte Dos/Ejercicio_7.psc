Algoritmo Ejercicio_7		
	Escribir "Ingrese un número entero: "
	Leer num
	Si num < 2 Entonces
		Escribir "No es primo"
	Sino
		primo <- Verdadero
		Para i <- 2 Hasta Raiz(num) Hacer
			Si num MOD i = 0 Entonces
				primo <- Falso
			FinSi
		FinPara
		Si primo Entonces
			Escribir "Es primo"
		Sino
			Escribir "No es primo"
		FinSi
	FinSi
	
FinAlgoritmo


