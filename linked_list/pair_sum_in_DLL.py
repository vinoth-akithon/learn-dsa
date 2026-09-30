"""

"""

from typing import Self

class Node:
    def __init__(self, data: int, prev: Self|None = None, next: Self|None = None) -> None:
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        return f"{self.data} <-> {self.next}"
    
    def __repr__(self) -> str:
        return f"{self.data}"

def brute_force(head: Node, t: int) -> list[list[int]]:
    """
        - Fixing one node and find other node
        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(1)
    """
    res = []

    first = head
    while first.next:
        second = first.next
        while second:
            if first.data + second.data == t:
                res.append([first.data, second.data])

            second = second.next

        first = first.next

    return res


def optimal_approach(head: Node, t: int) -> list[list[int]]:
    """
        - Using two pointers approach (As DLL has prev point we can traverse the list from end without reversing the list)
        - Complexity Analysis:
            - Time -> O(2n)
            - Space -> O(1)
    """
    start = end = temp = head
    res = []

    while temp.next:
        temp = temp.next
    end = temp

    while (start and end and start.data <= end.data):
        sum_ = start.data + end.data
        if sum_ == t:
            res.append([start.data, end.data])
            start = start.next
            end = end.prev
        elif sum_ < t:
            start = start.next
        else:
            end = end.prev

    return res



if __name__ == "__main__":
    head = Node(1)
    head.next = Node(5)
    head.next.next = Node(6)

    head.next.prev = head
    head.next.next.prev = head.next


    # DLL.next.next = Node(3, prev=DLL.next)

    print(head)
    # print(brute_force(head, 6))
    print(optimal_approach(head, 6))
