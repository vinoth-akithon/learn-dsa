"""

"""

from typing import Self

class Node:
    def __init__(self, data: int, next: Self|None = None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"{self.data} -> {self.next}"
    

def brute_force(head: Node) -> int:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """

    # Getting the length of the LL
    temp = head
    cnt = 0
    while (temp):
        cnt += 1
        temp = temp.next
    
    # Getting the middle node
    temp = head
    i = 1
    mid = cnt//2 +1
    while True:
        if i == mid:
            return temp.data
        temp = temp.next
        i += 1


def optimal_approach(head: Node) -> int:
    """
        - The tortoise and hare algorithm
        - Complexity Analysis:
            - Time -> O(n/2)
            - Space -> O(1)
    """
    if not head:
        return None
    
    slow = head
    fast = head

    while (fast and fast.next):
        slow = slow.next
        fast = fast.next.next

    return slow.data



if __name__ == "__main__":
    LL = Node(1)
    LL.next = Node(2)
    # LL.next.next = Node(3)
    # LL.next.next.next = Node(4)
    # LL.next.next.next.next = Node(5)
    # LL.next.next.next.next.next = Node(6)

    print(LL)
    print(brute_force(LL))
    print(optimal_approach(LL))