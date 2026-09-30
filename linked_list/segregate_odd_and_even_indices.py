"""

"""

from typing import Self
from collections import deque

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
        - Using auxiliary DS (stacks)
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n)
    """
    temp = head
    idx = 1
    odd_queue = deque()
    even_queue = deque()


    while temp:
        if idx % 2 != 0:
            odd_queue.append(temp.data)
        else:
            even_queue.append(temp.data)

        idx += 1
        temp = temp.next

    temp = head
    for _ in range(len(odd_queue)):
        temp.data = odd_queue.popleft()
        temp = temp.next

    for _ in range(len(even_queue)):
        temp.data = even_queue.popleft()
        temp = temp.next

    return head
        

def optimal_approach(head: Node) -> Node:
    """
        - Using Two pointer approach
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    odd_list = Node(0)
    odd_tail = odd_list
    even_list = Node(0)
    even_tail = even_list

    temp = head
    idx = 1
    while (temp):
        if idx % 2 != 0:
            odd_tail.next = temp
            odd_tail = odd_tail.next
        else:
            even_tail.next = temp
            even_tail = even_tail.next

        idx += 1
        temp = temp.next
    
    even_tail.next = None
    odd_tail.next = even_list.next

    return odd_list.next

if __name__ == "__main__":
    LL = Node(1)
    LL.next = Node(2)
    LL.next.next = Node(3)
    LL.next.next.next = Node(4)
    LL.next.next.next.next = Node(5)

    print(LL)
    # print(brute_force(LL))
    print(optimal_approach(LL))



