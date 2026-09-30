"""

"""

from typing import Self

class Node:
    def __init__(self, data: int, next: Self|None = None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"{self.data} -> {self.next}"
    




def optimal_approach1(head: Node, data: int) -> Node:
    """
        Complexity Analysis:
            - Time -> O(1)
            - Space -> O(1)
    """
    new_node = Node(data)
    new_node.next = head

    head = new_node

    return head


def optimal_approach2(head: Node, data: int) -> Node:
    """
        Complexity Analysis:
            - Time -> O(1)
            - Space -> O(1)
    """
    new_node = Node(data, head)
    return new_node

if __name__ == "__main__":
    LL = Node(1)
    LL.next = Node(2)
    LL.next.next = Node(3)
        
    print(optimal_approach1(LL, 5))
    print(optimal_approach2(LL, 5))