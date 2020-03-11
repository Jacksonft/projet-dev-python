import pygame
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))


screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
FPS = 60  # Frames per second.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# RED = (255, 0, 0), GREEN = (0, 255, 0), BLUE = (0, 0, 255).

rect = pygame.Rect((0, 0), (32, 32))
image = pygame.Surface((32, 32))
image .fill(WHITE)

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                rect.move_ip(0, -2)
            elif event.key == pygame.K_s:
                rect.move_ip(0, 2)
            elif event.key == pygame.K_a:
                rect.move_ip(-2, 0)
            elif event.key == pygame.K_d:
                rect.move_ip(2, 0)

    screen.fill(BLACK)
    screen.blit(image, rect)
    pygame.display.update()  # Or pygame.display.flip()
import pygame

# Before you can do much with pygame, you will need to initialize it
pygame.init()
# Init de clock
clock = pygame.time.Clock()

CIEL = 0, 200, 255  # parenthèses inutiles, l'interpréteur reconnaît un tuple

def main():
    fenetre = pygame.display.set_mode((640, 480))

    # loop
    loop = True
    # Création d'une image de la taille de la fenêtre
    background = pygame.Surface(fenetre.get_size())

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        # Superposition du fond ciel
        background.fill(CIEL)
        fenetre.blit(background, (0, 0))

        # Rafraîchissement de l'écran
        pygame.display.flip()
        # By calling Clock.tick(10) once per frame, the program will never run
        # at more than 10 frames per second
        clock.tick(10)

if name == 'main':
    main()