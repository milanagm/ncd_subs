# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return []

        initial = []
        head = head
        while head.next != None: 
            initial.append(head.val)
            head = head.next
        
       
        head.val = initial[-1] # ist glaube ich falsch
        p_next = len(initial) - 2
        while p_next >= 0:
            head.next = p_next
            head = head.next
            p_next -= 1

        return head

        
        

        