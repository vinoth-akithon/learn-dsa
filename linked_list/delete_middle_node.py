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
        Complexity Analysis:
            - TIme -> O(n) + O(n/2)
            - Space -> O(1)
    """
    if not head or not head.next:
        return

    temp = head
    length = 0
    while temp:
        length += 1
        temp = temp.next

    mid = length//2
    print(mid)

    prev_node = None
    curr_node = head
    cnt = 0

    while curr_node:
        if cnt == mid:
            prev_node.next = curr_node.next
            break
        
        cnt += 1
        prev_node = curr_node
        curr_node = curr_node.next

    return head



def optimal_approach(head: Node) -> Node:
    """
        - Using fast and slow pointer
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    dummy = Node(0, head)
    prev_to_slow = dummy
    slow = head
    fast = head

    # moving pointer until reach tail node or exceed the tail node 
    while (fast and fast.next):
        prev_to_slow = slow
        slow = slow.next
        fast = fast.next.next

    prev_to_slow.next = slow.next

    return dummy.next


if __name__ == "__main__":
    LL = Node(1)
    # LL.next = Node(2)
    # LL.next.next = Node(3)
    # LL.next.next.next = Node(4)
    # LL.next.next.next.next = Node(5)

    print(LL)

    # print(optimal_approach(LL))
    print(brute_force(LL))
