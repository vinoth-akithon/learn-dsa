"""
"""

from typing import Self

class Node:
    def __init__(self, data: int, next: Self|None = None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"{self.data} -> {self.next}"
    
    def __repr__(self) -> str:
        return f"{self.data} -> {self.next}"
    

def brute_force(head: Node) -> Node:
    """
        - Using Auxiliary DS (Stack)
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n)
    """

    temp = head
    stack = []

    while (temp):
        stack.append(temp.data)
        temp = temp.next

    temp = head
    while (temp):
        temp.data = stack.pop()
        temp = temp.next

    return head


def better_approach(head: Node) -> Node:
    """
        - Using recursion
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n) -> Due to recursive calls
    """
    # Base condition
    if not head or not head.next:
        return head
    
    new_head = better_approach(head.next)

    next_ = head.next
    next_.next = head
    head.next = None

    return new_head





def optimal_approach(head: Node) -> Node:
    """
        Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    if not head or not head.next:
        return head
    
    prev = None
    curr = head

    while (curr):
        next = curr.next
        curr.next = prev

        prev = curr
        curr = next

    return prev




if __name__ == "__main__":
    LL = Node(1)
    LL.next = Node(2)
    LL.next.next = Node(3)
    LL.next.next.next = Node(4)
    LL.next.next.next.next = Node(5)
    LL.next.next.next.next.next = Node(6)

    print(LL)
    # print(brute_force(LL))
    print(better_approach(LL))
    # print(optimal_approach(LL))