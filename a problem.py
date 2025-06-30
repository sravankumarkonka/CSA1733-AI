import heapq

class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        self.name = name
        self.parent = parent
        self.g = g  # Cost from start to node
        self.h = h  # Heuristic cost from node to goal
        self.f = g + h  # Total cost

    def __lt__(self, other):
        return self.f < other.f

def a_star(start, goal, graph, heuristic):
    open_list = []
    closed_list = set()
    
    start_node = Node(start, None, 0, heuristic[start])
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        
        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        closed_list.add(current_node.name)

        for neighbor, cost in graph[current_node.name].items():
            if neighbor in closed_list:
                continue
            
            g_cost = current_node.g + cost
            h_cost = heuristic[neighbor]
            neighbor_node = Node(neighbor, current_node, g_cost, h_cost)

            if any(open_node.name == neighbor and open_node.g <= g_cost for open_node in open_list):
                continue
            
            heapq.heappush(open_list, neighbor_node)

    return None  # No path found

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'E': 1},
    'D': {'B': 2, 'E': 1},
    'E': {'B': 5, 'C': 1, 'D': 1}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0
}

path = a_star('A', 'E', graph, heuristic)
print("Path from A to E:", path)
