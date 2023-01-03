mode_de_joc = 3
M = [[1,1,1],[1,0,0],[2,0,0]]

def condicio_de_victoria(M,mode_de_joc):
    contador_total = 0                               #iniciem contador en 0
    for i in range(0,len(M)-1):
        for j in range(0,len(M)-1):
            contador_individual = 1                 #sabem que hi ha minim 1 valor igual, inicialitzem en 1
            for k in range(j+1,len(M)-1):             #comprobem les files
                if M[i][k] == M[i][j]:
                    contador_individual += 1

            contador_total = max(contador_individual,contador_total)
            contador_individual = 1

            for l in range(i+1,len(M)-1):             #comprobem les columnes
                if M[l][j] == M[i][j]:
                    contador_individual += 1

            contador_total = max(contador_individual,contador_total)
            
            if i == j:
                contador_individual = 1
                for m in range(i+1,len(M)-1):         #comprobem la diagonal principal
                    if M[m][m] == M[i][j]:
                        contador_individual += 1

                contador_total = max(contador_individual,contador_total)

            if i + j == len(M)-1:
                contador_individual = 1
                for n in range(i+1,len(M)-1):         #comprobem la diagonal secundaria
                    if M[n][len(M)-1-n] == M[i][j]:
                        contador_individual += 1
                contador_total = max(contador_total,contador_individual)
    return contador_total

print(condicio_de_victoria(M,mode_de_joc))
