
triangles = 1
spaces = 20

while triangles < 20 and spaces > 0:
    print(" " * spaces + " ^" * triangles)
    triangles += 2
    spaces -=2
