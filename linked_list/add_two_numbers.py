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
    

def optimal_approach(head1: Node, head2: Node) -> Node:
    """
        - Using Reversing List Approach

        - Complexity Analysis:
            - Time -> O(n + m + 2Max(m, n))
    """
    # Reversing the First List
    pre = None
    curr = head1
    while curr:
        next_ = curr.next
        curr.next = pre

        pre = curr
        curr = next_
    head1 = pre

    # Reversing the second list
    pre = None
    curr = head2
    while curr:
        next_ = curr.next
        curr.next = pre

        pre = curr
        curr = next_
    head2 = pre

    # Summing the individual digits and add it into the new list
    dummy_head = dummy_tail = Node(-1)
    carry = 0
    while (head1 or head2):
        digit1 = 0 if not head1 else head1.data
        digit2 = 0 if not head2 else head2.data

        new_digit = digit1 + digit2 + carry
        carry = new_digit//10
        new_node = Node(new_digit%10)
        dummy_tail.next = new_node
        dummy_tail = dummy_tail.next

        if head1:
            head1 = head1.next
        if head2:
            head2 = head2.next

    # Creating new node if still carry persist
    if carry:
        new_tail = Node(carry)
        dummy_tail.next = new_tail

    # Reversing the resultant list
    pre = None
    curr = dummy_head.next
    while curr:
        next_ = curr.next
        curr.next = pre

        pre = curr
        curr = next_

    return pre
  

def optimal_approach2(head1: Node, head2: Node) -> Node:
        """
            - Using Reversing List Approach

            - Complexity Analysis:
                - Time -> O(n + m + 2Max(m, n) )
        """
        # # Reversing the First List
        # pre = None
        # curr = head1
        # while curr:
        #     next_ = curr.next
        #     curr.next = pre

        #     pre = curr
        #     curr = next_
        # head1 = pre

        # # Reversing the second list
        # pre = None
        # curr = head2
        # while curr:
        #     next_ = curr.next
        #     curr.next = pre

        #     pre = curr
        #     curr = next_
        # head2 = pre

        # Summing the individual digits and add it into the new list
        dummy_head = dummy_tail = Node(-1)
        carry = 0
        while (head1 or head2):
            digit1 = 0 if not head1 else head1.data
            digit2 = 0 if not head2 else head2.data

            new_digit = digit1 + digit2 + carry
            carry = new_digit//10
            new_node = Node(new_digit%10)
            dummy_tail.next = new_node
            dummy_tail = dummy_tail.next

            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next

        # Creating new node if still carry persist
        if carry:
            new_tail = ListNode(carry)
            dummy_tail.next = new_tail

        # # Reversing the resultant list
        # pre = None
        # curr = dummy_head.next
        # while curr:
        #     next_ = curr.next
        #     curr.next = pre

        #     pre = curr
        #     curr = next_

        return dummy_head.next
    

if __name__ == "__main__":
    head1 = Node(2)
    head1.next = Node(4)
    head1.next.next = Node(3)

    head2 = Node(5)
    head2.next = Node(6)
    head2.next.next = Node(4)

    print(f"head1: {head1}")
    print(f"head2: {head2}")

    # print(optimal_approach(head1, head2))
    print(optimal_approach2(head1, head2))
