# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return []

        initial = []
        while head.next != None: 
            initial.append(head.val)
            head = head.next
        
        new_head = head
        p_next = len(initial) - 2
        while p_next >= 0:
            head.next = ListNode(initial[p_next])
            head = head.next
            p_next -= 1

        return new_head

        
        

        