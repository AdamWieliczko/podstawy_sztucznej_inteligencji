import math

radius_one = int(input("First radius:"))
radius_two = int(input("Second radius"))

first_x = int(input("First circle x coordiante:"))
first_y = int(input("First circle y coordiante:"))
second_x = int(input("Second circle x coordinate:"))
second_y = int(input("Second circle y coordinate:"))

if math.dist([first_x, first_y], [second_x, second_y]) > radius_one + radius_two: #if distance between two points is greater than sum of radiuses
    print("There aren't any non-empty intersections")
else:
    print("There is a non-empty intersection")