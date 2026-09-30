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
        - Using Auxiliary DS (string)
        - Complexity Analysis:
            - Time -> O(3n)
            - Space -> O(n)
    """
    # forming the given number as string
    temp = head
    stack = []
    while temp:
        stack.append(temp.data)
        temp = temp.next

    # Add 1 to the number
    # for i in range(len(num)-1, -1, -1):
    #     digit = num[i] + 1
    #     num[i] = digit%10
    #     carry = digit//10

    #     if carry == 0:
    #         break

    #  # Check length is differ, if so add a new node at the head
    # if carry > 0:
    #     num.insert(0, str(carry))
    #     head = Node(0, head)

    # # Updating the new number to the list
    # temp = head
    # for i in range(len(num)):
    #     temp.data = num[i]
    #     temp = temp.next


    # Add 1 to the number
    new_stack = []
    carry = 1
    for _ in range(len(stack)):
        digit = stack.pop() + carry
        new_stack.append(digit%10)
        carry = digit//10

    if carry:
        head = Node(0, head)
        new_stack.append(carry)
    
   # Updating the new number to the list
    temp = head
    for _ in range(len(new_stack)):
        temp.data = new_stack.pop()
        temp = temp.next
    
    return head


def optimal_approach(head: Node) -> Node:
    """
        - Using Reversing the List approach
        
        - Complexity Analysis:
            - Time -> O(3n)
            - Space -> O(1)
    """
    # Reversing the List
    pre = None
    curr = head
    while curr:
        next_ = curr.next
        curr.next = pre

        pre = curr
        curr = next_

    head = pre

    # Adding 1 to the List
    temp = head
    pre_tail = None
    while temp:
        digit = temp.data + 1
        temp.data = digit%10
        carry = digit//10

        if carry == 0:
            break
        
        pre_tail = temp
        temp = temp.next

    if carry:
        tail = Node(carry)
        pre_tail.next = tail

    # Reversing the List Again 
    pre = None
    curr = head
    while curr:
        next_ = curr.next
        curr.next = pre

        pre = curr
        curr = next_
    
    head = pre

    return head


def recursive_func(head: Node) -> Node:
    # Base condition
    if not head:
        return 1

    carry = recursive_func(head.next)

    digit = head.data + carry
    head.data = digit%10
    carry = digit//10

    return carry


def optimal_approach2(head: Node) -> Node:
    """
        - Using Recursive function

        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n) -> Due to recursive call
    """
    carry = recursive_func(head)
    if carry:
        return Node(carry, head)
    else:
        return head
    


if __name__ == "__main__":
    head = Node(9)
    head.next = Node(9)
    # head.next.next = Node(9)
    # head.next.next.next = Node(2)
    # head.next.next.next.next = Node(4)

    print(head)
    # print(brute_force(head))
    # print(optimal_approach(head))
    print(optimal_approach2(head))
