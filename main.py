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
    pygame.font.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Game Of Life')
    clock = pygame.time.Clock()
    main_font = pygame.font.Font(None, 24)
    is_running = True
    is_paused = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if is_paused:
                        is_paused = False
                    else:
                        is_paused = True
                elif event.type == pygame.K_ESCAPE:
                    is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_pos = event.pos
                x_pos = cursor_pos[0] // 15
                y_pos = cursor_pos[1] // 15
                new_state = gof.field[y_pos][x_pos]
                if event.button == 1:
                    new_state = 1
                elif event.button == 3:
                    new_state = 0
                gof.field[y_pos][x_pos] = new_state
        if not is_paused:
            gof.run_transition_rule()
        screen.fill((0, 0, 0))
        render_pygame(gof.field, screen)
        text1 = main_font.render('I love python', True, (255, 255, 255))
        screen.blit(text1, (10, 610))
        pygame.display.flip()
        clock.tick(60)
        pygame.time.delay(200)


if __name__ == '__main__':
    main()
