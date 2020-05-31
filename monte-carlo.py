import random as random
import math

#-------------------------------------

SAMPLE_COUNT = 10000
A = 0
B = math.pi

#-------------------------------------

def func(x):
  return math.sin(x)

def random_sample(a, b):
  return random.uniform(a, b)

#-------------------------------------

sum = 0
for i in range(SAMPLE_COUNT):
  sum = sum + func(random_sample(A,B))

print(str(sum * (B-A) / SAMPLE_COUNT))