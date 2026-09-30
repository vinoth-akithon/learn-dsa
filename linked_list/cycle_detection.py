"""

"""

from typing import Self

class Node:
    def __init__(self, data: int, next: Self|None = None) -> None:
        self.data = data
        self.next = next

    # def __str__(self) -> str:
    #     return f"{self.data} -> {self.next}"
    

def brute_force(head: Node) -> bool:
    """
        Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n)
    """
    temp = head
    hash_set = set()

    while (temp):
        if temp in hash_set:
            return True
        hash_set.add(temp)
        temp = temp.next
    return False


def optimal_approach(head: Node) -> bool:
    """
        - Using Fast and Slow pointers
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    slow = head
    fast = head

    while (fast and fast.next):
        slow = slow.next
        fast = fast.next.next
    
        if slow is fast:
            return True 
    return False




if __name__ == "__main__":
    LL = Node(1)
    LL.next = Node(2)
    LL.next.next = Node(3)
    LL.next.next.next = LL

    # print(LL)
    # print(brute_force(LL))
    print(optimal_approach(LL))