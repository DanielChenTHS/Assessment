import pygame
from sys import exit

'''
Setting Up Main
'''
class Game:
    def __init__(self):
        # Player setup
        player_sprite = Player((screen_width / 2, screen_height), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.update()
        self.player.draw(screen)
        self.player.draw(screen)

'''
Setting Up Player
'''
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, constraint, speed):
        super().__init__()
        self.image = pygame.image.load("images/player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = speed

        self.max_x_constraint = constraint

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint

    def update(self):
        self.get_input()
        self.constraint()

'''
Setting Up First Rubbish Obstacle
'''
class Rubbish(pygame.sprite.Sprite):

    def __init__(self, x, y, ):
        super().__init__()
        self.image = pygame.image.load("images/Can.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


if __name__ == '__main__':
    pygame.init()
    screen_width = 564
    screen_height = 764
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()
    background = pygame.image.load('images/background.png').convert()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.blit(background, (0, 0))
        game.run()

        pygame.display.flip()
        clock.tick(60)
