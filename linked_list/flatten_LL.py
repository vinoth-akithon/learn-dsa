"""

"""


from typing import Self

class Node:
    def __init__(self, data: int, next: Self|None = None, child: Self|None = None) -> None:
        self.data = data
        self.next = next
        self.child = child

    def __str__(self) -> str:
        return f"{self.data} -> {self.next}"
    
    def __repr__(self) -> str:
        return f"{self.data} -> {self.next}"



def brute_force(head: Node) -> Node:
    """
        - Using Auxiliary DS
        - Complexity Analysis:
            - Time -> O(n + n log n + n) ~= O(2n + n log n)
            - Space -> O(2n)
    """
    dummy_tail = head
    arr = []

    while dummy_tail:
        future_head = dummy_tail.next

        dummy_tail.next = dummy_tail.child
        while dummy_tail:
            arr.append(dummy_tail.data)

            if dummy_tail.next is None:
                dummy_tail = future_head
                break
            else:
                dummy_tail = dummy_tail.next

    arr.sort()
    dummy = dummy_tail = Node(0)
    for e in arr:
        dummy_tail.next = Node(e)
        dummy_tail = dummy_tail.next

    return dummy.next
    

def merge(left_head: Node|None, right_head: Node|None) -> Node:
    """
        - Complexity Analysis:
            - Time -> O(n1 + n1)
            - Space -> O(1)
    """
    result_head = Node(0)
    result_tail = result_head

    left_tail = left_head
    right_tail = right_head

    while (left_tail and right_tail):
        if left_tail.data < right_tail.data:
            result_tail.next = left_tail
            result_tail = result_tail.next
            left_tail = left_tail.next
        else:
            result_tail.next = right_tail
            result_tail = result_tail.next
            right_tail = right_tail.next
        
    
    if (left_tail):
        result_tail.next = left_tail
    elif right_tail:
        result_tail.next = right_tail

    return result_head.next

            
def sort(head: Node|None) -> Node:
    """
        - Complexity Analysis:
            - Time -> O(n logn)
            - Space -> O(log n) -> Due to recursive call
    
    """

    # Base condition 
    if not head or not head.next:
        return head

    # Find the first middle of LL
    prev_to_slow = None
    slow = head
    fast = head

    while (fast and fast.next):
        prev_to_slow = slow
        slow = slow.next
        fast = fast.next.next

    prev_to_slow.next = None
    left_head = sort(head)
    right_head = sort(slow)

    # print(f"Left Half -> {left_half}")
    # print(f"Right Half -> {right_half}")

    # Merging logic
    return merge(left_head, right_head)


def better_approach(head: Node) -> Node:
    """
        - Flatten the each linked list and then sort

        - Complexity Analysis:
            - Time -> O(n + n log n)
            - Space -> O(log n) -> Due to sorting involves recursive
    """
    dummy_tail = head
    while dummy_tail:
        next_ = dummy_tail.next
        dummy_tail.next = dummy_tail.child

        while dummy_tail.next:
            dummy_tail = dummy_tail.next

        dummy_tail.next = next_
        dummy_tail = dummy_tail.next

    return sort(head)


def optimal_approach(head: Node) -> Node:
    """
        - Complexity Analysis:
            - Time -> O(m * (n1 * n2))
            - Space -> O(1)
    
    """
    pre_head = future_head = None
    curr_head = head

    while curr_head:
        future_head = curr_head.next

        curr_head.next = curr_head.child
        curr_head.child = None

        pre_head = merge(pre_head, curr_head)
        curr_head = future_head

    return pre_head


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)

    child1 = Node(10)
    child1.next = Node(11)
    head.child = child1

    child2 = Node(20)
    child2.next = Node(21)
    head.next.child = child2

    # print(head)
    # print(brute_force(head))
    # print(better_approach(head))
    print(optimal_approach(head))