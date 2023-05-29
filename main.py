import pygame
from cellular_automata import *


def render_pygame(field, scr, scale, color_alive, color_dead):
    for y in range(0, len(field)):
        for x in range(0, len(field[0])):
            if field[y][x] == 0:
                pygame.draw.rect(scr, color_dead, (x * scale, y * scale, scale, scale))
            elif field[y][x] == 1:
                pygame.draw.rect(scr, color_alive, (x * scale, y * scale, scale, scale))
            pygame.draw.rect(scr, (0, 0, 0), (x * scale, y * scale, scale, scale), 2)


def count_alive_and_dead_cells(field):
    number_alive_cells = 0
    width = len(field[0])
    height = len(field)
    for y in range(0, height):
        for x in range(0, width):
            if field[y][x] == 1:
                number_alive_cells += 1
    number_dead_cells = height * width - number_alive_cells
    return number_alive_cells, number_dead_cells


def main():
    width = int(input('Введите ширину поля: '))
    height = int(input('Введите длину поля: '))
    life_fraction = int(input('Введите долю живых клеток: '))
    scale = int(input('Введите размер клеток при рисовке: '))

    dict_alive_colors = {'blue': (0, 0, 255), 'red': (255, 0, 0), 'green': (0, 255, 0)}
    dict_dead_colors = {'white': (255, 255, 255), 'violet': (255, 0, 255), 'yellow': (255, 255, 0)}
    list_alive_colors = ['blue', 'red', 'green']
    list_dead_colors = ['white', 'violet', 'yellow']
    current_alive_color_name = 'blue'
    current_dead_color_name = 'white'
    curr_color_alive = dict_alive_colors[current_alive_color_name]
    curr_color_dead = dict_dead_colors[current_dead_color_name]

    gof = GameOfLife(width, height)
    gof.initialize(life_fraction)
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((width * scale + 400, height * scale + 110))
    pygame.display.set_caption('Game Of Life')
    clock = pygame.time.Clock()
    main_font = pygame.font.Font(None, 24)
    iteration_number = 0
    is_running = True
    is_paused = True
    is_iteration_mode = False
    do_iteration = False
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
                elif event.key == pygame.K_ESCAPE:
                    is_running = False
                elif event.key == pygame.K_BACKSPACE:
                    gof = GameOfLife(width, height)
                    gof.initialize(life_fraction)
                    pygame.init()
                    pygame.font.init()
                    screen = pygame.display.set_mode((width * scale + 400, height * scale + 110))
                    iteration_number = 0
                    is_paused = True
                elif event.key == pygame.K_RETURN:
                    if not is_iteration_mode:
                        is_iteration_mode = True
                    else:
                        is_iteration_mode = False
                elif event.key == pygame.K_LEFT:
                    new_color_index = (list_alive_colors.index(current_alive_color_name) + 1) % len(list_alive_colors)
                    current_alive_color_name = list_alive_colors[new_color_index]
                    curr_color_alive = dict_alive_colors[list_alive_colors[new_color_index]]
                elif event.key == pygame.K_RIGHT:
                    new_color_index = (list_dead_colors.index(current_dead_color_name) + 1) % len(list_dead_colors)
                    current_dead_color_name = list_dead_colors[new_color_index]
                    curr_color_dead = dict_dead_colors[list_dead_colors[new_color_index]]

                elif event.key == pygame.K_DOWN:
                    if is_iteration_mode:
                        do_iteration = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_pos = event.pos
                x_pos = cursor_pos[0] // scale
                y_pos = cursor_pos[1] // scale
                if y_pos > len(gof.field) - 1 or x_pos > len(gof.field[0]) - 1:
                    continue
                new_state = gof.field[y_pos][x_pos]
                if event.button == 1:
                    new_state = 1
                elif event.button == 3:
                    new_state = 0
                gof.field[y_pos][x_pos] = new_state
        if not is_paused:
            if is_iteration_mode:
                if do_iteration:
                    do_iteration = False
                else:
                    continue
            iteration_number += 1
            gof.run_transition_rule()
            screen.fill((0, 0, 0))
            render_pygame(gof.field, screen, scale, curr_color_alive, curr_color_dead)
            number_alive_cells, number_dead_cells = count_alive_and_dead_cells(gof.field)
            text_field_size = main_font.render(f'Filed size is {width} by {height} cells', True, (255, 255, 255))
            text_count_life = main_font.render(f'Number of alive cells: {number_alive_cells}', True, (255, 255, 255))
            text_count_dead = main_font.render(f'Number of dead cells: {number_dead_cells}', True, (255, 255, 255))
            text_square_size = main_font.render(f'Count of dead cells: {scale}', True, (255, 255, 255))
            text_alive_color = main_font.render(f'Color of alive cells: {current_alive_color_name}', True,
                                                (255, 255, 255))
            text_dead_color = main_font.render(f'Color of dead cells:  {current_dead_color_name}', True,
                                               (255, 255, 255))
            text_iteration_number = main_font.render(f'Number of iteration: {iteration_number}', True, (255, 255, 255))

            text_title_key = main_font.render(f'KEYBOARD CONTROLS:', True, (255, 255, 255))
            text_exit = main_font.render(f'Exit program: \'ESC\'', True, (255, 255, 255))
            text_pause = main_font.render(f'Pause program: \'SPACE\'', True, (255, 255, 255))
            text_iter_mode = main_font.render(f'Iter mode: \'ENTER\'', True, (255, 255, 255))
            text_iter_action = main_font.render(f'Iter action: \'ARROW_DOWN\'', True, (255, 255, 255))
            text_alive_color_mode = main_font.render(f'Change alive cells color: \'ARROW_LEFT\'', True, (255, 255, 255))
            text_dead_color_mode = main_font.render(f'Change dead cells color: \'ARROW_RIGHT\'', True, (255, 255, 255))

            screen.blit(text_field_size, (10, height * scale + 10))
            screen.blit(text_count_life, (10, height * scale + 35))
            screen.blit(text_count_dead, (10, height * scale + 60))
            screen.blit(text_square_size, (10, height * scale + 85))
            screen.blit(text_alive_color, (350, height * scale + 10))
            screen.blit(text_dead_color, (350, height * scale + 35))
            screen.blit(text_iteration_number, (350, height * scale + 60))

            screen.blit(text_title_key, (width * scale + 10, 10))
            screen.blit(text_exit, (width * scale + 10, 35))
            screen.blit(text_pause, (width * scale + 10, 60))
            screen.blit(text_iter_mode, (width * scale + 10, 85))
            screen.blit(text_iter_action, (width * scale + 10, 110))
            screen.blit(text_alive_color_mode, (width * scale + 10, 135))
            screen.blit(text_dead_color_mode, (width * scale + 10, 160))

            pygame.display.flip()
            clock.tick(60)
            pygame.time.delay(200)


if __name__ == '__main__':
    main()
