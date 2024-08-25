def distance_points(A, B):
    (x1, y1) = A
    (x2, y2) = B
    dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return dist


print(distance_points((1.0, 1.0), (2.0, 1.0)))
print(distance_points((-1.0, 0.5), (2.0, 1.0)))