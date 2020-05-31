import numpy as np
import xlsxwriter

RANGE = 40
scheme = []
for i in range(RANGE):
  for y in range(RANGE):
    scheme.append((i,y))

matrix = np.zeros((RANGE*RANGE,RANGE*RANGE), dtype=int)
for row in range(RANGE*RANGE):
  element = scheme[row]
  if element[0]<RANGE-1:
    matrix[row][scheme.index((element[0]+1,element[1]))] = 1
  if element[1]<RANGE-1:
    matrix[row][scheme.index((element[0],element[1]+1))] = 1
  if element[0]>0:
    matrix[row][scheme.index((element[0]-1,element[1]))] = 1
  if element[1]>0:
    matrix[row][scheme.index((element[0],element[1]-1))] = 1
  matrix[row][scheme.index(element)] = -4
#print(matrix)

matrix_B = np.zeros(RANGE*RANGE, dtype=int)
for index in range(RANGE*RANGE):
  element = scheme[index]
  if (element[0]==RANGE-1 and element[1]==0) or (element[0]==0 and element[1]==RANGE-1):
    matrix_B[index] = -250
  elif element[0]==0 and element[1]==0:
    matrix_B[index] = -300
  elif element[0]==RANGE-1 and element[1]==RANGE-1:
    matrix_B[index] = -200

  elif element[0]==RANGE-1:
    matrix_B[index] = -150
  elif element[0]==0:
    matrix_B[index] = -200
  elif element[1]==0:
    matrix_B[index] = -100
  elif element[1]==RANGE-1:
    matrix_B[index] = -50

#print(matrix_B)

solution = np.linalg.solve(matrix,matrix_B).reshape(RANGE,RANGE)
#print(solution)
workbook = xlsxwriter.Workbook('plate.xlsx')
worksheet = workbook.add_worksheet()

row = 1
col = 1
for col_num, data in enumerate(solution):
  worksheet.write_row(row, 0, data)
  row = row + 1

workbook.close()