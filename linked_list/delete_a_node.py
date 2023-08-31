"""
Delete a Node in Single Linked List
(Given a singly linked list and an integer x. Delete xth node from the singly linked list.)

input --> head 1 -> 3 -> 4,    x --> x = 3    result --> 1 -> 3

input --> head 1 -> 5 -> 2 -> 9 ,    x --> x = 2    result --> 1 -> 2 -> 9

"""

from single_linked_list import LinkedList, _Node


def delete_a_node(head, h):
    input_ll = head
    current_index = 1 # consider 1-base index here
    previous_node = head
    while head:
        if current_index == h:
            if previous_node is head:
                return input_ll.next
            previous_node.next = head.next
            return input_ll
        current_index += 1
        previous_node = head
        head = head.next



#input --> head 1 -> 3 -> 4,    x --> x = 3    result --> 1 -> 3
ll = LinkedList()
ll.add_last(10)
ll.add_last(20)
ll.add_last(30)
print(ll)

print(delete_a_node(ll.first, 3))