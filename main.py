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
    while True:
        screen.fill((0, 0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()
