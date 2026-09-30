"""

"""

from typing import Self

class Node:
    def __init__(self, data: int, next: Self|None = None, prev: Self|None=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return f"{self.data} <-> {self.next}"

    
    def __repr__(self) -> str:
        return f"{self.data} <-> {self.next}"


def brute_force(head: Node) -> Node:
    """
        - Using Auxiliary DS (Set)
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(d)
    """
    hash_set = set()
    temp = head

    while temp:
        if temp.data in hash_set:
            prev = temp.prev
            next_ = temp.next

            if temp.next is None:
                prev.next = None
            else:
                prev.next = next_
                next_.prev = prev
        else:
            hash_set.add(temp.data)

        temp = temp.next

    return head


def optimal_approach(head: Node) -> Node:
    """
        - If it's already sorted array
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    temp = head.next

    while temp:
        prev = temp.prev
        if temp.data == prev.data:
            next_ = temp.next

            if next_ is None:
                prev.next = None
            else:
                prev.next = next_
                next_.prev = prev

        temp = temp.next

    return head




if __name__ == "__main__":
    head = Node(1)

    head.next = Node(2, prev=head)

    head.next.next = Node(3, prev=head.next)
    head.next.next.next = Node(1, prev=head.next.next)
    head.next.next.next.next = Node(1, prev=head.next.next.next)

    print(head)

    # print(brute_force(head))
    print(optimal_approach(head))
