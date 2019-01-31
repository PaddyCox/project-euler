# Approach: Iterate over each 0 and replace with possible values based
#           simple row/column/square elimination

import re
import itertools



"""with open('p096_sudoku.txt', 'r') as text:
    sudoku_i = []
    count = 0
    for line in text.readlines():
        if 'Grid' in line:
            count = 0
        else:
            sudoku_i.append(line.strip().split())
        print(line, 'l')
        word_list = re.sub('"', '', words.read()).split(',')"""


with open('p096_sudoku.txt', 'r') as text:
    sudokus = [[list(map(int, l)) for l in text.read().splitlines() if l.isdigit()][9 * i: 9 * i + 9] for i in range(50)]



class SodokuSolve:
    def __init__(self, s_puzzle):
        self.s_puzzle = s_puzzle
        self.unknown_tiles = []

    def s_print(self):
        print(*self.s_puzzle, sep='\n')
        print('\n')

    def simple_solve(self):
        count = 999
        while count != 0:
            count = 0
            count_solved = 0
            count_not_solved = 0
            for coord in itertools.product(range(0, 9), repeat=2):
                x = coord[0]
                y = coord[1]
                if self.s_puzzle[y][x] == 0 or type(self.s_puzzle[y][x]) is list:
                    count_not_solved += 1
                    self.unknown_tiles.append((x, y))
                    if self.s_puzzle[y][x]:
                        possible = self.s_puzzle[y][x]
                    else:
                        possible = list(range(1, 10))
                    for p in possible[:]:
                        if p in self.s_puzzle[y]:
                            count_solved += 1
                            possible.remove(p)
                        elif [self.s_puzzle[j][x] for j in range(9) if self.s_puzzle[j][x] == p]:
                            count_solved += 1
                            possible.remove(p)
                        elif [self.s_puzzle[y - (y % 3) + j][x - (x % 3) + i] for i in range(3) for j in range(3)
                                                        if self.s_puzzle[y - (y % 3) + j][x - (x % 3) + i] == p]:
                            count_solved += 1
                            possible.remove(p)

                    if len(possible) == 1:
                        count_solved += 1
                        self.s_puzzle[y][x] = possible[0]
                        self.unknown_tiles.remove((x, y))
                    else:
                        count += 1
                        self.s_puzzle[y][x] = possible

        if count_not_solved > 0:
            return False
        else:
            return True


    def second_solve(self, t):
        t_y = t[1]
        t_x = t[0]
        t_options = self.s_puzzle[t[1]][t[0]]
        # create sets to store possible values of unknown cells in t column, row and local square
        oc_set = set()
        or_set = set()
        ol_set = set()
        # iterate over other unknown cells and populate cells
        for ot in self.unknown_tiles:
            if ot[1] == t_y:
                oc_set |= set(self.s_puzzle[ot[1]][ot[0]])
            elif ot[0] == t_x:
                or_set |= set(self.s_puzzle[ot[1]][ot[0]])
            if ot[0] // 3 == t_x // 3 and ot[1] // 3 == t_y // 3:
                ol_set |= set(self.s_puzzle[ot[1]][ot[0]])
        # if available values for t unique to column, row or local; assign that value to t
        if set(t_options).difference(oc_set):
            self.s_puzzle[t_y][t_x] = set(t_options).difference(oc_set).pop()
            self.unknown_tiles.remove(t)
            print('column replace')
            return True
        if set(t_options).difference(or_set):
            self.s_puzzle[t_y][t_x] = set(t_options).difference(or_set).pop()
            self.unknown_tiles.remove(t)
            print('row replace')
            return True
        if set(t_options).difference(ol_set):
            self.s_puzzle[t_y][t_x] = set(t_options).difference(ol_set).pop()
            self.unknown_tiles.remove(t)
            print('local replace')
            return True

        return False

    def iter_solve(self):
        while self.unknown_tiles:
            changes = 0
            for t_i in self.unknown_tiles:
                if self.second_solve(t_i):
                    changes += 1
            print('changes', changes)
            if changes == 0:
                self.s_print()
                break










s_0 = SodokuSolve(sudokus[0])
if s_0.simple_solve():
    print('check1')
    s_0.s_print()
else:
    s_0.iter_solve()


