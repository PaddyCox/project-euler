import itertools

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
        self.min_index = (1, 0)
        self.max_index = (self.x_domain, self.y_domain)

    def cell_solve(self, x, y, x_y_p_n=(1, 1, 1, 1)):
        if min(x, y) < 0:
            return
        if x > self.x_domain or y > self.y_domain:
            return
        current_max = self.sum_path[y][x]
        cell_value = self.matrix[y][x]
        moves = (1, 1, -1, -1)
        change = False
        for r in range(0, 4):
            if x_y_p_n[r]:
                try:
                    new_val = self.sum_path[y + moves[r] * (r % 2)][x + moves[r] * ((r + 1) % 2)] + cell_value
                except IndexError:
                    continue
                if new_val < current_max:
                    self.sum_path[y][x] = new_val
                    self.direction[y][x] = (moves[r] * ((r + 1) % 2), moves[r] * (r % 2))
                    current_max = new_val
                    change = True
        return change

    def sweep_cells(self):
        for x_s in range(1, self.x_domain):
            self.sum_path[0][x_s] += self.sum_path[0][x_s - 1]
            for y_s in range(1, self.y_domain):
                cell_0 = self.sum_path[y_s][x_s]
                option_y = self.sum_path[y_s - 1][x_s]
                option_x = self.sum_path[y_s][x_s - 1]
                self.sum_path[y_s][x_s] = min(option_x, option_y) + cell_0
                self.direction[y_s][x_s] = (- 1 * (option_x >= option_y), -1 * (option_y > option_x))

    def check_adjacent_cells(self, x, y):
        adj_cells_changed = []
        for dx in (-1 * x > 0, 1 * x < self.x_domain - 2):
            if self.cell_solve(x + dx, y):
                adj_cells_changed.append((x + dx, y))
        for dy in (-1 * y > 0, 1 * y < self.y_domain - 2):
            if self.cell_solve(x, y + dy):
                adj_cells_changed.append((x, y + dy))
        return adj_cells_changed

    def all_solve(self, forward=True):
        cells_changed = []
        cell_gen = itertools.product(range(self.min_index[0], self.x_domain), range(self.min_index[1], self.y_domain))
        for cell in cell_gen:
            if self.cell_solve(cell[0], cell[1], x_y_p_n=(1 * forward * (cell[0] < self.x_domain - 1), 1 * forward * (cell[1] < self.y_domain - 1), 1 * (cell[0] > 0), 1 * (cell[1] > 0))):
                cells_changed.append(cell)
        return cells_changed

    def smart_solve(self):
        self.sweep_cells()
        num_changed = 99
        i_changed =[]
        while num_changed > 10:
            i_changed = self.all_solve()
            num_changed = len(i_changed)
            print('while_1', num_changed)
        while num_changed > 0:
            print('while_2', num_changed)
            j_changed = []
            for c in i_changed:
                print(c)
                j_changed += self.check_adjacent_cells(c[0], c[1])
            i_changed = j_changed[:]
            num_changed = len(i_changed)

        return self.sum_path, min((y[self.x_domain - 1] for y in self.sum_path))

sol_a = PathSolve(matrix_in).smart_solve()

print(len(sol_a[0]), len(sol_a[0][1]))
print(sol_a[1])

for l in sol_a[0]:
    print(l)

print('\n')

direction_a = PathSolve(matrix_in)

direction_a.smart_solve()


for j, a in enumerate(direction_a.direction):
    for i, d in enumerate(a):
        if d == (1, 0):
            print(d)
            print(i, j)