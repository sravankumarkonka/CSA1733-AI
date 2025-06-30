import itertools

def calculate_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def total_distance(points, path):
    distance = 0
    for i in range(len(path) - 1):
        distance += calculate_distance(points[path[i]], points[path[i + 1]])
    distance += calculate_distance(points[path[-1]], points[path[0]])  # Return to starting point
    return distance

def traveling_salesman(points):
    n = len(points)
    min_path = None
    min_distance = float('inf')
    
    for perm in itertools.permutations(range(n)):
        current_distance = total_distance(points, perm)
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = perm
            
    return min_path, min_distance

# Example usage
points = [(0, 0), (1, 2), (2, 1), (3, 3)]
best_path, best_distance = traveling_salesman(points)
print("Best path:", best_path)
print("Minimum distance:", best_distance)
