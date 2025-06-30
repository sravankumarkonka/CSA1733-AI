from collections import defaultdict

class MapColoringCSP:
    def __init__(self, countries, colors):
        self.countries = countries
        self.colors = colors
        self.adjacency_list = defaultdict(list)

    def add_edge(self, country1, country2):
        self.adjacency_list[country1].append(country2)
        self.adjacency_list[country2].append(country1)

    def is_valid(self, country, color, assignment):
        for neighbor in self.adjacency_list[country]:
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True

    def backtrack(self, assignment):
        if len(assignment) == len(self.countries):
            return assignment
        
        country = self.select_unassigned_country(assignment)
        for color in self.colors:
            if self.is_valid(country, color, assignment):
                assignment[country] = color
                result = self.backtrack(assignment)
                if result:
                    return result
                del assignment[country]
        return None

    def select_unassigned_country(self, assignment):
        for country in self.countries:
            if country not in assignment:
                return country
        return None

    def solve(self):
        return self.backtrack({})

# Example usage
if __name__ == "__main__":
    countries = ['A', 'B', 'C', 'D']
    colors = ['Red', 'Green', 'Blue']
    map_coloring = MapColoringCSP(countries, colors)
    
    map_coloring.add_edge('A', 'B')
    map_coloring.add_edge('A', 'C')
    map_coloring.add_edge('B', 'C')
    map_coloring.add_edge('B', 'D')
    
    solution = map_coloring.solve()
    print("Coloring Assignment:", solution)
