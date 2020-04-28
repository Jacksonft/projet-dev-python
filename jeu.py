import pygame

pygame.init()

import random

class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.5
        self.image = pygame.image.load('monster.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 3)

    def damage(self, amount):
        #faire des dégats
        self.health -= amount


        if self.health <= 0:

            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1,3)
            self.health = self.max_health



    def update_health_bar(self, surface):
        # dessiner la barre de vie
        pygame.draw.rect(surface, (234, 27, 13), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (35, 19, 169), [self.rect.x + 10, self.rect.y - 20, self.health, 5])


    def forward(self):
        #colision avec le joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity

        #si le monstre touche le joueur
        else:
        #degats subis par le joeur
            self.game.player.damage(self.attack)



class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        #colision
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            #les dégats
            monster.damage(self.player.attack)

        #supprimer le tire
        if self.rect.x > 1080:
            self.remove()



class Game:

    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
        self.spawn_monster()

    def check_collision(self, sprite , group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask )

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)



#class joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount

    def update_health_bar(self, surface):
        # dessiner la barre de vie
        pygame.draw.rect(surface, (234, 27, 13), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (35, 19, 169), [self.rect.x + 50, self.rect.y + 20, self.health, 7])

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity



#fenetre de jeu
pygame.display.set_caption("jeu")
screen = pygame.display.set_mode((1080, 720))


background = pygame.image.load('bg.jpg')

#joueur
game = Game()

son = pygame.mixer.Sound("slideup.wav")

running = True

#boucle affichage
while running:


    screen.blit(background, (0,-200))

    screen.blit(game.player.image, game.player.rect)

    #actualiser la barre de vie du joueur
    game.player.update_health_bar(screen)


    for projectile in game.player.all_projectiles:
        projectile.move()

    #avancement monstre
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    #image Projectile
    game.player.all_projectiles.draw(screen)

    #image monstres
    game.all_monsters.draw(screen)

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
        son.play()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
        son.play()



    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
