from re import X
import sys


class WeightedGraph:

    def __init__(self, graph=None):
        self.graph = graph
        self.size = 0

    def bfs(self, start_vertex, end_vertex):
        if start_vertex == end_vertex: # Start and end vertices are the same
            return start_vertex # Return start vertex
        visited = [start_vertex] # Mark start vertex as visited
        queue = [] # Queue for holding traversable vertices
        queue.append(start_vertex) # Add start vertex to queue
        while len(queue) != 0: # Continue until there are no vertices to traverse
            current_vertex = queue.pop(0) # Remove first vertex from queue
            for neighbor_vertex in self.graph[current_vertex]: # Loop all neighboring vertices
                if neighbor_vertex[0] == end_vertex: # Neighboring vertex is the end vertex
                    visited.append(neighbor_vertex[0]) # Add neighboring vertex to the path
                    return visited # Return the path
                if neighbor_vertex[0] not in visited: # If we have not visited this vertex
                    queue.append(neighbor_vertex[0]) # Add neighboring vertex to the queue
                    visited.append(neighbor_vertex[0]) # Mark the neighboring vertex as visited
        return None # End vertex was not found
            

    def dfs(self, start_vertex, end_vertex, visited=None):
        if start_vertex == end_vertex: # Start and end vertices are the same
            return visited # Return start vertex
        if not visited: # No vertices have been visited yet
            visited = [start_vertex] # Mark start vertex as visited
        for neighbor_vertex in self.graph[start_vertex]: # Loop all neighboring vertices
            if neighbor_vertex[0] == end_vertex: # Neighboring vertex is the end vertex
                visited.append(neighbor_vertex[0]) # Add neighboring vertex to the path
                return visited # Return the path
            if neighbor_vertex[0] not in visited: # If we have not visited this vertex
                visited.append(neighbor_vertex[0]) # Add neighboring vertex to the path
                return self.dfs(neighbor_vertex[0], end_vertex, visited) # Explore new vertex
        return None # End vertex was not found


    def dijkstra(self, start_vertex):
        unvisited = {} # Hold unvisited vertices
        visited = {} # Hold visited vertices with final distances
        for vertex in self.graph.keys(): # Set starting distances to max
            unvisited[vertex] = sys.maxsize
        current_vertex  = start_vertex # Starting vertex
        current_distance = 0 # Distance from start to start is 0
        unvisited[current_vertex] = current_distance # Set distance in unvisited
        while True: # Maintin loop while there are vertices to visit
            for vertex, distance in self.graph[current_vertex].items():
                print(unvisited) # Print current state of distances
                if vertex not in unvisited: # If vertex is already visited
                    continue
                new_distance = current_distance + distance # Update distance to vertex
                if not unvisited[vertex] or unvisited[vertex] > new_distance: # Pick optimal distance
                    unvisited[vertex] = new_distance # Update distance in unvisted
            visited[current_vertex] = current_distance # Once visited update distance
            del unvisited[current_vertex] # Remove vertex from unvisited
            if not unvisited: # Once all vertices have been visited
                break
            others = [vertex for vertex in unvisited.items() if vertex[1]] # Indices that are not visited
            current_vertex, current_distance = sorted(others, key=lambda x: x[1])[0] # Sort the vertices by distance
        return visited # Return all distances
