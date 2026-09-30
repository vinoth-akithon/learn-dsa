"""


"""


from typing import Self

class Node:
    def __init__(self, data: int, next: Self|None = None, child: Self|None = None) -> None:
        self.data = data
        self.next = next
        self.random = child

    def __str__(self) -> str:
        return f"{self.data} -> {self.next}"
    
    def __repr__(self) -> str:
        return f"{self.data} -> {self.next}"



def brute_force(head: Node) -> Node:
    """
        - Complexity Analysis:
            - Time -> O(2n)
            - Space -> O(2n)
    """
    hash_map = {}
    temp = head

    while temp:
        hash_map[temp] = Node(temp.data)
        temp = temp.next

    dummy = dummy_tail = Node(0)
    old_node = head
    while old_node:
        new_node = hash_map.get(old_node)
        new_next_node = hash_map.get(old_node.next)
        new_random_node = hash_map.get(old_node.random)
        new_node.next = new_next_node
        new_node.random = new_random_node

        dummy_tail.next = new_node
        dummy_tail = dummy_tail.next
        old_node = old_node.next

    return dummy.next



def optimal_approach(head: Node) -> Node:
    """
        - Pointer manipulation
        - Complexity Analysis:
            - Time -> O(3n)
            - Space -> O(n)
    """
    # Creating copy of a node and inserting in between two original node
    temp = head
    while temp:
        next_node = temp.next
        new_node = Node(temp.data)
        temp.next = new_node
        new_node.next = next_node

        temp = next_node

    # Updating the random pointer of each copied nodes
    temp = head
    while temp:
        copied_node = temp.next

        if temp.random:
            copied_node.random = temp.random.next
        else:
            copied_node.random = None

        temp = temp.next.next

    # Splitting the mixed list into copied list and head by manipulating the pointers
    dummy = dummy_tail = Node(-1)
    temp = head
    while temp:
        copied_node = temp.next

        dummy_tail.next = copied_node
        dummy_tail = dummy_tail.next

        temp.next = temp.next.next
        temp = temp.next

    return dummy.next




if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    # head.random = head.next

    # head.next.random = head.next

    print(head)
    # print(brute_force(head))
    print(optimal_approach(head))