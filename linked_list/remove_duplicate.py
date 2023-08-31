"""
Remove duplicate element from sorted Linked List
"""

from single_linked_list import LinkedList

# Instansiate the linked list
ll = LinkedList()

# 2->2->4->5
# ll.add_last(2)
# ll.add_last(2)
# ll.add_last(4)
# ll.add_last(5)


# 2->2->2->2->2
ll.add_last(1)
ll.add_last(1)
ll.add_last(1)
ll.add_last(1)
ll.add_last(1)


# 1->2->5->6->7->8->9->10->10
# ll.add_last(1)
# ll.add_last(2)
# ll.add_last(5)
# ll.add_last(6)
# ll.add_last(7)
# ll.add_last(8)
# ll.add_last(9)
# ll.add_last(10)
# ll.add_last(10)

# printing input linked list
print(ll)


def remove_duplicates(current_node):
    hash_table = set()
    previous_node = current_node
    while current_node:
        if current_node.value not in hash_table:
            hash_table.add(current_node.value)
            previous_node = current_node
        else:
            previous_node.next = current_node.next
        current_node = current_node.next


remove_duplicates(ll.first)
# printing resultant linked list
print(ll)
