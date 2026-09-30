"""

"""


from typing import Self

class Node:
    def __init__(self, data: int, next: Self|None = None) -> None:
        self.data = data
        self.next = next

    # def __str__(self) -> str:
    #     return f"{self.data} -> {self.next}"

    def __repr__(self) -> str:
        return f"{self.data}"


def brute_force(head: Node) -> int:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n)
    """
    temp = head
    hash_set = set()

    while (temp):
        if temp in hash_set:
            return temp.data
        
        hash_set.add(temp)
        temp = temp.next

    return None



def optimal_approach(head: Node) -> int:
    """
    
    """
    slow = head
    fast = head

    while (fast and fast.next):
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            slow = head

            while (slow is not fast):
                slow = slow.next
                fast = fast.next

            return slow

    return None



if __name__ == "__main__":
    LL = Node(1)
    LL.next = Node(2)
    LL.next.next = Node(3)
    LL.next.next.next = Node(4)
    LL.next.next.next.next = Node(5)
    LL.next.next.next.next.next = LL.next.next

    print(brute_force(LL))
    print(optimal_approach(LL))

