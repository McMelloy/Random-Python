import time, os, random, sys
import numpy as np

def clear_console():
   os.system("cls")

# ------------------------------------------------------------------------
rows = 30
cols = 30

generations = 1000
# ------------------------------------------------------------------------

def create_grid():
   return np.random.randint(2, size=(rows, cols))

# ------------------------------------------------------------------------

def create_next_grid(grid, next_grid):
   for row in range(rows):
      for col in range(cols):
         neighbors = alive_neighbors(row, col, grid)

         if neighbors < 2 or neighbors > 3:
               next_grid[row, col] = 0
         elif neighbors == 3 and grid[row, col] == 0:
               next_grid[row, col] = 1
         else:
               next_grid[row, col] = grid[row, col]

# ------------------------------------------------------------------------

def alive_neighbors(row, col, grid):
   return np.sum(grid[row-1:row+2, col-1:col+2]) - grid[row, col]

# ------------------------------------------------------------------------

def stop_process(grid, next_grid):
   comparison = grid == next_grid 
   return comparison.all()

# ------------------------------------------------------------------------

def print_grid(grid, generation):
   clear_console()
   output_str = ""

   output_str += "Generation {0} (To exit the program press Ctrl+C) \n\r".format(generation)
   for row in range(rows):
      for col in range(cols):
         if grid[row, col] == 0:
               output_str += "- "
         else:
               output_str += "O "
      output_str += "\n\r"
   print(output_str, end=" ")

# ------------------------------------------------------------------------

def run_game():

   clear_console()

   input("Press <Enter> to start.")

   current_generation = create_grid()
   next_generation = create_grid()

   gen = 0
   for gen in range(generations):
      if stop_process(current_generation, next_generation):
         break
      print_grid(current_generation, gen)
      create_next_grid(current_generation, next_generation)
      time.sleep(1 / 5.0)
      current_generation, next_generation = next_generation, current_generation

   print_grid(current_generation, gen)
   input("Press <Enter> to exit.")


# Start the Game of Life
run_game()