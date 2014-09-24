import math
def polyarea(n,s):
    area = 1/4 * n * s ** 2 / math.tan(math.pi / n)
    return area
print(polyarea(7,3))
print(polyarea(5,7))
