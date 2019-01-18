
def two_path_check(dy, x_goal, y_goal, dynamic_matrix, original_matrix):

    different_path_total = []

    y_0 = max(0, y_goal - dy)
    y_1 = min(79, y_goal + dy + 1)

    for y_start in range(y_0, y_1):

        first_square = dynamic_matrix[y_start, x_goal - 1]

        for x_move in range(abs(y_start - y_goal)):
            count = 0
            if x_move


def single_point_check(y_start, y_end, x_start, x_end):


    x_move = abs(y_start - y_end)
    direction = (y_start - y_end)/abs(y_start - y_end)

    for x in range(x_move):
        count = 0

        i = x_start
        j = y_start
        while count < x_move + 1:
            if count = x:
                i += 1
            else:
                j += 1


