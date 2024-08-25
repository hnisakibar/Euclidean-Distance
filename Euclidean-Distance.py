import math
from itertools import combinations

# 1. Identifying Points
points = [(1, 2), (4, 6), (7, 8), (10, 12)]

# 2. Writing a Function for Euclidean Distance
def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)*2 + (y2 - y1)*2)

# 3. Calculating Distances
distances = [euclidean_distance(p1, p2) for p1, p2 in combinations(points, 2)]

# 4. Finding the Minimum Distance
min_distance = min(distances)
print(f"Minimum Distance: {min_distancEuclidean-Distance.txte}")