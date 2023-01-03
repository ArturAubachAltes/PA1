
M = [[0,1,1],[2,1,2],[1,2,2]]
mode = 3


def ganador(M,mode):
	for jugador in range(1,2):
		contadorcolumna = 1
		contadorfila = 1
		contadordiagp = 1
		contadordiagn = 1
		for fila in range(mode-1):
			for columna in range(mode-1):
				if M[fila][columna+1] == M[fila][columna] and jugador == M[fila][columna]:
					contadorcolumna +=1 
					if contadorcolumna == mode:
						return jugador 
					
				elif M[fila+1][columna] == M[fila][columna] and jugador == M[fila][columna]:
					contadorfila += 1
					if contadorfila == mode:
						return jugador
					
				elif M[fila+1][columna+1] == M[fila][columna] and jugador == M[fila][columna]:
					contadordiagp += 1
					if contadordiagp == mode:
						return jugador
					
				elif M[fila][len(M)-1-columna] == M[fila+1][len(M)-2-columna] and jugador == M[fila][len(M)-1-columna]:
					contadordiagn += 1
					if contadordiagn == mode:
						return jugador
	return 0				
						
print(ganador(M,mode))
					
				
				
				
				
	
