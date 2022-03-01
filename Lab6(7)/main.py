from Graph import Graph

graph = Graph({ 'a': ['b', 'c', 'f', 'g'], 
                'b': ['a', 'c'],
                'c': ['a', 'b', 'e', 'd'],
                'd': ['e', 'c', 'd'],
                'e': ['d', 'c', 'g'],
                'f': ['a'],
                'g': ['a', 'e']})

graph2 = Graph({ 'a': ['b', 'e'], 
                'b': ['d'],
                'c': ['d', 'a'],
                'd': ['e'],
                'e': ['a', 'd'],
                'h': []})

print("Connceted (Graph 1):")
print(graph.is_connected())
print("Connceted (Graph 22):")
print(graph2.is_connected())
print()

print("Edges (Graph 1):")
print(graph.generate_edges())
print("Edges (Graph 2):")
print(graph2.generate_edges())
print()

print("Isolated Nodes (Graph 1):")
print(graph.find_isolated_nodes())
print("Isolated Nodes (Graph 2):")
print(graph2.find_isolated_nodes())
print()

print(graph.find_all_paths('a', 'g'))
print(graph.find_path('f', 'e'))
print(graph.generate_edges())