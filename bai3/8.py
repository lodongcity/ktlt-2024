print ("lô văn đồng")
print ("235752021610070")

import math

def calculate_distance(moves):

  x, y = 0, 0

  for move in moves:
    direction, steps = move.split()
    steps = int(steps)

    if direction == "UP":
      y += steps
    elif direction == "DOWN":
      y -= steps
    elif direction == "LEFT":
      x -= steps
    elif direction == "RIGHT":
      x += steps

  distance = math.sqrt(x**2 + y**2)
  return round(distance)

moves = ["UP 5", "DOWN 3", "LEFT 3", "RIGHT 2"]
result = calculate_distance(moves)
print("Khoảng cách:", result)
