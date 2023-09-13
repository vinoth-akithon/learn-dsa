"""
Graph Implementation using Adjacent List
"""

class Node(object):
    def __init__(self, label: str) -> None:
        self.__label = label

    @property
    def get_label(self):
        return self.__label

    def __repr__(self) -> str:
        return f"{self.__label}"
    

class Graph(object):
    def __init__(self) -> None:
        self.__nodes: dict[str, Node] = {}
        self.__adjacency_list: dict[Node, list[Node]] = {}


    def add_node(self, label: str) -> None:
        """Add a new node in adjacency list."""

        new_node = Node(label)
        self.__nodes[label] = new_node
        self.__adjacency_list[new_node] = []


    def add_edge(self, from_label, to_label) -> None:
        from_node = self.__nodes.get(from_label)
        if from_node is None: 
            raise ValueError(f"{from_label} is not a valid node")

        to_node = self.__nodes.get(to_label)
        if to_node is None:
            raise ValueError(f"{to_label} is not a valid node")
        
        self.__adjacency_list[from_node].append(to_node)


    def remove_edge(self, from_label, to_label) -> None:
        from_node = self.__nodes.get(from_label)
        if from_node is None: 
            raise ValueError(f"{from_label} is not a valid node")
        
        to_node = self.__nodes.get(to_label)
        if to_node is None:
            raise ValueError(f"{to_label} is not a valid node")
        
        try:
            self.__adjacency_list[from_node].remove(to_node)
        except ValueError:
            return

    
    def remove_node(self, label: str):
        """First remove the node and remove 
        links in the  adjacency list."""

        # removing from the nodes list
        node = self.__nodes.pop(label)
        if node is None:
            raise ValueError(f"{label} is not a valid node")
        
        # removing from the adjacency list
        self.__adjacency_list.pop(node)
        
        for edges in self.__adjacency_list.values():
            for target in edges:
                if target is node:
                    edges.remove(target)
                    break
        
        
    def __repr__(self):
        return f"{self.__adjacency_list}"
    

    def __str__(self):
        self.print_adjacent_nodes()
        return ""
    

    def unique_label_generator(self, label):
        return f"{label}-{len(self.__adjacency_list)}"
    
    
    def print_adjacent_nodes(self):
        for key, value in self.__adjacency_list.items():
            print(f"{key} is connected with {value}")

 
    

# Instantiate new graph
graph = Graph()

# Adding Node
graph.add_node("Jhon")
graph.add_node("Bob")
graph.add_node("Mary")
graph.add_node("Alice")

# Adding Edges
graph.add_edge("Jhon", "Bob")
graph.add_edge("Jhon", "Mary")
# graph.add_edge("Jhon", "Alice")
# graph.add_edge("Mary", "Bob")
# graph.add_edge("Mary", "Alice")
# graph.add_edge("Alice", "Bob")

# Remove Edge
graph.remove_edge("Jhon", "Alice")

# Remove node
# graph.remove_node("Mary")

# Prining Connection
# graph.print_adjacent_nodes()
print(graph)