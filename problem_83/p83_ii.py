# Version 83ii: update code to find smallest path from (0,0) -> (79, 79)
import time
import itertools

t_0 = time.time()

matrix_in = []

with open('p083_matrix.txt', 'r') as rows:
    for row in rows:
        matrix_in.append(list(map(int, row.split(','))))

matrix_test = [matrix_in[y][0:10] for y in range(10)]

class PathSolve():
    def __init__(self, m):
        from copy import deepcopy
        self.matrix = deepcopy(m)
        self.x_domain = len(self.matrix[0])
        self.y_domain = len(self.matrix)
        self.sum_path = deepcopy(m)
        self.direction = [[None] * self.x_domain] * self.y_domain
        self.min_index = {'x': 0, 'y': 0}
        self.max_index = {'x': self.x_domain - 1, 'y': self.y_domain - 1}

    def initial_sweep(self):
        xy_gen = itertools.product(range(self.min_index['x'], self.x_domain), range(self.min_index['y'], self.y_domain))
        next(xy_gen)

        for cell in xy_gen:
            x_i, y_i = cell[0], cell[1]
            if x_i == 0:
                dx = self.sum_path[y_i - 1][x_i]
                self.sum_path[y_i][x_i] += dx
                self.direction[y_i][x_i] = (-1, 0)
                continue
            elif y_i == 0:
                dy = self.sum_path[y_i][x_i - 1]
                self.sum_path[y_i][x_i] += dy
                self.direction[y_i][x_i] = (0, -1)
                continue
            else:
                dx = self.sum_path[y_i][x_i - 1]
                dy = self.sum_path[y_i - 1][x_i]
                if dx <= dy:
                    self.sum_path[y_i][x_i] += dx
                    self.direction[y_i][x_i] = (-1, 0)
                else:
                    self.sum_path[y_i][x_i] += dy
                    self.direction[y_i][x_i] = (0, -1)

    def focused_sweep(self):
        path_changes = 0
        xy_gen = itertools.product(range(self.min_index['x'], self.x_domain), range(self.min_index['y'], self.y_domain))
        next(xy_gen)
        dx_dy = ((1, 0), (0, 1), (-1, 0), (0, -1))
        for cell in xy_gen:
            cell_sum = self.sum_path[cell[1]][cell[0]]
            for move in dx_dy:
                dc = (cell[0] + move[0], cell[1] + move[1])
                if self.min_index['x'] <= dc[0] <= self.max_index['x'] and self.min_index['y'] <= dc[1] <= self.max_index['y']:
                    cell_check = self.sum_path[dc[1]][dc[0]] + self.matrix[cell[1]][cell[0]]
                    if cell_check < cell_sum:
                        self.sum_path[cell[1]][cell[0]] = cell_check
                        self.direction[cell[1]][cell[0]] = move
                        # print("focused sweep updated {} from {} to {}".format(cell, cell_sum, cell_check))
                        path_changes += 1
        return path_changes

    def repeat_sweep(self):
        iteration = 0
        path_changes = -1
        while path_changes != 0:
            path_changes = self.focused_sweep()
            iteration += 1
            print(iteration, path_changes)
        return(self.sum_path)



p_solution = PathSolve(matrix_in)

l_0 = p_solution.x_domain

frmt = "{:>8}"*l_0

p_solution.initial_sweep()

p_solution.repeat_sweep()

for l in p_solution.sum_path:
    print(frmt.format(*l))

print("Run time is:", time.time() - t_0)

"""frmt = "{:>3}"*len(lst)

print(frmt.format(*lst))"""