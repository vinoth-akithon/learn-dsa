""""
Delete nodes having greater value on right
"""


from single_linked_list import LinkedList, _Node


ll = LinkedList()


# 10->20->30->40->50->60 result --> 60
# ll.add_last(10)
# ll.add_last(20)
# ll.add_last(30)
# ll.add_last(40)
# ll.add_last(50)
# ll.add_last(60)


# 10->9->8->7->20 result --> 10->9->8->20
# ll.add_last(10)
# ll.add_last(9)
# ll.add_last(8)
# ll.add_last(7)
# ll.add_last(20)

# 12->15->10->11->5->6->2->3   result --> 15->11->6->3 
ll.add_last(12)
ll.add_last(15)
ll.add_last(10)
ll.add_last(11)
ll.add_last(50)
ll.add_last(6)
ll.add_last(2)
ll.add_last(3)
print(ll)

def delete_node(head):
    if not head or not head.next:
        return head
    
    new_head = current = head
    prev = None
    
    while current:
        next_node = current.next
        remove_current = False
        
        temp = next_node
        while temp:
            if temp.value > current.value:
                remove_current = True
                break
            temp = temp.next
        
        if remove_current:
            if prev:
                prev.next = next_node
            else:
                new_head = next_node
        else:
            prev = current
        
        current = next_node
    
    return new_head


retuned_one = delete_node(ll.first)
print(ll)
