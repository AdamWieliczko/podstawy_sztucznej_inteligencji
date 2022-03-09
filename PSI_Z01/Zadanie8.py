import random

how_many_points = int(input("How many points:"))
radius = int(input("Radius:"))

how_many_in_circle = 0

for i in range(0, how_many_points):
    x = random.uniform(-radius, radius)
    y = random.uniform(-radius, radius)

    if radius * radius >= (x * x) + (y * y):
        how_many_in_circle += 1

pi = 4*how_many_in_circle/how_many_points
print(pi)