import numpy as np
def alive_neighbors(row, col, rows, cols, grid):
  life_sum = 0
  for i in range(-1, 2):
    for j in range(-1, 2):
        if not (i == 0 and j == 0):
              life_sum += grid[((row + i) % rows)][((col + j) % cols)]
  return life_sum

def alive_neighbors_2(row, col, grid):
  return np.sum(grid[row-1:row+2, col-1:col+2]) - grid[row, col]

grid = np.random.randint(2, size=(10, 10))
print(grid)
print(alive_neighbors(1, 1, 10, 10, grid))
print(alive_neighbors_2(1, 1, grid))