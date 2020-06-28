import engine
import pygame
from threading import Thread
from os import path
import sudoku_configuration as sc
import gui


def read_input(input_path):
    global input_array_matrix
    input_array_matrix = []
    if path.exists(input_path):
        if path.isfile(input_path):
            f = open(input_path, "r")
            matrix = []
            for l in f:
                if l == "\n":
                    if matrix == []:
                        break
                    input_array_matrix.append(matrix)
                    matrix = []
                    continue
                arr = list(map(int,l.rstrip().split(",")))
                matrix.append(arr)
            f.close()
        else:
            print("Input Name " + input_path + " is directory. Exiting ...")
            return False
    else:
        print("Input File " + input_path + " does not exsit. Exiting ...")
        return False
    return True


input_array_matrix = []
if not read_input(sc.input_path):
    exit(1)
#  Initialization : Drawing UI, seting up threads
screen = gui.init_gui()
done = False
engine_run = False
index_matrix = 0

#  matrix_to_show is a shared recource between threads
matrix_to_show = input_array_matrix[index_matrix]
#  print(len(input_array_matrix))

while not done and index_matrix < len(input_array_matrix):
    if not engine_run:
        engine.print_sudoku(input_array_matrix[index_matrix])
        t = Thread(target=engine.main_method, args=(input_array_matrix[index_matrix],0,))
        engine_run = True
        t.start()
    if engine.num_unknowns(engine.matrix_to_show) == 0:
        gui.final_update(screen, engine.matrix_to_show, input_array_matrix[index_matrix], sc.ui_green_color, sc.ui_blue_color)
    else:
        gui.update_win(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            t.do_run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and engine.num_unknowns(engine.matrix_to_show) == 0:
            index_matrix += 1
            engine_run = False
            #  print("Cycle ", index_matrix)
            continue
t.join()

