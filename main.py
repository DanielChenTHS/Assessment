import pygame
from sys import exit
from player import Player


class Game:
    def __init__(self):
        # Player setup
        player_sprite = Player((screen_width / 2, screen_height), screen_width, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.update()
        self.player.draw(screen)
        self.player.draw(screen)


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
