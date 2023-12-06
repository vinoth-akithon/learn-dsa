from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"Node: {self.val}"

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.head = head
        self.head = self.__reverse_using_recursion(head)
        # self.head = self.__reverse_using_iteration(head)
        return self.head
    

    def __reverse_using_recursion(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        reversed_head = self.__reverse_using_recursion(head.next)
        head.next.next = head
        head.next = None
        
        return reversed_head

    
    def __reverse_using_iteration(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.head = head
        if head is None:
            return None
        
        previous = head
        current = head.next
        while current:
            future = current.next
            current.next = previous
            previous = current
            current = future

        head.next = None
        head = previous
        self.head = head
        return head
    

    
    def __repr__(self) -> str:
        return f'{self.head}'

    def __str__(self) -> str:
        result_list = []
        current = self.head
        while current:
            result_list.append(current.val)
            current = current.next
        return f"{result_list}"


if __name__ == "__main__":
    # ll = None
    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)
    # ll.next.next = ListNode(4)
    # ll.next.next = ListNode(5)

    sn = Solution()
    sn.reverseList(ll)

    print(sn)

