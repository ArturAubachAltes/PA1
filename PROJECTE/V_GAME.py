#Inici
import pygame
import sys
pygame.init()

#-------------------------------------------------------------
#GENERAL

## Crear finestra
SCREEN_X = 800
SCREEN_Y = 450

size = (SCREEN_X, SCREEN_Y)
screen = pygame.display.set_mode(size)

## Fons de pantalla general
fons = pygame.image.load("IMATGES/FONS.png")

## FPS
FPS = 60  # FPS
temps = pygame.time.Clock()

## Icono
icono = pygame.image.load("IMATGES/ICONO.png")
pygame.display.set_icon(icono)

## Jugadores
O = pygame.image.load("IMATGES/O.png")
X = pygame.image.load("IMATGES/X.png")

# FONTS DE LLETRES
main_font = pygame.font.SysFont("cambria", 50)

#-------------------------------------------------------------
#MAIN MENU (retocar boto play)

## Fons de pantalla TITOL
fons_titol = pygame.image.load("IMATGES/FONS_TITOL.png")

## PANTALLA DEL "MAIN MENU"
def GAME():
    # Nom del "MAIN MENU" (nom del joc)
    pygame.display.set_caption("GAME")

    #BUCLE GENERAL
    while True:

        #DETECTAR OPSICCIO DE RATOLI
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # "IMATGES" PANTALLA
        ## Fons de pantalla GENERAL
        screen.blit(fons, (0, 0))

        # Rectangele PUNTUACCIO
        ## PUNTUACCIO X
        rect_color_X = (0,255,0)

        pos_x_inicial_X = (SCREEN_X/14)
        pos_y_inicial_X = (SCREEN_Y/7)*2

        allargada_X = (SCREEN_X/14)*2
        altura_X = (SCREEN_Y/7)*3

        pygame.draw.rect(screen, rect_color_X, (pos_x_inicial_X,
                         pos_y_inicial_X, allargada_X, altura_X))

        ## PUNTUACCIO O
        rect_color_O = (0, 255, 0)

        pos_x_inicial_O = SCREEN_X-allargada_X-pos_x_inicial_X
        pos_y_inicial_O = pos_y_inicial_X

        allargada_O = allargada_X
        altura_O = altura_X

        pygame.draw.rect(screen, rect_color_O, (pos_x_inicial_O,
                         pos_y_inicial_O, allargada_O, altura_O))

        ## TABLERO

        rect_color_TABLERO = (150, 150, 150)

        allargada_TABLERO = 350
        altura_TABLERO = 350

        pos_x_inicial_TABLERO = (SCREEN_X-allargada_TABLERO)/2
        pos_y_inicial_TABLERO = (SCREEN_Y-altura_TABLERO)/2


        #pygame.draw.rect(screen, rect_color_TABLERO, (pos_x_inicial_TABLERO, pos_y_inicial_TABLERO, allargada_TABLERO, altura_TABLERO))

        ###
        #QUADRICULA
        MODO_DE_JOC = 4
        line_color = (0, 0, 0)
        line_grux = 7

        ##LINIES VERTICALS
        VarX_TABLERO = allargada_TABLERO/MODO_DE_JOC
        pos_y_inicial_L_V = pos_y_inicial_TABLERO

        pos_y_final_L_V = pos_y_inicial_TABLERO+altura_TABLERO

        for i in range(MODO_DE_JOC-1):
            pos_x_inicial_L_MODIF = pos_x_inicial_TABLERO+VarX_TABLERO*(i+1)
            pygame.draw.line(screen, line_color, (pos_x_inicial_L_MODIF,
                            pos_y_inicial_L_V), (pos_x_inicial_L_MODIF, pos_y_final_L_V), line_grux)

        ##LINIES HORITZONTAL

        pos_x_inicial_L_H = pos_x_inicial_TABLERO
        VarY_TABLERO = VarX_TABLERO

        pos_x_final_L_H = pos_x_inicial_TABLERO+allargada_TABLERO

        for i in range(MODO_DE_JOC-1):
            pos_y_inicial_L_MODIF = pos_y_inicial_TABLERO+VarY_TABLERO*(i+1)
            pygame.draw.line(screen, line_color, (pos_x_inicial_L_H,
                            pos_y_inicial_L_MODIF), (pos_x_final_L_H, pos_y_inicial_L_MODIF), line_grux)


        #DIBUIXAR X i O
        M_3X3 = [[1,0,2],[1,1,2],[0,0,1]]
        M_4X4 = [[1, 1, 2, 2], [2, 2, 2, 2], [1, 1, 1, 1], [1, 0, 0, 0]]

        n = int(VarX_TABLERO-line_grux)

        X_redimensionada = pygame.transform.scale(X, (n, n))
        O_redimensionada = pygame.transform.scale(O, (n, n))
        
        mitad_del_gruix = line_grux/2

        Num_fila = 0

        for i in M_4X4:
            CORDENADES_X_per_peca_MOD = pos_x_inicial_TABLERO+VarX_TABLERO*Num_fila
            Num_column = 0

            for j in i:
                CORDENADES_y_per_peca_MOD = pos_y_inicial_TABLERO+VarY_TABLERO*Num_column
                if j == 1:
                    screen.blit(
                        X_redimensionada, (CORDENADES_X_per_peca_MOD+mitad_del_gruix, CORDENADES_y_per_peca_MOD+mitad_del_gruix))
                elif j == 2:
                    screen.blit(
                        O_redimensionada, (CORDENADES_X_per_peca_MOD+mitad_del_gruix, CORDENADES_y_per_peca_MOD+mitad_del_gruix))
                Num_column +=1
            
            Num_fila +=1



        


        '''
        #RAYAA !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        line_color=(0,0,0)

        pos_x_inicial_L = 400
        pos_y_inicial_L = 0

        pos_x_final_L = 400
        pos_y_final_L = 450

        line_grux = 15

        pygame.draw.line(screen, line_color, (pos_x_inicial_L,
                         pos_y_inicial_L), (pos_x_final_L, pos_y_final_L), line_grux)
       
        '''
        # EVENTOS QUE PODEN PASSAR DINS DE MAIN MENU
        ## Registra tots els "eventos" que passa a la pantalla
        for event in pygame.event.get():
            ### Sortir al clicar la X
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            ### AL CLCAR
            if event.type == pygame.MOUSEBUTTONDOWN:
                '''
                # Si has clicat a play
                if MENU_PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # Canviar de pantalla a play
                    play()
                '''

        # FPS
        temps.tick(FPS)

        # Actualitzar (repetir comando de adalt)
        pygame.display.update()

#-------------------------------------------------------------
#INICIAR AMB "MAIN MENU"

GAME()
