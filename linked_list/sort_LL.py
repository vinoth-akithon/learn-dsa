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
    
    
def merge(left_head: Node|None, right_head: Node|None) -> Node:
    result_head = Node(0)
    result_tail = result_head

    left_tail = left_head
    right_tail = right_head

    while (left_tail and right_tail):
        if left_tail.data < right_tail.data:
            result_tail.next = left_tail
            result_tail = result_tail.next
            left_tail = left_tail.next
        else:
            result_tail.next = right_tail
            result_tail = result_tail.next
            right_tail = right_tail.next
        
    
    if (left_tail):
        result_tail.next = left_tail
    elif right_tail:
        result_tail.next = right_tail

    return result_head.next


def optimal_approach(head: Node|None) -> Node:
    """
        - Complexity Analysis:
            - Time -> O(n logn)
            - Space -> O(n)
    
    """

    # Base condition 
    if not head or not head.next:
        return head

    # Find the first middle of LL
    prev_to_slow = None
    slow = head
    fast = head

    while (fast and fast.next):
        prev_to_slow = slow
        slow = slow.next
        fast = fast.next.next

    prev_to_slow.next = None
    left_head = optimal_approach(head)
    right_head = optimal_approach(slow)

    # print(f"Left Half -> {left_half}")
    # print(f"Right Half -> {right_half}")

    # Merging logic
    return merge(left_head, right_head)


def brute_force(head)


if __name__ == "__main__":
    LL = Node(3)
    LL.next = Node(1)
    LL.next.next = Node(2)
    LL.next.next.next = Node(4)

    print(LL)
    print(optimal_approach(LL))