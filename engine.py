#  Private Methodes
import copy
import time
import sudoku_configuration as sc
current_row = -1
current_col = -1


def validate_sudoku(tmp_arr):
    row_s = [0] * 9
    col_s = [0] * 9
    rec_s = [0] * 9
    row_m = [1] * 9
    col_m = [1] * 9
    rec_m = [1] * 9
    expected_sum = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9
    expected_mul = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9
    expected_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    is_valid = True
    for i in range(len(tmp_arr)):
        if not (set(tmp_arr[i]) == expected_set):
            is_valid = False
            print("set")
            break
        for j in range(len(tmp_arr)):
            if not (tmp_arr[i][j] in expected_set):
                is_valid = False
                print("range")
                break
            row_s[i] += tmp_arr[i][j]
            row_m[i] *= tmp_arr[i][j]
            col_s[j] += tmp_arr[i][j]
            col_m[j] *= tmp_arr[i][j]
            ind = int(i / 3) * 3 + int(j / 3)
            rec_s[ind] += tmp_arr[i][j]
            rec_m[ind] *= tmp_arr[i][j]
    for i in range(len(row_s)):
        if not (row_s[i] == expected_sum and col_s[i] == expected_sum and rec_s[i] == expected_sum and
                row_m[i] == expected_mul and col_m[i] == expected_mul and rec_m[i] == expected_mul):
            is_valid = False
            break
    if is_valid:
        return True
    else:
        return False


def num_unknowns(in_matrix):
    res = 0
    for i in range(len(in_matrix)):
        res += in_matrix[i].count(0)
    return res


def is_possible(in_matrix, i, j, n):
    # print("Checking possition", i, j, " for ", n)
    return is_possible_on_row(in_matrix, i, n) and is_possible_on_col(in_matrix, j, n) and \
           is_possible_on_rec(in_matrix, i, j, n)


def is_possible_on_row(in_matrix, i, n):
    for k in range(9):
        # print("checking row", i, k, n)
        if in_matrix[i][k] == n:
            return False
    return True


def is_possible_on_col(in_matrix, j, n):
    for k in range(9):
        # print("checking column", k, j, n)
        if in_matrix[k][j] == n:
            return False
    return True


def is_possible_on_rec(in_matrix, i, j, n):
    ind_i = int(i / 3) * 3
    ind_j = int(j / 3) * 3
    for k_i in range(ind_i, ind_i + 3):
        for k_j in range(ind_j, ind_j + 3):
            #  print("checking rec", k_i, k_j, n)
            if in_matrix[k_i][k_j] == n:
                return False
    return True


def print_sudoku(in_matrix, row=-1, col=-1):
    '''
    for row_i in range(9):
        if row_i % 3 == 0:
            print(" ------------------------------------")
        for col_i in range(9):
            if col_i % 3 == 0:
                print(" | ", end="")
            if row_i == row and col_i == col:
                print("<" + str(in_matrix[row_i][col_i]) + ">", end="")
            else:
                if in_matrix[row_i][col_i] == 0:
                    print("   ", end="")
                else:
                    print(" " + str(in_matrix[row_i][col_i]) + " ", end="")
        print("|")
    print(" ------------------------------------")'''
    global current_row
    global current_col
    global matrix_to_show
    current_row = row
    current_col = col
    matrix_to_show = in_matrix
    time.sleep(sc.sleep_time)


def print_ch_mat():
    # time.sleep(2)
    for row_i in range(9):
        for col_i in range(9):
            for j in range(9):
                print(str(ch_mat[row_i][col_i][j]), end="", sep=" | ")
            print(" | ", end="")
        print("\n")


def find_possible_solution():
    possible_solution_x, possible_solution_y = 0, 0
    possible_solution_1, possible_solution_2 = 0, 0
    for row_ind in range(9):
        for col_ind in range(9):
            found_numbrs = 0
            for n_ind in range(9):
                if ch_mat[row_ind][col_ind][n_ind] != 0:
                    found_numbrs += 1
                    if found_numbrs == 1:
                        possible_solution_1 = ch_mat[row_ind][col_ind][n_ind]
                    elif found_numbrs == 2:
                        possible_solution_2 = ch_mat[row_ind][col_ind][n_ind]
                    else:
                        break
            if found_numbrs == 2:
                possible_solution_x = row_ind
                possible_solution_y = col_ind
                #  print_ch_mat(ch_mat)
                return [possible_solution_x, possible_solution_y, possible_solution_1, possible_solution_2]
    return [possible_solution_x, possible_solution_y, possible_solution_1, possible_solution_2]


def main_method(in_mat, indent):
    in_matrix = copy.deepcopy(in_mat)
    indent += 1
    num_x = num_unknowns(in_matrix)
    if num_x == 0:
        #  print("Solution !!!!!!!!")
        print_sudoku(in_matrix)
        return True
    #  in_wos = in_wos_v_hard
    #  Method N 1
    try:
        method_1(in_matrix)
    except:
        #  print("Something wrong happened!!")
        return False
    num_x = num_unknowns(in_matrix)
    if num_x == 0:
        #  print("Solution !!!!!!!!")
        print_sudoku(in_matrix)
        return True

    #  Method N 2
    method_2(in_matrix)
    #  print("Number of unknowns is " + str(num_unknowns) + " Terminate? " + str(no_progress_1 and no_progress_2))
    no_progress = num_x == num_unknowns(in_matrix)
    num_x = num_unknowns(in_matrix)
    if num_x == 0:
        #  print("Solution !!!!!!!!")
        print_sudoku(in_matrix)
        return True
    if no_progress:
        #  print("No PROGRESS")
        fps = find_possible_solution()
        in_matrix[fps[0]][fps[1]] = fps[2]
        #  print(fps[0], fps[1], fps[2])
        #  print_sudoku(in_matrix)
        #  print("Calling First path ...")
        if main_method(in_matrix, indent):
            #  print("First path success")
            return True
        else:
            in_matrix[fps[0]][fps[1]] = fps[3]
            #  print_sudoku(in_matrix)
            #  print("Calling Second path ...")
            if main_method(in_matrix, indent):
                #  print("Second path success")
                return True
            else:
                #  print(fps[0], fps[1], fps[3])
                #  print("Second path FAILED")
                return False
    else:
        return main_method(in_matrix, indent)


def method_1(in_matrix):
    #  Method N 1
    no_progress_1 = False
    num_x = num_unknowns(in_matrix)
    #  print("Running method N 1 " + str(num_x))
    while num_x > 0 and not no_progress_1:
        for row_ind in range(9):
            for col_ind in range(9):
                if in_matrix[row_ind][col_ind] == 0:
                    possible_val_array = []
                    for n_ind in range(1, 10):
                        if is_possible(in_matrix, row_ind, col_ind, n_ind):
                            possible_val_array.append(n_ind)

                    if len(possible_val_array) == 0:
                        #  print("Strange possible_val_array cant be empty!!!")
                        raise("Error!")
                    elif len(possible_val_array) == 1:
                        #  print("Good!!! we found number " + str(possible_val_array[0]) + "'s right possition",
                        #  row_ind, col_ind)
                        in_matrix[row_ind][col_ind] = possible_val_array[0]
                        #  print_sudoku(in_matrix, row_ind, col_ind, num_unknowns(in_matrix))
                        print_sudoku(in_matrix, row_ind, col_ind)
                    #  else:
                    #  print("Could not find a right possition for " + str(n_ind))
        no_progress_1 = num_x == num_unknowns(in_matrix)
        num_x = num_unknowns(in_matrix)
    #  print("Number of unknowns is " + str(num_x))
    #  print_sudoku(in_matrix)
    return in_matrix


def method_2(in_matrix):
    global ch_mat
    ch_mat = sc.ch_mat_or.copy()
    no_progress_2 = False
    num_x = num_unknowns(in_matrix)
    #  print("Running method N 2 " + str(num_x))
    while num_x > 0 and not no_progress_2:
        # preparing relational matrix ch_mat
        #  print("BEFORE Matrix update")
        #  print_ch_mat(ch_mat)
        for row_ind in range(9):
            for col_ind in range(9):
                for n_ind in range(9):
                    #  print(row_ind, col_ind, n_ind, in_wos[row_ind][col_ind], is_possible(row_ind, col_ind, n_ind))
                    if in_matrix[row_ind][col_ind] != 0:
                        ch_mat[row_ind][col_ind][n_ind] = 0
                    else:
                        if not is_possible(in_matrix, row_ind, col_ind, n_ind + 1):
                            ch_mat[row_ind][col_ind][n_ind] = 0
                            # print_ch_mat()
                        else:
                            ch_mat[row_ind][col_ind][n_ind] = n_ind + 1
        #  print_ch_mat()
        #  Improving ch_mat by Rows
        #  print("AFTER Matrix update")
        #  print_ch_mat(ch_mat)
        for n_ind in range(9):
            for i in range(3):
                for j in range(3):
                    ind_i = i * 3
                    ind_j = j * 3
                    t_sum = 0
                    for k_i in range(ind_i, ind_i + 3):
                        for k_j in range(ind_j, ind_j + 3):
                            t_sum += ch_mat[k_i][k_j][n_ind]
                    for k_i in range(ind_i, ind_i + 3):
                        row_sum = 0
                        for k_j in range(ind_j, ind_j + 3):
                            row_sum += ch_mat[k_i][k_j][n_ind]
                        if row_sum == t_sum and row_sum != 0:
                            for k_j in range(9):
                                if (k_j < ind_j) or (k_j >= (ind_j + 3)):
                                    #  print(k_j, ind_j, n_ind)
                                    #  print_ch_mat(ch_mat)
                                    ch_mat[k_i][k_j][n_ind] = 0
        #  print("AFTER matrix improvment")
        #  print_ch_mat(ch_mat)

        #  Improving ch_mat by Cols
        #  print_ch_mat(ch_mat)
        for n_ind in range(9):
            for i in range(3):
                for j in range(3):
                    ind_i = i * 3
                    ind_j = j * 3
                    t_sum = 0
                    for k_j in range(ind_j, ind_j + 3):
                        for k_i in range(ind_i, ind_i + 3):
                            t_sum += ch_mat[k_i][k_j][n_ind]
                    for k_j in range(ind_j, ind_j + 3):
                        row_sum = 0
                        for k_i in range(ind_i, ind_i + 3):
                            row_sum += ch_mat[k_i][k_j][n_ind]
                        if row_sum == t_sum and row_sum != 0:
                            for k_i in range(9):
                                if (k_i < ind_i) or (k_i >= (ind_i + 3)):
                                    #  print(k_j, ind_j, n_ind)
                                    #  print_ch_mat(ch_mat)
                                    ch_mat[k_i][k_j][n_ind] = 0
        #  print("AFTER Matrix update")
        for n_ind in range(9):
            is_found = False
            #  check by rows
            if not is_found:
                for row_ind in range(9):
                    t_sum = 0
                    f_ind = 0
                    for col_ind in range(9):
                        t_sum += ch_mat[row_ind][col_ind][n_ind]
                        if ch_mat[row_ind][col_ind][n_ind] != 0:
                            f_ind = col_ind
                    if t_sum == (n_ind+1):
                        #  print("Woow found a new number with method 2 ROW !!!")
                        #  print("Good!!! we found number " + str(n_ind+1) + "'s right possition",
                        #      row_ind, f_ind)
                        in_matrix[row_ind][f_ind] = n_ind + 1
                        print_sudoku(in_matrix, row_ind, f_ind)
                        #  print_sudoku(in_matrix, row_ind, f_ind, num_unknowns(in_matrix))
                        #  print_ch_mat(ch_mat)
                        row_ind = 9
                        n_ind = 9
                        is_found = True
                        break
            #  check by columns
            if not is_found:
                for col_ind in range(9):
                    t_sum = 0
                    f_ind = 0
                    for row_ind in range(9):
                        t_sum += ch_mat[row_ind][col_ind][n_ind]
                        if ch_mat[row_ind][col_ind][n_ind] != 0:
                            f_ind = row_ind
                            #  print(row_ind, col_ind, ch_mat[row_ind][col_ind][n_ind])
                    if t_sum == (n_ind+1):
                        #  print("Woow found a new numer with method 2 COL !!!", t_sum, )
                        #  print("Good!!! we found number " + str(n_ind+1) + "'s right possition",
                        #      f_ind, col_ind)
                        in_matrix[f_ind][col_ind] = n_ind + 1
                        print_sudoku(in_matrix, f_ind, col_ind)
                        #  print_sudoku(in_matrix, f_ind, col_ind, num_unknowns(in_matrix))
                        #  print_ch_mat(ch_mat)
                        row_ind = 9
                        col_ind = 9
                        n_ind = 9
                        is_found = True
                        break
            #  check by rectangles
            if not is_found:
                for i in range(3):
                    for j in range(3):
                        ind_i = i * 3
                        ind_j = j * 3
                        t_sum = 0
                        f_ind_i = 0
                        f_ind_j = 0
                        for k_i in range(ind_i, ind_i + 3):
                            for k_j in range(ind_j, ind_j + 3):
                                t_sum += ch_mat[k_i][k_j][n_ind]
                                if ch_mat[k_i][k_i][n_ind] != 0:
                                    f_ind_i = k_i
                                    f_ind_j = k_j
                        if t_sum == (n_ind + 1):
                            #  print("Woow found a new numer with method 2 REC !!!")
                            #  print("Good!!! we found number " + str(n_ind + 1) + "'s right possition",
                            #      f_ind_i, f_ind_j)
                            in_matrix[f_ind_i][f_ind_j] = n_ind + 1
                            print_sudoku(in_matrix, f_ind_i, f_ind_j)
                            #  print_sudoku(in_matrix, f_ind_i, f_ind_j, num_unknowns(in_matrix))
                            #  print_ch_mat(ch_mat)
                            i = 4
                            j = 4
                            n_ind = 9
                            is_found = True
                            break
        no_progress_2 = num_x == num_unknowns(in_matrix)
        num_x = num_unknowns(in_matrix)
    return in_matrix

