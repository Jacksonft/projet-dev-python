import pygame

def bouger (vitesse, acceleration):
      vx, vy = vitesse
      ax, ay = acceleration
      vitesse = (vx + ax, vy + ay)
      return vitesse


if __name__ == "__main__":
    pygame.init()

    taille_fenetre=(800,600)
    screen_surface = pygame.display.set_mode(taille_fenetre)

    BLANC    =  (255,255,255)
    BLEUCIEL =  (185,240,240)
    BLEUNUIT =  (5,5,30)
    ROUGE    =  (255,0,0)
    MARRON   =  (145,35,30)
    VERT     =  (0,255,0)
    BLEU     =  (0,0,255)
    JAUNE    =  (255,255,0)





    x = 50
    y = 440
    width = 40
    height = 60
    vel = 5



    isJump = False
    jumpCount = 10

    pygame.image.load("player.png").convert()
#    player_aventurier_surface = surface.set_colorkey(ROUGE)
#    player_rect = player_surface.get_rect(center=(400,300))
    player_vitesse = (0, 0)



    continuer = True
    while continuer:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                      aventurier_vitesse = bouger(player_vitesse, (1, 0))
                elif event.key == pygame.K_LEFT:
                      aventurier_vitesse = bouger(player_vitesse, (-1, 0))
         if not(isJump):
            if keys[pygame.K_UP] and y > vel:
                y -= vel
            if keys[pygame.K_DOWN] and y < 500 - height - vel:
                y += vel
            if keys[pygame.K_SPACE]:
                isJump = True
         else:
            if jumpCount >= -10:
                neg = 1
                if jumpCount < 0:
                    neg = -1
                y -= (jumpCount ** 2) * 0.5 * neg
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 10

         screen.fill(BLACK)
         screen.blit(image, rect)
         pygame.display.update()  # Or pygame.display.flip()




         vx, vy = player_vitesse
         player_rect.left += vx
         player_rect.top  += vy



    pygame.quit()
