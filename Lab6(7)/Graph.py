class Graph:

    def __init__(self, graph=None):
        self.graph = graph

    def generate_edges(self):
        edges = [] # Empty list to hold all the edges
        for node in self.graph: # Iterate through each key
            for neighbor in self.graph[node]: # Through each edge
                if neighbor: # Add node and neighbor edge
                    edges.append((node, neighbor))
        return edges
                
    def find_isolated_nodes(self):
        isolated = [] # Empty list to hold all isolated nodes
        for node in self.graph: # Iterate through every node
            if not self.graph[node]: # If that node does not have its own connections
                isolated += node # Count node as isolated
        return isolated

    def find_path(self, start, end, path=None):
        if not path: # Initialize the path to an empty list
            path = []
        path = path + [start] # Add the start index to the path
        if start == end: # If the start and end are the same
            return path
        if start not in self.graph: # If start is not in the graph
            return None
        for neighbor in self.graph[start]: # Iterate through start nodes neighbors
            if neighbor not in path: # Add the neighbor to a potential extended path from start
                # Check the start nodes neighbors to see if there is a path to end node
                extend = self.find_path(neighbor, end, path)
                if extend: # If there is a path to the end node
                    return extend
        return None

    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        all_paths = []
        for neighbor in self.graph[start]:
            if neighbor not in path:
                extend = self.find_all_paths(neighbor, end, path)
                for vertex in extend:
                    all_paths.append(vertex)
        return all_paths

    def is_connected(self, vertices_encountered=None, start=None):
        if not vertices_encountered:
            vertices_encountered = set()
        vertices = list(self.graph.keys())
        if not start:
            start = vertices[0]
        vertices_encountered.add(start)
        if len(vertices_encountered) != len(vertices):
            for neighbor in self.graph[start]:
                if neighbor not in vertices_encountered:
                    if self.is_connected(vertices_encountered, neighbor):
                        return True
        else:
            return True
        return False
