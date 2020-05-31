import matplotlib.pyplot as plt
import math
n = 2

string = "X"
coordinates_stack = []
cur_coordinates = [0,0,math.radians(60)]

for i in range(n):
  string = string.replace("F","FF")
  string = string.replace("X","F+[[X]-X]-F[-FX]+X")

for char in string:
  print(cur_coordinates)
  if char == "F":
    next_coordinates = [cur_coordinates[0] + math.cos(cur_coordinates[2]), cur_coordinates[1] + math.sin(cur_coordinates[2])]
    x_values = [cur_coordinates[0], next_coordinates[0]]
    y_values = [cur_coordinates[1], next_coordinates[1]]
    plt.plot(x_values, y_values)
    cur_coordinates[0] = next_coordinates[0]
    cur_coordinates[1] = next_coordinates[1]
  if char == "-":
    cur_coordinates[2] = cur_coordinates[2] - math.radians(25)
  if char == "+":
    cur_coordinates[2] = cur_coordinates[2] + math.radians(25)
  if char == "[":
    coordinates_stack.append(list(cur_coordinates))
  if char == "]":
    cur_coordinates = coordinates_stack[len(coordinates_stack)-1]
    coordinates_stack.pop()

plt.show()