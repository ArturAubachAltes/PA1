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

        # EVENTOS QUE PODEN PASSAR DINS DE MAIN MENU
        ## Registra tots els "eventos" que passa a la pantalla
        for event in pygame.event.get():
            ###Sortir al clicar la X
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #FPS
        temps.tick(FPS)


        # Actualitzar (repetir comando de adalt)
        pygame.display.update()


#-------------------------------------------------------------
#INICIAR AMB "MAIN MENU"

main_menu()
