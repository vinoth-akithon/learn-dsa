from __future__ import annotations

class Node:
    def __init__(self, data: int, next: Node|None = None) -> None:
        self.data = data
        self.next = next
    
    def __repr__(self) -> str:
        return str(self.data)


def remove_nth_node_from_list1(head: Node, n: int) -> Node:
    dummy = Node(0, head)
    slow = fast = dummy

    for i in range(n+1):
        fast = fast.next
        
    while fast:
        fast = fast.next
        slow = slow.next
    
    slow.next = slow.next.next
    return dummy.next



def remove_nth_node_from_list(head: Node, n: int) -> Node:
    list_length = 0
    list = head
    while list:
        list_length += 1
        list = list.next

    if n > list_length or n <= 0:
        return head
    break_node_index = list_length - n
    break_node = head
    for i in range(break_node_index-1):
        break_node = break_node.next
    
    break_node.next = break_node.next.next
    return head

    


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    # head.next.next.next.next.next = Node(6)


    head = remove_nth_node_from_list1(head, 2)
    
    while head:
        print(head.data)
        head = head.next
