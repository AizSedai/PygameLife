import pygame
from cellular_automata import *


def render_field(field):
    for y in range(0, len(field)):
        for x in range(0, len(field[0])):
            if field[y][x] == 0:
                print(' ', end='')
            elif field[y][x] == 1:
                print('X', end='')
        print()
    print('-----------------------------')


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Game Of Life')
    clock = pygame.time.Clock()
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        screen.fill((0, 0, 0))
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
