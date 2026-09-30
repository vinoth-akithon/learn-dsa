"""
Given linked list contains three kind of elements. 0, 1 or 2 (also called sort color and dutch national flag problem)

We have to sort them in ascending order 
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
        - Using bubble sort algorithm
        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(1)
    """
    temp = head
    tail = head

    # determine tail
    while temp:
        tail = temp
        temp = temp.next

    temp = head
    while temp.next and head is not tail:
        if temp.data > temp.next.data:
            temp.data, temp.next.data = temp.next.data, temp.data
        
        if temp.next is tail:
            tail = temp
            temp = head
        else:
            temp = temp.next

    return head


def better_approach(head: Node) -> Node:
    """
        - Using two pointer (left and right) approach with auxiliary array
        - Complexity Analysis:
            - Time -> O(3n)
            - Space -> O(n)
    """

    temp = head
    arr = []

    while temp:
        arr.append(temp.data)
        temp = temp.next

    n = len(arr)
    left = 0
    right = n-1

    i = 0
    while i <= right:
        if arr[i] == 0:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[right] = arr[right], arr[i]
            right -= 1

    temp = head
    for i in range(len(arr)):
        temp.data = arr[i]
        temp = temp.next

    return head



def optimal_approach(head: Node) -> Node:
    """
        - Using Link arrangements
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    zero_head = zero_tail = Node(-1)
    one_head = one_tail = Node(-1)
    two_head = two_tail = Node(-1)

    temp = head
    while temp:
        if temp.data == 0:
            zero_tail.next = temp
            zero_tail = zero_tail.next
        elif temp.data == 1:
            one_tail.next = temp
            one_tail = one_tail.next
        else:
            two_tail.next = temp
            two_tail = two_tail.next

        
        temp = temp.next

    if one_head.next:        
        zero_tail.next = one_head.next
        one_tail.next = two_head.next
    else:
        zero_tail.next = two_head.next
        
    two_tail.next = None

    return zero_head.next


if __name__ == "__main__":
    LL = Node(0)
    LL.next = Node(1)
    # LL.next.next = Node(0)
    # LL.next.next.next = Node(0)

    print(LL)
    # print(brute_force(LL))
    # print(better_approach(LL))
    print(optimal_approach(LL))
