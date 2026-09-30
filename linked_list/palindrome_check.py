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
        return f"{self.data}"


def brute_force(head: Node) -> bool:
    """
        - Using auxiliary DS (Stack)
        - Complexity Analysis:
            - Time -> O(n) + O(n) ~= O(n)
            - Space -> O(n)
    """
    stack = []
    temp = head

    while (temp):
        stack.append(temp.data)
        temp = temp.next

    temp = head
    while (temp):
        if temp.data != stack.pop():
            return False
        temp = temp.next
        
    return True


def better_approach(head: Node) -> bool:
    """
        - Small optimization using two pointer while comparing 
        - Using auxiliary DS (list)
        - Complexity Analysis:
            - Time -> O(n) + O(n/2) -> O(n)
            - Space -> O(n)
    """
    temp = head
    arr = []
    
    while (temp):
        arr.append(temp.data)
        temp = temp.next

    n = len(arr)
    s = 0
    e = n-1

    while (s < e):
        if arr[s] != arr[e]:
            return False
        
        s += 1
        e -= 1

    return True
    

def reversal(node: Node):
    prev = None
    curr = node

    while curr:
        next_ = curr.next
        curr.next = prev

        prev = curr
        curr = next_

    return prev



def optimal_approach(head: Node) -> bool:
    """
        - Complexity Analysis:
            - Time -> O(n) + O(n/2) + O(n/2) -> O(n)
            - Space -> O(1)
    """
    # Find the middle (second middle approach)
    prev_of_slow = None
    slow = head
    fast = head

    while (fast and fast.next):
        prev_of_slow = slow
        slow = slow.next
        fast = fast.next.next

    # Revering the second half
    # for cutting the second half
    # from the middle itself
    second_half = reversal(slow)

    # Cutting the original LL permanently
    prev_of_slow.next = None
    first_half = head

    first = first_half
    second = second_half

    while (first and second):
        if first.data != second.data:
            # Restore the original LL
            # Undoing reversal of second half
            second_half = reversal(second_half) # as second is the running pointer
            prev_of_slow.next = second_half
            return False
        
        first = first.next
        second = second.next
    
    second_half = reversal(second_half) # as second is the running pointer
    prev_of_slow.next = second_half
    return True




if __name__ == "__main__":
    LL = Node(1)
    LL.next = Node(2)
    LL.next.next = Node(3)
    LL.next.next.next = Node(2)
    LL.next.next.next.next = Node(1)

    # LL = Node(1)
    # LL.next = Node(2)
    # LL.next.next = Node(2)
    # LL.next.next.next = Node(1)

    # print(brute_force(LL))
    # print(better_approach(LL))
    print(optimal_approach(LL))

    print(is_palindrome(LL))


"""
1 2 3 2 1


1 2

        1 2 3


        
1 2 2 1
    1 2 2 
            1

"""

# 1 -> 2 -> 3

# 3 <- 2 <- 1

