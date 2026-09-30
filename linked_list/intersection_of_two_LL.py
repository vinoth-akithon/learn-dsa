"""

Intersection of two nodes mean, checking whether the same node (object not vale) exist in both the list.

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



def brute_force(head1: Node, head2: Node) -> Node|None:
    """
        - Fixing one list node and checking all the nodes in second list against it.
        - Complexity Analysis:
            - Time -> O(n*m)
            - Space -> O(1)
    """

    temp1 = head1
    while temp1:
        temp2 = head2
        while temp2:
            if temp1 is temp2:
                return temp1
            temp2 = temp2.next

        temp1 = temp1.next

    return None


def better_approach(head1: Node, head2: Node) -> Node|None:
    """
        - Using Hash Set
        - Complexity Analysis:
            - Time -> O(n+m)
            - Space -> O(n)
    """
    temp1 = head1
    hash_set = set()

    while temp1:
        hash_set.add(temp1)
        temp1 = temp1.next

    temp2 = head2
    while temp2:
        if temp2 in hash_set:
            return temp2
        temp2 = temp2.next

    return None


def optimal_approach(head1: Node, head2: Node) -> Node|None:
    """
        - Reducing the search length of the larger list like smaller list
        - And comparing each node of the list are same
        
        - Complexity Analysis:
            - Time -> O(Max(n, m)+ diff(n-m) + Min(n,m))
            - Space -> O(1)
    
    """
    # finding the length of list 1 and list 2
    temp1 = head1
    temp2 = head2
    len1 = 0
    len2 = 0

    while temp1 or temp2:
        if temp1:
            len1 += 1
            temp1 = temp1.next
        if temp2:
            len2 += 1
            temp2 = temp2.next

    # Checking which list is larger for reducing the search length
    is_head1_larger = len1 > len2
    temp1 = head1 if is_head1_larger else head2
    temp2 = head1 if not is_head1_larger else head2

    # Reducing the larger list length
    diff = abs(len1 - len2)
    while True:
        if diff == 0:
            break
        diff -= 1
        temp1 = temp1.next
    
    while temp2:
        if temp1 is temp2:
            return temp1
        temp1 = temp1.next
        temp2 = temp2.next

    return None
        

def intersectionPresent(head1, head2):
    d1, d2 = head1, head2
    # Traverse both lists, when one reaches the end, redirect it to the head of the other list
    while d1 != d2:
        d1 = head2 if d1 is None else d1.next
        d2 = head1 if d2 is None else d2.next

    return d1



if __name__ == "__main__":
    # head1 = Node(1)
    # head1.next = Node(3)
    # head1.next.next = Node(1)
    # head1.next.next.next = Node(2)
    # head1.next.next.next.next = Node(4)

    # head2 = Node(3)
    # head2.next = head1.next.next.next


    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)


    head2 = Node(1)
    head2.next = Node(2)


    # print(brute_force(head1, head2))
    # print(better_approach(head1, head2))
    # print(optimal_approach(head1, head2))
    print(intersectionPresent(head1, head2))