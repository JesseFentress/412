from WeightedGraph import WeightedGraph

graph = {'1': {'2': 10, '3': 15, '6': 5},
         '2': {'3': 7},
         '3': {'4': 7, '6': 10},
         '4': {'5': 7},
         '5': {'6': 13},
         '6': {'4': 7}}

wg = WeightedGraph(graph)

print("Breadth-First Search (Path from 1 to 4):")
print(wg.bfs('1', '5'))
print()

print("Depth-First Search (Path from 1 to 4):")
print(wg.dfs('1', '5'))
print()

print("Dijkstra's Algorithm (Starting at 1):")
print(wg.dijkstra('1'))