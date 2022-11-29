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



X = pygame.image.load("IMATGES/X.png")
X_redimensionada = pygame.transform.scale(X, (30, 30))


while True:
    screen.blit(fons, (0, 0))
    screen.blit(X_redimensionada, (0, 0))
    for event in pygame.event.get():  # Registra tots els "eventos" que passa a la pantalla
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()  # Actualitzar (repetir comando de adalt)

main_menu()
