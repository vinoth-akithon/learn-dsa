"""
Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val}"


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = tail= ListNode(-1)
        
        while True:
            if list1 is None:
                tail.next = list2
                break

            if list2 is None:
                tail.next = list1
                break

            if list1.val <= list2.val:
                tail.next = ListNode(list1.val)
                list1 = list1.next
            else:
                tail.next = ListNode(list2.val)
                list2 = list2.next

            tail = tail.next
        print(tail is dummy_node)
        self.new_list = dummy_node.next
        return self.new_list
    
    
    def __str__(self) -> str:
        result_list = []
        current = self.new_list
        while current:
            result_list.append(current.val)
            current = current.next
        return f"{result_list}"
    

if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(2)
    # list1.next.next = ListNode(4)

    list2 = ListNode(1)
    # list2.next = ListNode(3)
    # list2.next.next = ListNode(4)


    sn = Solution()
    sn.mergeTwoLists(list1, list2)

    print(sn)