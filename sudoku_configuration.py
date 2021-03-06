ui_width_step = 80
ui_height_step = 80
ui_width = 724
ui_height = 724
ui_line_width = 2
ui_green_color = (0, 180, 0)
ui_black_color = (0, 0, 0)
ui_blue_color = (0, 0, 128)
ui_white_color = (255, 255, 255)

input_path = "sudoku_input.txt"
sleep_time = 0


ch_mat_or = [
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9],
     [1, 2, 3, 4, 5, 6, 7, 8, 9]]
]


in_ws_old = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
in_wos_old = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
in_wos = [
    [0, 2, 0, 0, 4, 0, 0, 0, 7],
    [0, 5, 1, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 8, 0, 0, 0, 6, 5],
    [7, 0, 4, 0, 0, 0, 5, 8, 0],
    [6, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 0, 0, 0],
    [5, 0, 8, 9, 0, 0, 4, 0, 0],
    [0, 0, 0, 6, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 3, 0]
]  # hard no solution
in_wos_2 = [
    [6, 7, 0, 1, 0, 3, 4, 0, 9],
    [8, 3, 1, 0, 0, 4, 0, 0, 2],
    [0, 4, 0, 0, 8, 0, 3, 1, 0],
    [1, 0, 7, 0, 4, 9, 2, 3, 0],
    [3, 9, 6, 0, 2, 1, 0, 4, 7],
    [2, 0, 4, 3, 0, 0, 0, 9, 1],
    [4, 1, 0, 0, 0, 6, 0, 0, 3],
    [0, 2, 0, 4, 3, 0, 1, 0, 5],
    [0, 6, 3, 0, 1, 0, 9, 0, 4]
]  # hard solution
in_wos_v_hard = [
    [6, 0, 0, 0, 0, 0, 4, 0, 0],
    [0, 0, 1, 0, 0, 4, 0, 0, 2],
    [0, 0, 0, 0, 8, 0, 3, 1, 0],
    [1, 0, 7, 0, 0, 9, 0, 0, 0],
    [3, 0, 0, 0, 2, 0, 0, 4, 7],
    [0, 0, 4, 3, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 6, 0, 0, 3],
    [0, 2, 0, 4, 3, 0, 0, 0, 5],
    [0, 6, 3, 0, 1, 0, 9, 0, 0]
]  # very hard no solution
in_wos_v_hard2 = [
    [0, 0, 9, 0, 0, 0, 0, 4, 0],
    [2, 0, 0, 0, 0, 5, 6, 8, 0],
    [0, 0, 5, 0, 0, 2, 0, 0, 1],
    [0, 0, 0, 0, 6, 0, 9, 0, 0],
    [5, 0, 7, 0, 0, 0, 2, 0, 3],
    [0, 0, 8, 0, 9, 0, 0, 0, 0],
    [3, 0, 0, 4, 0, 0, 1, 0, 0],
    [0, 5, 4, 3, 0, 0, 0, 0, 7],
    [0, 8, 0, 0, 0, 0, 4, 0, 0]
]  # very hard no solution
in_wos_v_hard3 = [
    [4, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 3, 6, 7, 0, 0],
    [7, 0, 0, 0, 0, 0, 1, 9, 0],
    [0, 0, 4, 2, 0, 0, 0, 0, 1],
    [0, 8, 0, 6, 0, 0, 0, 2, 0],
    [9, 6, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 3],
    [0, 0, 0, 0, 8, 0, 2, 0, 0],
    [0, 3, 1, 0, 6, 0, 9, 8, 0]
]  # very hard no solution
in_wos_v_hard4 = [
    [0, 0, 2, 0, 8, 5, 0, 0, 0],
    [5, 9, 0, 0, 3, 4, 6, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 0, 0, 0, 8, 0, 0, 9],
    [0, 1, 0, 0, 0, 0, 0, 7, 6],
    [0, 0, 0, 0, 0, 0, 5, 0, 0],
    [0, 7, 0, 9, 0, 0, 0, 0, 3],
    [3, 0, 0, 8, 0, 0, 2, 6, 0],
    [0, 5, 0, 0, 7, 0, 0, 0, 0]
]  # very hard no solution
