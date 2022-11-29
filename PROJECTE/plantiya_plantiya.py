while True:
    for event in pygame.event.get():  # Registra tots els "eventos" que passa a la pantalla
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #FPS
    temps.tick(FPS)

    '''
    #Opció tecla premuda
    keys = pygame.key.get_pressed()

    # Control audio
    #Baixar volum
    if keys[pygame.K_F6] and pygame.mixer.music.get_volume() > 0.0:
        pygame.mixer.set_volume(pygame.mixer.music.get_volumen() - 0.01)
        screen.blit(baixar_volum, (500, 250))
    elif keys[pygame.K_F6] and pygame.mixer.music.get_volume() == 0.0:
        screen.blit(no_volum, (500, 250))

    #Pujar volum
    if keys[pygame.K_F7] and pygame.mixer.music.get_volume() < 1.0:
        pygame.mixer.set_volume(pygame.mixer.music.get_volumen() + 0.01)
        screen.blit(baixar_volum, (500, 250))
    elif keys[pygame.K_F7] and pygame.mixer.music.get_volume() == 1.0:
        screen.blit(si_volum, (500, 250))

    #Desactivar volum
    elif keys[pygame.K_F5]:
        pygame.mixer.music.set_volume(0.0)
        screen.blit(no_volum, (k, 250))
        k += 1
        print(k)

    #Activar volum
    elif keys[pygame.K_F8]:
        pygame.mixer.music.set_volume(1.0)
        screen.blit(si_volum, (k, 250))
        k += 1
    '''
    pygame.display.update()  # Actualitzar (repetir comando de adalt)

main_menu()
    