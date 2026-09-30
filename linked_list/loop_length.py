"""
"""

from typing import Self

class Node:
    def __init__(self, data: int, next: Self|None = None) -> None:
        self.data = data
        self.next = next

    # def __str__(self) -> str:
    #     return f"{self.data} -> {self.next}"


def brute_force(head: Node) -> int:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n)
    """
    temp = head
    hash_map = {}
    cnt = 0
    while (temp):
        cnt += 1
        if temp in hash_map:
            return cnt - hash_map[temp]
        
        hash_map[temp] = cnt
        temp = temp.next
    
    return 0


def better_approach(head: Node) -> int:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """

    slow = head
    fast = head
    starting_point = None

    while (fast and fast.next):
        slow = slow.next
        fast = fast.next.next

        if slow is fast: # Cycle detected
            slow = head

            while (slow is not fast):
                slow = slow.next
                fast = fast.next
            
            starting_point = slow
            break

    if starting_point:
        cnt = 1
        temp = starting_point
        while (temp.next is not starting_point):
            cnt += 1
            temp = temp.next

        return cnt

    return None


if __name__ == "__main__":
    LL = Node(1)
    LL.next = Node(2)
    LL.next.next = Node(3)
    LL.next.next.next = Node(4)
    LL.next.next.next.next = Node(5)
    LL.next.next.next.next.next = LL.next.next.next

    print(brute_force(LL))
    print(better_approach(LL))
