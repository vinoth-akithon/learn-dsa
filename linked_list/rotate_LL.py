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


def brute_force(head: Node, k: int) -> Node:
    """
        - Repeatedly traverse the list k times and insert the last node at the front

        - Complexity Analysis:
            - Time -> O(n*k)
            - Space -> O(1)
    """
    if not head or not head.next or not k:
        return head

    for _ in range(k):
        sec_tail = Node
        tail = head

        while tail.next:
            sec_tail = tail
            tail = tail.next

        sec_tail.next = None
        tail.next = head
        head = tail

    return head


def better_approach(head: Node, k: int) -> Node:
    """
        - Complexity Analysis:
            - Time -> O(2n)
            - Space -> O(2n)

    """
    arr = []
    temp = head
    while temp:
        arr.append(temp.data)
        temp = temp.next

    first_arr = arr[:len(arr) - k%len(arr)]
    second_arr = arr[len(arr) - k%len(arr):]

    temp = head
    for e in second_arr:
        temp.data = e
        temp = temp.next

    for e in first_arr:
        temp.data = e
        temp = temp.next

    return head


def optimal_approach1(head: Node, k: int) -> Node:
    """
        - Using Reversing strategy 
        - Complexity Analysis:
            - Time -> O(2n)
            - Space -> O(1)
    """
    if not head or not head.next or not k:
        return head
    
    # Revering the whose list
    length = 0
    pre = None
    curr = head
    while curr:
        length += 1
        next_ = curr.next
        curr.next = pre

        pre = curr
        curr = next_

    head = pre

    # Reversing the first k nodes 
    dummy = dummy_tail = Node(0)
    cnt = 0
    first_start = first_tail = head
    second_start = head

    while first_tail:
        cnt += 1

        if cnt != k%length:
            first_tail = first_tail.next
        else:
            second_start = first_tail.next
            first_tail.next = None
            
            pre = None
            curr = first_start
            while curr:
                next_ = curr.next
                curr.next = pre

                pre = curr
                curr = next_

            dummy_tail.next = pre
            dummy_tail = first_start
            break

    # Reversing the remaining nodes
    pre = None
    curr = second_start
    while curr:
        next_ = curr.next
        curr.next = pre

        pre = curr
        curr = next_

    dummy_tail.next = pre

    return dummy.next


def optimal_approach2(head: Node, k: int) -> Node:
    """
        - Making the given linked list to circular linked list and shifting the head at right place.

        - Complexity Analysis:
            - Time -> O(2n)
            - Space -> O(1)
    """ 
    length = 0
    temp = head
    while temp:
        length += 1

        if temp.next is None:
            temp.next = head
            break
        temp = temp.next

    cnt = 0
    temp = head
    while temp:
        cnt += 1
        if cnt == length - k%length:
            head = temp.next
            temp.next = None

        temp = temp.next

    return head

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print(head)
    # print(brute_force(head, 6))
    # print(better_approach(head, 6))
    # print(optimal_approach1(head, 6))
    print(optimal_approach2(head, 6))


