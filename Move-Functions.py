"""Presuably"""
grid_trile = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

#move left
def move_l(grid):
    grid = shift_l(grid)
    grid = merge_l(grid)

#move right
def move_r(grid):
    grid = shift_r(grid)
    grid = merge_r(grid)

#move up
def move_u(grid):
    grid = shift_u(grid)
    grid = merge_u(grid)

#move down
def move_d(grid):
    grid = shift_d(grid)
    grid = merge_d(grid)

#All the shifts
def shift_l():
    for row in grid:
        count = 0
        while 0 in row:
            row.remove(0)
            count += 1
        for add in range(count):
            row.append(0)

def shift_r():
    for row in grid:
        count = 0
        while 0 in row:
            row.remove(0)
            count += 1
        for add in range(count):
            row.insert(0, 0)

#All the merges
