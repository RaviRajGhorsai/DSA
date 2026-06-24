"""
Here we use adjacency list(using dictionary) instead of adjacency matrix(using list) like in graph.py

"""


class Graph:
    def __init__(self) -> None:
        self.graph = {}
    
    def depth_first_search(self, start_vertex: str) -> list[str]:
        visited = []
        self.depth_first_search_r(visited, start_vertex)

        return visited

    def depth_first_search_r(self, visited: list[str], current_vertex: str) -> None:
        visited.append(current_vertex)

        neighbour = sorted(self.graph[current_vertex])

        for n in neighbour:
            if n not in visited:
                self.depth_first_search_r(visited, n)

    def breadth_first_search(self, v: str) -> list[str]:
        visited_vertices = []
        queue = []

        queue.append(v)

        while len(queue) > 0:
            nexts = queue[0]

            del queue[0]
            visited_vertices.append(nexts)
            neighbours = sorted(self.graph[nexts])

            for n in neighbours:
                if n not in visited_vertices and n not in queue:
                    queue.append(n)

        return visited_vertices

    def unconnected_vertices(self) -> list[int]:
        unconnected = []
        for i in self.graph:
            if len(self.graph[i]) == 0:
                unconnected.append(i)

        return unconnected

    def adjacent_nodes(self, node: int) -> set[int]:
        return self.graph.get(node, set())

    def add_edge(self, u: int, v: int) -> None:
        if u not in self.graph:
            self.graph[u] = set()

        if v not in self.graph:
            self.graph[v] = set()

        self.graph[u].add(v)
        self.graph[v].add(u)

    def add_node(self, u: int) -> None:
        if u not in self.graph:
            self.graph[u] = set()

    # don't touch below this line

    def edge_exists(self, u: int, v: int) -> bool:
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False
