"""
Graph Implementation using Adjacent List
"""

from collections import deque

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


    def depth_first_traversal(self, label):
        node = self.__nodes.get(label)
        if not node:
            raise ValueError(f"{label} is not a valid node")
        # self.__depth_first_traversal_using_recursion(node, set())
        self.__depth_first_traversal_using_iteration(node, set())

    
    def __depth_first_traversal_using_recursion(self, node: Node, visited_node: set):
        print(node)
        visited_node.add(node)
        for edge in self.__adjacency_list[node]:
            if edge not in visited_node:
                self.__depth_first_traversal_using_recursion(edge, visited_node)

    
    def __depth_first_traversal_using_iteration(self, node: Node, visited_node: set):
        stack = [ node ]
        while (stack):
            current_node = stack.pop()
            print(current_node)
            visited_node.add(current_node)
            for edge in self.__adjacency_list[current_node]:
                if edge not in visited_node:
                    stack.append(edge)


    def breadth_first_traversal(self, label):
        node = self.__nodes.get(label)
        if not node:
            raise ValueError(f"{label} is not a valid node")
        self.__breadth_first_traversal_using_iteration(node, set())

    
    def __breadth_first_traversal_using_iteration(self, node: Node, visited_nodes: set):
        queue = deque((node,))
        while (queue):
            current_node = queue.popleft()
            print(current_node)
            visited_nodes.add(current_node)
            for edge in self.__adjacency_list[current_node]:
                if edge not in visited_nodes:
                    queue.append(edge)


    def topological_sort(self):
        stack: list[Node] = []
        visited_nodes: set[Node] = set()

        for node in self.__nodes.values():
            self.__topological_sorting(node, visited_nodes, stack)  
        
        sorted: list[str] = []
        while (stack):
            sorted.append(stack.pop().get_label)
        return sorted
    

    def __topological_sorting(self, node: Node, visited_nodes: set, stack: list):
        visited_nodes.add(node)
        for edge in self.__adjacency_list[node]:
            if edge not in visited_nodes:
                self.__topological_sorting(edge, visited_nodes, stack)

        if node not in stack:
            stack.append(node)

    
    def has_cycle(self) -> bool:
        all_set = set(self.__nodes.values())
        visiting_set: set[Node] = set()
        visited_set: set[Node] = set()
        for node in self.__nodes.values():
            if (node not in visiting_set) and (node not in visited_set):
                if self.__dedect_cycle(node, all_set, visiting_set, visited_set):
                    return True
        return False
    
    
    def __dedect_cycle(self, node, all_set: set, visiting_set: set, visited_set: set):
        visiting_set.add(node)
        all_set.remove(node)
        for edge in self.__adjacency_list[node]:
            if (edge not in visiting_set) and (edge not in visited_set):
                if self.__dedect_cycle(edge, all_set, visiting_set, visited_set):
                    return True
            elif (edge in visiting_set):
                return True

        visited_set.add(node)
        visiting_set.remove(node)
        return False
    


if __name__ == "__main__":
    # Instantiate new graph
    graph = Graph()

    # Adding Node
    # graph.add_node("Jhon")
    # graph.add_node("Bob")
    # graph.add_node("Mary")
    # graph.add_node("Alice")

    # Adding Edges
    # graph.add_edge("Jhon", "Bob")
    # graph.add_edge("Jhon", "Mary")
    # graph.add_edge("Jhon", "Alice")
    # graph.add_edge("Mary", "Bob")
    # graph.add_edge("Mary", "Alice")
    # graph.add_edge("Alice", "Bob")

    # Remove Edge
    # graph.remove_edge("Jhon", "Alice")

    # Remove node
    # graph.remove_node("Mary")

    # Prining Connection
    # graph.print_adjacent_nodes()
    # print(graph)


    # Traversals
    # graph.add_node("A")
    # graph.add_node("B")
    # graph.add_node("C")
    # graph.add_node("D")

    # graph.add_edge("A", "B")
    # graph.add_edge("B", "D")
    # graph.add_edge("D", "C")
    # graph.add_edge("A", "C")


    # graph.depth_first_traversal("C")
    # graph.breadth_first_traversal("A")


    # Topological sorting
    graph.add_node("X")
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("P")

    graph.add_edge("X", "A")
    graph.add_edge("X", "B")
    graph.add_edge("A", "P")
    graph.add_edge("B", "P")

    print(graph.topological_sort())


    # Cycle dedection
    # graph.add_node("A")
    # graph.add_node("B")
    # graph.add_node("C")
    # graph.add_node("D")

    # graph.add_edge("A", "B")
    # graph.add_edge("B", "C")
    # graph.add_edge("A", "C")
    # graph.add_edge("C", "A")
    # graph.add_edge("A", "D")


    # print(graph.has_cycle())
    # print(graph)