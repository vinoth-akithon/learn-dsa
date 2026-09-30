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
    

def brute_force(head: Node, n: int) -> Node:
    """
        - Using auxiliary DS (Hash Map)
        - Complexity Analysis:
            - Time -> O(n) + O(n) ~= O(n)
            - Space -> O(n)
    """
    if not head:
        return 
    
    temp = head
    length = 0
    hash_map = {}

    while temp:
        length += 1
        hash_map[length] = temp
        
        temp = temp.next
    
    if n > length:
        return head
    elif n == length:
        return head.next
    
    curr = length - n + 1
    next_node = hash_map[curr].next
    pre_node = hash_map[curr-1]

    pre_node.next = next_node

    return head


def better_approach(head: Node, n: int) -> Node:
    """
        - Complexity Analysis:
            - Time -> O(n) + O(n) ~= O(n)
            - Space -> O(1)
    """
    if not head:
        return 
    
    temp = head
    length = 0
    while temp:
        length += 1
        temp = temp.next
    
    if n > length:
        return head
    elif n == length:
        return head.next
    
    temp = head
    pre = length - n
    while temp:
        pre -= 1
        if pre == 0:
            break
        temp = temp.next
    
    temp.next = temp.next.next
    return head

def optimal_approach(head: Node, n: int) -> Node:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    if not head:
        return 
    
    dummy = Node(0, head)
    
    slow = dummy
    fast = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next





if __name__ == "__main__":
    LL = Node(1)
    LL.next = Node(2)
    LL.next.next = Node(3)
    LL.next.next.next = Node(4)
    LL.next.next.next.next = Node(5)

    print(LL)
    # print(brute_force(LL, 6))
    # print(better_approach(LL, 1))
    print(optimal_approach(LL, 5))

