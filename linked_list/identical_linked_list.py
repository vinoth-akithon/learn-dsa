"""
Identical Linked Lists

Given two Singly Linked List of N and M nodes respectively.
The task is to check whether two linked lists are identical or not. 
Two Linked Lists are identical when they have same
data and with same arrangement too.


Example 1:

Input:
    LinkedList1: 1->2->3->4->5->6
    LinkedList2: 99->59->42->20
Output: Not identical


Example 2:

Input:
    LinkedList1: 1->2->3->4->5
    LinkedList2: 1->2->3->4->5
Output: Identical

Your Task:
The task is to complete the function areIdentical() which 
takes the head of both linked lists as arguments and returns True or False.
"""

def areIdentical(head1, head2):
    
    if (head1 is None) and (head2 is None):
        return False
        
    while (head1 is not None) and (head2 is not None):
        if head1.data != head2.data:
            return False
        
        head1 = head1.next
        head2 = head2.next
        
        if (head1 is None) and (head2 is None):
            return True
    return False


if __name__ == "__main__":
    pass
    # areIdentical(head1, head2)