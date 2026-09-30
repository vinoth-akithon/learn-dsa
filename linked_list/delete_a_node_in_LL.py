"""

"""

from typing import Self

class Node:
    def __init__(self, data: int, next: Self|None = None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"{self.data} -> {self.next}"
    


def optimal_approach(head: Node, t: int) -> Node:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    if not head:
        return None
    
    temp = Node(0, head)

    pre = temp
    curr = head

    while (curr):
        if curr.data != t:
            pre = curr
            curr = curr.next
        else:
            next = curr.next
            curr.next = None # cutting the connection
            pre.next = next # Connecting previous and next nodes as current node needs to be removed
            break
    return temp.next


if __name__ == "__main__":
    LL = Node(1)
    # LL.next = Node(2)
    # LL.next.next = Node(3)


    print(LL)
    print(optimal_approach(LL, 10))