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
main_font2 = pygame.font.SysFont("cambria", 20)

#Temany taula predeterminat
MODO_DE_TAULA = 3

#Modo de joc predeterminat
MODO_DE_JOC = 3


'''
##Paleta de colors
#blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)

color_1 = (237, 246, 116)
color_2 = (116, 233, 246)
'''

#-------------------------------------------------------------
#BOTO


class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

#-------------------------------------------------------------
#MAIN MENU (retocar boto play)


## Fons de pantalla TITOL
fons_titol = pygame.image.load("IMATGES/FONS_TITOL.png")

## PANTALLA DEL "MAIN MENU"


def main_menu():
    # Nom del "MAIN MENU" (nom del joc)
    pygame.display.set_caption("3 in the line baby")

    #BUCLE GENERAL
    while True:

        #DETECTAR OPSICCIO DE RATOLI
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # "IMATGES" PANTALLA
        ## Fons de pantalla GENERAL
        screen.blit(fons, (0, 0))
        ## Titol
        screen.blit(fons_titol, (0, 0))

        #BOTONS
        ##PLAY
        PLAY = pygame.image.load("IMATGES/PLAY.png")
        quadre_play = pygame.transform.scale(PLAY, (300, 100))
        MENU_PLAY_BUTTON = Button(image=quadre_play, pos=(
            640, 250), text_input="PLAY", font=main_font, base_color=(255, 255, 255), hovering_color=(0, 0, 0))

        for button in [MENU_PLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        # EVENTOS QUE PODEN PASSAR DINS DE MAIN MENU
        ## Registra tots els "eventos" que passa a la pantalla
        for event in pygame.event.get():
            ### Sortir al clicar la X
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            ### AL CLCAR
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si has clicat a play
                if MENU_PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # Canviar de pantalla a play
                    play()

        # FPS
        temps.tick(FPS)

        # Actualitzar (repetir comando de adalt)
        pygame.display.update()

#-------------------------------------------------------------
#PLAY (tot)

## PANTALLA DEL "PLAY"


def play():
    # Nom de la finestra "PLAY"
    pygame.display.set_caption("Play")

    #BUCLE GENERAL
    while True:

        global MODO_DE_TAULA
        global MODO_DE_JOC

        #DETECTAR OPSICCIO DE RATOLI
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        # "IMATGES" PANTALLA
        ## Assersion
        ERROR = main_font2.render("Tipos de joc > Tauler de joc " , True, (155, 155, 155))


        ## Fons de pantalla GENERAL
        screen.blit(fons, (0, 0))

        ## Temany taula
        TEXT_TAULA = main_font2.render("Tauler de joc:  " + str(MODO_DE_TAULA), True, (0, 0, 0))
        screen.blit(TEXT_TAULA, (100, 100))

        ## Modo de joc en pantalla
        TEXT_MODO = main_font2.render("Tipos de joc:  " + str(MODO_DE_JOC), True, (255, 255, 255))
        screen.blit(TEXT_MODO, (500, 100))

        #BOTONS
        ##PLAY
        PLAY_2 = pygame.image.load("IMATGES/PLAY_2.png")
        quadre_play2 = pygame.transform.scale(PLAY_2, (300, 100))
        MENU_PLAY2_BUTTON = Button(image=quadre_play2, pos=(
            640, 250), text_input="PLAY2", font=main_font2, base_color=(255, 255, 255), hovering_color=(0, 0, 0))

        ##
        TAULA_MENYS = Button(image=None, pos=(80, 110),
                             text_input="<", font=main_font2, base_color="White", hovering_color="Green")

        TAULA_MES = Button(image=None, pos=(270, 110),
                           text_input=">", font=main_font2, base_color="White", hovering_color="Green")

        MODO_MENYS = Button(image=None, pos=(460, 110),
                            text_input="<", font=main_font2, base_color="White", hovering_color="Green")

        MODO_MES = Button(image=None, pos=(660, 110),
                          text_input=">", font=main_font2, base_color="White", hovering_color="Green")

        ##gEENERAL
        for button in [MENU_PLAY2_BUTTON, TAULA_MENYS, TAULA_MES, MODO_MENYS, MODO_MES]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(screen)

        # EVENTOS QUE PODEN PASSAR DINS DE MAIN MENU
        ## Registra tots els "eventos" que passa a la pantalla
        for event in pygame.event.get():
            ###Sortir al clicar la X
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                ### AL CLCAR

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si has clicat a play
                if MENU_PLAY2_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    if MODO_DE_JOC > MODO_DE_TAULA:
                        print("error")
                    # Canviar de pantalla a play
                    else:
                        game()

                if TAULA_MENYS.checkForInput(PLAY_MOUSE_POS):
                    if MODO_DE_TAULA > 3:
                        MODO_DE_TAULA -= 1

                if TAULA_MES.checkForInput(PLAY_MOUSE_POS):
                    if 12 > MODO_DE_TAULA:
                        MODO_DE_TAULA += 1

                if MODO_MENYS.checkForInput(PLAY_MOUSE_POS):
                    if MODO_DE_JOC > 2:
                        MODO_DE_JOC -= 1

                if MODO_MES.checkForInput(PLAY_MOUSE_POS):
                    if 12 > MODO_DE_JOC:
                        MODO_DE_JOC += 1
        #FPS
        temps.tick(FPS)

        # Actualitzar (repetir comando de adalt)
        pygame.display.update()


#-------------------------------------------------------------
#GAME (tot)

## PANTALLA DEL "GAME"

def game():
    # Nom del "MAIN MENU" (nom del joc)
    pygame.display.set_caption("GAME")

    #BUCLE GENERAL
    while True:
        global MODO_DE_TAULA
        global MODO_DE_JOC

        #GENERAR MATRIU TABLERO
        MATRIU = [[0] * MODO_DE_TAULA for i in range(MODO_DE_TAULA)]
        
        #DETECTAR OPSICCIO DE RATOLI
        GAME_MOUSE_POS = pygame.mouse.get_pos()

        # "IMATGES" PANTALLA
        ## Fons de pantalla GENERAL
        screen.blit(fons, (0, 0))

        # Rectangele PUNTUACCIO
        ## PUNTUACCIO X
        rect_color_X = (0, 255, 0)

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
        line_color = (0, 0, 0)
        line_grux = 2

        ##LINIES VERTICALS
        VarX_TABLERO = allargada_TABLERO/MODO_DE_TAULA
        pos_y_inicial_L_V = pos_y_inicial_TABLERO

        pos_y_final_L_V = pos_y_inicial_TABLERO+altura_TABLERO

        for i in range(MODO_DE_TAULA-1):
            pos_x_inicial_L_MODIF = pos_x_inicial_TABLERO+VarX_TABLERO*(i+1)
            pygame.draw.line(screen, line_color, (pos_x_inicial_L_MODIF,
                                                  pos_y_inicial_L_V), (pos_x_inicial_L_MODIF, pos_y_final_L_V), line_grux)

        ##LINIES HORITZONTAL

        pos_x_inicial_L_H = pos_x_inicial_TABLERO
        VarY_TABLERO = VarX_TABLERO

        pos_x_final_L_H = pos_x_inicial_TABLERO+allargada_TABLERO

        for i in range(MODO_DE_TAULA-1):
            pos_y_inicial_L_MODIF = pos_y_inicial_TABLERO+VarY_TABLERO*(i+1)
            pygame.draw.line(screen, line_color, (pos_x_inicial_L_H,
                                                  pos_y_inicial_L_MODIF), (pos_x_final_L_H, pos_y_inicial_L_MODIF), line_grux)

        #Marcar tablero
        def Marcar_On_Qui(row, col, player):
            MATRIU[row][col] = player
        
        #Marcar_On_Qui(0,0,1)
        #print(MATRIU)

        
        #DIBUIXAR X i O
        M_3X3 = [[1, 0, 2], [1, 1, 2], [0, 0, 1]]
        M_4X4 = [[1, 1, 2, 2], [2, 2, 2, 2], [1, 1, 1, 1], [1, 0, 0, 0]]

        n = int(VarX_TABLERO-line_grux)

        X_redimensionada = pygame.transform.scale(X, (n, n))
        O_redimensionada = pygame.transform.scale(O, (n, n))

        mitad_del_gruix = line_grux/2

        Num_fila = 0

        for i in M_3X3:
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
                Num_column += 1

            Num_fila += 1

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

                ratX = event.pos[0] #cordenada X al clicar
                ratY = event.pos[1] #cordenades Y al clicar

                if (pos_x_inicial_TABLERO < ratX < pos_x_inicial_TABLERO+allargada_TABLERO) and (pos_y_inicial_TABLERO < ratY < pos_y_inicial_TABLERO+altura_TABLERO):

                    valor_clic_files = int((-pos_x_inicial_TABLERO+ratX)// VarX_TABLERO)
                    valor_clic_columnes = int((-pos_y_inicial_TABLERO+ratY)// VarY_TABLERO)

                    print(valor_clic_files)
                    print(valor_clic_columnes)

                

        # FPS
        temps.tick(FPS)

        # Actualitzar (repetir comando de adalt)
        pygame.display.update()

#-------------------------------------------------------------
#INICIAR AMB "MAIN MENU"


main_menu()
