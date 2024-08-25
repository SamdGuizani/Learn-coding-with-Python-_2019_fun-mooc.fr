def distance_points(A, B):
    (x1, y1) = A
    (x2, y2) = B
    dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return dist


def longueur(*points):
    long = 0
    for i in range(len(points)-1) :
        long = long + distance_points(points[i + 1], points[i])
    return long


print(distance_points((1.0, 1.0), (2.0, 1.0)))
print(distance_points((-1.0, 0.5), (2.0, 1.0)))

print(longueur((1.0, 1.0), (2.0, 1.0), (3.0, 1.0)))
print(longueur((0.5, 1.0), (2.0, 1.0), (2.5, -0.5), (-1.5, -1.0)))