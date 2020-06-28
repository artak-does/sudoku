import pygame
import sudoku_configuration as sc
import engine

#  Initialization : Drawing UI, seting up threads
def init_gui():
    pygame.init()
    screen = pygame.display.set_mode((sc.ui_width, sc.ui_height))
    pygame.display.set_caption('Sudoku Solver')

    return screen


def update_win(screen):
    screen.fill(sc.ui_white_color)
    for i in range(8):
        lw = sc.ui_line_width
        if (i + 1) % 3 == 0:
            lw *= 2
        pygame.draw.line(screen, sc.ui_black_color, ((i + 1) * sc.ui_width_step, 0),
                         ((i + 1) * sc.ui_width_step, sc.ui_height_step * 9), lw)
        pygame.draw.line(screen, sc.ui_black_color, (0, (i + 1) * sc.ui_height_step),
                         (sc.ui_width_step * 9, (i + 1) * sc.ui_height_step), lw)
    font = pygame.font.SysFont("comicsansms", 72)
    for row_ind in range(9):
        for col_ind in range(9):
            color = sc.ui_blue_color
            if (row_ind == engine.current_row and col_ind == engine.current_col) or engine.num_unknowns(
                    engine.matrix_to_show) == 0:
                color = sc.ui_green_color
            if engine.matrix_to_show[row_ind][col_ind] == 0:
                text = font.render("", True, color)
            else:
                text = font.render(str(engine.matrix_to_show[row_ind][col_ind]), True, color)
            screen.blit(text, [
                ((col_ind * 2 + 1) * sc.ui_width_step - text.get_width()) // 2,
                ((row_ind * 2 + 1) * sc.ui_height_step - text.get_height()) // 2])
    pygame.display.flip()


def final_update(screen, solution, matrix, color_solution, color):
    font = pygame.font.SysFont("comicsansms", 72)
    screen.fill(sc.ui_white_color)
    for i in range(8):
        lw = sc.ui_line_width
        if (i + 1) % 3 == 0:
            lw *= 2
        pygame.draw.line(screen, sc.ui_black_color, ((i + 1) * sc.ui_width_step, 0),
                         ((i + 1) * sc.ui_width_step, sc.ui_height_step * 9), lw)
        pygame.draw.line(screen, sc.ui_black_color, (0, (i + 1) * sc.ui_height_step),
                         (sc.ui_width_step * 9, (i + 1) * sc.ui_height_step), lw)
    for row_ind in range(9):
        for col_ind in range(9):
            if matrix[row_ind][col_ind] != 0:
                text = font.render(str(matrix[row_ind][col_ind]), True, color)
            else:
                text = font.render(str(solution[row_ind][col_ind]), True, color_solution)
            screen.blit(text, [
                ((col_ind * 2 + 1) * sc.ui_width_step - text.get_width()) // 2,
                ((row_ind * 2 + 1) * sc.ui_height_step - text.get_height()) // 2])
    pygame.display.flip()