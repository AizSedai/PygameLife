import pygame
from cellular_automata import *


def render_pygame(field, scr):
    scale = 15
    for y in range(0, len(field)):
        for x in range(0, len(field[0])):
            if field[y][x] == 0:
                pygame.draw.rect(scr, (255, 255, 255), (x * scale, y * scale, scale, scale))
            elif field[y][x] == 1:
                pygame.draw.rect(scr, (0, 0, 255), (x * scale, y * scale, scale, scale))
            pygame.draw.rect(scr, (0, 0, 0), (x * scale, y * scale, scale, scale), 2)


def main():
    width = int(input('Введите ширину поля: '))
    height = int(input('Введите длину поля: '))
    life_fraction = int(input('Введите долю живых клеток: '))
    gof = GameOfLife(width, height)
    gof.initialize(life_fraction)
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Game Of Life')
    clock = pygame.time.Clock()
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        gof.run_transition_rule()
        screen.fill((0, 0, 0))
        render_pygame(gof.field, screen)
        pygame.display.flip()
        clock.tick(60)
        pygame.time.delay(200)


if __name__ == '__main__':
    main()
