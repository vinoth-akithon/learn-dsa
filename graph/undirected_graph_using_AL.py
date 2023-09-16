
from typing import Self
from queue import PriorityQueue


from dataclasses import dataclass, field
from typing import Any


class Node(object):
    def __init__(self, label: str) -> None:
        self.__label = label
        self.__edges: list[Edge] = [] 

    @property
    def get_label(self):
        return self.__label
    
    @property
    def get_edges(self):
        return self.__edges

    def __repr__(self) -> str:
        return f"{self.__label}"
    
    def add_edge(self, to_node: Self, weight: int):
        self.__edges.append(Edge(self, to_node, weight))
    

class Edge(object):
    def __init__(self, from_node: Node, to_node: Node, weight: int) -> None:
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    def __repr__(self) -> str:
        return f"{self.from_node} -> {self.to_node}"

class Path(object):
    def __init__(self):
        self.__nodes: list[str] = []

    def add(self, node: str):
        self.__nodes.append(node)

    def __repr__(self) -> str:
        return f"{self.__nodes}"
    

class Graph(object):
    def __init__(self) -> None:
        self.__nodes: dict[str, Node] = {}

    def __len__(self):
        return len(self.__nodes)


    def add_node(self, label: str) -> None:
        """Adding a new node."""
        self.__nodes[label] = Node(label)


    def add_edge(self, from_label: str, to_label: str, weight: int) -> None:
        from_node = self.__nodes.get(from_label)
        if from_node is None:
            raise ValueError(f"{from_label} is not a valid node")
        
        to_node = self.__nodes.get(to_label)
        if to_node is None:
            raise ValueError(f"{to_node} is not a valid node")
        
        from_node.add_edge(to_node, weight)
        to_node.add_edge(from_node, weight)
        

    def __repr__(self) -> str:
        return f"{self.__nodes}"


    def __str__(self):
        self.print_adjacent_nodes()
        return ""
    
    def print_adjacent_nodes(self):
        for node in self.__nodes.values():
            print(f"{node} is connected with {node.get_edges}")


    def get_shortest_distance(self, from_label: str, to_label: str):
        from_node = self.__nodes.get(from_label)
        if from_node is None:
            raise ValueError(f"{from_label} is not a valid node")
        
        to_node = self.__nodes.get(to_label)
        if to_node is None:
            raise ValueError(f"{to_label} is not a valid node")

        visited_nodes: set[Node] = set()
        distances: dict[Node, int] = {node:float("inf") for node in self.__nodes.values()}
        distances[from_node] = 0

        queue = PriorityQueue()
        queue.put_nowait((0, from_node))
        while (queue.qsize() != 0):
            try:
                current_node: Node  = queue.get_nowait()[1]
            except TypeError:
                pass
            visited_nodes.add(current_node)

            for edge in current_node.get_edges:
                neighbour = edge.to_node
                weight = edge.weight
                if neighbour in visited_nodes:
                    continue

                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbour]:
                    distances[neighbour] = new_distance
                    try:
                        queue.put_nowait((new_distance, neighbour))
                    except TypeError:
                        pass

        return distances[to_node]
    

    def get_shortest_path(self, from_label: str, to_label: str):
        from_node = self.__nodes.get(from_label)
        if from_node is None:
            raise ValueError(f"{from_label} is not a valid node")
        
        to_node = self.__nodes.get(to_label)
        if to_node is None:
            raise ValueError(f"{to_label} is not a valid node")

        distances: dict[Node, int] = {node:float("inf") for node in self.__nodes.values()}
        distances[from_node] = 0

        previous_nodes: dict[Node, Node] = {}

        visited_nodes: set[Node] = set()

        queue = PriorityQueue()
        queue.put_nowait((0, from_node))
        while (queue.qsize() != 0):
            try:
                current_node: Node  = queue.get_nowait()[1]
            except TypeError:
                pass
            visited_nodes.add(current_node)

            for edge in current_node.get_edges:
                neighbour = edge.to_node
                weight = edge.weight
                if neighbour in visited_nodes:
                    continue

                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbour]:
                    distances[neighbour] = new_distance
                    previous_nodes[neighbour] = current_node
                    try:
                        queue.put_nowait((new_distance, neighbour))
                    except TypeError:
                        pass
        
        return self.__path_builder(previous_nodes, to_node)
    

    def __path_builder(self, previous_nodes: Node, to_node: Node):
        stack = []
        stack.append(to_node)
        previous = previous_nodes.get(to_node)
        while (previous):
            stack.append(previous)
            previous = previous_nodes.get(previous)

        path = Path()
        while (stack):
            path.add(stack.pop())
        return path

    def has_cycle(self) -> bool:
        visited_nodes: set[Node] = set()
        for node in self.__nodes.values():
            if node not in visited_nodes:
                if self.__has_cycle(node, node, visited_nodes):
                    return True
        return False

    
    def __has_cycle(self, node: Node, parent_node:Node, visited_node: set[Node]):
        visited_node.add(node)
        for edge in node.get_edges:
            neighbour = edge.to_node
            if parent_node is neighbour:
                continue
            if neighbour in visited_node:
                return True
            if self.__has_cycle(neighbour, node, visited_node):
                return True
        return False
    
    
    def get_spanning_tree(self):
        tree = Graph() # creating tree
        queue = PriorityQueue() # creating priority queue for storing edges
        try:
            start_node: Node = list(self.__nodes.values())[0] # take any one of node as starting point
        except IndexError:
            return tree
        
        for edge in start_node.get_edges:
            queue.put_nowait((edge.weight, edge))
        tree.add_node(start_node.get_label)
        
        while (len(tree) < len(self)):
            if (queue.qsize() == 0):
                return tree
            min_edge: Edge = queue.get_nowait()[1]
            next_node = min_edge.to_node
            if tree.contain_node(next_node.get_label):
                continue

            tree.add_node(next_node.get_label)
            tree.add_edge(min_edge.from_node.get_label, next_node.get_label, min_edge.weight)

            for edge in next_node.get_edges:
                if not tree.contain_node(edge.to_node.get_label):
                    queue.put_nowait((edge.weight, edge)) 

        return tree
    

    def contain_node(self, label: str) -> bool:
        return label in self.__nodes




if __name__ == "__main__":
    graph = Graph()

    # Adding nodes
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    # graph.add_node("E")

    # Adding Edges
    graph.add_edge("A", "B", 3)
    graph.add_edge("A", "C", 1)
    graph.add_edge("B", "C", 2)
    graph.add_edge("B", "D", 4)
    graph.add_edge("C", "D", 5)


    # graph.add_edge("A", "C", 10)
    # graph.add_edge("D", "C", 1)
    # graph.add_edge("B", "E", 1)
    # graph.add_edge("D", "E", 5)


    # getting shortest path
    # print(graph.get_shortest_distance("A", "E"))
    # print(graph.get_shortest_path("A", "C"))

    # Checking cyclic
    # print(graph.has_cycle())

    # Minimum spanning tree
    print(graph.get_spanning_tree())
    print("pass")