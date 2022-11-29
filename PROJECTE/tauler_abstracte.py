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
        MENU_PLAY_BUTTON = Button(image=quadre_play, pos=(640, 250), text_input="PLAY", font=main_font, base_color=(255,255,255), hovering_color=(0,0,0))

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

        #DETECTAR OPSICCIO DE RATOLI
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        # "IMATGES" PANTALLA
        ## Fons de pantalla GENERAL
        screen.blit(fons, (0, 0))

        #BOTONS
        ##PLAY
        PLAY_2 = pygame.image.load("IMATGES/PLAY_2.png")
        quadre_play2 = pygame.transform.scale(PLAY_2, (300, 100))
        MENU_PLAY2_BUTTON = Button(image=quadre_play2, pos=(
            640, 250), text_input="PLAY2", font=main_font, base_color=(255, 255, 255), hovering_color=(0, 0, 0))
    
        for button in [MENU_PLAY2_BUTTON]:
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
                    # Canviar de pantalla a play
                    game()
        
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
        MODO_DE_JOC = 20
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
        M_3X3 = [[1, 0, 2], [1, 1, 2], [0, 0, 1]]
        M_4X4 = [[1, 1, 2, 2], [2, 2, 2, 2], [1, 1, 1, 1], [1, 0, 0, 0]]

        n = int(VarX_TABLERO-line_grux)

        X_redimensionada = pygame.transform.scale(X, (n, n))
        O_redimensionada = pygame.transform.scale(O, (n, n))

        mitad_del_gruix = line_grux/2

        Num_fila = 0

        M_4X4 = [[1, 1, 2, 2], [2, 2, 2, 2], [1, 1, 1, 1], [1, 0, 0, 0]]
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


main_menu()
